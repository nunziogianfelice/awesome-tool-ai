"""One-shot: backfill `added_at` in tools.json from the real git history.

Walks every commit touching tools.json (oldest first), parses the file at
each revision and records the date of the first commit where each tool id
appears. Run once, then commit the updated tools.json.
"""
from __future__ import annotations

import json
import subprocess
from pathlib import Path

ROOT = Path(__file__).resolve().parent.parent
SRC = ROOT / "tools.json"


def git(*args: str) -> str:
    return subprocess.run(
        ["git", "-C", str(ROOT), *args],
        check=True,
        capture_output=True,
        text=True,
    ).stdout


def first_seen_dates() -> dict[str, str]:
    """Map tool id -> ISO date (YYYY-MM-DD) of the commit introducing it."""
    log = git("log", "--reverse", "--format=%H %cs", "--", "tools.json")
    seen: dict[str, str] = {}
    for line in log.splitlines():
        sha, date = line.split(" ", 1)
        try:
            data = json.loads(git("show", f"{sha}:tools.json"))
        except (subprocess.CalledProcessError, json.JSONDecodeError):
            continue  # revision missing or unparsable: skip it
        for item in data:
            tool_id = item.get("id")
            if tool_id and tool_id not in seen:
                seen[tool_id] = date
    return seen


def main() -> None:
    dates = first_seen_dates()
    data = json.loads(SRC.read_text(encoding="utf-8"))
    missing: list[str] = []
    for item in data:
        date = dates.get(item["id"])
        if date:
            item["added_at"] = date
        else:
            missing.append(item["id"])
    SRC.write_text(
        json.dumps(data, ensure_ascii=False, indent=2) + "\n", encoding="utf-8"
    )
    print(f"Backfilled added_at for {len(data) - len(missing)}/{len(data)} tools")
    if missing:
        print("No history found for:", ", ".join(missing))


if __name__ == "__main__":
    main()
