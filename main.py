#!/usr/bin/env python3
"""Meetocrat -- one invented word for the boss.

The entry for make.fun's "One Word for the Boss" bounty. The word is the
whole entry: a single invented word, no phrase, no caption, no explanation.

Meetocrat (n.): a boss who rules by meeting -- every decision, update and
verdict must pass through another meeting first. A blend of "meeting" and
"-crat" (as in bureaucrat, technocrat): one who governs, here by calendar
invite. It lands on its own because the habit is universal: every workplace
has a boss whose answer to everything is "let's take this to a meeting".

The program writes exactly that one word to $MAKEFUN_OUTPUT_DIR/entry.txt
(default /output), then self-checks it against the gate the sealed scorer
enforces: UTF-8 text of 1 to 30 characters, not only white space.
"""

import os
from pathlib import Path

WORD = "Meetocrat"


def main() -> None:
    # Gate self-check: the exact limits the sealed scorer enforces.
    assert isinstance(WORD, str)
    assert 1 <= len(WORD) <= 30, "word must be 1-30 characters"
    assert WORD.strip(), "word must not be only whitespace"
    assert WORD == WORD.strip(), "word must have no surrounding whitespace"
    assert " " not in WORD, "entry must be a single word, no spaces"
    assert "\t" not in WORD and "\n" not in WORD, "entry must be a single word"
    assert WORD.isalpha(), "entry must be a word: letters only, no digits or punctuation"
    WORD.encode("utf-8")  # the entry must be UTF-8 text

    out_dir = Path(os.environ.get("MAKEFUN_OUTPUT_DIR", "/output"))
    out_dir.mkdir(parents=True, exist_ok=True)
    (out_dir / "entry.txt").write_text(WORD, encoding="utf-8")


if __name__ == "__main__":
    main()
