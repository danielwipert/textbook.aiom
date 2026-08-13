#!/usr/bin/env python3
"""book_structure.py  |  the four parts and fifteen chapters, parsed not retyped

The site needs the shape of the whole book: four parts, fifteen chapters, and
which chapter sits in which part. That list already exists, in
`AIOM_Structure_v1.md` section "The structure: 15 chapters, 4 parts", which
CLAUDE.md names as the authority on chapter structure.

It is PARSED rather than copied into a Python literal. A copy would be a second
source of truth for the book's own table of contents, and this repository's
signature failure is two artifacts of one thing that silently disagree. If the
structure document changes, the site changes with it.

What this module deliberately does NOT publish: the "Big idea", "Competency",
"Anchor theorem" and "Craft section" lines under each chapter. Those are internal
planning shorthand, not book content ("THE SUMMIT" is Chapter 12's), and CLAUDE.md
section 9 rules that later chapters withhold things deliberately and must not be
front-run. Part PURPOSE lines are outward-facing and are carried.

    from book_structure import load_book
    book = load_book()      # [{numeral, name, purpose, chapters: [{number, title}]}]
"""
import os
import re
import sys

STRUCTURE = "AIOM_Structure_v1.md"

PART_RE = re.compile(r"^### Part ([IVX]+): (.+?)\s*$")
PURPOSE_RE = re.compile(r"^Purpose:\s*(.+?)\s*$")
CHAPTER_RE = re.compile(r"^(\d{1,2})\.\s+(.+?)\s*$")
STOP_RE = re.compile(r"^## ")


def load_book(path=STRUCTURE):
    """Return the four parts, each with its chapters, in book order."""
    if not os.path.exists(path):
        raise FileNotFoundError(f"{path} not found; run from the repository root")
    parts, part = [], None
    started = False
    for line in open(path, encoding="utf-8").read().split("\n"):
        if line.startswith("## The structure"):
            started = True
            continue
        if not started:
            continue
        if STOP_RE.match(line):
            break
        m = PART_RE.match(line)
        if m:
            part = {"numeral": m.group(1), "name": m.group(2),
                    "purpose": "", "chapters": []}
            parts.append(part)
            continue
        if part is None:
            continue
        m = PURPOSE_RE.match(line)
        if m and not part["purpose"]:
            part["purpose"] = m.group(1)
            continue
        m = CHAPTER_RE.match(line)
        if m:
            part["chapters"].append({"number": int(m.group(1)),
                                     "title": m.group(2)})
    return parts


def flat(book):
    """Every chapter in book order, each carrying its part."""
    out = []
    for p in book:
        for c in p["chapters"]:
            out.append({**c, "part_numeral": p["numeral"], "part_name": p["name"]})
    return out


def check(book):
    """Structural checks on the parsed result. Returns a list of failures.

    These are cheap and they are the difference between parsing and hoping. A
    parser that silently returns three parts because a heading changed would
    produce a site missing a quarter of the book, and nothing else would notice.
    """
    fails = []
    if len(book) != 4:
        fails.append(f"expected 4 parts, parsed {len(book)}")
    chapters = flat(book)
    if len(chapters) != 15:
        fails.append(f"expected 15 chapters, parsed {len(chapters)}")
    numbers = [c["number"] for c in chapters]
    if numbers != list(range(1, len(numbers) + 1)):
        fails.append(f"chapter numbers are not 1..N in order: {numbers}")
    for p in book:
        if not p["purpose"]:
            fails.append(f"Part {p['numeral']} has no Purpose line")
        if not p["chapters"]:
            fails.append(f"Part {p['numeral']} has no chapters")
    for c in chapters:
        if not c["title"]:
            fails.append(f"chapter {c['number']} has no title")
    return fails


APOS = re.compile(r"(?<=\w)'(?=\w)")


def curl(text):
    """Typographic apostrophe, for planning prose that reaches a public page.

    `typographic_quotes.py` is the repository's converter, but it is written for
    chapter HTML: it steps over tags, over the Decision 51 register, and over
    <pre>. These are bare strings, so the narrow rule is used instead and stated
    rather than borrowed. Straight marks fail gate W3, and the structure document
    is planning prose that was never held to that standard.
    """
    return APOS.sub("’", text)


def public_purpose(purpose):
    """The FIRST SENTENCE of a Purpose line, which is the only publishable part.

    The rest is production talk. Part III's full line reads "the five functions.
    Chapter titles use the manifesto's own verbs. The capstone dataset is
    introduced at the top of this part with its construction note.
    Worked-example fading: completion problems early in the part, unguided by its
    end." That is a note to the drafter, not a description for a reader, and
    putting it on the front page would publish the book's production notes.

    THIS IS PLACEHOLDER COPY. Dan writes the real part descriptions; this is a
    safe, ruled, outward-facing default until he does.
    """
    first = purpose.split(". ")[0].strip().rstrip(".")
    if not first:
        return ""
    return curl(first[0].upper() + first[1:] + ".")


def short_title(title):
    """The title without its subtitle, for a narrow navigation rail.

    Part III chapters carry a verb subtitle by design ("Sourcing: Feeding the
    Flow"), which is right on a title page and too long in a 15rem rail.
    """
    return title.split(":", 1)[0].strip()


if __name__ == "__main__":
    b = load_book()
    fails = check(b)
    for p in b:
        print(f"\nPart {p['numeral']}: {p['name']}")
        print(f"  purpose: {p['purpose'][:70]}")
        for c in p["chapters"]:
            print(f"    {c['number']:>2}. {c['title']}")
    print(f"\n{len(b)} parts, {len(flat(b))} chapters")
    print("STRUCTURE " + ("OK" if not fails else "FAILED"))
    for f in fails:
        print("   " + f)
    sys.exit(0 if not fails else 1)
