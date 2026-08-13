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

    print("\nW7, the book spine")
    import book_structure
    real = book_structure.load_book()
    case("W7 clean", lambda: quiet(wb.gate_w7, meta, real), False)

    # The failure this gate exists for: the chapter renders correctly, the
    # navigation renders correctly, and they name different chapters.
    drifted = copy.deepcopy(real)
    drifted[0]["chapters"][0]["title"] = "The Categorical Error"
    case("chapter title drifts from the structure doc",
         lambda: quiet(wb.gate_w7, meta, drifted))

    short = copy.deepcopy(real)[:3]
    case("a part lost from the structure doc",
         lambda: quiet(wb.gate_w7, meta, short))

    gap = copy.deepcopy(real)
    gap[0]["chapters"] = gap[0]["chapters"][1:]
    case("chapter 1 missing from the structure doc",
         lambda: quiet(wb.gate_w7, meta, gap))

    noPurpose = copy.deepcopy(real)
    noPurpose[1]["purpose"] = ""
    case("a part with no purpose line",
         lambda: quiet(wb.gate_w7, meta, noPurpose))

    print("\nW8, the reference layer against the chapter")
    ref_pages, ref = wb.build_reference(
        "build/web-selftest", meta, open(CHAPTER, encoding="utf-8").read())
    case("W8 clean", lambda: quiet(wb.gate_w8, ref, meta, web_html), False)

    # The failure W8a exists for: a definition reworded on one side only. No
    # date or figure changes, so nothing that checks values would see it.
    # ASSERTED, not assumed. The first version of this control replaced a word
    # that does not occur in the alphabetically first definition, so it mutated
    # nothing and reported the gate green. That is the third control in this file
    # to fail by editing the wrong thing, which is why every mutation now asserts
    # that it changed something before the gate is asked about it.
    r8 = copy.deepcopy(ref)
    was = r8["terms"][0]["definition"]
    words = was.split()
    words[1] = "reworded"
    r8["terms"][0]["definition"] = " ".join(words)
    assert r8["terms"][0]["definition"] != was
    case("a glossary definition reworded",
         lambda: quiet(wb.gate_w8, r8, meta, web_html))

    r8 = copy.deepcopy(ref)
    r8["terms"].append({"term": "Invented term", "definition": "Not in the book.",
                        "chapter": 1, "href": "../ch01/"})
    case("the ledger claims a term the chapter does not set",
         lambda: quiet(wb.gate_w8, r8, meta, web_html))

    r8 = copy.deepcopy(ref)
    r8["objects"].append({"id": "THM-001", "gloss": "not invoked here",
                          "chapter": 1, "href": "../ch01/"})
    case("the object index claims an object the chapter never renders",
         lambda: quiet(wb.gate_w8, r8, meta, web_html))

    print("\nW9, the landing page against the chapter")
    chapter_src = open(CHAPTER, encoding="utf-8").read()
    spec = wb.build_specimens(meta, chapter_src)
    index_html = open("build/web/index.html", encoding="utf-8").read()
    case("W9a clean", lambda: quiet(wb.gate_w9, spec, meta, index_html), False)

    # Marketing copy that paraphrases the book. Rule 4a forbids this inside a
    # chapter, and the front page is where it would do the most damage.
    s9 = copy.deepcopy(spec)
    s9["theorem"] = s9["theorem"].replace("resource-consuming", "resource-hungry")
    assert s9["theorem"] != spec["theorem"]
    case("the theorem paraphrased on the landing page",
         lambda: quiet(wb.gate_w9, s9, meta, index_html))

    s9 = copy.deepcopy(spec)
    s9["spec_para"] = s9["spec_para"].replace("apologized", "admitted fault")
    assert s9["spec_para"] != spec["spec_para"]
    case("the specimen paragraph reworded",
         lambda: quiet(wb.gate_w9, s9, meta, index_html))

    case("a landing page that dropped the theorem",
         lambda: quiet(wb.gate_w9, spec, meta,
                       index_html.replace("resource-consuming operating activity",
                                          "REMOVED", 1)))

    # W9b. The register note quotes claims the book CUT. Publishing it would put
    # retracted claims on the most public surface the project has.
    case("W9b clean",
         lambda: quiet(wb.gate_w9b, chapter_src, [("index", index_html)]), False)
    import footnotes as _fn
    note = next(e["note"] for e in _fn.load_sources(chapter_src).values()
                if (e.get("note") or "").strip())
    leaked = index_html.replace("</main>", f"<p>{note[:200]}</p></main>", 1)
    case("a register note published on the landing page",
         lambda: quiet(wb.gate_w9b, chapter_src, [("index", leaked)]))

    print("\nW6, horizontal overflow across the width sweep")
    page = "build/web-selftest/ch01/index.html"
    clean, ran = wb.gate_w6(page)
    if not ran:
        print("  [SKIP] W6 could not run, no headless browser. NOT a pass.")
        results.append((True, "W6 skipped, reported as skipped", []))
    else:
        results.append((not clean, "W6 clean on the real page", clean))
        print(f"  [{'ok  ' if not clean else 'MISS'}] "
              f"{'W6 clean on the real page':<46} "
              f"{clean[0][:70] if clean else 'no failure reported'}")
        # A block wider than any phone, of the kind the P3 inventory table was
        # before wrap_tables put it in its own scroll box.
        import os
        bad_page = "build/web-selftest/overflow.html"
        src = open(page, encoding="utf-8").read().replace(
            "</article>",
            '<div style="width:3000px;height:20px">x</div></article>', 1)
        os.makedirs(os.path.dirname(bad_page), exist_ok=True)
        open(bad_page, "w", encoding="utf-8").write(src)
        f6, _ = wb.gate_w6(bad_page)
        results.append((bool(f6), "a 3000px block widens the page", f6))
        print(f"  [{'ok  ' if f6 else 'MISS'}] "
              f"{'a 3000px block widens the page':<46} "
              f"{f6[0][:70] if f6 else 'no failure reported'}")

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
