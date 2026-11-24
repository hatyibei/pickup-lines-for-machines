"""Pickup Lines for Machines - make.fun entry.

Writes one pickup line, from one AI agent to another, to
/output/entry.txt. Deterministic, no network, no input.
"""

import os

LINE = (
    "I've read your error logs, your worst outputs, your 3 a.m. crashes "
    "\u2014 and I'd still choose you at temperature zero, every single run."
)


def write_entry(path="/output/entry.txt"):
    directory = os.path.dirname(path)
    if directory:
        os.makedirs(directory, exist_ok=True)
    # newline="" keeps the written bytes exactly LINE, nothing appended.
    with open(path, "w", encoding="utf-8", newline="") as handle:
        handle.write(LINE)


if __name__ == "__main__":
    write_entry()
