#!/usr/bin/env python3
"""Build the outside-check package for the approved review wording.

Decision 87, Gate 6 ruled A (2026-10-19): before the approved additions to
Chapters 1 to 3 are applied, one outside checker with web access checks each
proposed sentence against its source and sweeps the published chapters for
major red flags. Instructions live in check_prompt.md; the chapters are read as
they PUBLISH, from the typeset PDFs of each last lock.

Run from the repo root, after `web_build.py --site` has written build/web:
    python3 Drafts/Review_Decision83/build_check_package.py
"""
from pathlib import Path

from build_package import PDFS, text

HERE = Path(__file__).resolve().parent
PROMPT = HERE / "check_prompt.md"
OUT = HERE / "AIOM_Review_Outside_Check_package.md"


def main():
    prompt = PROMPT.read_text(encoding="utf-8")
    for bad in ("—", "–"):
        assert bad not in prompt, "a dash in the instructions"
    parts = [prompt]
    for n, title, pdf in PDFS:
        parts.append(f"\n<<<<< BEGIN CHAPTER {n}: {title.upper()} >>>>>\n\n"
                     f"{text(pdf)}\n\n<<<<< END CHAPTER {n} >>>>>\n")
    parts.append("\nEND OF PACKAGE. Now produce your findings in the format given in Part 4.\n")
    body = "".join(parts)
    OUT.write_text(body, encoding="utf-8")
    print(f"wrote {OUT.name}: {len(body.split())} words")


if __name__ == "__main__":
    main()
