# Awesome Tool AI — pagine tool, share, star, RSS, MCP (2026-07-12)

Approvato da Nunzio via Telegram. Vincolo esplicito: **NIENTE conteggio stelle GitHub** — solo bottone e scritta.

Base URL pubblica: `https://nunziogianfelice.github.io/awesome-tool-ai/`
Repo: `https://github.com/nunziogianfelice/awesome-tool-ai`

Architettura invariata: sito statico, zero framework, vanilla HTML/CSS/JS, build via script Python in `scripts/`. Stile visivo coerente con l'esistente (stesso tema della index).

## 1. Pagina singola per tool

- Nuovo script `scripts/build_tool_pages.py` che genera `tools/<id>.html` per ogni entry di `tools.json`
- URL: `https://nunziogianfelice.github.io/awesome-tool-ai/tools/<id>.html`
- Contenuto: nome, categoria, pricing, descrizione completa, tag (cliccabili → tornano alla index con filtro `?tag=`), link al sito/repo del tool, sezione "Tool correlati" (max 4, per tag condivisi, escluso se stesso)
- Meta **Open Graph + Twitter card** per pagina (og:title, og:description, og:url, og:type) — indispensabili per l'anteprima LinkedIn
- `added_at` (vedi §4) mostrato come "Aggiunto il ..."
- Le card della index linkano alla pagina del tool (il titolo resta link esterno al tool; aggiungere link/icona "dettagli →" alla pagina interna)
- La index deve supportare il filtro `?tag=<tag>` in query string (oggi filtra solo via UI)

## 2. Share per tool

Su ogni pagina tool E su ogni card della index, tre azioni:
- **LinkedIn**: `https://www.linkedin.com/sharing/share-offsite/?url=<url-encoded pagina tool>`
- **Copia link GitHub** del tool (item.url) — clipboard API con feedback visivo ("copiato ✓")
- **Copia link** della pagina tool sul nostro sito — clipboard API con feedback

Icone sobrie, niente librerie esterne (SVG inline).

## 3. Free + Star (SENZA conteggio)

- Header della index e footer delle pagine tool: riga "100% free & open source" + bottone "⭐ Star on GitHub" che porta a `https://github.com/nunziogianfelice/awesome-tool-ai`
- NESSUN badge di conteggio stelle, né shields.io né API GitHub — richiesta esplicita

## 4. Campo `added_at`

- Script one-shot `scripts/backfill_added_at.py`: per ogni tool ricava la data del commit che ha introdotto la sua entry in `tools.json` (`git log --follow -p tools.json` o `git log -S '"id": "<id>"'`) e scrive `added_at: YYYY-MM-DD` nella entry. Eseguirlo una volta e committare il risultato
- `build_tools_js.py` (o il flusso esistente) propaga il campo
- Index: badge "nuovo" sulle card con added_at < 30 giorni + opzione ordinamento "Più recenti"
- I nuovi inserimenti futuri dovranno valorizzare added_at (aggiornare il README di manutenzione)

## 5. RSS

- `scripts/build_feed.py` genera `feed.xml` (RSS 2.0): un item per tool, ordinato per added_at desc, limite 50. Link alle pagine tool
- `<link rel="alternate" type="application/rss+xml">` nella index

## 6. Contributi

- `.github/ISSUE_TEMPLATE/suggest-tool.yml`: form con campi nome, URL, descrizione breve, categoria (dropdown con le categorie esistenti), perché è interessante

## 7. llms.txt

- Generato in build: intro di una riga + elenco tool (nome, URL, one-liner, link pagina) — formato llms.txt standard

## 8. Server MCP

- Cartella `mcp/` con server Python **FastMCP** (`mcp/server.py` + `mcp/pyproject.toml`), avviabile con `uvx --from <repo-o-path> awesome-tool-ai-mcp` o `uv run`
- All'avvio scarica `https://nunziogianfelice.github.io/awesome-tool-ai/tools.json` (cache in memoria, refresh ogni ora; fallback al file locale se offline e disponibile)
- Tool esposti:
  - `search_tools(query, category?, tag?, limit=10)` — ricerca full-text su nome/descrizione/tag
  - `get_tool(id)` — entry completa + URL pagina
  - `list_categories()` — categorie con conteggi
- README in `mcp/` con istruzioni di configurazione per Claude Code/Desktop (snippet JSON)

## Build unificata

- `scripts/build_all.py` (o Makefile) che esegue in ordine: tools.js, README, pagine tool, feed, llms.txt — e va documentato nel flusso di manutenzione (il flusso attuale "aggiungi tool → build → commit → push" acquisisce i nuovi artefatti)

## Verifica (checklist per il builder)

1. Build completa senza errori; `tools/` popolata con una pagina per ogni tool (114+)
2. Aprire 2-3 pagine tool in locale: OG meta presenti nel sorgente, correlati sensati, share funzionanti (il copy si può verificare via console/DOM)
3. Index: badge "nuovo" coerente con added_at, sort per data funziona, `?tag=` filtra
4. `feed.xml` valido (well-formed XML, date RFC822)
5. MCP: avviare il server in locale e chiamare i 3 tool (anche via script di test con client MCP stdio o fastmcp dev), verificare risultati su query reali ("office", categoria developer-tools)
6. NESSUN conteggio stelle da nessuna parte

## Fuori scope

- Backend/analytics, commenti, login
- Conteggio stelle (esplicitamente escluso)
- Hosting MCP remoto (fase 2)
