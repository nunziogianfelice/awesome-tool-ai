"""Generate llms.txt: one-line intro + tool list in llms.txt format."""
from __future__ import annotations

from common import (
    ROOT,
    SITE_DESCRIPTION,
    SITE_NAME,
    category_label,
    load_tools,
    tool_page_url,
)
from build_tool_pages import one_liner

DST = ROOT / "llms.txt"


def main() -> None:
    tools = load_tools()
    by_cat: dict[str, list[dict]] = {}
    for tool in tools:
        by_cat.setdefault(tool["category"], []).append(tool)

    lines: list[str] = [f"# {SITE_NAME}", "", f"> {SITE_DESCRIPTION}", ""]
    for cat in sorted(by_cat):
        lines.append(f"## {category_label(cat)}")
        lines.append("")
        for tool in sorted(by_cat[cat], key=lambda t: t["name"].lower()):
            brief = one_liner(tool.get("description", ""))
            url = tool.get("url") or tool_page_url(tool["id"])
            lines.append(
                f"- [{tool['name']}]({url}): {brief} "
                f"(dettagli: {tool_page_url(tool['id'])})"
            )
        lines.append("")

    DST.write_text("\n".join(lines), encoding="utf-8")
    print(f"Wrote {DST.relative_to(ROOT)} with {len(tools)} tools")


if __name__ == "__main__":
    main()
