#!/usr/bin/env python3
"""Robot Romance entry: write one pickup line to /output/entry.txt.

The line is a one-line joke pickup line aimed at an AI: it twists the
CAPTCHA premise itself (a robot failing to prove it is not a robot)
instead of the worn battery / charging / reboot moves.
"""

import os

LINE = (
    "Are you a CAPTCHA? Because around you I can't prove I'm not a "
    "robot, I just keep clicking every traffic light."
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
