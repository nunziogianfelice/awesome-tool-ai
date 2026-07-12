"""Generate one static HTML page per tool in tools/<id>.html."""
from __future__ import annotations

from pathlib import Path
from urllib.parse import quote

from common import (
    REPO_URL,
    ROOT,
    SITE_NAME,
    SITE_URL,
    category_label,
    esc,
    format_date_it,
    load_tools,
    tool_page_url,
)

OUT_DIR = ROOT / "tools"

FAVICON = (
    "data:image/svg+xml,%3Csvg xmlns='http://www.w3.org/2000/svg' "
    "viewBox='0 0 64 64'%3E%3Ctext y='52' font-size='52'%3E%F0%9F%A4%96"
    "%3C/text%3E%3C/svg%3E"
)

ICON_LINKEDIN = (
    '<svg viewBox="0 0 24 24" width="16" height="16" fill="currentColor" '
    'aria-hidden="true"><path d="M20.45 20.45h-3.55v-5.57c0-1.33-.03-3.04-1.85'
    '-3.04-1.85 0-2.14 1.45-2.14 2.94v5.67H9.36V9h3.41v1.56h.05c.47-.9 1.63-1.85'
    ' 3.36-1.85 3.6 0 4.27 2.37 4.27 5.46v6.28zM5.34 7.43a2.06 2.06 0 1 1 0-4.12'
    ' 2.06 2.06 0 0 1 0 4.12zM7.12 20.45H3.56V9h3.56v11.45z"/></svg>'
)
ICON_GITHUB = (
    '<svg viewBox="0 0 24 24" width="16" height="16" fill="currentColor" '
    'aria-hidden="true"><path d="M12 .5A11.5 11.5 0 0 0 .5 12c0 5.08 3.29 9.39 '
    '7.86 10.91.58.11.79-.25.79-.55v-2.17c-3.2.7-3.87-1.36-3.87-1.36-.52-1.33-'
    '1.28-1.68-1.28-1.68-1.04-.71.08-.7.08-.7 1.15.08 1.76 1.19 1.76 1.19 1.03 '
    '1.75 2.69 1.25 3.34.95.1-.74.4-1.25.72-1.54-2.55-.29-5.24-1.28-5.24-5.68 0'
    '-1.26.45-2.28 1.19-3.09-.12-.29-.52-1.46.11-3.05 0 0 .97-.31 3.18 1.18a11'
    '.1 11.1 0 0 1 5.8 0c2.2-1.49 3.17-1.18 3.17-1.18.63 1.59.23 2.76.11 3.05.'
    '74.81 1.19 1.83 1.19 3.09 0 4.41-2.69 5.38-5.25 5.67.41.35.77 1.04.77 2.1'
    'v3.11c0 .3.21.66.8.55A11.5 11.5 0 0 0 23.5 12 11.5 11.5 0 0 0 12 .5z"/>'
    "</svg>"
)
ICON_LINK = (
    '<svg viewBox="0 0 24 24" width="16" height="16" fill="none" '
    'stroke="currentColor" stroke-width="2" stroke-linecap="round" '
    'aria-hidden="true"><path d="M10 13a5 5 0 0 0 7.54.54l3-3a5 5 0 0 0-7.07-'
    '7.07l-1.72 1.71"/><path d="M14 11a5 5 0 0 0-7.54-.54l-3 3a5 5 0 0 0 7.07 '
    '7.07l1.71-1.71"/></svg>'
)

STYLE = """
:root {
  --bg: #0b1020; --bg-elev: #131a30; --bg-card: #161e36; --border: #243056;
  --text: #e8ecf7; --text-dim: #9aa3bd; --accent: #7c9cff;
  --accent-soft: rgba(124, 156, 255, 0.15); --chip-bg: #1d2747;
  --chip-text: #b9c5ee; --badge-bg: #2a356a; --badge-text: #d6deff;
  --shadow: 0 4px 20px rgba(0, 0, 0, 0.35);
}
* { box-sizing: border-box; }
html, body {
  margin: 0; padding: 0; background: var(--bg); color: var(--text);
  font-family: -apple-system, BlinkMacSystemFont, "Segoe UI", Inter, Roboto,
    "Helvetica Neue", Arial, sans-serif;
  line-height: 1.5; -webkit-font-smoothing: antialiased;
}
a { color: var(--accent); text-decoration: none; }
a:hover { text-decoration: underline; }
.wrap { max-width: 860px; margin: 0 auto; padding: 0 24px; }
header.site { padding: 24px 0 8px; }
header.site a.back { color: var(--text-dim); font-size: 14px; }
header.site a.back:hover { color: var(--accent); }
article.tool {
  background: var(--bg-card); border: 1px solid var(--border);
  border-radius: 14px; padding: 28px; margin-top: 16px; box-shadow: var(--shadow);
}
.tool-head { display: flex; align-items: flex-start; gap: 12px; flex-wrap: wrap; }
.tool-head h1 { margin: 0; font-size: 30px; letter-spacing: -0.01em; flex: 1; }
.badge {
  font-size: 12px; padding: 5px 10px; border-radius: 6px;
  background: var(--badge-bg); color: var(--badge-text); white-space: nowrap;
}
.badge.resource { background: #3a2a5a; color: #d8c8ff; }
.meta { color: var(--text-dim); font-size: 14px; margin: 10px 0 0; }
.pricing-pill {
  display: inline-block; font-size: 12px; padding: 3px 10px;
  border-radius: 999px; background: var(--accent-soft); color: var(--accent);
  border: 1px solid var(--accent); margin-right: 8px;
}
.desc { font-size: 16px; color: var(--text); margin: 18px 0; }
.tags { display: flex; flex-wrap: wrap; gap: 8px; margin: 16px 0; }
a.tag {
  font-size: 12px; padding: 4px 10px; border-radius: 999px;
  background: var(--chip-bg); color: var(--chip-text);
  border: 1px solid transparent;
}
a.tag:hover { border-color: var(--accent); color: var(--text); text-decoration: none; }
.actions { display: flex; align-items: center; gap: 12px; flex-wrap: wrap; margin-top: 22px; }
a.btn-primary {
  display: inline-block; background: var(--accent); color: #0b1020;
  font-weight: 600; padding: 10px 18px; border-radius: 10px; font-size: 15px;
}
a.btn-primary:hover { text-decoration: none; filter: brightness(1.1); }
.share { display: flex; align-items: center; gap: 8px; }
.share-label { color: var(--text-dim); font-size: 13px; }
.share button, .share a.share-btn {
  display: inline-flex; align-items: center; gap: 6px; cursor: pointer;
  background: var(--bg-elev); border: 1px solid var(--border);
  color: var(--text-dim); border-radius: 8px; padding: 7px 10px;
  font-size: 12px; font-family: inherit; transition: all 0.12s ease;
}
.share button:hover, .share a.share-btn:hover {
  color: var(--text); border-color: var(--accent); text-decoration: none;
}
.share button.copied { color: var(--accent); border-color: var(--accent); }
section.related { margin-top: 36px; }
section.related h2 { font-size: 18px; margin: 0 0 14px; }
.rel-grid {
  display: grid; grid-template-columns: repeat(auto-fill, minmax(240px, 1fr));
  gap: 12px;
}
a.rel-card {
  display: block; background: var(--bg-card); border: 1px solid var(--border);
  border-radius: 10px; padding: 14px 16px; color: var(--text);
  transition: border-color 0.12s ease, transform 0.12s ease;
}
a.rel-card:hover { border-color: var(--accent); transform: translateY(-1px); text-decoration: none; }
a.rel-card strong { display: block; font-size: 14px; margin-bottom: 4px; }
a.rel-card span { font-size: 12px; color: var(--text-dim); display: block; }
footer.site {
  max-width: 860px; margin: 40px auto 0; padding: 20px 24px 40px;
  border-top: 1px solid var(--border); color: var(--text-dim); font-size: 13px;
  display: flex; align-items: center; gap: 14px; flex-wrap: wrap;
}
a.star-btn {
  display: inline-flex; align-items: center; gap: 6px;
  background: var(--bg-elev); border: 1px solid var(--border);
  color: var(--text); border-radius: 8px; padding: 7px 12px; font-size: 13px;
}
a.star-btn:hover { border-color: var(--accent); text-decoration: none; }
@media (max-width: 640px) {
  .wrap { padding: 0 16px; }
  article.tool { padding: 20px; }
  .tool-head h1 { font-size: 24px; }
}
"""

COPY_SCRIPT = """
document.querySelectorAll("button[data-copy]").forEach(function (btn) {
  var original = btn.innerHTML;
  btn.addEventListener("click", function () {
    navigator.clipboard.writeText(btn.dataset.copy).then(function () {
      btn.innerHTML = "copiato \\u2713";
      btn.classList.add("copied");
      setTimeout(function () {
        btn.innerHTML = original;
        btn.classList.remove("copied");
      }, 1500);
    });
  });
});
"""


def one_liner(description: str, max_len: int = 200) -> str:
    """First sentence of the description, capped at max_len chars."""
    first = description.split(". ")[0].rstrip(".") + "."
    if len(first) > max_len:
        first = first[: max_len - 1].rstrip() + "…"
    return first


def related_tools(tool: dict, tools: list[dict], limit: int = 4) -> list[dict]:
    """Rank other tools by shared tags (weighted by rarity), then category."""
    tag_freq: dict[str, int] = {}
    for other in tools:
        for t in other.get("tags") or []:
            tag_freq[t] = tag_freq.get(t, 0) + 1
    my_tags = set(tool.get("tags") or [])
    scored: list[tuple[float, int, str, dict]] = []
    for other in tools:
        if other["id"] == tool["id"]:
            continue
        shared = my_tags & set(other.get("tags") or [])
        weight = sum(1.0 / tag_freq[t] for t in shared)
        same_cat = 1 if other["category"] == tool["category"] else 0
        if shared or same_cat:
            scored.append((-weight, -same_cat, other["name"].lower(), other))
    scored.sort(key=lambda entry: entry[:3])
    return [entry[3] for entry in scored[:limit]]


def render_related(items: list[dict]) -> str:
    if not items:
        return ""
    cards = []
    for item in items:
        cards.append(
            f'<a class="rel-card" href="{esc(item["id"])}.html">'
            f"<strong>{esc(item['name'])}</strong>"
            f"<span>{esc(category_label(item['category']))} · "
            f"{esc(item.get('pricing', ''))}</span></a>"
        )
    return (
        '<section class="related"><h2>Tool correlati</h2>'
        f'<div class="rel-grid">{"".join(cards)}</div></section>'
    )


def render_page(tool: dict, tools: list[dict]) -> str:
    name = esc(tool["name"])
    page_url = tool_page_url(tool["id"])
    desc_full = tool.get("description", "")
    og_desc = esc(one_liner(desc_full))
    cat = category_label(tool["category"])
    badge_class = "badge resource" if tool.get("type") == "resource" else "badge"
    pricing = esc(tool.get("pricing", ""))
    added = tool.get("added_at")
    added_html = (
        f" · Aggiunto il {esc(format_date_it(added))}" if added else ""
    )
    tags_html = "".join(
        f'<a class="tag" href="../index.html?tag={quote(t)}">{esc(t)}</a>'
        for t in tool.get("tags") or []
    )
    tool_url = tool.get("url", "")
    linkedin = (
        "https://www.linkedin.com/sharing/share-offsite/?url="
        + quote(page_url, safe="")
    )
    visit_btn = (
        f'<a class="btn-primary" href="{esc(tool_url)}" target="_blank" '
        f'rel="noopener noreferrer">Vai al sito →</a>'
        if tool_url
        else ""
    )
    copy_gh_btn = (
        f'<button data-copy="{esc(tool_url)}" title="Copia il link del tool">'
        f"{ICON_GITHUB} link tool</button>"
        if tool_url
        else ""
    )
    return f"""<!doctype html>
<html lang="it">
  <head>
    <meta charset="utf-8" />
    <meta name="viewport" content="width=device-width, initial-scale=1" />
    <title>{name} — {SITE_NAME}</title>
    <meta name="description" content="{og_desc}" />
    <link rel="canonical" href="{page_url}" />
    <link rel="icon" href="{FAVICON}" />
    <link rel="alternate" type="application/rss+xml" title="{SITE_NAME}" href="{SITE_URL}/feed.xml" />
    <meta property="og:title" content="{name} — {SITE_NAME}" />
    <meta property="og:description" content="{og_desc}" />
    <meta property="og:url" content="{page_url}" />
    <meta property="og:type" content="website" />
    <meta property="og:site_name" content="{SITE_NAME}" />
    <meta name="twitter:card" content="summary" />
    <meta name="twitter:title" content="{name} — {SITE_NAME}" />
    <meta name="twitter:description" content="{og_desc}" />
    <style>{STYLE}</style>
  </head>
  <body>
    <div class="wrap">
      <header class="site">
        <a class="back" href="../index.html">← {SITE_NAME} — tutti i tool</a>
      </header>
      <article class="tool">
        <div class="tool-head">
          <h1>{name}</h1>
          <span class="{badge_class}">{esc(cat)}</span>
        </div>
        <p class="meta"><span class="pricing-pill">{pricing}</span>{added_html}</p>
        <p class="desc">{esc(desc_full)}</p>
        <div class="tags">{tags_html}</div>
        <div class="actions">
          {visit_btn}
          <div class="share">
            <span class="share-label">Condividi:</span>
            <a class="share-btn" href="{esc(linkedin)}" target="_blank" rel="noopener noreferrer" title="Condividi su LinkedIn">{ICON_LINKEDIN} LinkedIn</a>
            {copy_gh_btn}
            <button data-copy="{page_url}" title="Copia il link di questa pagina">{ICON_LINK} link pagina</button>
          </div>
        </div>
      </article>
      {render_related(related_tools(tool, tools))}
    </div>
    <footer class="site">
      <span>100% free &amp; open source</span>
      <a class="star-btn" href="{REPO_URL}" target="_blank" rel="noopener noreferrer">⭐ Star on GitHub</a>
    </footer>
    <script>{COPY_SCRIPT}</script>
  </body>
</html>
"""


def main() -> None:
    tools = load_tools()
    OUT_DIR.mkdir(exist_ok=True)
    valid = {f"{tool['id']}.html" for tool in tools}
    for stale in OUT_DIR.glob("*.html"):
        if stale.name not in valid:
            stale.unlink()
            print(f"Removed stale {stale.name}")
    for tool in tools:
        (OUT_DIR / f"{tool['id']}.html").write_text(
            render_page(tool, tools), encoding="utf-8"
        )
    print(f"Wrote {len(tools)} pages in {OUT_DIR.relative_to(ROOT)}/")


if __name__ == "__main__":
    main()
