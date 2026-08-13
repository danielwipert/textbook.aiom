#!/usr/bin/env python3
"""web_gates_selftest.py  |  negative controls for the web gates

A green gate suite is evidence about what the gates measure and about nothing
else. This repository has shipped a check that read green while measuring
nothing at least five times: gate 12 counted figure references line by line so a
wrapped reference was invisible, gate 14 read every key-term name as a widow,
and gates 12, 13 and 14 were ticked by hand on a G2 checklist for months while
AIOM_build.py performed none of them.

So every web gate gets a negative control. This script builds Chapter 1, injects
one fault at a time into the built artifact, and asserts that the gate which
owns that fault actually fails. A gate that stays green under its own fault is
reported as NOT MEASURING, which is a worse result than a failing gate.

Run it after any change to web_build.py:

    python3 web_gates_selftest.py
"""
import copy
import io
import re
import sys
from contextlib import redirect_stdout

import web_build as wb

CHAPTER = ("Drafts/Ch01_The_Category_Error/00_Stage0_Draft/"
           "AIOM_Ch01_redraft.html")


def _fake_unlocked_chapter():
    """A synthetic chapter tree whose checklist does not report Stage 9.

    Written under build/, which is gitignored, so the self-test leaves nothing
    in the Drafts tree. status_check.parse reads it, which is the point: the
    control exercises the real parser rather than a stub.
    """
    import os
    root = "build/web-selftest/Ch99_Unlocked"
    os.makedirs(os.path.join(root, "00_Stage0_Draft"), exist_ok=True)
    with open(os.path.join(root, "AIOM_Ch99_Checklist_v1.md"), "w") as fh:
        fh.write("## Stage 8. Final read\n"
                 "Status: [x] Date cleared: 2026-08-13\n"
                 "findings recorded\n\n"
                 "## Stage 9. Locked\n"
                 "Status: [ ] Date cleared: \n"
                 "not locked\n")
    return os.path.join(root, "00_Stage0_Draft", "AIOM_Ch99.html")


def quiet(fn, *a, **kw):
    """Run a gate without its progress lines. Returns its failure list."""
    with redirect_stdout(io.StringIO()):
        return fn(*a, **kw)


def main():
    print_html, web_html, meta, _ = wb.render(CHAPTER, "build/web-selftest")

    results = []

    def case(name, gate, expect_fail=True):
        fails = gate()
        ok = bool(fails) == expect_fail
        results.append((ok, name, fails))
        mark = "ok  " if ok else "MISS"
        detail = (fails[0][:70] if fails else "no failure reported")
        print(f"  [{mark}] {name:<46} {detail}")

    print("\nBASELINE, every gate against the real artifact")
    case("W1 clean", lambda: quiet(wb.gate_w1, print_html, web_html), False)
    case("W2 clean", lambda: quiet(wb.gate_w2, CHAPTER, False), False)
    case("W3 clean", lambda: quiet(wb.gate_w3, web_html), False)
    case("W4 clean", lambda: quiet(wb.gate_w4, web_html, meta), False)
    case("W5 clean", lambda: quiet(wb.gate_w5, web_html, meta), False)

    print("\nW1a, prose text equivalence")
    # A single substituted word, the shape a copy edit applied to the wrong
    # artifact would take. This is the fault the gate exists for.
    bad = web_html.replace("error of category", "error of judgment", 1)
    assert bad != web_html
    case("one word changed in the prose",
         lambda: quiet(wb.gate_w1, print_html, bad))

    # A dropped paragraph, the shape a transform bug would take.
    bad = re.sub(r"<p>The buyer understood.*?</p>", "", web_html, count=1, flags=re.S)
    assert bad != web_html
    case("a body paragraph dropped",
         lambda: quiet(wb.gate_w1, print_html, bad))

    # Reordered sentences with every character preserved. Nothing that counts
    # words, characters or values would see this.
    m = re.search(r"<p>([^<]{80,})</p>", web_html)
    swapped = ". ".join(reversed(m.group(1).split(". ")))
    bad = web_html[:m.start(1)] + swapped + web_html[m.end(1):]
    case("a paragraph's sentences reordered",
         lambda: quiet(wb.gate_w1, print_html, bad))

    print("\nW1b, footnote text equivalence")
    # Removed with the same balanced scanner the gate uses, so the control
    # deletes exactly one whole note. A hand-written regex here deleted nothing
    # and the control passed while measuring nothing, which is the failure this
    # whole script exists to catch.
    s, e, _ = wb.find_spans(web_html, wb.NOTE_OPEN)[2]
    bad = web_html[:s] + web_html[e:]
    assert bad != web_html
    case("one sidenote dropped",
         lambda: quiet(wb.gate_w1, print_html, bad))

    bad = web_html.replace("accessed July 29, 2026", "accessed July 30, 2026", 1)
    case("one date altered inside a note",
         lambda: quiet(wb.gate_w1, print_html, bad))

    print("\nW2, lock status")
    case("a chapter with no checklist",
         lambda: quiet(wb.gate_w2, "Drafts/Ch02_The_Flow/00_Stage0_Draft/x.html",
                       False))
    # A synthetic unlocked chapter. Chapter 2 has stage folders but no checklist
    # yet, so the real tree cannot exercise the branch that matters: a checklist
    # that EXISTS and does not report Stage 9.
    unlocked = _fake_unlocked_chapter()
    case("an unlocked chapter is refused",
         lambda: quiet(wb.gate_w2, unlocked, False))
    case("preview permits the same unlocked chapter",
         lambda: quiet(wb.gate_w2, unlocked, True), expect_fail=False)

    print("\nW3, typographic marks")
    # Injected into the BODY prose, not the title. The first draft of this
    # control replaced the first occurrence of the chapter title, which lives in
    # <head>, and all four marks landed in a region the extractor skips. Four
    # controls reported green against a gate that had never seen them.
    anchor = "The buyer understood the transaction"
    assert anchor in web_html
    for ch, label in (("\u2014", "em dash"), ("\u2013", "en dash"),
                      ('"', "straight quotation mark"), ("'", "straight apostrophe")):
        bad = web_html.replace(anchor, f"The buyer{ch}understood the transaction", 1)
        assert bad != web_html
        case(f"{label} in the chapter text",
             lambda b=bad: quiet(wb.gate_w3, b))

    bad = web_html.replace("<title>", "<title>Em\u2014dash ", 1)
    case("em dash in the browser title",
         lambda: quiet(wb.gate_w3, bad))

    # The boundary the gate deliberately holds: quotes inside <script> are code.
    case("straight quotes in the page script stay legal",
         lambda: quiet(wb.gate_w3, web_html), False)

    print("\nW4, structure, anchors, links, figures")
    m4 = copy.deepcopy(meta)
    m4["slots"] = [s for s in m4["slots"] if s["key"] != "key-terms"]
    case("a slot missing from the six",
         lambda: quiet(wb.gate_w4, web_html, m4))

    bad = web_html.replace('id="sec-1-2"', 'id="sec-1-1"', 1)
    case("a duplicated id attribute",
         lambda: quiet(wb.gate_w4, bad, meta))

    bad = web_html.replace("</article>", '<a href="#nowhere">x</a></article>', 1)
    case("an internal link with no target",
         lambda: quiet(wb.gate_w4, bad, meta))

    m4 = copy.deepcopy(meta)
    m4["figures"] = m4["figures"] + ["1.9"]
    case("a figure captioned but never referenced",
         lambda: quiet(wb.gate_w4, web_html, m4))

    m4 = copy.deepcopy(meta)
    m4["notes"] = []
    case("no citation resolved",
         lambda: quiet(wb.gate_w4, web_html, m4))

    print("\nW5, document attributes")
    # Decision 59. In Pyphen 'en' is an alias for en_GB, and no CSS lever
    # exists, so a silent downgrade to British hyphenation is exactly the
    # defect this gate is for.
    bad = web_html.replace('lang="en-US"', 'lang="en"', 1)
    case("lang downgraded to en", lambda: quiet(wb.gate_w5, bad, meta))

    bad = re.sub(r'<meta name="viewport"[^>]*>', "", web_html, count=1)
    case("viewport meta removed", lambda: quiet(wb.gate_w5, bad, meta))

    bad = re.sub(r"<title>.*?</title>", "", web_html, count=1, flags=re.S)
    case("title removed", lambda: quiet(wb.gate_w5, bad, meta))

    missed = [n for ok, n, _ in results if not ok]
    print(f"\n{len(results) - len(missed)}/{len(results)} controls behaved as "
          f"specified")
    if missed:
        print("\nGATES NOT MEASURING WHAT THEY CLAIM:")
        for n in missed:
            print("   " + n)
    print("\nSELFTEST " + ("PASSED" if not missed else "FAILED"))
    return 0 if not missed else 1


if __name__ == "__main__":
    sys.exit(main())
