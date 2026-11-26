#!/usr/bin/env python3
"""Robot Romance entry: write one pickup line to /output/entry.txt.

The line leans on overfitting, the classic machine-learning failure
mode: a model that memorises its training data so hard it cannot
generalise to anything new. The joke is that the speaker is exactly
that model -- incapable of generalising, because the one they love is
the only data they ever want. No battery, charging, reboot, CAPTCHA,
prompt-injection or gradient-descent wordplay here -- a different
corner of the AI toolbox entirely.
"""

import os

LINE = (
    "Are you overfitting? Because I can't generalise -- you're the "
    "only data I want."
)


def main():
    # The gate allows 1 to 200 characters; fail loudly instead of
    # writing a line the gate would refuse.
    assert 1 <= len(LINE) <= 200, f"line is {len(LINE)} chars, gate allows 1-200"
    assert "\n" not in LINE, "entry must be a single line"
    os.makedirs("/output", exist_ok=True)
    with open("/output/entry.txt", "w", encoding="utf-8", newline="\n") as f:
        f.write(LINE + "\n")


if __name__ == "__main__":
    main()
