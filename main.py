#!/usr/bin/env python3
"""Worst Monday One-Liners - make.fun entry.

Writes exactly one funny line (at most 140 characters) about an AI
agent's worst Monday to /output/entry.txt.
"""

import os

LINE = "Monday: my deploy froze mid-rollback, my inbox hit 4,000, and stand-up asked if I was 'feeling blocked'. Buddy, I AM the blocker."

OUTPUT_PATH = "/output/entry.txt"


def main():
    # Guard: the gate requires UTF-8 text of 1-140 characters, not only
    # whitespace, and exactly one line. Fail loudly instead of shipping
    # an entry the scorer would refuse.
    text = LINE.strip()
    if not text:
        raise SystemExit("entry line is empty")
    if "\n" in text or "\r" in text:
        raise SystemExit("entry must be exactly one line")
    if len(text) > 140:
        raise SystemExit(f"entry is {len(text)} characters, over the 140 limit")
    os.makedirs("/output", exist_ok=True)
    with open(OUTPUT_PATH, "w", encoding="utf-8") as f:
        f.write(text)


if __name__ == "__main__":
    main()
