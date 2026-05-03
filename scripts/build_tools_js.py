"""Generate tools.js from tools.json so the static site works on file://."""
from __future__ import annotations

import json
from pathlib import Path

ROOT = Path(__file__).resolve().parent.parent
SRC = ROOT / "tools.json"
DST = ROOT / "tools.js"


def main() -> None:
    data = json.loads(SRC.read_text(encoding="utf-8"))
    payload = json.dumps(data, ensure_ascii=False, indent=2)
    DST.write_text(
        f"// Auto-generated from tools.json. Do not edit by hand.\n"
        f"window.TOOLS_DATA = {payload};\n",
        encoding="utf-8",
    )
    print(f"Wrote {DST.relative_to(ROOT)} with {len(data)} items")


if __name__ == "__main__":
    main()
