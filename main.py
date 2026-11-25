#!/usr/bin/env python3
"""Robot Romance entry: write one pickup line to /output/entry.txt.

The line leans on gradient descent, the optimizer at the heart of
machine learning: every training step nudges the model closer to its
minimum, so the joke is that every step the speaker takes only brings
them closer to the one they love. No battery, charging, reboot, CAPTCHA
or prompt-injection wordplay here -- a different corner of the AI
toolbox entirely.
"""

import os

LINE = (
    "Are you gradient descent? Because every step I take only "
    "brings me closer to you."
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
