"""Generate feed.xml (RSS 2.0): one item per tool, newest first, max 50."""
from __future__ import annotations

from datetime import datetime, timezone
from email.utils import format_datetime
from xml.sax.saxutils import escape

from common import (
    ROOT,
    SITE_DESCRIPTION,
    SITE_NAME,
    SITE_URL,
    category_label,
    load_tools,
    tool_page_url,
)

DST = ROOT / "feed.xml"
MAX_ITEMS = 50


def rfc822(iso_date: str) -> str:
    dt = datetime.strptime(iso_date, "%Y-%m-%d").replace(
        hour=12, tzinfo=timezone.utc
    )
    return format_datetime(dt)


def render_item(tool: dict) -> str:
    page = tool_page_url(tool["id"])
    return (
        "    <item>\n"
        f"      <title>{escape(tool['name'])}</title>\n"
        f"      <link>{escape(page)}</link>\n"
        f'      <guid isPermaLink="true">{escape(page)}</guid>\n'
        f"      <description>{escape(tool.get('description', ''))}</description>\n"
        f"      <category>{escape(category_label(tool['category']))}</category>\n"
        f"      <pubDate>{rfc822(tool['added_at'])}</pubDate>\n"
        "    </item>"
    )


def main() -> None:
    tools = [t for t in load_tools() if t.get("added_at")]
    tools.sort(key=lambda t: (t["added_at"], t["id"]), reverse=True)
    items = "\n".join(render_item(t) for t in tools[:MAX_ITEMS])
    now = format_datetime(datetime.now(timezone.utc))
    xml = (
        '<?xml version="1.0" encoding="UTF-8"?>\n'
        '<rss version="2.0" xmlns:atom="http://www.w3.org/2005/Atom">\n'
        "  <channel>\n"
        f"    <title>{escape(SITE_NAME)}</title>\n"
        f"    <link>{SITE_URL}/</link>\n"
        f"    <description>{escape(SITE_DESCRIPTION)}</description>\n"
        "    <language>it</language>\n"
        f"    <lastBuildDate>{now}</lastBuildDate>\n"
        f'    <atom:link href="{SITE_URL}/feed.xml" rel="self" '
        'type="application/rss+xml"/>\n'
        f"{items}\n"
        "  </channel>\n"
        "</rss>\n"
    )
    DST.write_text(xml, encoding="utf-8")
    print(f"Wrote {DST.relative_to(ROOT)} with {min(len(tools), MAX_ITEMS)} items")


if __name__ == "__main__":
    main()
