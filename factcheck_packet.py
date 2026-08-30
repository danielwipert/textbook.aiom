#!/usr/bin/env python3
"""Build a fact-check packet: every cited passage paired with its register entry.

Repo tooling as of 2026-08-10, on Dan's ruling, closing the open thread that had
asked whether the packet was worth having on every chapter. It is: Stages 3 and 7
both need one, so fifteen chapters need thirty.

The history is the argument. The Stage 3 packet of 2026-08-10 was built by a
throwaway script in a session scratchpad and died with its container; the Stage 7
packet four hours later had to rebuild the same work from nothing. A script that
has to be rewritten to reproduce a step is not a reproducible step.

THE VALUE-SURFACE LINE WAS REMOVED 2026-08-29 BECAUSE THIS SCRIPT NEVER
PERFORMED IT. It asserted "175 numeric atoms and 32 date atoms, identical to the
Stage 3 audited render", which was a Chapter 1 measurement taken by hand and
recorded in that chapter's checklist, printed unconditionally into every packet.
At Stage 3 there is no prior audited render to be identical to. A checker who
wants that comparison at Stage 7 runs it and records it; the packet no longer
claims it was run.

WHAT THIS DOES NOT DO. It does not verify anything. Stages 3 and 7 are
STRUCTURALLY external, not external by preference: no source host is reachable
from the Claude environment, verified 2026-08-06 against six of them. This
assembles what a human checker needs and states the mechanical checks that were
run locally. It must never be described as a fact check.

The register notes are reproduced IN FULL and verbatim, never summarised. They
carry the verification history and, for findings already ruled, the condition that
would reverse the ruling. SF7 and SF11 both exist because a note outlived the
prose it described, and both were catchable only because the note quoted the
actual sentence.

Usage:
    python3 factcheck_packet.py <chapter.html> --stage 7 --render <name.pdf> --out <out.md>
"""

import argparse
import json
import re
from pathlib import Path

import claimcheck


def footnote_report(html_path):
    """(count, sentence) describing the footnotes this chapter builds.

    Counted by running the SAME footnotes.inject the print and web builds run,
    so the number cannot drift from the artifact. Returns a stated failure
    rather than a number when the build raises, because a packet that omits a
    broken footnote build tells a checker less than nothing.
    """
    try:
        import footnotes
        raw = Path(html_path).read_text(encoding="utf-8")
        _, report = footnotes.inject(raw, url_policy="none")
        n = len(report)
        return n, (f"{n} footnote(s) generated. Gate 8 checks each sits on its "
                   f"calling page; its verdict on the shipped render is on the "
                   f"RENDER line above, where it is measured rather than assumed.")
    except Exception as exc:                       # noqa: BLE001
        return None, f"NOT RUN. footnotes.inject raised: {exc}"


def render_gates(render_path, html_path):
    """What the fifteen print gates ACTUALLY say about the render being shipped.

    THIS LINE USED TO ASSERT "all fifteen gates green" WITHOUT RUNNING A GATE,
    and the footnote line asserted that gate 8 had passed on the strength of a
    footnote COUNT. Both were scope claims written from intention, in the one
    document that leaves this repository for an external checker, who has no way
    to test either and every reason to believe them. Found 2026-08-30, when
    Chapter 2's Stage 7 packet was generated on a render that fails gate 8 and
    said so nowhere.

    A missing toolchain reports NOT RUN rather than reading as an absence of
    defects, which is W16b's recorded failure. A FAILING gate cannot reach that
    branch: qa() returns False, it does not raise, so the except catches an
    absent pdfplumber and nothing else.

    source_html is passed and is NOT optional: gate 14 excludes a one-line
    paragraph from its widow count by reading the chapter's whole paragraphs
    from it, and passed None it returns an empty set SILENTLY and reports a
    phantom widow.
    """
    try:
        import contextlib
        import io

        import AIOM_build
        buf = io.StringIO()
        with contextlib.redirect_stdout(buf):
            ok = AIOM_build.qa(render_path, source_html=html_path)
    except Exception as exc:                       # noqa: BLE001
        return f"print gates NOT RUN on this file, so it is ungated here: {exc}"
    if ok:
        return "all fifteen print gates pass on this file, run here"
    return ("FAILING a print gate on this file: "
            + "; ".join(AIOM_build.LAST_FAILS))


def split_register(raw):
    """Return (body_html, register_json_text). The register is the Decision 51
    block: a JSON object whose first key is _README."""
    m = re.search(r'\{\s*"_README"', raw)
    if not m:
        raise SystemExit("no source register found (expected a _README key)")
    start = m.start()
    depth, end = 0, None
    for i in range(start, len(raw)):
        if raw[i] == "{":
            depth += 1
        elif raw[i] == "}":
            depth -= 1
            if depth == 0:
                end = i + 1
                break
    if end is None:
        raise SystemExit("source register never closes")
    return raw[:start], raw[start:end]


def render_field(v):
    """Register fields are strings, lists of strings, or lists of author objects
    carrying family, given and sometimes handle. Render all three without
    dropping a name, since a checker verifies bylines against the source."""
    if isinstance(v, list):
        return ", ".join(render_field(x) for x in v)
    if isinstance(v, dict):
        name = " ".join(p for p in (v.get("given"), v.get("family")) if p)
        return f"{name} ({v['handle']})" if v.get("handle") else (name or json.dumps(v))
    return str(v)


def strip_tags(s):
    s = re.sub(r"<span class=\"ckey\">.*?</span>", "", s, flags=re.S)
    s = re.sub(r"<[^>]+>", "", s)
    return re.sub(r"\s+", " ", s).strip()


def main():
    ap = argparse.ArgumentParser()
    ap.add_argument("html")
    ap.add_argument("--stage", required=True)
    ap.add_argument("--render", required=True)
    ap.add_argument("--out", required=True)
    a = ap.parse_args()

    raw = Path(a.html).read_text(encoding="utf-8")
    body, regtext = split_register(raw)
    reg = json.loads(regtext)

    # Every paragraph carrying a citation marker, in document order.
    cited = []
    for m in re.finditer(r"<p[^>]*>.*?</p>", body, flags=re.S):
        block = m.group(0)
        keys = []
        for km in re.finditer(r"<span class=\"ckey\">\[([^\]]+)\]</span>", block):
            keys += [k.strip() for k in re.split(r"\s*\+\s*", km.group(1))]
        if not keys:
            continue
        cite = re.search(r"<cite[^>]*>(.*?)</cite>", block, flags=re.S)
        claim = strip_tags(re.sub(r"<cite[^>]*>.*?</cite>", "", block, flags=re.S))
        gloss = strip_tags(cite.group(1)) if cite else ""
        cited.append((claim, keys, gloss))

    defined = {k for k in reg if not k.startswith("_")}
    used = {k for _, ks, _ in cited for k in ks}

    orphans = sorted(defined - used)
    dangling = sorted(used - defined)

    # THE PREAMBLE IS DERIVED FROM THIS CHAPTER, NEVER CARRIED FORWARD FROM THE
    # LAST ONE. Every line below was hardcoded Chapter 1 fact until 2026-08-29,
    # when the tool was first run on a second chapter: the title said Chapter 1,
    # the footnote count said 6 against an actual 9, the ruled-form line listed
    # Chapter 1's SF and CE rulings, and the value-surface line claimed a
    # comparison against a "Stage 3 audited render" that does not exist for a
    # chapter arriving AT Stage 3. A packet that states checks nobody ran is the
    # exact failure this repository keeps finding, committed by the artifact a
    # checker is meant to trust.
    chap = claimcheck.chapter_id_for(a.html)
    chap_label = f"Chapter {int(chap[2:])}" if chap else "Chapter (unknown)"

    fn_count, fn_note = footnote_report(a.html)
    live, req, forb, rev = claimcheck.summary(a.html, chapter=chap)

    out = []
    out.append(f"# {chap_label}, Stage {a.stage}. Claim inventory and source packet\n")
    out.append("Generated from the live text by `factcheck_packet.py` at the repo root.")
    out.append(f"Stage {a.stage} is STRUCTURALLY external: no source host is reachable from the")
    out.append("Claude environment, verified 2026-08-06 against six of them, so nothing")
    out.append("below is a verification. It is the material a checker needs.\n")
    out.append(f"LIVE TEXT      `{a.html}`")
    out.append(f"RENDER         `{a.render}`, {render_gates(a.render, a.html)}.\n")
    out.append("WHAT THIS IS. Every passage carrying a citation marker, with the keys it")
    out.append("cites and the register entry behind each key. The register note is")
    out.append("reproduced in full because it carries the verification history and, for")
    out.append("findings already ruled, the condition that would reverse the ruling.\n")
    if live:
        out.append("WHAT A CHECKER SHOULD NOT RE-RAISE. This chapter carries "
                   f"{live} ruling(s) already")
        out.append("made and still in force, recorded in `AIOM_Claim_Ledger.md` and in the")
        out.append("register notes below. A checker who reaches one should say whether the")
        out.append("condition named in the note is now met, not restate the finding.\n")
    else:
        out.append("WHAT A CHECKER SHOULD NOT RE-RAISE. Nothing yet. This chapter carries no")
        out.append("ruled claim narrowings, so every finding a checker raises here is new.\n")
    out.append("MECHANICAL CHECKS ALREADY RUN, so they need not be repeated:\n")
    out.append(f"  Register closure    {len(defined)} keys defined, {len(used)} cited. "
               f"{len(orphans)} orphan(s), {len(dangling)} dangling.")
    if orphans:
        out.append(f"                      orphans: {', '.join(orphans)}")
    if dangling:
        out.append(f"                      dangling: {', '.join(dangling)}")
    out.append(f"  Citation markers    {len(cited)} cited passages, every marker resolving to a key.")
    out.append(f"  Footnote build      {fn_note}")
    if live:
        out.append(f"  Ruled-form check    {live} ruling(s) in force for {chap or 'this chapter'}: "
                   f"{req} required, {forb} forbidden,")
        out.append(f"                      {rev} by reading. `claimcheck.py` reports "
                   f"{'PASS' if not claimcheck.broken_rulings(a.html, chapter=chap) else 'FAIL'}.")
    else:
        out.append(f"  Ruled-form check    nothing to check. No ruling is recorded for "
                   f"{chap or 'this chapter'} yet.")
    out.append("")
    out.append("---\n")
    out.append("## Part 1. Cited passages, in document order\n")

    for n, (claim, keys, gloss) in enumerate(cited, 1):
        out.append(f"### C{n}\n")
        out.append("CLAIM TEXT AS IT STANDS\n")
        out.append(f"> {claim}\n")
        out.append("CITES: " + ", ".join(f"`{k}`" for k in keys) + "\n")
        if gloss:
            out.append(f"IN-CHAPTER GLOSS: {gloss}\n")

    out.append("---\n")
    out.append("## Part 2. Register entries, verbatim\n")
    for k in sorted(used):
        e = reg[k]
        out.append(f"### `{k}`\n")
        for field in ("type", "authors", "title", "container", "date", "url",
                      "volume", "issue", "pages", "doi", "perishable",
                      "accessed", "upgrade"):
            if field in e and e[field] not in (None, "", []):
                out.append(f"- **{field}**: {render_field(e[field])}")
        if e.get("note"):
            note = e["note"]
            note = " ".join(note) if isinstance(note, list) else note
            out.append(f"\nNOTE, verbatim:\n\n> {note}\n")
        out.append("")

    Path(a.out).write_text("\n".join(out), encoding="utf-8")
    print(f"wrote {a.out}")
    print(f"  cited passages : {len(cited)}")
    print(f"  keys defined   : {len(defined)}")
    print(f"  keys cited     : {len(used)}")
    print(f"  orphans        : {sorted(defined - used) or 'none'}")
    print(f"  dangling       : {sorted(used - defined) or 'none'}")


if __name__ == "__main__":
    main()
