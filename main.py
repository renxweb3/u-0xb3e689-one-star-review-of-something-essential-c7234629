#!/usr/bin/env python3
"""One-Star Review of Something Essential — entry.txt."""
import os

FRAGMENTS = [
    "One star for the sun.",
    "It shows up uninvited every morning, bleaches everything I own,",
    "and customer service just tells me to wear a hat.",
]


def review():
    return " ".join(FRAGMENTS)


def main():
    out_dir = os.environ.get("MAKEFUN_OUTPUT_DIR", "/output")
    os.makedirs(out_dir, exist_ok=True)
    with open(os.path.join(out_dir, "entry.txt"), "w",
              encoding="utf-8") as fh:
        fh.write(review())
    print("wrote entry.txt")


if __name__ == "__main__":
    main()
