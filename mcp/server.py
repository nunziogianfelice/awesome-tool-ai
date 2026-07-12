"""MCP server for the awesome-tool-ai knowledge base.

Fetches tools.json from the public GitHub Pages site, caches it in memory
(1 h TTL) and falls back to the local repo copy when offline.
"""
from __future__ import annotations

import json
import time
from pathlib import Path
from typing import Any

import httpx
from fastmcp import FastMCP

SITE_URL = "https://nunziogianfelice.github.io/awesome-tool-ai"
TOOLS_URL = f"{SITE_URL}/tools.json"
LOCAL_FALLBACK = Path(__file__).resolve().parent.parent / "tools.json"
CACHE_TTL_SECONDS = 3600

mcp = FastMCP(
    "awesome-tool-ai",
    instructions=(
        "Knowledge base curata di tool, framework e risorse per l'AI "
        "agentica (agent framework, MCP, coding assistant, ...). "
        "Usa search_tools per cercare, get_tool per i dettagli, "
        "list_categories per esplorare."
    ),
)

_cache: dict[str, Any] = {"data": None, "fetched_at": 0.0}


def _page_url(tool_id: str) -> str:
    return f"{SITE_URL}/tools/{tool_id}.html"


def _load_tools() -> list[dict[str, Any]]:
    """Return the tool list, refreshing the in-memory cache when stale."""
    now = time.monotonic()
    if _cache["data"] is not None and now - _cache["fetched_at"] < CACHE_TTL_SECONDS:
        return _cache["data"]
    try:
        resp = httpx.get(TOOLS_URL, timeout=10.0, follow_redirects=True)
        resp.raise_for_status()
        _cache["data"] = resp.json()
        _cache["fetched_at"] = now
        return _cache["data"]
    except (httpx.HTTPError, json.JSONDecodeError):
        if _cache["data"] is not None:  # stale cache beats nothing
            return _cache["data"]
        if LOCAL_FALLBACK.exists():
            _cache["data"] = json.loads(LOCAL_FALLBACK.read_text(encoding="utf-8"))
            _cache["fetched_at"] = now
            return _cache["data"]
        raise


def _summary(tool: dict[str, Any]) -> dict[str, Any]:
    return {
        "id": tool["id"],
        "name": tool["name"],
        "description": tool.get("description", ""),
        "category": tool["category"],
        "tags": tool.get("tags", []),
        "pricing": tool.get("pricing"),
        "url": tool.get("url"),
        "page_url": _page_url(tool["id"]),
    }


@mcp.tool
def search_tools(
    query: str,
    category: str | None = None,
    tag: str | None = None,
    limit: int = 10,
) -> list[dict[str, Any]]:
    """Cerca tool nella knowledge base (full-text su nome, descrizione, tag).

    Args:
        query: Testo da cercare (case-insensitive). Stringa vuota = tutti.
        category: Filtra per categoria esatta (vedi list_categories).
        tag: Filtra per tag esatto.
        limit: Numero massimo di risultati (default 10).
    """
    q = query.strip().lower()
    results: list[tuple[int, str, dict[str, Any]]] = []
    for tool in _load_tools():
        if category and tool.get("category") != category:
            continue
        if tag and tag not in (tool.get("tags") or []):
            continue
        if q:
            name = tool.get("name", "").lower()
            desc = tool.get("description", "").lower()
            tags = " ".join(tool.get("tags") or []).lower()
            if q in name:
                score = 3
            elif q in tags:
                score = 2
            elif q in desc:
                score = 1
            else:
                continue
        else:
            score = 0
        results.append((-score, tool.get("name", "").lower(), tool))
    results.sort(key=lambda entry: entry[:2])
    return [_summary(tool) for _, _, tool in results[: max(1, limit)]]


@mcp.tool
def get_tool(id: str) -> dict[str, Any]:
    """Restituisce la scheda completa di un tool dato il suo id.

    Args:
        id: Identificatore del tool (es. "langgraph"). Usa search_tools
            per trovarlo.
    """
    for tool in _load_tools():
        if tool["id"] == id:
            return {**tool, "page_url": _page_url(tool["id"])}
    raise ValueError(f"Nessun tool con id '{id}'. Usa search_tools per cercarlo.")


@mcp.tool
def list_categories() -> list[dict[str, Any]]:
    """Elenca le categorie della knowledge base con il conteggio dei tool."""
    counts: dict[str, int] = {}
    for tool in _load_tools():
        counts[tool["category"]] = counts.get(tool["category"], 0) + 1
    return [
        {"category": cat, "count": count}
        for cat, count in sorted(counts.items())
    ]


def main() -> None:
    mcp.run()


if __name__ == "__main__":
    main()
