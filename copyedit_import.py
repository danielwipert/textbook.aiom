#!/usr/bin/env python3
"""
copyedit_import.py  |  a copy-edited .docx back into the chapter HTML

The other half of copyedit_export.py. Stage 6 happens in Word; the live text is
the HTML (Decision 50), so the edits have to come back, and they have to come
back without a human retyping them.

The rule this pass is built around: NEVER GUESS. A copy edit is small and local,
so almost every change is a word or a mark inside one block. Where a change is
unambiguous the pass applies it and says so. Where it is not, the pass refuses
and prints the block for a human, rather than writing something plausible into a
chapter that is about to lock. A silent wrong edit here is worse than fifty
edits applied by hand, because nothing downstream would catch it: Stage 7 checks
sources, G3 checks continuity, and neither reads for a word that changed meaning.

Tracked changes are read in their ACCEPTED form. python-docx concatenates the
runs inside <w:ins> and drops <w:delText>, which is exactly the accepted view.
Insertions that were never accepted therefore arrive as edits, which is what an
editor means by leaving them tracked.

Usage:
    python3 copyedit_import.py <edited.docx> <manifest.json> <chapter.html>
    python3 copyedit_import.py ... --apply      # write the HTML
"""
import argparse
import difflib
import html as htmllib
import json
import re
import sys

TAG_RE = re.compile(r"^\[([A-Z][A-Z ]+)\]\s*(.*)$", re.S)
SOURCES_RE = re.compile(r"^\(([^)]*)\)\s*(.*)$", re.S)

# Kept in step with copyedit_export.REGISTRY_BOUND. Duplicated rather than
# imported so neither tool can be run without the other present.
REGISTRY_BOUND = {"THEOREM STATEMENT", "THEOREM SCOPE",
                  "THEOREM ANTECEDENT", "THEOREM CONSEQUENT"}

# Only these kinds are exported with a "(...)" note after the tag. Any other
# block whose prose merely OPENS with a parenthetical is prose, not an annotated
# block. Reading the group unconditionally silently ate the "(a) ", "(b) ",
# "(c) " that open three paragraphs of the Chapter 1 P2 model inventory. Found
# 2026-08-08 by the unedited round trip, which is the only check that sees it.
SOURCED_KINDS = {"FOOTNOTE"} | REGISTRY_BOUND


def read_docx(path):
    """(kind, sources, text) per tagged paragraph, in document order."""
    from docx import Document
    out = []
    for p in Document(path).paragraphs:
        t = re.sub(r"\s+", " ", p.text).strip()
        if not t:
            continue
        m = TAG_RE.match(t)
        if not m:
            continue          # front matter: title line and the instructions
        kind, rest, sources = m.group(1).strip(), m.group(2).strip(), ""
        if kind in SOURCED_KINDS:
            s = SOURCES_RE.match(rest)
            if s:
                sources, rest = s.group(1).strip(), s.group(2).strip()
        out.append((kind, sources, rest))
    return out


def align(returned, blocks):
    """Match returned paragraphs to manifest blocks, and say how confident it is.

    Position alone is not enough: an editor may legitimately split a paragraph
    in two or merge two into one, and either shifts every index after it. The
    type sequence is the check. When it holds, position is trusted. When it
    breaks, the pass stops at the break and reports rather than sliding every
    later block by one and calling it an edit.
    """
    kinds_r = [k for k, _, _ in returned]
    kinds_b = [b["kind"] for b in blocks]
    if kinds_r == kinds_b:
        return list(zip(range(len(blocks)), returned)), []

    pairs, problems = [], []
    sm = difflib.SequenceMatcher(a=kinds_b, b=kinds_r, autojunk=False)
    for op, i1, i2, j1, j2 in sm.get_opcodes():
        if op == "equal":
            pairs += [(i, returned[j]) for i, j in zip(range(i1, i2),
                                                       range(j1, j2))]
        else:
            problems.append({
                "op": op,
                "html_blocks": [{"i": i, "kind": blocks[i]["kind"],
                                 "text": blocks[i]["text"][:90]}
                                for i in range(i1, i2)],
                "returned": [{"kind": returned[j][0],
                              "text": returned[j][2][:90]}
                             for j in range(j1, j2)],
            })
    return pairs, problems


def segments(old, new):
    """Minimal changed word spans between two versions of one block."""
    a, b = old.split(" "), new.split(" ")
    out = []
    for op, i1, i2, j1, j2 in difflib.SequenceMatcher(a=a, b=b,
                                                      autojunk=False).get_opcodes():
        if op == "equal":
            continue
        # Widen by one settled word on each side so the search string is
        # distinctive: "the" replaced by "a" is not findable on its own.
        lo, hi = max(0, i1 - 1), min(len(a), i2 + 1)
        jlo, jhi = max(0, j1 - 1), min(len(b), j2 + 1)
        out.append((" ".join(a[lo:hi]), " ".join(b[jlo:jhi])))
    return out


def locate(html_block, needle):
    """Find `needle` in a block that may carry inline markup.

    Returns (start, end) into html_block, or None. A match that spans a tag is
    refused: rewriting across <b> or <cite> is how inline markup gets eaten.
    """
    plain, index = [], []
    depth = 0
    for i, ch in enumerate(html_block):
        if ch == "<":
            depth += 1
        elif ch == ">":
            depth -= 1
        elif depth == 0:
            plain.append(ch)
            index.append(i)
    flat = htmllib.unescape("".join(plain))
    if len(flat) != len("".join(plain)):
        return None           # entities present: offsets would be wrong
    norm = re.sub(r"\s+", " ", flat)
    if norm != flat:
        # Collapse whitespace and keep a parallel index.
        keep = []
        prev_sp = False
        for n, ch in enumerate(flat):
            sp = ch.isspace()
            if sp and prev_sp:
                continue
            keep.append(n)
            prev_sp = sp
        norm = "".join(" " if flat[n].isspace() else flat[n] for n in keep)
        index = [index[n] for n in keep]
    hits = [m.start() for m in re.finditer(re.escape(needle), norm)]
    if len(hits) != 1:
        return None
    s = hits[0]
    return index[s], index[s + len(needle) - 1] + 1


def main():
    ap = argparse.ArgumentParser()
    ap.add_argument("docx")
    ap.add_argument("manifest")
    ap.add_argument("html")
    ap.add_argument("--apply", action="store_true",
                    help="write the HTML; without it, report only")
    a = ap.parse_args()

    man = json.load(open(a.manifest, encoding="utf-8"))
    blocks = man["blocks"]
    returned = read_docx(a.docx)
    print(f"{len(returned)} tagged paragraph(s) returned against "
          f"{len(blocks)} exported block(s)")

    pairs, problems = align(returned, blocks)
    refused = []
    if problems:
        print(f"\nSTRUCTURE CHANGED in {len(problems)} place(s). "
              f"These are NOT applied and need a human:")
        for p in problems:
            print(f"  {p['op']}:")
            for h in p["html_blocks"]:
                print(f"    HTML  [{h['i']}] {h['kind']}: {h['text']}")
            for r in p["returned"]:
                print(f"    DOCX      {r['kind']}: {r['text']}")

    src = open(a.html, encoding="utf-8").read()
    edits = []
    changed = 0

    for i, (kind, _sources, text) in pairs:
        original = blocks[i]["text"]
        if text == original:
            continue
        # A theorem panel renders a locked registry statement (standing rule 6,
        # Decision 56): the registry is the authority and the panel is its
        # rendering, so no antecedent may be added, dropped, merged, split,
        # weakened, or strengthened here. These blocks travel in the proof to be
        # proofread, not rewritten. Report and refuse.
        if kind in REGISTRY_BOUND:
            refused.append((i, original, text,
                            "REGISTRY BOUND. This renders a locked registry "
                            "statement and cannot be edited in a copy edit. "
                            "Amend and re-lock the registry, then re-render the "
                            "panel"))
            continue
        changed += 1
        print(f"\n[{i}] {kind}")
        s0, e0 = blocks[i]["span"]
        frag = src[s0:e0]
        for old, new in segments(original, text):
            print(f"    - {old}")
            print(f"    + {new}")
            where = locate(frag, old)
            if where is None:
                refused.append((i, old, new, "not uniquely locatable inside "
                                             "its own block, or it spans inline markup"))
                continue
            edits.append((s0 + where[0], s0 + where[1], new, i))

    # Applied last first, so an earlier edit cannot move a later offset.
    edits.sort(key=lambda e: e[0], reverse=True)
    for s0, e0, new, _i in edits:
        src = src[:s0] + new + src[e0:]

    blocks_touched = len({i for _, _, _, i in edits})
    print(f"\n{changed} block(s) edited; {len(edits)} span(s) applied across "
          f"{blocks_touched} block(s); {len(refused)} span(s) refused")
    for i, old, new, why in refused:
        print(f"  REFUSED block {i}: {why}. Apply by hand."
              f"\n    - {old}\n    + {new}")

    if a.apply and not problems and not refused:
        open(a.html, "w", encoding="utf-8").write(src)
        print(f"\nwrote {a.html}")
    elif a.apply:
        print("\nNOTHING WRITTEN. Resolve the reports above first: a partial "
              "import is harder to audit than none.")


if __name__ == "__main__":
    sys.exit(main())
