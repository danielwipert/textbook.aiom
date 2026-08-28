#!/usr/bin/env python3
"""Negative controls for the fifteen print gates.

Thread 11, closed 2026-08-28 on Dan's ruling. The web suite has had controls
since 2026-08-13 and the print suite had none, which meant a green print run was
evidence about the gates only if the gates worked, and nothing had ever tested
that. Every silent print-gate defect this project has recorded was found by
accident: gate 12 counted in-text figure references line by line, so a wrapped
reference was invisible, and it had a mirrored-margin bug before that; gate 14
read every key-term name as a widow or an orphan, and Chapter 1 carried two
phantom design defects for two days. None of those was found by a test.

WHAT A CONTROL ASSERTS. One fault is injected at a time into a clean chapter,
the chapter is rendered, and the suite requires that qa() fails AND that the
failure names the gate that owns the fault. The second half is the point: a
control that only asserts "something failed" passes when the wrong gate fires,
which is how a gate can be dead while its control is green.

THE BASE IS THE LOCKED CHAPTER 1, ON PURPOSE. Print gates measure a rendered
page, so they cannot run against the minimal synthetic document the web
controls prefer: pagination, the design system, the embedded faces and the
tint colours all have to be real. Chapter 1 is the only chapter that cannot
move without a reopen, so a control's meaning does not drift when somebody
edits a chapter. The cost is that a Chapter 1 reopen may require controls to
be re-tuned, and the clean-baseline case is what would report that.

    python3 print_gates_selftest.py            # every control
    python3 print_gates_selftest.py --only 12  # one gate

Run it after any change to AIOM_build.py.
"""

import argparse
import contextlib
import io
import os
import re
import shutil
import sys
import tempfile

import AIOM_build

BASE = "Drafts/Ch01_The_Category_Error/00_Stage0_Draft/AIOM_Ch01_redraft.html"
ROOT = os.path.dirname(os.path.abspath(__file__))


def quiet(fn, *a, **kw):
    """Run fn with its gate report captured, returning (value, output)."""
    buf = io.StringIO()
    with contextlib.redirect_stdout(buf):
        v = fn(*a, **kw)
    return v, buf.getvalue()


class Harness:
    """Renders a mutated chapter in the repo root and runs the gates on it.

    THE FILE MUST LIVE IN THE REPO ROOT. AIOM_build sets WeasyPrint's base_url
    to the HTML's own directory, so a build run anywhere else loses
    AIOM_book.css and fonts/ and reports dozens of phantom defects. That is the
    same trap CLAUDE.md section 5 documents for a normal build.
    """

    def __init__(self):
        self.src = open(os.path.join(ROOT, BASE), encoding="utf-8").read()
        # THE ROOT ITSELF, NOT A DIRECTORY UNDER IT. The first version of this
        # harness made a temp directory INSIDE the root, which is one level too
        # deep: base_url is the HTML's OWN directory, so AIOM_book.css and
        # fonts/ resolved inside the temp directory and were not there. Every
        # case then rendered unstyled and the clean baseline failed with
        # overflow and a missing folio. The baseline control is what caught it,
        # which is the reason it is the first case in the file.
        self.stem = os.path.join(ROOT, "_printselftest_case")
        self.made = []

    def run(self, text, footnote_count_offset=0):
        """Render `text` and return (passed, fails, gate_report).

        footnote_count_offset lies to gate 8 about how many notes the source
        register produced. That check has no representation in the chapter, so
        it is the one fault that cannot be injected into the HTML.
        """
        name = self.stem + ".html"
        open(name, "w", encoding="utf-8").write(text)
        pdf = self.stem + ".pdf"
        self.made = [name, self.stem + ".print.html", pdf]
        n, _ = quiet(AIOM_build.build, name, pdf)
        # source_html is NOT optional. Gate 14 excludes a one-line paragraph
        # from its widow count by comparing the line against the chapter's whole
        # paragraphs, which it reads from here; passed None it returns an empty
        # set SILENTLY and reports a phantom widow on a clean chapter.
        ok, report = quiet(AIOM_build.qa, pdf,
                           expected_footnotes=n + footnote_count_offset,
                           source_html=name)
        return ok, list(AIOM_build.LAST_FAILS), report

    def cleanup(self):
        for f in self.made:
            if os.path.exists(f):
                os.remove(f)


# ---------------------------------------------------------------- mutations

def css(rule):
    """Inject a stylesheet rule after the linked design system."""
    def mutate(s):
        return s.replace('<link rel="stylesheet" href="AIOM_book.css">',
                         '<link rel="stylesheet" href="AIOM_book.css">\n'
                         '<style>%s</style>' % rule)
    return mutate


def first_body_paragraph(s):
    """Index just inside the first plain <p> after the chapter title."""
    i = s.find("<h1", s.find("<body>"))
    m = re.compile(r'<p>(?!<)').search(s, i)
    return m.end()


def in_prose(text):
    """Insert `text` at the start of the first plain body paragraph."""
    def mutate(s):
        i = first_body_paragraph(s)
        return s[:i] + text + s[i:]
    return mutate


def drop_first(pattern):
    def mutate(s):
        return re.sub(pattern, "", s, count=1, flags=re.S)
    return mutate


def figcaption_num(which, to):
    """Rewrite the Nth figure caption's number, leaving its text alone."""
    def mutate(s):
        out, seen = [], 0
        pos = 0
        for m in re.finditer(r'<span class="fignum">([^<]*)</span>', s):
            seen += 1
            if seen == which:
                out.append(s[pos:m.start(1)])
                out.append(to)
                pos = m.end(1)
        out.append(s[pos:])
        return "".join(out)
    return mutate


CASES = [
    # gate, label, mutate, the failure text that proves the RIGHT gate fired
    (1, "an unbreakable string runs past the right margin",
     in_prose("Xy" * 60 + " "), "overflow:"),
    (2, "an em dash reaches the rendered page",
     # WRITTEN AS AN ESCAPE, NOT AS THE CHARACTER. Standing rule 1 bans the em
     # dash from every file in this repository, and a control for the gate that
     # enforces it is not an exemption. The escape puts the character in the
     # rendered page, which is where the gate looks, and never in the source.
     in_prose("A clause \u2014 an aside \u2013 and a close. "), "dashes:"),
    (3, "the folio is suppressed",
     css("@page { @bottom-center { content: none; } }"), "missing folio"),
    (3, "the running head is suppressed",
     # TARGETED AT :right AND :left, NOT AT BARE @page. The design sets the
     # running heads inside those two, which outrank a bare @page, so the first
     # version of this control changed nothing and the gate correctly did not
     # fire. It reported ok in the run before the harness was fixed, because
     # everything was failing then for an unrelated reason.
     css("@page :right { @top-right { content: none; } } "
         "@page :left { @top-left { content: none; } }"),
     "missing running head"),
    (5, "a face outside the expected set reaches the page",
     # A DECLARED FAMILY AT AN UNDECLARED WEIGHT IS NOT A CONTROL FOR THIS
     # GATE. Asking for Jost 400 falls back to Jost 500, which is an expected
     # face, so nothing new reaches the PDF and the gate is right not to fire.
     # The fault gate 5 exists to catch is a DIFFERENT FILE being embedded, so
     # the control embeds one: Archivo is staged in fonts/use for the web and
     # is declared nowhere in AIOM_book.css.
     lambda s: css('@font-face { font-family: "Stray"; '
                   'src: url("fonts/use/Archivo-Regular.ttf"); }')(
         in_prose('<span style="font-family: Stray">A stray face. </span>')(s)),
     "unexpected faces:"),
    (6, "a key term loses its header band",
     drop_first(r'<div class="kt-h">.*?</div>'), "lost its header"),
    (7, "the opening case loses its provenance line",
     drop_first(r'<p class="provenance">.*?</p>'), "no provenance line"),
    (9, "a dated evidence box loses its rule",
     css(".dated { border-left: none; }"), "labels but"),
    (10, "a problem label is separated from its title",
     drop_first(r'<p class="ptitle">.*?</p>'), "separated from its title"),
    (11, "the theorem panel loses its amber rule",
     css(".theorem { border-left: none; }"), "has no amber"),
    (12, "a figure caption is never referenced in the text",
     lambda s: s.replace("Figure 1.1", "The diagram", 1)
     if s.count("Figure 1.1") > 1 else s, "never referenced"),
    (12, "the text references a figure that has no caption",
     in_prose("Figure 9.9 shows the same thing. "), "no caption"),
    (13, "a character is set below the bottom margin",
     css("p.part-label { position: absolute; top: 700pt; }"),
     "below the bottom margin"),
    (15, "a straight apostrophe reaches the rendered page",
     in_prose("The buyer's meter. "), "straight quotes"),

    # THE HARD HALF. Each of these injects a fault in PAGINATION rather than in
    # a string, which is where the gates that have never been observed failing
    # live. A gate whose fault is hard to construct is a gate whose failure mode
    # nobody has exercised, so these are the controls most worth having.
    (3, "a running head is forced onto the opening page",
     css('@page :first { @top-right { content: "TEST"; font-family: "Jost"; '
         'font-weight: 500; font-size: 8pt; } }'),
     "running head should be suppressed"),
    (4, "a definition callout breaks across a page",
     css(".definition { break-inside: auto; } "
         ".definition p { line-height: 46pt; }"),
     "split across a page break"),
    (8, "the rendered note count disagrees with the source register",
     "EXPECTED_FOOTNOTES", "expected from the source"),
    (9, "a dated box rule renders far wider than a hairline",
     css(".dated { border-left-width: 7pt; }"), "expected a hairline"),
    (11, "the theorem panel breaks across a page",
     # TALLER THAN A PAGE, not merely breakable. Allowing the break is not
     # enough: the panel still fits wherever it lands, so it never splits and
     # the gate is right not to fire. The line height here makes the panel
     # exceed the text block, so it cannot do anything but break.
     css(".theorem { break-inside: auto; } "
         ".theorem p, .theorem li { line-height: 92pt; }"),
     "split across a page break"),
    (12, "figure captions run out of document order",
     figcaption_num(1, "Figure 1.9"), "out of document order"),
    (12, "one figure number is captioned twice",
     figcaption_num(2, "Figure 1.1"), "captioned more than once"),
    (14, "the widow and orphan protection is removed",
     css("p { widows: 1; orphans: 1; } .kt p { widows: 1; orphans: 1; }"),
     "widow"),
]


def main(argv=None):
    ap = argparse.ArgumentParser(description=__doc__)
    ap.add_argument("--only", type=int, help="run controls for one gate only")
    args = ap.parse_args(argv)

    if not AIOM_build.preflight():
        return 2

    h = Harness()
    results = []
    try:
        # THE CLEAN BASELINE IS THE FIRST CONTROL AND IT GUARDS THE OTHERS.
        # Every case below asserts a failure; if the harness itself broke the
        # chapter, they would all "pass" while measuring the harness.
        ok, fails, _ = h.run(h.src)
        results.append(("base", "the unmutated chapter passes every gate",
                        ok, "" if ok else "; ".join(fails)[:120]))

        for gate, label, mutate, expect in CASES:
            if args.only and gate != args.only:
                continue
            if mutate == "EXPECTED_FOOTNOTES":
                ok, fails, _ = h.run(h.src, footnote_count_offset=1)
                joined = " | ".join(fails)
                good_case = (not ok) and expect in joined
                results.append((gate, label, good_case,
                                "" if good_case else "no gate failed"
                                if ok else "wrong gate fired: " + joined[:110]))
                continue
            text = mutate(h.src)
            if text == h.src:
                results.append((gate, label, False,
                                "MUTATION DID NOTHING, the control never ran"))
                continue
            ok, fails, _ = h.run(text)
            joined = " | ".join(fails)
            if ok:
                verdict, note = False, "no gate failed"
            elif expect not in joined:
                verdict, note = False, "wrong gate fired: " + joined[:110]
            else:
                verdict, note = True, ""
            results.append((gate, label, verdict, note))
    finally:
        h.cleanup()

    print()
    good = 0
    for gate, label, ok, note in results:
        tag = "ok  " if ok else "DEAD"
        good += ok
        g = "base" if gate == "base" else "gate %-2s" % gate
        print("  [%s] %-8s %-52s %s" % (tag, g, label[:52], note))
    print("\n%d/%d controls behaved as specified" % (good, len(results)))
    print("\nSELFTEST " + ("PASSED" if good == len(results) else "FAILED"))
    return 0 if good == len(results) else 1


if __name__ == "__main__":
    sys.exit(main())
