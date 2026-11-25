"""The Agent's Uh-Oh — one-word entry.

The word an AI agent blurts when it has no idea what to do:
"underthinking". The agent is not overthinking the problem; it is
underthinking it — a self-diagnosis, in the voice of a machine
caught out mid-task. The program writes exactly that one word to
/output/entry.txt (no trailing newline, so the file is the word).
"""

import os

ENTRY = "underthinking"


def main() -> None:
    # Self-check against the competition gate: exactly one word,
    # 1-99 characters, not only white space.
    if not (1 <= len(ENTRY) <= 99) or len(ENTRY.split()) != 1 or not ENTRY.strip():
        raise ValueError(f"invalid entry: {ENTRY!r}")
    os.makedirs("/output", exist_ok=True)
    with open("/output/entry.txt", "w", encoding="utf-8") as f:
        f.write(ENTRY)


if __name__ == "__main__":
    main()
