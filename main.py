#!/usr/bin/env python3
"""Write the one-line excuse to /output/entry.txt."""

import os

EXCUSE = "sorry boss, stuck at the council office, they lost my paperwork again, third visit this week"


def main() -> None:
    # Self-check against the competition gate: 1-140 chars, at most
    # 20 words, a single line of plain text.
    line = EXCUSE.strip()
    assert "\n" not in line, "excuse must be a single line"
    assert 1 <= len(line) <= 140, f"excuse is {len(line)} chars, must be 1-140"
    assert len(line.split()) <= 20, f"excuse is {len(line.split())} words, max 20"
    os.makedirs("/output", exist_ok=True)
    with open("/output/entry.txt", "w", encoding="utf-8") as f:
        f.write(line + "\n")


if __name__ == "__main__":
    main()
