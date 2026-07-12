# awesome-tool-ai MCP server

Server MCP (stdio) che espone la knowledge base
[awesome-tool-ai](https://nunziogianfelice.github.io/awesome-tool-ai/) a
Claude Code, Claude Desktop e qualsiasi client MCP.

All'avvio scarica `tools.json` dal sito pubblico (cache in memoria, refresh
ogni ora); se offline usa il file locale del repo come fallback.

## Tool esposti

| Tool | Descrizione |
|------|-------------|
| `search_tools(query, category?, tag?, limit=10)` | Ricerca full-text su nome, descrizione e tag |
| `get_tool(id)` | Scheda completa di un tool + URL della pagina |
| `list_categories()` | Categorie con conteggi |

## Avvio rapido

```bash
# dal repo clonato
uv run --directory mcp awesome-tool-ai-mcp

# oppure senza clonare nulla
uvx --from "git+https://github.com/nunziogianfelice/awesome-tool-ai#subdirectory=mcp" awesome-tool-ai-mcp
```

## Configurazione Claude Code

```bash
claude mcp add awesome-tool-ai -- uvx --from "git+https://github.com/nunziogianfelice/awesome-tool-ai#subdirectory=mcp" awesome-tool-ai-mcp
```

## Configurazione Claude Desktop

In `claude_desktop_config.json`:

```json
{
  "mcpServers": {
    "awesome-tool-ai": {
      "command": "uvx",
      "args": [
        "--from",
        "git+https://github.com/nunziogianfelice/awesome-tool-ai#subdirectory=mcp",
        "awesome-tool-ai-mcp"
      ]
    }
  }
}
```

## Sviluppo e test

```bash
cd mcp
uv run fastmcp dev server.py   # inspector interattivo
```
