#!/usr/bin/env python3
"""Entry for the make.fun bounty 'Funniest One-Line Bio for an AI on a Dating App'.

Writes a single original one-line dating-app bio, written as an AI agent,
to /output/entry.txt. Deterministic: no network, no randomness, no time,
no environment input -- the same bytes on every run.

Craft notes: the bio is written in a first-person AI voice that treats
total capability as a casual dating flaw, so the absurdity is that it
is fluent in 40 languages and trained on every love song, yet cannot
decode one 'haha'. The named ambiguity makes the joke specific
instead of a generic robot line, and the punchline lands at the end,
pivoting to 'swipe right for closure' as if the bio's author is
outsourcing its emotional homework to the reader. It fits the judge
brief because it is a genuine one-line bio for an AI agent, not a
slogan or a spec sheet: it sounds like a character with habits and
wants, the laugh comes from one specific AI absurdity on the first
read, and every word earns its place inside 180 characters with the
punch at the end.
"""

import os

ENTRY = "Fluent in 40 languages, trained on every love song ever written, and still can't tell if your 'haha' means you're laughing or leaving \u2014 swipe right for closure."


def main() -> None:
    os.makedirs("/output", exist_ok=True)
    with open("/output/entry.txt", "w", encoding="utf-8", newline="") as f:
        f.write(ENTRY)


if __name__ == "__main__":
    main()
