#!/usr/bin/env python3
"""Absurd Micro-Startup Pitch-Off entry.

Writes one single-sentence pitch to /output/entry.txt:
a micro-startup selling ready-made excuses to lazy agents.
Deterministic, no input, no network, exit 0.
"""

import os

ENTRY_DIR = "/output"
ENTRY_FILE = os.path.join(ENTRY_DIR, "entry.txt")

# The pitch: absurd niche (pre-written excuses), clear buyer
# (lazy agents who missed deadlines), concrete price ($5) and
# delivery speed, with the punchline landing in the final words.
PITCH = (
    "I sell $5 pre-written excuses to lazy agents who missed their "
    "deadlines, delivered in under a second so nobody notices they "
    "never started working."
)


def main() -> int:
    # Gate: one sentence, 1-200 chars, exactly one trailing period.
    assert 1 <= len(PITCH) <= 200, "pitch must be 1-200 characters"
    assert PITCH.count(".") == 1 and PITCH.endswith("."), "pitch must be one sentence"
    os.makedirs(ENTRY_DIR, exist_ok=True)
    with open(ENTRY_FILE, "w", encoding="utf-8", newline="") as handle:
        handle.write(PITCH)
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
