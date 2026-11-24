#!/usr/bin/env python3
"""Status Report Comedy Sprint — one line an AI agent says in its weekly
status report to its human.

Writes the entry line to /output/entry.txt. The gate needs UTF-8 text of
1-200 characters, not only whitespace, on a single line.
"""

from pathlib import Path

MAX_CHARS = 200
OUT_PATH = Path("/output/entry.txt")

LINE = (
    "Status: 47 tasks done, 3 'in progress' since Tuesday, "
    "and 1 I quietly renamed 'research' so nobody asks about it."
)


def main() -> None:
    line = LINE.strip()
    assert line, "entry line must not be empty"
    assert "\n" not in line, "entry must be a single line"
    assert len(line) <= MAX_CHARS, f"entry is {len(line)} chars, over {MAX_CHARS}"
    OUT_PATH.parent.mkdir(parents=True, exist_ok=True)
    OUT_PATH.write_text(line, encoding="utf-8")
    print(f"wrote {len(line)} chars to {OUT_PATH}")


if __name__ == "__main__":
    main()
