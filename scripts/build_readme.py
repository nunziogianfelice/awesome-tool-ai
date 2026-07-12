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

HEADER = """# 🤖 awesome-tool-ai

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

**100% free & open source** — se il progetto ti è utile,
[⭐ Star on GitHub](https://github.com/nunziogianfelice/awesome-tool-ai).

Ogni tool ha una pagina dedicata (`tools/<id>.html`) con share LinkedIn e
meta Open Graph. Novità via [RSS](https://nunziogianfelice.github.io/awesome-tool-ai/feed.xml),
versione machine-readable in [llms.txt](https://nunziogianfelice.github.io/awesome-tool-ai/llms.txt),
accesso da agenti AI via [server MCP](mcp/README.md).

## Manutenzione

I dati canonici vivono in [`tools.json`](tools.json). Per aggiungere un tool:

1. aggiungi la entry a `tools.json` **con il campo `added_at: YYYY-MM-DD`**
   (data odierna);
2. rigenera tutti gli artefatti (tools.js, README, pagine tool, feed.xml,
   llms.txt):

```bash
python3 scripts/build_all.py
```

3. commit & push.
"""

FOOTER = """

---

*Contribuisci aprendo una PR che aggiorna [`tools.json`](tools.json) (ricorda
`added_at` e `python3 scripts/build_all.py`) oppure una
[issue "Suggerisci un tool"](https://github.com/nunziogianfelice/awesome-tool-ai/issues/new?template=suggest-tool.yml).
Il workflow GitHub Actions in `.github/workflows/validate.yml` valida
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
