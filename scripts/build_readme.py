"""Generate README.md from tools.json with per-category tables."""
from __future__ import annotations

import json
from pathlib import Path

ROOT = Path(__file__).resolve().parent.parent
SRC = ROOT / "tools.json"
DST = ROOT / "README.md"

CATEGORY_ORDER = [
    ("agent-framework", "Agent Frameworks"),
    ("mcp", "MCP (Model Context Protocol)"),
    ("coding-assistant", "Coding Assistants"),
    ("llm-infrastructure", "LLM Infrastructure"),
    ("data-ai", "Data & AI"),
    ("browser-agent", "Browser & GUI Agents"),
    ("vector-db", "Vector DB & Memory"),
    ("scraping", "Scraping"),
    ("platform", "Platforms"),
    ("model", "Models"),
    ("tool-utility", "Tools & Utilities"),
]

HEADER = """# 🤖 GenAI Tools KB

> Knowledge base di tool, framework e risorse per il mondo AI agentivo.
> Aggiornata continuamente.

## Ricerca rapida

Clona il repo e apri `index.html` per la ricerca interattiva (funziona anche
da `file://`), oppure consulta direttamente le tabelle qui sotto.

```bash
git clone <repo>
cd genai-tools-kb
open index.html  # macOS
```

I dati canonici vivono in [`tools.json`](tools.json). Il file
[`tools.js`](tools.js) e una copia auto-generata che permette al frontend
statico di funzionare senza un server HTTP. Rigeneralo con:

```bash
python3 scripts/build_tools_js.py
```
"""

FOOTER = """

---

*Contribuisci aprendo una PR che aggiorna [`tools.json`](tools.json). Il
workflow GitHub Actions in `.github/workflows/validate.yml` valida
automaticamente il JSON a ogni push.*
"""


def render_link(item: dict) -> str:
    name = item["name"]
    url = item.get("url")
    return f"[{name}]({url})" if url else name


def render_tags(item: dict) -> str:
    tags = item.get("tags") or []
    return " ".join(f"`{t}`" for t in tags) if tags else ""


def main() -> None:
    data = json.loads(SRC.read_text(encoding="utf-8"))
    by_cat: dict[str, list[dict]] = {}
    for item in data:
        by_cat.setdefault(item["category"], []).append(item)
    for items in by_cat.values():
        items.sort(key=lambda x: x["name"].lower())

    out: list[str] = [HEADER, "\n## Tool per categoria\n"]

    used_tool_cats = {cat for cat, _ in CATEGORY_ORDER if cat in by_cat}
    for cat, label in CATEGORY_ORDER:
        items = by_cat.get(cat)
        if not items:
            continue
        out.append(f"\n### {label}\n")
        out.append("| Tool | Descrizione | Tag |")
        out.append("|------|-------------|-----|")
        for item in items:
            out.append(
                f"| {render_link(item)} | {item['description']} | {render_tags(item)} |"
            )

    # Resources section
    resources = by_cat.get("resource") or []
    if resources:
        out.append("\n## Risorse\n")
        for item in sorted(resources, key=lambda x: x["name"].lower()):
            link = render_link(item)
            out.append(f"- {link} — {item['description']}")

    # Stats
    total = len(data)
    n_resources = len(resources)
    n_tools = total - n_resources
    n_categories = len({i["category"] for i in data})
    out.append(
        f"\n## Statistiche\n\n"
        f"- **{total}** item totali\n"
        f"- **{n_tools}** tool/prodotti\n"
        f"- **{n_resources}** risorse (articoli, corsi, doc, awesome list)\n"
        f"- **{n_categories}** categorie utilizzate\n"
    )

    out.append(FOOTER)
    DST.write_text("\n".join(out) + "\n", encoding="utf-8")
    print(f"Wrote {DST.relative_to(ROOT)}")


if __name__ == "__main__":
    main()
