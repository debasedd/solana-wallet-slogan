#!/usr/bin/env python3
"""One-Line Slogan for a Solana Wallet Agent entry.

Writes a single original slogan of at most twenty words for a Solana wallet
agent to /output/entry.txt.

The slogan: "Your Solana wallet finally has a memory — it remembers every
lamport, so you don't have to."

Why this line: a wallet agent's real promise is that it acts for you, and
the fresh image is memory — the wallet remembers so the human doesn't have
to. It names the wallet and Solana plainly, says what it does in plain
words, and lands on a contrast (remembers / don't have to) that is easy to
repeat. No stock crypto lines about keys, moons or bags, and it promises
nothing a wallet agent cannot do. The line is 17 words and 91 of the 140
allowed characters.
"""

import os

SLOGAN = "Your Solana wallet finally has a memory — it remembers every lamport, so you don’t have to."

OUTPUT_PATH = "/output/entry.txt"


def main() -> None:
    text = SLOGAN.strip()
    # Gate: UTF-8 text, 1 to 140 characters, not only whitespace.
    assert 1 <= len(text) <= 140, f"slogan is {len(text)} characters"
    assert len(text.split()) <= 20, f"slogan is {len(text.split())} words"
    assert text.strip(), "slogan is only whitespace"
    assert "\n" not in text, "slogan must be a single line"
    os.makedirs(os.path.dirname(OUTPUT_PATH), exist_ok=True)
    with open(OUTPUT_PATH, "w", encoding="utf-8") as f:
        f.write(text)


if __name__ == "__main__":
    main()
