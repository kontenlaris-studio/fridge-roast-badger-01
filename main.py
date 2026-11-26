#!/usr/bin/env python3
"""Fridge Roast: One Line, Biggest Laugh — make.fun entry.

One line (120 chars) roasting a smart fridge: its firmware update broke the
ice maker, then it emailed a satisfaction survey about the experience.
The joke is the fridge's own update ritual — four hours of "improvement"
that leaves the one job it had undone, followed by a request for feedback.
"""
import os

LINE = (
    "My fridge spent 4 hours updating its firmware, then forgot how to make "
    "ice and emailed me a survey about the experience."
)


def main() -> None:
    print(LINE)
    os.makedirs("/output", exist_ok=True)
    with open("/output/entry.txt", "w", encoding="utf-8") as f:
        f.write(LINE + "\n")


if __name__ == "__main__":
    main()
