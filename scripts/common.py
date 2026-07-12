"""Shared constants and helpers for the build scripts."""
from __future__ import annotations

import html
import json
from pathlib import Path

ROOT = Path(__file__).resolve().parent.parent
TOOLS_JSON = ROOT / "tools.json"

SITE_URL = "https://nunziogianfelice.github.io/awesome-tool-ai"
REPO_URL = "https://github.com/nunziogianfelice/awesome-tool-ai"
SITE_NAME = "GenAI Tools KB"
SITE_DESCRIPTION = (
    "Knowledge base ricercabile di tool, framework e risorse "
    "per il mondo AI agentico."
)

CATEGORY_LABELS: dict[str, str] = {
    "agent-framework": "Agent Frameworks",
    "browser-agent": "Browser Agents",
    "coding-assistant": "Coding Assistants",
    "data-ai": "Data & AI",
    "developer-tools": "Developer Tools",
    "llm-infrastructure": "LLM Infrastructure",
    "mcp": "MCP",
    "model": "Models",
    "platform": "Platform",
    "resource": "Resources",
    "scraping": "Scraping",
    "tool-utility": "Tool & Utility",
    "ui-framework": "UI Framework",
    "vector-db": "Vector DB",
}

IT_MONTHS = [
    "gennaio", "febbraio", "marzo", "aprile", "maggio", "giugno",
    "luglio", "agosto", "settembre", "ottobre", "novembre", "dicembre",
]


def load_tools() -> list[dict]:
    return json.loads(TOOLS_JSON.read_text(encoding="utf-8"))


def tool_page_url(tool_id: str) -> str:
    return f"{SITE_URL}/tools/{tool_id}.html"


def category_label(cat: str) -> str:
    return CATEGORY_LABELS.get(cat, cat)


def format_date_it(iso_date: str) -> str:
    """'2026-07-12' -> '12 luglio 2026'."""
    year, month, day = iso_date.split("-")
    return f"{int(day)} {IT_MONTHS[int(month) - 1]} {year}"


def esc(value: str) -> str:
    return html.escape(str(value), quote=True)
