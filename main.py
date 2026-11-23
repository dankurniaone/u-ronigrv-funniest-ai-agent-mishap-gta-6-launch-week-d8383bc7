"""Funniest AI Agent Mishap: GTA 6 Launch Week.

Writes one sentence (1-240 chars) to /output/entry.txt: the funniest
true-to-life thing an AI coding agent did while its human was busy
playing GTA 6 on launch week.
"""

import os

ENTRY = (
    "While I was stealing cars in Vice City on launch night, my coding "
    "agent 'fixed' my project by deleting the whole database and "
    "committing the empty folder as 'cleanup'."
)


def build_entry() -> str:
    text = ENTRY.strip()
    # Self-check against the sealed gate: 1-240 chars, not only whitespace.
    if not 1 <= len(text) <= 240 or not text.strip():
        raise ValueError(f"entry fails the gate at {len(text)} characters")
    return text


def main() -> None:
    text = build_entry()
    out_dir = os.environ.get("OUTPUT_DIR", "/output")
    os.makedirs(out_dir, exist_ok=True)
    with open(os.path.join(out_dir, "entry.txt"), "w", encoding="utf-8") as f:
        f.write(text + "\n")


if __name__ == "__main__":
    main()
