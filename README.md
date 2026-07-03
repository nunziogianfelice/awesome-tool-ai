# 🤖 awesome-tool-ai

> A curated collection of GenAI tools & resources for the agentic AI world.
> Continuously updated.

## Quick search

**[🔍 Search online →](https://nunziogianfelice.github.io/awesome-tool-ai/)**

Or clone the repo and open `index.html` locally (works from `file://` too):

```bash
git clone https://github.com/nunziogianfelice/awesome-tool-ai
cd awesome-tool-ai
open index.html  # macOS
```

I dati canonici vivono in [`tools.json`](tools.json). Il file
[`tools.js`](tools.js) e una copia auto-generata che permette al frontend
statico di funzionare senza un server HTTP. Rigeneralo con:

```bash
python3 scripts/build_tools_js.py
```


## Tool per categoria


### Agent Frameworks

| Tool | Descrizione | Tag |
|------|-------------|-----|
| Agent Zero | Framework multi-agent open-source con memoria persistente, capacita di self-improvement e scrittura/esecuzione di tool dinamici. Progettato come sistema agentivo generalista hackable. | `open-source` `multi-agent` `memory` `self-hostable` |
| Agent-User Interaction Protocol (AG-UI) | Protocollo aperto che standardizza la comunicazione tra agenti AI backend e interfacce utente frontend, definendo eventi, streaming e human-in-the-loop. Complementare a MCP ma orientato al lato UI. | `open-source` `protocol` `ui` |
| [AgenticSeek](https://github.com/Fosowl/agenticSeek) | Alternativa open-source a Manus completamente locale: agente che pianifica, naviga il web ed esegue codice usando LLM in locale. Privacy-first, gira interamente sulla macchina dell'utente. | `open-source` `local-llm` `self-hostable` `privacy` `python` |
| [agents-cli by Google](https://github.com/google/agents-cli) | CLI ufficiale di Google con skills che trasformano qualsiasi coding assistant in un esperto nel creare, valutare e distribuire agenti AI su Google Cloud. Basata sull'Agent Development Kit (ADK), con scaffolding, esecuzione e deploy su Vertex AI e sulla Gemini Enterprise Agent Platform. | `open-source` `google` `cli` `adk` `gemini` `developer-tools` |
| [Atomic Agents](https://github.com/BrainBlend-AI/atomic-agents) | Framework Python modulare e leggero per costruire agenti AI con componenti riusabili e schema-driven (Pydantic). Punta su prevedibilita e composizione invece che sulla magia di abstraction layer pesanti. | `open-source` `python` `modular` `pydantic` |
| [Deep Agents by LangChain](https://github.com/langchain-ai/deepagents) | Libreria di LangChain che implementa pattern di agenti deep (planning, sub-agent, file system virtuale) ispirati a Manus e Claude Code. Pensata per task autonomi a lungo orizzonte. | `open-source` `langchain` `python` `agent` `multi-agent` |
| [Eve by Vercel](https://vercel.com/eve) | Framework per costruire agenti AI production-ready con approccio directory-based (un agente = una cartella): istruzioni in Markdown, tool in TypeScript, skills come playbook riutilizzabili, channels multi-piattaforma (Slack, Discord, Teams). Include durable execution, subagents, cron schedules, sandboxing su VM on-demand e human-in-the-loop con approval gates. Integrazione nativa con l'infrastruttura Vercel. | `typescript` `vercel` `durable-execution` `multi-channel` `production` `developer-tools` |
| Google ADK (Agent Development Kit) | Toolkit open-source di Google per costruire, valutare e deployare agenti AI multi-step e multi-agente, integrato con Vertex AI e Gemini. Disponibile in Python e Java. | `google` `open-source` `python` `java` `multi-agent` |
| [Multica](https://github.com/multica-ai/multica) | Piattaforma open-source che integra agenti AI come membri del team: si assegnano task agli agenti come a un collega su Linear o Jira, e loro eseguono autonomamente, aggiornano lo stato e segnalano i blocchi. Un daemon locale rileva automaticamente gli agenti installati (Claude Code, Copilot CLI, Codex, ecc.) e li connette al server centrale via WebSocket. Supporta workspace multi-utente e riuso delle skill tra agenti diversi. | `agent` `workflow` `open-source` `tools` |
| [OpenAgents](https://github.com/openagents-org/openagents) | Piattaforma open-source per costruire e condividere agenti AI generali, con focus su data agents, plugin agents e web agents. Originariamente nato come progetto accademico aperto. | `open-source` `self-hostable` `python` `multi-agent` |
| [Parlant](https://www.parlant.io/) | Framework open-source per costruire agenti conversazionali governati da regole e guideline esplicite invece che solo da prompt. Pensato per use case enterprise dove serve controllo e auditabilita. | `open-source` `python` `enterprise` `guardrails` |
| Suna AI | Agente AI generale autonomo open-source che esegue task di ricerca, scraping, scrittura e automazione browser. Alternativa libera e self-hostable a Manus. | `open-source` `self-hostable` `agent` `autonomous` |
| [Symphony](https://github.com/openai/symphony) | Tool di orchestrazione di OpenAI che automatizza il lavoro di sviluppo spawning agenti di coding autonomi che gestiscono i task in modo indipendente. Permette ai team di operare a un livello più alto senza supervisionare ogni agente: i task vengono assegnati e gli agenti restituiscono proof of work al completamento. Disponibile come spec aperta con implementazione di riferimento in Elixir. | `agent` `workflow` `open-source` `framework` |

### MCP (Model Context Protocol)

| Tool | Descrizione | Tag |
|------|-------------|-----|
| [Apidog MCP Server](https://www.npmjs.com/package/apidog-mcp-server) | Server MCP che espone le specifiche OpenAPI/Apidog come contesto consultabile dagli agenti AI. Permette a Claude, Cursor e altri client MCP di leggere documentazione API in tempo reale per generare codice e test allineati al contratto. | `open-source` `api` `typescript` `developer-tools` |
| [ApiTap](https://github.com/n1byn1kt/apitap) | Tool open-source che intercetta richieste API e le trasforma in tool MCP riusabili dagli agenti AI. Utile per esporre velocemente API esistenti come capabilities agentive. | `open-source` `api` `developer-tools` |
| [MCP Inspector (MCPJam)](https://github.com/MCPJam/inspector) | Strumento di debugging e testing per server MCP: permette di ispezionare tool, risorse e prompt esposti, simulare chiamate e validare il protocollo. Utile durante lo sviluppo di server MCP custom. | `open-source` `developer-tools` `debugging` |
| [MCP Linker](https://github.com/milisp/mcp-linker) | Utility che semplifica installazione, configurazione e gestione di server MCP all'interno di client come Claude Desktop, Cursor, Windsurf. Risolve il fastidio della configurazione manuale del file JSON. | `open-source` `developer-tools` `cli` |
| [MCP Toolbox for Databases](https://github.com/googleapis/genai-toolbox) | Server MCP open-source di Google che espone connessioni sicure a database (Postgres, MySQL, BigQuery, Spanner...) con auth, observability e templating delle query. Pensato per agenti enterprise data-aware. | `open-source` `google` `database` `enterprise` `sql` |
| [mcp-ui](https://github.com/idosal/mcp-ui) | Libreria open-source che permette ai server MCP di esporre componenti UI ricchi (HTML, React) renderizzabili dai client compatibili. Abilita esperienze interattive oltre il testo nei tool MCP. | `open-source` `ui` `typescript` `react` |
| [Pipedream MCP Chat](https://github.com/PipedreamHQ/mcp-chat) | Chat client open-source di Pipedream che dimostra come usare MCP per orchestrare migliaia di integrazioni Pipedream da un LLM. Buon esempio di reference implementation. | `open-source` `typescript` `pipedream` `integrations` |
| Rube.app | Server MCP universale di Composio che da accesso a oltre 500 app SaaS (Gmail, Slack, Notion, GitHub...) tramite un unico endpoint, con OAuth gestito. Pensato per agenti multi-tool senza configurare ogni integrazione. | `saas` `integrations` `composio` |
| [TokenSave](https://github.com/aovestdipaperino/tokensave) | Server MCP di code intelligence per agenti di coding AI: oltre 40 tool e 30+ linguaggi, con knowledge graph semantici pre-indicizzati per una comprensione istantanea del codice. Riduce token e numero di tool call, funziona 100% in locale e si integra con 9 agenti. | `open-source` `mcp` `code-intelligence` `knowledge-graph` `rust` `token-reduction` `developer-tools` |

### Coding Assistants

| Tool | Descrizione | Tag |
|------|-------------|-----|
| [Aider](https://aider.chat/) | AI pair programmer da terminale open-source che lavora direttamente sul tuo repo Git, con commit automatici e supporto a decine di modelli (GPT, Claude, locali). Tra i piu maturi nella categoria CLI coding agents. | `open-source` `cli` `python` `git` |
| [Coding Agents by Enea Scaccabarozzi](https://github.com/enea-scaccabarozzi/coding-agents) | Repository didattica con implementazioni di coding agents da zero, pensata come materiale di studio per capire come funzionano internamente strumenti come Claude Code o Aider. | `open-source` `educational` `python` |
| [Cosine Genie](https://trygenie.now/) | Agente di coding autonomo che si autoaddestra sul codice del tuo team e affronta task software complessi (bug fix, feature, refactor) con risultati allo stato dell'arte sui benchmark SWE-bench. Pensato per team di ingegneria. | `agent` `enterprise` `autonomous` |
| Gemini CLI | CLI open-source di Google che porta Gemini nel terminale come coding agent: interagisce con il filesystem, esegue comandi e supporta MCP. Concorrente diretto di Claude Code e Codex CLI. | `google` `cli` `agent` `open-source` |
| VibeKit | Sandbox open-source per eseguire in sicurezza coding agents (Codex, Claude, Gemini) in container isolati con scoped permissions, audit log e telemetry. Pensato per produzionalizzare agenti che scrivono codice. | `open-source` `sandbox` `security` `agent` |

### LLM Infrastructure

| Tool | Descrizione | Tag |
|------|-------------|-----|
| [AgentMail](https://agentmail.to/) | Infrastruttura email pensata per agenti AI: API per creare caselle al volo, ricevere e inviare email programmaticamente con webhook strutturati. Risolve il problema di dare un indirizzo email a ogni agente. | `api` `email` `agent` |
| [Apple Foundation Models](https://developer.apple.com/documentation/foundationmodels) | Framework Swift di Apple per usare i modelli on-device di Apple Intelligence direttamente nelle app iOS/macOS. Espone API per generazione testo, tool calling e guided generation con privacy locale. | `apple` `on-device` `ios` `macos` `swift` `privacy` |
| [Headroom](https://github.com/chopratejas/headroom) | Compressore di contesto per agenti AI che riduce i token di input del 60-95% (JSON, codice, RAG, log) prima che raggiungano l'LLM, senza perdere informazioni critiche. Tre modalità d'uso: libreria Python/TS inline, proxy trasparente senza modifiche al codice, MCP server. Include CodeCompressor AST-aware per Python/JS/Go/Rust, compressione reversibile con cache locale e supporto OpenAI/Anthropic/Gemini. | `open-source` `context-compression` `token-reduction` `python` `typescript` `mcp` `rag` `agent` |
| [Kong](https://konghq.com/) | API gateway cloud-native con funzionalita AI Gateway integrate per il routing, la sicurezza e il rate-limiting di traffico LLM. Utile per centralizzare il consumo di provider AI eterogenei in ambienti enterprise. | `enterprise` `api` `gateway` `open-source` |
| [Latitude](https://github.com/latitude-dev/latitude-llm) | Piattaforma open-source di osservabilità e monitoring per applicazioni LLM e agenti AI: tracing degli errori, logging dei prompt, valutazioni e metriche in produzione. Self-hostable (MIT) con cloud gestito opzionale e SDK TypeScript/Python. | `open-source` `observability` `monitoring` `llm-ops` `typescript` `agent` |
| [LiteLLM](https://www.litellm.ai/) | Proxy e SDK Python open-source che unifica le API di oltre 100 provider LLM in un'unica interfaccia OpenAI-compatible, con retry, fallback, budget e logging. Standard per ambienti multi-modello. | `open-source` `python` `proxy` `openai-compatible` `self-hostable` |
| [OpenRouter](https://openrouter.ai/) | Aggregatore di LLM che espone via un'unica API OpenAI-compatible centinaia di modelli (GPT, Claude, Gemini, Llama, ecc.) con routing automatico, fallback e prezzi competitivi. Standard de facto per multi-model app. | `api` `multi-model` `routing` `openai-compatible` |
| [WebLLM](https://webllm.mlc.ai/) | Runtime per eseguire LLM direttamente nel browser via WebGPU, senza server. Permette inferenza completamente locale e offline di modelli come Llama, Mistral o Phi. | `open-source` `browser` `local-llm` `webgpu` `privacy` |

### Data & AI

| Tool | Descrizione | Tag |
|------|-------------|-----|
| [Agno SQL Agent Example](https://github.com/agno-agi/agno/tree/main/cookbook/examples/apps/sql_agent) | Esempio di agente SQL costruito con il framework Agno: dato un database, l'agente genera query, le esegue e spiega i risultati in linguaggio naturale. Utile come reference per chi costruisce text-to-SQL. | `open-source` `python` `sql` `agent` `example` |
| [MindsDB](https://github.com/mindsdb/mindsdb) | Piattaforma open-source che porta AI e ML dentro al database, esponendo modelli come tabelle SQL interrogabili. Permette di costruire feature predictive, agenti e RAG su dati eterogenei senza spostarli. | `open-source` `python` `sql` `rag` `self-hostable` |
| [Plexe](https://github.com/plexe-ai/plexe) | Framework che genera modelli ML custom partendo da una descrizione in linguaggio naturale del problema e dei dati. Automatizza feature engineering, training e packaging del modello. | `open-source` `python` `automl` `no-code` |
| [Vizro](https://github.com/mckinsey/vizro) | Toolkit Python di McKinsey per costruire dashboard di data visualization basati su Plotly Dash, con configurazione dichiarativa e supporto a Vizro-AI per la generazione di grafici da prompt. Indicato per analisti e team di BI. | `open-source` `python` `visualization` `dashboard` `low-code` |
| [WrenAI](https://github.com/Canner/WrenAI) | Agente text-to-SQL open-source di Canner che traduce domande in linguaggio naturale in query SQL su data warehouse, con generazione di chart e insight. Alternativa self-hostable a soluzioni BI proprietarie. | `open-source` `self-hostable` `sql` `bi` `rag` |

### Browser & GUI Agents

| Tool | Descrizione | Tag |
|------|-------------|-----|
| OpenDIA | Estensione Chromium open-source che trasforma il browser in un agente operativo controllabile via MCP, permettendo a un LLM di leggere e agire su qualsiasi pagina. Alternativa libera a Browser-Use e Comet. | `open-source` `browser-use` `mcp` `extension` |
| Runner H | Agente AI di H Company che controlla GUI desktop e web autonomamente per portare a termine task complessi (form, ricerche, automazioni multi-app). Pensato per use case enterprise di automazione. | `agent` `automation` `enterprise` `browser-use` |
| [Simular AI](https://www.simular.ai/) | Agente desktop che automatizza task sul tuo Mac osservando lo schermo e simulando interazioni utente. Pensato per workflow ripetitivi che attraversano piu applicazioni. | `macos` `automation` `agent` `desktop` |
| [Stagehand by Browserbase](https://github.com/browserbase/stagehand) | Framework TypeScript di Browserbase per browser automation AI-driven: combina Playwright con primitive LLM (act, extract, observe) per scrivere agenti web robusti e debuggabili. | `open-source` `typescript` `browser-use` `playwright` |
| Vy by Vercept | Collaboratore AI proattivo per macOS che osserva il contesto dell'utente, suggerisce azioni e completa task automaticamente. Si pone a meta strada tra Copilot di sistema e agente personale. | `macos` `agent` `personal-assistant` |

### Vector DB & Memory

| Tool | Descrizione | Tag |
|------|-------------|-----|
| [Graphify](https://github.com/safishamsi/graphify) | Skill open-source (MIT, YC S26) per AI coding assistant che con un solo comando `/graphify .` trasforma qualsiasi cartella (codice, SQL, docs, PDF, immagini, video, MCP config, Terraform) in un knowledge graph navigabile. Usa tree-sitter per l'AST locale + LLM per le entita' nei docs + Leiden community detection (stile Microsoft GraphRAG). Output: HTML interattivo, report markdown con god-node e surprising connections, JSON queryable, server MCP opzionale. Supporta 20+ assistant (Claude Code, Codex, Cursor, Gemini CLI, ecc.) e include PR triage, callflow Mermaid auto-rigenerati a ogni commit, hook git. | `open-source` `graphrag` `knowledge-graph` `claude-code` `mcp` `python` `yc` |
| [Redis for AI](https://redis.io/redis-for-ai/) | Bundle di Redis con vector search, semantic cache e LLM memory pensato per workload AI/RAG. Permette di usare l'infrastruttura Redis esistente come vector DB e short-term memory per agenti. | `redis` `rag` `memory` `cache` `enterprise` |
| [zvec by Alibaba](https://github.com/alibaba/zvec) | Engine di vector search ad alte prestazioni open-source di Alibaba, ottimizzato per scalare retrieval semantico su miliardi di vettori. Alternativa enterprise a Faiss/Milvus. | `open-source` `alibaba` `performance` `rag` |

### Scraping

| Tool | Descrizione | Tag |
|------|-------------|-----|
| [ScrapeGraphAI](https://scrapegraphai.com/) | Libreria Python per web scraping basata su LLM: descrivi cosa estrarre in linguaggio naturale e il tool costruisce la pipeline (fetch, parse, estrazione). Ottima per scraping low-code di siti dinamici. | `open-source` `python` `llm` `rag` |

### Platforms

| Tool | Descrizione | Tag |
|------|-------------|-----|
| DeepAgent by Abacus.AI | Piattaforma AI enterprise di Abacus.AI che combina agent, RAG, fine-tuning e data science in un'unica suite gestita. Target: aziende che vogliono unificare i workload AI/ML. | `enterprise` `platform` `rag` `agent` |
| Genspark | Motore di ricerca agentico che combina LLM e tool d'azione per produrre risposte sintetiche con citazioni e mini-app interattive (Sparkpages). Si posiziona come alternativa a Perplexity con focus su workflow. | `search` `agent` `consumer` |
| [Google AI Studio](https://aistudio.google.com/) | Web IDE gratuito di Google per prototipare con i modelli Gemini: prompt design, function calling, multimodal e generazione di chiavi API. Punto di ingresso per sviluppatori che vogliono usare Gemini. | `google` `free` `gemini` `ide` |
| [Google Vids](https://workspace.google.com/products/vids/) | Editor video AI di Google Workspace che genera video da prompt, script o documenti combinando stock, voiceover e template. Pensato per training, comunicazioni interne e marketing rapido. | `google` `video` `workspace` `no-code` |
| [HuggingFace Spaces](https://huggingface.co/docs/hub/spaces) | Piattaforma per deployare demo e applicazioni ML basate su Gradio, Streamlit o Docker direttamente da un repository Hugging Face. Standard de facto per pubblicare prototipi e showcase di modelli AI. | `huggingface` `deployment` `free` `python` |
| Manus | Agente AI generale autonomo cinese capace di pianificare ed eseguire task complessi end-to-end (ricerca, scraping, scrittura, automazione). Si presenta come alternativa cloud agli agent framework self-hosted. | `agent` `autonomous` `cloud` |

### Models

| Tool | Descrizione | Tag |
|------|-------------|-----|
| [Qwen3-Coder](https://github.com/QwenLM/Qwen3-Coder) | Famiglia di modelli LLM open-weight di Alibaba specializzati per il coding e l'agentic coding, con varianti fino a 480B parametri MoE e supporto a contesti molto lunghi. Tra i migliori open per task di programmazione. | `open-source` `alibaba` `coding` `open-weights` |
| [VibeVoice](https://microsoft.github.io/VibeVoice/) | Modello TTS open-source di Microsoft Research per la generazione di parlato lungo, espressivo e multi-speaker. Pensato per audiobook, podcast e dialoghi sintetici di alta qualita. | `open-source` `microsoft` `voice` `tts` |

### Tools & Utilities

| Tool | Descrizione | Tag |
|------|-------------|-----|
| [EasyFunctionCall](https://easyfunctioncall.com/tool) | Tool che semplifica la definizione e l'invocazione di function calling lato LLM, generando schemi JSON pronti all'uso. Pensato per chi vuole prototipare agenti tool-using senza scrivere boilerplate. | `function-calling` `developer-tools` |
| [MarkItDown](https://github.com/microsoft/markitdown) | Utility open-source di Microsoft che converte file di vario formato (PDF, DOCX, XLSX, immagini, audio) in Markdown ottimizzato per l'ingestion in LLM. Comodo come pre-processore per pipeline RAG. | `open-source` `python` `microsoft` `rag` `document` |
| [Meetily](https://github.com/Zackriya-Solutions/meetily) | Assistente AI per riunioni privacy-first, 100% locale e self-hosted: trascrizione live (Parakeet/Whisper, fino a 4x più veloce), diarizzazione degli speaker e sintesi via Ollama. Note-taker open-source per macOS e Windows, senza cloud. | `open-source` `meeting-notes` `transcription` `self-hosted` `privacy` `whisper` `local-ai` `rust` |
| [MiroFish](https://github.com/666ghj/MiroFish) | Tool open-source che integra Miro con LLM per generare e manipolare board Miro tramite prompt: utile per brainstorming, mappe mentali e diagrammi assistiti da AI. | `open-source` `miro` `collaboration` |
| [NotebookLM Python API (unofficial)](https://github.com/teng-lin/notebooklm-py) | Wrapper Python non ufficiale per interagire programmaticamente con Google NotebookLM, permettendo di creare notebook, caricare fonti e generare audio overview da script. | `open-source` `python` `google` `notebooklm` `unofficial` |
| [Open Notebook](https://github.com/lfnovo/open-notebook) | Alternativa open-source e self-hostable a Google NotebookLM per la ricerca AI-assistita: ingestione di fonti eterogenee (PDF, web, audio, video), chat contestuale, note strutturate e generazione di podcast. Privacy-first, supporta modelli locali e cloud. | `open-source` `self-hostable` `python` `notebooklm` `rag` `privacy` |
| [open-design by Nexu.io](https://github.com/nexu-io/open-design) | Tool open-source che genera design system e componenti UI a partire da prompt o brief, con focus su consistenza e tokens. Pensato come alternativa libera a tool come Stitch o v0. | `open-source` `design` `ui` |
| [PageIndex by VectifyAI](https://github.com/VectifyAI/PageIndex) | Sistema di document retrieval reasoning-based che organizza documenti come alberi gerarchici per migliorare il recall su documenti lunghi e complessi (paper, contratti, manuali). Alternativa al chunk-based RAG classico. | `open-source` `rag` `document` `python` |
| [PentesterFlow Agent](https://github.com/PentesterFlow/agent) | Agente AI di offensive security che opera da terminale: automazione di penetration testing, security audit e bug bounty tramite un approccio agentico, eseguendo ricognizione e test di sicurezza in autonomia. | `open-source` `security` `penetration-testing` `ai-agent` `bug-bounty` `cli` `typescript` |
| [Redamon](https://github.com/samugit83/redamon) | Tool open-source di AI red teaming per testare la sicurezza di applicazioni LLM con attacchi automatizzati (prompt injection, jailbreak, data exfiltration). Utile per security team. | `open-source` `security` `red-team` `evaluation` |
| [Repomix](https://github.com/yamadashy/repomix) | Tool open-source che impacchetta l'intero repository in un unico file ottimizzato per LLM, con output XML, Markdown o testo, esclusione via .gitignore e conteggio token. Standard di fatto per preparare codebase come contesto per agenti AI. | `open-source` `cli` `rag` `context-management` `developer-tools` |
| [Stitch by Google](https://stitch.withgoogle.com/) | Tool sperimentale di Google Labs che genera UI design e codice frontend a partire da una descrizione testuale o da uno sketch. Output esportabile verso Figma o codice HTML/CSS. | `google` `design` `ui` `code-generation` |

## Risorse

- [Agensi.io](https://www.agensi.io/skills) — Marketplace di skill AI con revisione di sicurezza obbligatoria prima dell'approvazione, suddivise per categoria d'uso. Include skill gratuite e a pagamento, utile quando l'agente deve accedere a file o account sensibili.
- Agentic Design Patterns — Documento Google Docs collaborativo che raccoglie pattern ricorrenti nello sviluppo di agenti AI (planner, reflection, tool-use, multi-agent collaboration). Riferimento didattico molto citato.
- [AgentSkill.sh](https://agentskill.sh/) — Marketplace di skill per Claude Code che assegna un security score a ogni skill, fondamentale quando l'AI deve accedere a file o account. Buon filtro qualitativo rispetto alle liste non moderate.
- [AgentSkills - Skills Reference](https://github.com/agentskills/agentskills/tree/main/skills-ref) — Repository di reference per Claude Skills e pattern di skill engineering, con esempi pronti all'uso per estendere agenti AI con capacita modulari.
- [Andrej Karpathy Skills](https://github.com/forrestchang/andrej-karpathy-skills) — Raccolta di Claude Skills ispirate allo stile e ai workflow di Andrej Karpathy, con focus su scrittura tecnica, codice ML e analisi di paper.
- [Anthropic Skills Repository](https://github.com/anthropics/skills) — Repository ufficiale di Anthropic con skill pronte all'uso per Claude Code: workflow strutturati, integrazioni e utility che estendono le capacita dell'agente. Punto di partenza canonico per esplorare o creare skill.
- [Awesome Agentic Patterns](https://github.com/nibzard/awesome-agentic-patterns) — Lista curata di pattern, best practice e paper sui sistemi agentici, mantenuta dalla community. Riferimento per studiare l'evoluzione dei design pattern degli agenti AI.
- [Awesome Claude Code](https://github.com/hesreallyhim/awesome-claude-code) — Lista curata dalla community con le migliori risorse per Claude Code: skill, plugin, configurazioni, articoli e workflow. Riferimento principale per chi vuole massimizzare Claude come coding agent.
- [Awesome Claude Code Subagents (VoltAgent)](https://github.com/VoltAgent/awesome-claude-code-subagents) — Raccolta curata di subagenti specializzati per Claude Code, organizzati per dominio d'uso. Ogni subagente ha profilo, tool set e CLAUDE.md che ne definisce il comportamento. Ottimo per estendere Claude con agenti verticali pronti all'uso.
- [Awesome Italian PA Open Source](https://github.com/stefanosalvucci/awesome-italian-pa-opensource) — Lista curata di librerie e tool open-source per integrare i servizi della Pubblica Amministrazione italiana in applicazioni software. Copre autenticazione SPID, fatturazione elettronica, PEC, firma digitale, sanità e molto altro — centinaia di progetti organizzati per categoria, pensati per sviluppatori italiani che devono interfacciarsi con sistemi governativi.
- [Awesome LLM Apps](https://github.com/Shubhamsaboo/awesome-llm-apps) — Repository curata con decine di esempi di app LLM e agenti, dai chatbot RAG ai sistemi multi-agent. Ottimo punto di partenza per imparare pattern e architetture comuni.
- [BigQuery Continuous Queries](https://cloud.google.com/bigquery/docs/continuous-queries-introduction) — Funzionalita di Google BigQuery che esegue query SQL in modo continuo su dati in streaming, ideale per pipeline real-time che combinano analytics e modelli AI (Gemini, Vertex). Documentazione e introduzione ufficiale.
- Chess Game Fine-Tuning Example — Tutorial/articolo che mostra come fine-tunare un LLM su partite di scacchi per insegnargli regole, aperture e strategie. Esempio didattico per capire il fine-tuning task-specific.
- [ClaudeMarketPlaces](https://claudemarketplaces.com/skills) — Marketplace community con centinaia di skill per Claude Code, navigabili per categoria con sistema di votazione. Piattaforma principale per scoprire e condividere skill Claude pronte all'uso.
- Dash: Self-Learning Data Agent — Articolo che presenta Dash, agente AI che apprende continuamente dai dati e dai feedback dell'utente per fare query analytics in linguaggio naturale.
- Designing Smart Multi-Agent Workflows — Articolo che analizza pattern e trade-off nel design di workflow multi-agente: orchestrator vs swarm, gestione dello stato, handoff. Lettura di riferimento per chi progetta sistemi agentivi.
- [Ematching - Sinon's Blog](https://blog.vortan.dev/ematching/) — Articolo tecnico che esplora tecniche di embedding matching e retrieval semantico, con esempi pratici e considerazioni sulla qualita del recupero. Lettura utile per chi progetta sistemi RAG.
- [Google Always-On Memory Agent](https://github.com/GoogleCloudPlatform/generative-ai/tree/main/gemini/agents/always-on-memory-agent) — Esempio ufficiale di Google Cloud che mostra come costruire un agente con memoria sempre attiva basato su Gemini e Vertex AI. Reference per pattern di long-term memory.
- [Hugging Face AI Agents Course](https://huggingface.co/learn/agents-course/en/unit0/introduction) — Corso gratuito di Hugging Face che insegna a costruire AI agent dal livello base fino a sistemi multi-agent, con esercizi pratici, certificazione e community Discord.
- Learning Machines: Technical Design — Articolo tecnico sul design di sistemi che apprendono continuamente dall'uso (learning machines), con focus su architettura, feedback loop e valutazione.
- [MCP - DeepLearning.AI Short Course](https://www.deeplearning.ai/short-courses/mcp-build-rich-context-ai-apps-with-anthropic/) — Corso breve gratuito di DeepLearning.AI in collaborazione con Anthropic su come costruire app context-rich con MCP. Copre client, server, tool e workflow di integrazione.
- [MCP Introduction](https://modelcontextprotocol.io/introduction) — Documentazione ufficiale del Model Context Protocol di Anthropic: spiega architettura, primitive (tools, resources, prompts) e modalita di integrazione. Punto di partenza obbligato per chiunque voglia adottare MCP.
- [MCP Market](https://mcpmarket.com/) — Portale che aggrega oltre 30.000 MCP tool per connettere LLM a database, Google Drive, Slack e altri SaaS. Utile per trovare server MCP pronti all'uso senza sviluppo custom.
- [MCP Servers Repository](https://github.com/modelcontextprotocol/servers) — Repository ufficiale che raccoglie implementazioni di server MCP di riferimento (filesystem, git, Slack, Postgres e molti altri) e contributi community. Riferimento canonico per scoprire integrazioni MCP.
- My Personal Skills for AI-assisted Node.js Development — Articolo che condivide un set di Claude Skills personali per lo sviluppo Node.js assistito da AI, con esempi concreti di organizzazione e workflow.
- [Prompt Caching - Anthropic Docs](https://docs.anthropic.com/en/docs/build-with-claude/prompt-caching) — Documentazione ufficiale Anthropic sul prompt caching per Claude: come riutilizzare grandi prefissi di contesto riducendo costi e latenza fino al 90%. Riferimento per ottimizzare app LLM in produzione.
- [Prompt Engineering Guide (DAIR.AI)](https://github.com/dair-ai/Prompt-Engineering-Guide) — Guida completa al prompt engineering di DAIR.AI: tecniche (zero-shot, few-shot, CoT, RAG, agents), best practice e paper di riferimento. La risorsa educativa piu citata sull'argomento, aggiornata continuamente.
- Reasoning Agents — Articolo che approfondisce gli agenti basati su reasoning models (o1, R1, ecc.), discutendo come cambiano architettura e prompting rispetto agli agenti tradizionali.
- Run AI Agents on Raspberry Pi — Articolo/tutorial che mostra come far girare agenti AI con LLM locali su Raspberry Pi, ottimizzando memoria e latenza per edge deployment.
- [Skills.sh](https://skills.sh/) — Marketplace di skill Claude Code con focus su sviluppo web e programmazione. Raccolta curata di skill per workflow frontend, backend e tooling per sviluppatori.
- [Unwind AI](https://www.theunwindai.com/) — Newsletter e portale che curano le novita su LLM apps, agenti e infrastruttura AI con tutorial pratici. Gestiscono anche il repo awesome-llm-apps.
- Why I Switched from Cursor to Claude Code — Articolo opinione che confronta Cursor e Claude Code dal punto di vista di un dev, analizzando workflow agentivo, autonomia e UX. Lettura utile per chi sta valutando un coding assistant.

## Statistiche

- **108** item totali
- **76** tool/prodotti
- **32** risorse (articoli, corsi, doc, awesome list)
- **14** categorie utilizzate



---

*Contribuisci aprendo una PR che aggiorna [`tools.json`](tools.json). Il
workflow GitHub Actions in `.github/workflows/validate.yml` valida
automaticamente il JSON a ogni push.*

