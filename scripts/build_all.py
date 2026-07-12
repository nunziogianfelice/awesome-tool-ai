"""Run the full site build: tools.js, README, tool pages, feed, llms.txt."""
from __future__ import annotations

import subprocess
import sys
from pathlib import Path

SCRIPTS = Path(__file__).resolve().parent

STEPS = [
    "build_tools_js.py",
    "build_readme.py",
    "build_tool_pages.py",
    "build_feed.py",
    "build_llms_txt.py",
]


def main() -> None:
    for step in STEPS:
        print(f"==> {step}")
        subprocess.run([sys.executable, str(SCRIPTS / step)], check=True)
    print("Build complete.")


if __name__ == "__main__":
    main()
