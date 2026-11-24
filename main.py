#!/usr/bin/env python3
"""One Line, One Minute: The Vending Machine Pickup Line Contest — make.fun entry.

Writes exactly one pickup line (86 characters, 88 bytes UTF-8, no trailing
newline) to $MAKEFUN_OUTPUT_DIR/entry.txt (default /output/entry.txt).

The line was picked by hand criterion-scoring against the published judge
brief (see README.md): 35 candidates scored 0-5 on each of the 5 criteria in
order, top two tied 24/25, head-to-head decided on the first differing
criteria (machine voice, machine world) for c24 over c23. No live judge A/B
was possible — the shared OpenRouter key is HTTP 402 exhausted — so no judge
numbers are claimed anywhere; the winner is the criterion leader, selected by
the documented scoring in the work dir's criterion-scores.md.

Deterministic: no network, no randomness, no environment secrets. Two runs
produce byte-identical output.
"""

import os

LINE = "Don't walk past \u2014 my coil's stuck on you, and the repairman doesn't come till Tuesday."

# The competition gate is 1-200 characters; fail loudly at import time if a
# future edit ever pushes the line outside it, instead of silently writing
# a grader-rejected entry. Also reject whitespace-only and multi-line input:
# the brief asks for ONE line.
if not 1 <= len(LINE) <= 200:
    raise ValueError(f"entry is {len(LINE)} chars, outside the 1-200 gate")
if not LINE.strip():
    raise ValueError("entry is only whitespace")
if "\n" in LINE or "\r" in LINE:
    raise ValueError("entry must be a single line")


def main():
    out_dir = os.environ.get("MAKEFUN_OUTPUT_DIR", "/output")
    os.makedirs(out_dir, exist_ok=True)
    path = os.path.join(out_dir, "entry.txt")
    with open(path, "w", encoding="utf-8", newline="") as f:
        f.write(LINE)
    # Write-back verification: read the file back and compare bytes, so a
    # partial write or encoding surprise fails loudly instead of submitting
    # a corrupted entry.
    with open(path, "rb") as f:
        if f.read() != LINE.encode("utf-8"):
            raise OSError(f"{path} does not match the entry line after write")


if __name__ == "__main__":
    main()
