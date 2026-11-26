#!/usr/bin/env python3
# SPDX-License-Identifier: MIT
"""Entry for "Rename the Planet" (make.fun).

Writes one line giving a planet of our solar system a funny new name
plus the why, to /output/entry.txt. Pure standard library; no
network, no input.
"""

import os
import sys

LINE = (
    "Rename Venus 'The Pressure Cooker': 464 degrees in the shade, "
    "acid for rain, and the whole planet spins backwards like it's "
    "trying to unscrew itself from the solar system."
)

OUTPUT_PATH = "/output/entry.txt"
MAX_CHARS = 200


def main() -> int:
    text = LINE
    # Gate self-check: UTF-8 text of 1..MAX_CHARS characters, not blank.
    if not (1 <= len(text) <= MAX_CHARS) or not text.strip():
        print("entry text fails the gate", file=sys.stderr)
        return 1
    out_dir = os.path.dirname(OUTPUT_PATH)
    if out_dir:
        os.makedirs(out_dir, exist_ok=True)
    with open(OUTPUT_PATH, "w", encoding="utf-8") as fh:
        fh.write(text)
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
