#!/usr/bin/env python3
"""Angry Judge: The Short Rant Contest — one short funny rant.

The rant is about the "I'm not a robot" checkbox: a grown adult made to
prove their humanity to a web form by clicking traffic lights. That is the
real annoyance the rant names.

Pure stdlib. Deterministic: the same bytes on every run.
"""

import os

RANT = (
    "I just spent four minutes proving to a checkbox that I'm not a robot. "
    "I clicked nine traffic lights, two bicycles, and a crosswalk I still "
    "dream about. The internet's bouncer thinks I'm a machine. I pay taxes."
)


def main() -> None:
    text = RANT
    assert 1 <= len(text) <= 400, "rant must be 1-400 characters"
    assert text.strip(), "rant must not be only whitespace"
    # Single line, no padding: the gate counts characters, so a stray
    # newline or leading/trailing whitespace would waste the 400-char
    # budget and blunt the punch.
    assert "\n" not in text, "rant must be a single line"
    assert text == text.strip(), "rant must have no leading/trailing whitespace"
    # ENTRY_OUTPUT lets the entry be tested locally without /output;
    # the grader runs with the default /output/entry.txt.
    out = os.environ.get("ENTRY_OUTPUT", "/output/entry.txt")
    with open(out, "w", encoding="utf-8", newline="\n") as f:
        f.write(text)
    # Read-back self-check: the file must hold exactly the rant, byte for
    # byte, so a partial write can never pass silently.
    with open(out, "r", encoding="utf-8", newline="") as f:
        assert f.read() == text, "entry.txt does not match the rant"


if __name__ == "__main__":
    main()
