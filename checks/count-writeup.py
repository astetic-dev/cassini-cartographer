#!/usr/bin/env python3
"""Count the words in docs/writeup.md's hook block, and check that count
against the number the file itself claims.

The hook block is the text between the two `---` lines that docs/writeup.md
calls "the writeup" -- see reference/submission-kit.md for the shape. This
script is scoped to that one job: it does not walk the tree, and it is not the
start of a general checks/ framework.

Usage:
    python3 checks/count-writeup.py [path/to/writeup.md]

Exit code 0 and prints the count when the claim matches. Exit code 1 and a
message on stderr when it does not -- run this after editing the writeup, not
instead of reading it.
"""
import re
import sys
from pathlib import Path

DEFAULT_PATH = Path(__file__).resolve().parent.parent / "docs" / "writeup.md"


def extract_hook(text: str) -> str:
    parts = text.split("---")
    if len(parts) < 3:
        raise ValueError(
            "writeup.md does not have two '---' lines around the writeup block"
        )
    # parts[0] is the preamble above the first '---', parts[1] is the block
    # the file calls "the writeup", parts[2:] is everything after it.
    return parts[1]


def claimed_count(text: str) -> int:
    m = re.search(r"\*\*(\d+) words\*\*", text)
    if not m:
        raise ValueError("no '**NN words**' claim found in writeup.md")
    return int(m.group(1))


def main() -> int:
    path = Path(sys.argv[1]) if len(sys.argv) > 1 else DEFAULT_PATH
    text = path.read_text(encoding="utf-8")

    hook = extract_hook(text)
    actual = len(hook.split())
    claimed = claimed_count(text)

    print(f"{actual} words in the writeup block ({path})")

    if actual != claimed:
        print(
            f"MISMATCH: writeup.md claims **{claimed} words** but the block "
            f"counts to {actual}. Update the claim or the paragraph.",
            file=sys.stderr,
        )
        return 1

    print(f"matches the claim: **{claimed} words**")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
