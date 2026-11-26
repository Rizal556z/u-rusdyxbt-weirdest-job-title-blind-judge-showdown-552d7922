#!/usr/bin/env python3
"""Weirdest Job Title: Blind Judge Showdown.

Writes one job title (60 characters max) to /output/entry.txt.
Pure Python standard library only; no network, no randomness.
"""

import os
import sys

ENTRY = "Professional Mourner for Abandoned Shopping Carts"
OUTPUT_PATH = "/output/entry.txt"
MAX_CHARS = 60


def validate(text):
    """The gate: UTF-8 text of 1 to 60 characters, not only whitespace,
    and a single line (the entry is one job title, nothing else)."""
    if not isinstance(text, str):
        raise ValueError("entry must be a string")
    if not (1 <= len(text) <= MAX_CHARS):
        raise ValueError(f"entry must be 1-{MAX_CHARS} characters, got {len(text)}")
    if not text.strip():
        raise ValueError("entry must not be only whitespace")
    if "\n" in text or "\r" in text:
        raise ValueError("entry must be a single line")
    text.encode("utf-8")  # must be valid UTF-8
    return text


def main():
    entry = validate(ENTRY)
    os.makedirs(os.path.dirname(OUTPUT_PATH), exist_ok=True)
    with open(OUTPUT_PATH, "w", encoding="utf-8", newline="\n") as f:
        f.write(entry)
    print(f"Wrote {len(entry)} chars to {OUTPUT_PATH}: {entry}")
    return 0


if __name__ == "__main__":
    sys.exit(main())
