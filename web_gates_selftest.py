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
import os
import re
import sys
from contextlib import redirect_stdout

import web_build as wb
import claimcheck

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


def _multi_chapter_control(case):
    """Build a TWO chapter site before chapter 2 exists.

    The site builder has only ever been exercised with one chapter, and code that
    works for one is not thereby known to work for two. This control synthesises a
    second locked chapter in a throwaway Drafts tree, retitled to the structure
    document's own name for chapter 2, and asserts the whole site builds and gates
    clean. It is the cheapest possible proof that the pipeline scales past the
    single chapter that happens to exist today.
    """
    import glob
    import os
    import shutil
    root = "build/selftest-tree"
    shutil.rmtree(root, ignore_errors=True)
    src_dir = os.path.dirname(os.path.dirname(CHAPTER))
    for num, title in ((1, "The Category Error"), (2, "The Flow")):
        dst = os.path.join(root, f"Ch{num:02d}_Synthetic", "00_Stage0_Draft")
        os.makedirs(dst, exist_ok=True)
        html = open(CHAPTER, encoding="utf-8").read()
        if num != 1:
            html = html.replace("AI Operations Management, Chapter 1",
                                f"AI Operations Management, Chapter {num}")
            html = html.replace('<h1 class="chapter-title">The Category Error</h1>',
                                f'<h1 class="chapter-title">{title}</h1>')
        open(os.path.join(dst, f"AIOM_Ch{num:02d}_live.html"), "w",
             encoding="utf-8").write(html)
        # A stale fork beside the live text, which discovery must skip rather
        # than choose. Chapter 1's real folder still carries one.
        open(os.path.join(dst, "DRAFT-old.html"), "w", encoding="utf-8").write("<html></html>")
        for f in glob.glob(os.path.join(src_dir, "AIOM_Ch*_Checklist*.md")):
            shutil.copy(f, os.path.join(root, f"Ch{num:02d}_Synthetic",
                                        f"AIOM_Ch{num:02d}_Checklist.md"))

    found, notes = wb.discover_chapters(root)
    case("two locked chapters are discovered",
         lambda: [] if len(found) == 2 else ["found " + str(len(found))], False)
    case("the stale fork beside each live text is skipped",
         lambda: [] if sum("skipped" in n for n in notes) == 2 else ["not skipped"],
         False)

    out = "build/selftest-site"
    shutil.rmtree(out, ignore_errors=True)
    os.makedirs(out, exist_ok=True)
    fails, metas = quiet(wb.build_site, [p for _, p in found], out,
                         False, True, "", notes)
    # Chapter 2 is synthetic, so gates that compare it against the real ledger
    # and the real structure document are expected to object. What this control
    # proves is that the SITE BUILD runs over more than one chapter and emits a
    # complete site, which is the thing that has never been exercised.
    case("a two chapter site emits two chapter pages",
         lambda: [] if len(metas) == 2 and os.path.exists(
             os.path.join(out, "ch02", "index.html")) else ["missing ch02"], False)
    case("the sitemap covers both chapters",
         lambda: [] if "/ch02/" in open(os.path.join(out, "sitemap.xml"),
                                        encoding="utf-8").read()
         else ["ch02 absent from sitemap"], False)
    case("a publish build carries no noindex page",
         lambda: [f for f in fails if "noindex" in f], False)

    # W11. Decision 66 rules out analytics and the build self-hosts its fonts.
    # Both were true only because nobody had added anything, which is an
    # intention. These controls are what make it a check.
    case("W11 clean on the real site",
         lambda: quiet(wb.gate_w11, "build/web"), False)
    for label, snippet in (
            ("an analytics script", '<script src="https://plausible.io/js/x.js"></script>'),
            ("a CDN stylesheet", '<link rel="stylesheet" href="https://cdn.example/x.css">'),
            ("a remote image", '<img src="https://example.org/pixel.gif">')):
        probe = os.path.join("build", "w11-probe")
        shutil.rmtree(probe, ignore_errors=True)
        os.makedirs(probe, exist_ok=True)
        open(os.path.join(probe, "index.html"), "w", encoding="utf-8").write(
            "<html><body>" + snippet + "</body></html>")
        case(label + " is refused",
             lambda d=probe: quiet(wb.gate_w11, d))
    # An outbound LINK is not a request the page makes, and must stay legal:
    # the sources page links to every cited source and that is its job.
    probe = os.path.join("build", "w11-link")
    shutil.rmtree(probe, ignore_errors=True)
    os.makedirs(probe, exist_ok=True)
    open(os.path.join(probe, "index.html"), "w", encoding="utf-8").write(
        '<html><body><a href="https://example.org/paper">Open source</a></body></html>')
    case("an outbound anchor link stays legal",
         lambda: quiet(wb.gate_w11, probe), False)


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

    # THE CONTROL FOR THE REAL DEFECT OF 2026-08-13, reproduced rather than
    # invented. add_anchors wrote the slot id before the last character of the
    # match, which for the two patterns that match a whole element put the
    # attribute on the CLOSING tag: `</p id="slot-craft-section">`. Parsers
    # discard it, so the id was in the file and never in the DOM and two rail
    # links did nothing when clicked, while W4b counted them as anchors and W4c
    # reported that every link resolved. Both read ids with a regex. They parse
    # now, and this control is what proves the parse is doing the work.
    bad = web_html.replace('<p class="slot-label" id="slot-craft-section">',
                           '<p class="slot-label">', 1)
    bad = bad.replace("Craft section</p>",
                      'Craft section</p id="slot-craft-section">', 1)
    case("a slot id written onto a closing tag, so no link can reach it",
         lambda: quiet(wb.gate_w4, bad, meta))

    m4 = copy.deepcopy(meta)
    m4["figures"] = m4["figures"] + ["1.9"]
    case("a figure captioned but never referenced",
         lambda: quiet(wb.gate_w4, web_html, m4))

    m4 = copy.deepcopy(meta)
    m4["notes"] = []
    case("no citation resolved",
         lambda: quiet(wb.gate_w4, web_html, m4))

    # W4g. A mark added to the chapter template would pass every other gate in
    # this suite: it carries no text, so W1 text equivalence stays perfect. This
    # control is the only thing standing between the ruling and a reading page
    # that quietly fills with ornament.
    case("a spot mark added to the chapter page",
         lambda: quiet(wb.gate_w4,
                       web_html.replace("</article>",
                                        '<svg class="mark"></svg></article>'),
                       meta))

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

    print("\nW10, the site build and deploy readiness")
    _multi_chapter_control(case)

    print("\nW12 and W13, the theme layer")
    case("W12 clean on the real pages",
         lambda: quiet(wb.gate_w12, [("index", open("build/web/index.html",
                                                    encoding="utf-8").read())]), False)
    # A colour the design system does not own. tokenize_svg leaves it literal on
    # purpose, because silently rewriting an unknown colour would hide the drift.
    case("an unregistered colour in a figure",
         lambda: quiet(wb.gate_w12,
                       [("probe", '<svg><rect fill="#FF00AA"/></svg>')]))
    case("a tokenized figure passes",
         lambda: quiet(wb.gate_w12,
                       [("probe", '<svg><rect fill="var(--amber)"/></svg>')]), False)
    # tokenize_svg must map a known colour and leave an unknown one alone.
    out = wb.tokenize_svg('<svg><rect fill="#B4551F"/><rect fill="#FF00AA"/></svg>')
    case("tokenize_svg maps known and preserves unknown",
         lambda: [] if 'fill="var(--amber)"' in out and '#FF00AA' in out
         else ["mapping wrong: " + out], False)

    case("W13 clean on the real stylesheet",
         lambda: quiet(wb.gate_w13, "AIOM_web.css"), False)
    css = open("AIOM_web.css", encoding="utf-8").read()

    def probe_css(text, name):
        path = os.path.join("build", name)
        os.makedirs("build", exist_ok=True)
        open(path, "w", encoding="utf-8").write(text)
        return path

    # A foreground pushed below the AA floor, which is what a well-meant
    # "let us lighten that grey" edit looks like.
    bad = css.replace("  --folio:     #696154;", "  --folio:     #B7AEA0;", 1)
    assert bad != css
    case("a light token dropped below the AA floor",
         lambda: quiet(wb.gate_w13, probe_css(bad, "w13-aa.css")))

    # The two dark blocks are written twice because CSS cannot declare them once,
    # so they will drift the first time someone edits one of them.
    bad = css.replace(':root[data-theme="dark"] {\n    --paper:     #0F1D2B;',
                      ':root[data-theme="dark"] {\n    --paper:     #000000;', 1)
    assert bad != css
    case("the two dark token blocks drifting apart",
         lambda: quiet(wb.gate_w13, probe_css(bad, "w13-drift.css")))

    # ---------------------------------------------------------------- W14 ----
    # THE CONTROLS THAT MATTER MOST IN THIS FILE, because W14 is the only gate
    # in either suite that reads meaning, and because the damage it answers has
    # already happened five times. Each control below reproduces a REAL revert
    # from this chapter's history rather than an invented fault.
    print("\nW14, claim preservation")
    CH = ("Drafts/Ch01_The_Category_Error/00_Stage0_Draft/"
          "AIOM_Ch01_redraft.html")

    def probe_chapter(mutate, name):
        """Write a damaged Ch01 into a ChNN-shaped path, since W14 infers the
        chapter id from the path."""
        raw = open(CH, encoding="utf-8").read()
        lines = raw.split("\n")
        cut = next(i for i, l in enumerate(lines) if "Decision 51" in l)
        body, reg = "\n".join(lines[:cut]), "\n".join(lines[cut:])
        new = mutate(body)
        assert new != body, "injection was a no-op: " + name
        d = os.path.join("build", "w14", name, "Ch01", "00_Stage0_Draft")
        os.makedirs(d, exist_ok=True)
        p = os.path.join(d, "probe.html")
        open(p, "w", encoding="utf-8").write(new + "\n" + reg)
        return p

    case("W14 clean on the real chapter",
         lambda: quiet(wb.gate_w14, CH), False)

    # SF10, 2026-08-10: the consumption mechanism restored by a copy edit.
    case("a ruled narrowing reverted (SF10)",
         lambda: quiet(wb.gate_w14, probe_chapter(
             lambda b: b.replace(
                 "because subscribers used them more than the price had assumed",
                 "because customers were consuming more computing resources "
                 "than the monthly price covered"), "sf10")))

    # FC9, 2026-08-13: the absorbed-cost inference, cut as unsupported.
    case("a withdrawn claim restored (FC9)",
         lambda: quiet(wb.gate_w14, probe_chapter(
             lambda b: b.replace(
                 "The credit was consumed in a handful of prompts",
                 "Cursor had been paying the difference, but the difference "
                 "had become too expensive to absorb. The credit was consumed "
                 "in a handful of prompts"), "fc9")))

    # SF1, 2026-08-06: the superlative both external checks raised.
    case("a cut superlative returns (SF1)",
         lambda: quiet(wb.gate_w14, probe_chapter(
             lambda b: b.replace(
                 "Chief executive Sam Altman said publicly",
                 "The chief executive of the largest provider said publicly"),
             "sf1")))

    # NORMALIZATION IS LOAD BEARING AND THIS CONTROL IS WHY. Decision 58 wraps
    # proper nouns in <span class="nb">, so the SF3 sentence contains markup in
    # the middle. A checker comparing raw HTML would miss the revert entirely,
    # and the first draft of this control did exactly that and reported a
    # no-op.
    case("a revert hidden by .nb markup (SF3)",
         lambda: quiet(wb.gate_w14, probe_chapter(
             lambda b: b.replace(
                 'began enforcing monthly premium-request allowances for '
                 '<span class="nb">Copilot</span> and letting customers pay '
                 'for usage beyond them',
                 "began billing premium requests that had previously carried "
                 "no separate charge"), "sf3")))

    # THE BLIND SPOT. An empty ledger section must never read as a pass. This
    # control fails if gate_w14 reports success while checking nothing.
    def empty_ledger_probe():
        os.makedirs("build", exist_ok=True)
        p = os.path.join("build", "w14-empty-ledger.md")
        open(p, "w", encoding="utf-8").write("# AIOM Claim Ledger\n\n## Ch99\n")
        return claimcheck.summary(CH, p, "Ch01")

    case("an emptied ledger section reports checking nothing",
         lambda: [] if empty_ledger_probe() == (0, 0, 0, 0)
         else ["an empty ledger section did not report zero rulings"], False)

    # SUPERSESSION. Dan is the final editor and may overturn a fact-check
    # ruling; amend.py retires it by renaming its fields out of enforcement and
    # keeping them as history. Two things must both hold: the retired ruling
    # stops being enforced, AND it stops being counted, because a progress line
    # claiming protection that is no longer in force is this gate committing the
    # exact failure it exists to catch.
    def superseded_probe():
        src = open("AIOM_Claim_Ledger.md", encoding="utf-8").read()
        out = []
        for line in src.split("\n"):
            m = re.match(r"^-\s+(REQUIRED|FORBIDDEN|REVIEW):", line)
            out.append(re.sub(r"^-\s+(REQUIRED|FORBIDDEN|REVIEW):",
                              r"- SUPERSEDED-\1:", line) if m else line)
        os.makedirs("build", exist_ok=True)
        p = os.path.join("build", "w14-superseded.md")
        open(p, "w", encoding="utf-8").write("\n".join(out))
        return p

    sup = superseded_probe()
    case("a superseded ruling is no longer enforced",
         lambda: quiet(claimcheck.check, CH, sup, "Ch01"), False)
    case("a superseded ruling is no longer counted",
         lambda: [] if claimcheck.summary(CH, sup, "Ch01") == (0, 0, 0, 0)
         else ["superseded rulings are still counted as holding"], False)

    # ------------------------------------------------------- lock snapshots ---
    # What publishes is each chapter's last LOCK, never the working tree. These
    # controls guard the resolution itself, because a snapshot pointing at the
    # wrong commit would publish silently and correctly-looking.
    print("\nLock snapshots, what actually publishes")
    import snapshot as snap
    CH1_DIR = "Drafts/Ch01_The_Category_Error"
    CH1_CL = os.path.join(CH1_DIR, "AIOM_Ch01_Checklist_v6.md")

    lock = snap.lock_commit(CH1_CL)
    case("chapter 1's lock commit resolves",
         lambda: [] if lock and len(lock[0]) == 40 else ["no lock commit found"],
         False)

    snap_root = "build/selftest-snap"
    chapters, snotes = snap.materialize("Drafts", snap_root)
    case("only chapters that have locked are materialized",
         lambda: [] if [c[2] for c in chapters] == ["Ch01_The_Category_Error"]
         else ["materialized " + str([c[2] for c in chapters])], False)
    # Two distinct skips, both correct and both silent-if-unstated: a chapter
    # with no checklist has not been started, a chapter with one that never
    # reported Stage 9 is in progress. Neither publishes and neither is a
    # failure. The first draft of this control asserted the wrong message and
    # the self-test caught it, which is the self-test doing its job on itself.
    case("an unlocked chapter is skipped with a stated reason, not failed",
         lambda: [] if any("Ch02" in n and ("never locked" in n
                                            or "no checklist" in n)
                           for n in snotes)
         else ["Ch02 was not reported as skipped at all"], False)

    # THE CONTROL THAT MATTERS: the published bytes must be the LOCKED bytes.
    # A snapshot that silently resolved to HEAD would pass every other check in
    # this file while publishing unreviewed text.
    def snapshot_matches_lock():
        import subprocess
        live = os.path.join(snap_root, "Ch01_The_Category_Error",
                            "00_Stage0_Draft", "AIOM_Ch01_redraft.html")
        if not os.path.exists(live):
            return ["the live text was not materialized"]
        blob = subprocess.run(
            ["git", "show", "%s:%s/00_Stage0_Draft/AIOM_Ch01_redraft.html"
             % (lock[0], CH1_DIR)], capture_output=True)
        return ([] if blob.stdout == open(live, "rb").read()
                else ["materialized text differs from the lock commit's blob"])

    case("the materialized text IS the lock commit's text",
         snapshot_matches_lock, False)

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
