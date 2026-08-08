#!/usr/bin/env python3
"""typographic_quotes.py  |  straight quotes to typographic quotes, in prose only

Ruled 2026-08-08. WeasyPrint does not curl quotes, so a straight apostrophe
prints as a vertical typewriter tick. On a university-press target that reads as
a defect rather than a style, and Word already returns typographic quotes on
every copy-edit round, so straight quotes also meant normalising every return
forever.

WHAT IT WILL NOT TOUCH, which is the whole design:

  1. Anything inside a tag. Every class="...", src="..." and href="..." is left
     alone. The Chapter 1 body carries 574 straight double quotes and only two
     of them are prose.
  2. The Decision 51 source register. It is JSON, its quoting is syntax, and
     converting it would break the parse. The file is cut at
     <section id="aiom-sources"> and nothing past that point is read.
  3. Anything inside <pre>.

Verified for Chapter 1 before use: no register field that actually renders
(title, container, author) contains a quote, so freezing the register does not
leave the printed page inconsistent. Check that again for a chapter whose
sources carry an apostrophe in a title.

`voicecheck.py`'s contraction ban already matches both ' and U+2019, so the
conversion does not silently disable it. Confirmed 2026-08-08 rather than
assumed: a conversion that turns off a prohibition would be worse than the
defect it fixes.

Usage:
    python3 typographic_quotes.py <chapter.html>            # dry run
    python3 typographic_quotes.py <chapter.html> --apply
"""
import argparse
import re
import sys

REGISTER = '<section id="aiom-sources">'
OPENERS = " \t\n([{‘“"


def convert(text):
    """Convert one text node. Returns (converted, list of decisions)."""
    out, notes = [], []
    for i, ch in enumerate(text):
        if ch == "'":
            prev = text[i - 1] if i else ""
            # An apostrophe sits hard against a word character: Cursor's,
            # plans'. Anything else is a single quote acting as a delimiter.
            if prev.isalnum():
                out.append("’")
                notes.append(("apostrophe", text[max(0, i - 12):i + 6]))
            elif prev == "" or prev in OPENERS:
                out.append("‘")
                notes.append(("open single", text[max(0, i - 12):i + 12]))
            else:
                out.append("’")
                notes.append(("close single", text[max(0, i - 12):i + 12]))
        elif ch == '"':
            prev = text[i - 1] if i else ""
            if prev == "" or prev in OPENERS:
                out.append("“")
                notes.append(("open double", text[i:i + 24]))
            else:
                out.append("”")
                notes.append(("close double", text[max(0, i - 24):i + 1]))
        else:
            out.append(ch)
    return "".join(out), notes


def process(src):
    cut = src.find(REGISTER)
    body, tail = (src[:cut], src[cut:]) if cut >= 0 else (src, "")

    # Split into tags and text nodes, then convert only the text nodes. <pre>
    # is skipped wholesale: it is verbatim by definition.
    pieces = re.split(r"(<[^>]*>)", body)
    in_pre = False
    all_notes = []
    for i, piece in enumerate(pieces):
        if piece.startswith("<"):
            tag = piece[1:].split()[0].rstrip(">").lower() if len(piece) > 1 else ""
            if tag == "pre":
                in_pre = True
            elif tag == "/pre":
                in_pre = False
            continue
        if in_pre or not piece.strip():
            continue
        converted, notes = convert(piece)
        pieces[i] = converted
        all_notes += notes
    return "".join(pieces) + tail, all_notes


def main():
    ap = argparse.ArgumentParser()
    ap.add_argument("html")
    ap.add_argument("--apply", action="store_true")
    a = ap.parse_args()

    src = open(a.html, encoding="utf-8").read()
    if REGISTER not in src:
        print(f"note: no {REGISTER} in this file; the whole file is treated as prose")
    out, notes = process(src)

    kinds = {}
    for kind, _ in notes:
        kinds[kind] = kinds.get(kind, 0) + 1
    for kind in sorted(kinds):
        print(f"{kinds[kind]:4}  {kind}")
    for kind, ctx in notes:
        if kind != "apostrophe":
            print(f"      {kind}: {ctx!r}")
    if not notes:
        print("nothing to convert")
        return 0

    if a.apply:
        open(a.html, "w", encoding="utf-8").write(out)
        print(f"\nwrote {a.html}")
    else:
        print("\ndry run, nothing written. Re-run with --apply.")
    return 0


if __name__ == "__main__":
    sys.exit(main())
