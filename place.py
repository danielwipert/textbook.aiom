#!/usr/bin/env python3
"""
place.py  |  callout placement pass

Floated definition callouts split across page breaks in WeasyPrint 69 and
break-inside:avoid does not prevent it. This pass keeps the design untouched and
instead moves any splitting callout to a neighbouring anchor paragraph, re-rendering
until every callout is intact. Moves are constrained to the callout's own section so
a term is never defined outside the section that uses it.

Usage:  python3 place.py AIOM_ch01.html
"""
import re, shutil, sys
from weasyprint import HTML
import pdfplumber

TINT = "#EDE3D0"


def hexc(c):
    if not c:
        return None
    if isinstance(c, (int, float)):
        c = (c, c, c)
    if len(c) == 1:
        c = (c[0],) * 3
    return "#" + "".join(f"{int(round(v * 255)):02X}" for v in c[:3])


def analyse(pdf_path):
    """Return (n_fragments, [terms of callouts that split])."""
    pdf = pdfplumber.open(pdf_path)
    frags, split = 0, []
    last_term = None
    for page in pdf.pages:
        boxes = sorted([r for r in page.rects
                        if hexc(r.get("non_stroking_color")) == TINT
                        and (r["x1"] - r["x0"]) < 200], key=lambda r: r["top"])
        for r in boxes:
            frags += 1
            term = "".join(c["text"] for c in sorted(
                [c for c in page.chars
                 if r["top"] - 2 < c["top"] < r["bottom"] and r["x0"] < c["x0"] < r["x1"]
                 and "Plex-Semi-Bold" in c["fontname"] and round(c["size"], 1) == 11.0],
                key=lambda c: c["x0"]))
            if term:
                last_term = term
            else:
                split.append(last_term)
    pdf.close()
    return frags, split


def parse(lines):
    """Locate aside blocks, top-level anchor paragraphs, and section boundaries."""
    asides, anchors, heads = [], [], []
    i = 0
    while i < len(lines):
        if lines[i].startswith('<aside class="definition">'):
            j = i
            while not lines[j].startswith("</aside>"):
                j += 1
            term = ""
            for k in range(i, j):
                m = re.search(r'<p class="term">(.*?)</p>', lines[k])
                if m:
                    term = m.group(1)
            asides.append({"start": i, "end": j, "term": term})
            i = j + 1
            continue
        if lines[i].startswith("<p>"):
            anchors.append(i)
        if lines[i].startswith("<h3 class=") or lines[i].startswith("<section"):
            heads.append(i)
        i += 1
    return asides, anchors, heads


def move(lines, aside, target_line):
    block = lines[aside["start"]:aside["end"] + 1]
    rest = lines[:aside["start"]] + lines[aside["end"] + 1:]
    shift = len(block) if aside["start"] < target_line else 0
    at = target_line - shift
    return rest[:at] + block + rest[at:]


def prose_positions(lines, terms):
    """Character offset of each term's first use in the body prose, asides excluded."""
    asides, _, _ = parse(lines)
    skip = set()
    for a in asides:
        skip.update(range(a["start"], a["end"] + 1))
    prose = "\n".join(re.sub(r"<[^>]+>", "", l)
                      for i, l in enumerate(lines) if i not in skip).lower()
    out = {}
    for t in terms:
        i = prose.find(t.lower())
        out[t] = i if i >= 0 else 10 ** 9
    return out


def order_adjacent(lines):
    """Sort each run of adjacent callouts by the order their terms appear in the prose.

    Two callouts pushed onto the same anchor by the placement pass would otherwise sit
    in document order, which need not match the order the reader meets the terms.
    """
    changed = []
    while True:
        asides, _, _ = parse(lines)
        group = None
        for a, b in zip(asides, asides[1:]):
            if all(not lines[k].strip() for k in range(a["end"] + 1, b["start"])):
                group = [a, b]
                break
        if group is None:
            break
        # extend the run
        asides_by_start = {a["start"]: a for a in asides}
        while True:
            last = group[-1]
            nxt = next((a for a in asides if a["start"] > last["end"]), None)
            if nxt and all(not lines[k].strip() for k in range(last["end"] + 1, nxt["start"])):
                group.append(nxt)
            else:
                break
        pos = prose_positions(lines, [a["term"] for a in group])
        want = sorted(group, key=lambda a: pos[a["term"]])
        if [a["term"] for a in want] == [a["term"] for a in group]:
            break
        blocks = {a["term"]: lines[a["start"]:a["end"] + 1] for a in group}
        start, end = group[0]["start"], group[-1]["end"]
        rebuilt = []
        for k, a in enumerate(want):
            rebuilt += blocks[a["term"]]
            if k < len(want) - 1:
                rebuilt.append("")
        lines = lines[:start] + rebuilt + lines[end + 1:]
        changed.append([a["term"] for a in want])
        break
    return lines, changed


def run(html_path, budget=14):
    src = open(html_path).read()
    shutil.copy(html_path, html_path + ".bak")
    lines = src.split("\n")
    renders, log = 0, []

    def render_and_score(ls):
        nonlocal renders
        open(html_path, "w").write("\n".join(ls))
        HTML(html_path, base_url=".").write_pdf("_place.pdf")
        renders += 1
        return analyse("_place.pdf")

    frags, split = render_and_score(lines)
    n = len(parse(lines)[0])
    print(f"start: {n} callouts, {frags} fragments, splitting: {split}")

    while split and renders < budget:
        asides, anchors, heads = parse(lines)
        target = next((a for a in asides if a["term"] == split[0]), None)
        if target is None:
            print(f"  cannot identify callout for '{split[0]}', stopping")
            break
        # anchors inside the same section as the callout
        lo = max([h for h in heads if h < target["start"]], default=-1)
        hi = min([h for h in heads if h > target["start"]], default=len(lines))
        window = [a for a in anchors if lo < a < hi]
        current = min((a for a in window if a > target["end"]), default=None)
        if current is None or len(window) < 2:
            print(f"  '{target['term']}' has no alternative anchor in its section, stopping")
            break
        idx = window.index(current)
        # prefer moving the callout earlier: that keeps it before the paragraph
        # that first uses its term, which is the locked placement rule
        order = [-k for k in range(1, len(window))] + [k for k in range(1, len(window))]
        best = None
        for d in order:
            j = idx + d
            if not (0 <= j < len(window)):
                continue
            cand = move(lines, target, window[j])
            f, s = render_and_score(cand)
            if len(s) < len(split):
                best = (cand, f, s, d)
                break
            if renders >= budget:
                break
        if best is None:
            print(f"  no placement inside the section fixes '{target['term']}', stopping")
            break
        lines, frags, split, d = best
        log.append((target["term"], d))
        print(f"  moved '{target['term']}' {abs(d)} paragraph(s) "
              f"{'earlier' if d < 0 else 'later'}; splitting now: {split}")

    before = list(lines)
    lines, reordered = order_adjacent(lines)
    if reordered:
        frags, split = render_and_score(lines)
        for order in reordered:
            print("  reordered adjacent callouts to prose order: " + ", ".join(order))
        if split:
            print(f"  reordering reintroduced a split ({split}); reverting to placed order")
            lines = before
            frags, split = render_and_score(lines)

    open(html_path, "w").write("\n".join(lines))
    print(f"done: {renders} renders, {len(split)} callouts still split")
    for term, d in log:
        print(f"  {term}: moved {abs(d)} paragraph(s) {'earlier' if d < 0 else 'later'}")
    return not split


if __name__ == "__main__":
    sys.exit(0 if run(sys.argv[1]) else 1)
