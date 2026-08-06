#!/usr/bin/env python3
"""
AIOM_build.py  |  version 6.2  |  2026-07-30

One command to stage fonts, render a chapter, and run every QA gate.

Usage:
    python3 AIOM_build.py --fonts            # stage fonts (run once per session)
    python3 AIOM_build.py AIOM_ch01.html     # footnotes + render + QA
    python3 AIOM_build.py AIOM_ch01.html --out /mnt/user-data/outputs/Ch1.pdf
"""

import argparse, io, os, re, shutil, subprocess, sys, urllib.request, zipfile
from collections import Counter

FONT_DIR = "fonts/use"
PLEX_ZIP = ("https://github.com/IBM/plex/releases/download/"
            "%40ibm/plex-sans%401.1.0/ibm-plex-sans.zip")
JOST_VF  = ("https://raw.githubusercontent.com/google/fonts/main/"
            "ofl/jost/Jost%5Bwght%5D.ttf")
PLEX_FACES = ["Text", "SemiBold", "Medium", "Italic"]
JOST_INSTANCES = {"Jost-Medium": 500, "Jost-SemiBold": 600}


def stage_fonts():
    """Download IBM Plex Sans and build the two static Jost instances."""
    os.makedirs(FONT_DIR, exist_ok=True)
    print("Staging IBM Plex Sans ...")
    data = urllib.request.urlopen(PLEX_ZIP, timeout=120).read()
    with zipfile.ZipFile(io.BytesIO(data)) as z:
        for face in PLEX_FACES:
            member = next(n for n in z.namelist()
                          if n.endswith(f"complete/ttf/IBMPlexSans-{face}.ttf"))
            with z.open(member) as src, open(f"{FONT_DIR}/IBMPlexSans-{face}.ttf", "wb") as dst:
                shutil.copyfileobj(src, dst)
            print(f"   IBMPlexSans-{face}.ttf")

    print("Building Jost static instances ...")
    from fontTools.ttLib import TTFont
    from fontTools.varLib.instancer import instantiateVariableFont
    vf = urllib.request.urlopen(JOST_VF, timeout=120).read()
    for name, wght in JOST_INSTANCES.items():
        f = TTFont(io.BytesIO(vf))
        instantiateVariableFont(f, {"wght": wght}).save(f"{FONT_DIR}/{name}.ttf")
        print(f"   {name}.ttf  (wght {wght})")
    print("Fonts staged.")


def render(html, out):
    from weasyprint import HTML
    HTML(html, base_url=os.path.dirname(os.path.abspath(html)) or ".").write_pdf(out)
    print(f"Rendered {out}")


def build(html_path, out, url_policy="none"):
    """Generate footnotes from the chapter source block, then render.

    Returns the number of footnotes injected, for gate 8 to check against.
    URL policy is "none" by ruling: URLs live in the source block and the
    back-of-book bibliography, not in page footnotes.
    """
    import footnotes
    injected, rep = footnotes.inject(open(html_path).read(),
                                     url_policy=url_policy)
    print_html = html_path.replace(".html", ".print.html")
    open(print_html, "w").write(injected)
    print(f"{len(rep)} footnote(s) generated from the source block "
          f"(url_policy={url_policy})")
    render(print_html, out)
    return len(rep)


# The failure list from the most recent qa() call. place.py needs to know WHICH
# gates a candidate placement breaks, not merely that something broke: a
# placement that fixes gate 4 while pushing a footnote off its calling page is
# not a fix. Kept as a module-level record so qa()'s boolean return, which
# callers already branch on, does not change meaning.
LAST_FAILS = []


def qa(path, expected_footnotes=None):
    """Every gate from section 8 of AIOM_Design_QA_Spec_v1.md (11 gates).
    Returns True if all pass."""
    import pdfplumber

    def hexc(c):
        if not c:
            return None
        if isinstance(c, (int, float)):
            c = (c, c, c)
        if len(c) == 1:
            c = (c[0],) * 3
        return "#" + "".join(f"{int(round(v * 255)):02X}" for v in c[:3])

    pdf = pdfplumber.open(path)
    fails = []

    overflow = []
    for i, p in enumerate(pdf.pages):
        limit = 428.4 if (i + 1) % 2 == 1 else 417.6
        for c in p.chars:
            if 60 < c["top"] < 640 and c["x1"] > limit + 1.5:
                overflow.append((i + 1, round(c["x1"], 1), c["text"]))
    print(f"1. right-margin overflow ... {len(overflow)}")
    if overflow:
        fails.append(f"overflow: {overflow[:5]}")

    dashes = [(i + 1, c["text"]) for i, p in enumerate(pdf.pages)
              for c in p.chars if c["text"] in ("\u2014", "\u2013")]
    print(f"2. em / en dashes ......... {len(dashes)}")
    if dashes:
        fails.append(f"dashes: {dashes[:5]}")

    for i, p in enumerate(pdf.pages):
        head = [c for c in p.chars if round(c["size"], 1) == 8.0 and "Jost" in c["fontname"]]
        folio = [c for c in p.chars if round(c["size"], 1) == 9.0
                 and hexc(c.get("non_stroking_color")) == "#9B8F7C"]
        if not folio:
            fails.append(f"p{i + 1}: missing folio")
        if i > 0 and not head:
            fails.append(f"p{i + 1}: missing running head")
        if i == 0 and head:
            fails.append("p1: running head should be suppressed on the opener")
    print("3. heads and folios ....... checked")

    boxes = [(i + 1, r) for i, p in enumerate(pdf.pages) for r in p.rects
             if hexc(r.get("non_stroking_color")) == "#EDE3D0"
             and (r["x1"] - r["x0"]) < 200]
    tops = [b for b in boxes if abs(b[1]["top"] - 61.2) < 0.5]
    if tops:
        print(f"4. callout splits ......... {len(tops)}  run place.py to resolve")
        fails.append(f"{len(tops)} definition callout(s) split across a page break; "
                     "run place.py on this chapter")
    else:
        print("4. callout splits ......... 0")

    faces = sorted(set(c["fontname"].split("+")[-1] for p in pdf.pages for c in p.chars))
    expected = {"Jost-Medium", "Jost-Semi-Bold", "Plex", "Plex-Italic",
                "Plex-Medium", "Plex-Semi-Bold"}
    extra = set(faces) - expected
    print(f"5. font faces ............. {len(faces)}" + (f"  UNEXPECTED: {extra}" if extra else ""))
    if extra:
        fails.append(f"unexpected faces: {extra}")

    kt = [(i + 1, r) for i, p in enumerate(pdf.pages) for r in p.rects
          if hexc(r.get("non_stroking_color")) == "#EDE3D0"
          and (r["x1"] - r["x0"]) >= 200]
    bands = [(i + 1, r) for i, p in enumerate(pdf.pages) for r in p.rects
             if hexc(r.get("non_stroking_color")) == "#DCCFB4"]
    print(f"6. key terms .............. {len(kt)} entries, {len(bands)} header bands")
    if len(kt) != len(bands):
        fails.append(f"key terms: {len(kt)} fields but {len(bands)} bands, an entry lost its header")

    prov = [c for i, p in enumerate(pdf.pages) if i == 0 for c in p.chars
            if round(c["size"], 1) == 7.0 and hexc(c.get("non_stroking_color")) == "#B4551F"
            and "Semi-Bold" in c["fontname"]]
    print(f"7. opening case provenance  {'present' if prov else 'MISSING'}")
    if not prov:
        fails.append("opening case has no provenance line")

    fn_pages = {}
    for i, p in enumerate(pdf.pages):
        left = 68.4 if (i + 1) % 2 == 1 else 57.6
        rows = {}
        for c in p.chars:
            if (round(c["size"], 1) == 7.0
                    and hexc(c.get("non_stroking_color")) == "#B4551F"
                    and "Semi-Bold" not in c["fontname"]):
                rows.setdefault(round(c["top"], 0), []).append(c)
        calls, notes = set(), set()
        for cs in rows.values():
            cs = sorted(cs, key=lambda c: c["x0"])
            num = "".join(c["text"] for c in cs).strip().rstrip(".")
            (notes if abs(cs[0]["x0"] - left) < 0.6 else calls).add(num)
        if calls or notes:
            fn_pages[i + 1] = (calls, notes)
    total = sum(len(c) for c, _ in fn_pages.values())
    orphans = [(pg, sorted(c ^ n)) for pg, (c, n) in fn_pages.items() if c != n]
    print(f"8. footnotes .............. {total} called, all on the calling page"
          if not orphans else f"8. footnotes .............. {total} called, MISPLACED {orphans}")
    if orphans:
        fails.append(f"footnotes not on the page of their call: {orphans}")
    # Closes gap G-H. Without this a chapter whose footnote apparatus is not
    # wired renders zero footnotes and gate 8 reports success.
    if expected_footnotes is not None and total != expected_footnotes:
        fails.append(f"footnotes: {expected_footnotes} expected from the source "
                     f"block, {total} rendered")

    dated_pages = {}
    for i, p in enumerate(pdf.pages):
        left = 68.4 if (i + 1) % 2 == 1 else 57.6
        rows = {}
        for c in p.chars:
            if (round(c["size"], 1) == 7.0
                    and hexc(c.get("non_stroking_color")) == "#B4551F"
                    and "Semi-Bold" in c["fontname"]):
                rows.setdefault(round(c["top"], 0), []).append(c["x0"])
        n = sum(1 for xs in rows.values() if left + 6 < min(xs) < 200)
        if n:
            dated_pages[i] = n
    if not dated_pages:
        print("9. dated evidence boxes ... none in this chapter")
    else:
        from pdf2image import convert_from_path
        imgs = convert_from_path(path, dpi=110)
        found = widths = 0
        for i, n in dated_pages.items():
            im = imgs[i].convert("RGB")
            left = 68.4 if (i + 1) % 2 == 1 else 57.6
            x = int(round(left / 72 * 110)) + 1
            run = 0
            for y in range(60, im.size[1] - 60):
                if all(abs(a - b) <= 6 for a, b in zip(im.getpixel((x, y)), (110, 99, 83))):
                    run += 1
                else:
                    if run > 15:
                        found += 1
                        w = [xx for xx in range(x - 6, x + 8)
                             if all(abs(a - b) <= 6 for a, b in
                                    zip(im.getpixel((xx, y - 5)), (110, 99, 83)))]
                        widths = max(widths, len(w))
                    run = 0
        total = sum(dated_pages.values())
        print(f"9. dated evidence boxes ... {total} labelled, {found} rules, "
              f"max rule width {widths}px")
        if found != total:
            fails.append(f"dated boxes: {total} labels but {found} rules rendered")
        if widths > 3:
            fails.append(f"dated box rule rendering {widths}px wide, expected a hairline")

    import re as _re
    stranded = []
    labels = 0
    for i, p in enumerate(pdf.pages):
        rows = {}
        for c in p.chars:
            if round(c["size"], 1) == 8.5 and "Jost" in c["fontname"]:
                rows.setdefault(round(c["top"], 0), []).append(c)
        titles = [round(c["top"], 0) for c in p.chars
                  if round(c["size"], 1) == 11.5 and "Jost" in c["fontname"]]
        for t, cs in rows.items():
            txt = "".join(c["text"] for c in sorted(cs, key=lambda c: c["x0"]))
            if _re.match(r"^P\d", txt):
                labels += 1
                if not any(ti > t for ti in titles):
                    stranded.append((i + 1, txt[:16]))
    if labels:
        print(f"10. problem labels ........ {labels} found, "
              + ("all with their title" if not stranded else f"STRANDED {stranded}"))
        if stranded:
            fails.append(f"problem label separated from its title: {stranded}")
    else:
        print("10. problem labels ........ none in this chapter")

    # Gate 11: theorem panel integrity. Closes gap G-A.
    # .theorem is a block with break-inside: avoid, so the WeasyPrint float
    # bug does not apply. This gate catches the two failures the property
    # cannot prevent: WeasyPrint ignoring it, and a panel forced to break
    # because it does not fit the space remaining on the page.
    BOTTOM_EDGE = 684 - 57.6          # 626.4pt, bottom of the text block
    panels = [(i + 1, r) for i, p in enumerate(pdf.pages) for r in p.rects
              if hexc(r.get("non_stroking_color")) == "#F7EDE2"]
    amber = [(i + 1, r) for i, p in enumerate(pdf.pages) for r in p.rects
             if hexc(r.get("non_stroking_color")) == "#B4551F"]
    # WeasyPrint paints a border as a filled rect covering the whole border
    # box, then paints the background over it. A 3pt left border therefore
    # never appears as a 3pt sliver. Match the border box instead: same page,
    # same top and height, starting at or left of the tint rect.
    def has_rule(pg, t):
        return any(apg == pg and abs(a["top"] - t["top"]) < 0.6
                   and abs((a["bottom"] - a["top"]) - (t["bottom"] - t["top"])) < 0.6
                   and a["x0"] <= t["x0"] + 0.1
                   for apg, a in amber)
    # A panel legitimately beginning at the top of a page is indistinguishable
    # from a continuation by position alone, so position is not used as a
    # failure signal. A split is proved by either of two facts: a panel
    # truncated at the bottom text edge, or more tinted fields than labels
    # (a continuation carries no label of its own).
    labels = set()
    for i, p in enumerate(pdf.pages):
        rows = {}
        for c in p.chars:
            if (round(c["size"], 1) == 8.5 and "Jost" in c["fontname"]
                    and hexc(c.get("non_stroking_color")) == "#B4551F"):
                rows.setdefault(round(c["top"], 0), []).append(c)
        for t, cs in rows.items():
            txt = "".join(c["text"] for c in sorted(cs, key=lambda c: c["x0"]))
            if txt.strip().upper().startswith("THEOREM"):
                labels.add((i + 1, t))
    truncated = [pg for pg, r in panels if abs(r["bottom"] - BOTTOM_EDGE) < 0.5]
    unruled = [pg for pg, r in panels if not has_rule(pg, r)]
    if not panels:
        print("11. theorem panel ......... none in this chapter")
    else:
        state = "intact"
        if truncated or len(panels) > len(labels):
            state = "SPLIT"
        elif unruled:
            state = "RULE MISSING"
        print(f"11. theorem panel ......... {len(panels)} panel(s), "
              f"{len(labels)} label(s), {state}")
        if truncated:
            fails.append(f"theorem panel truncated at the bottom text edge on "
                         f"page(s) {truncated}; it split across a page break")
        if len(panels) > len(labels):
            fails.append(f"theorem panels: {len(panels)} tinted field(s) but "
                         f"only {len(labels)} label(s); a panel split and its "
                         f"continuation carries no label")
        if unruled:
            fails.append(f"theorem panel on page(s) {unruled} has no amber "
                         f"left rule")

    # ----------------------------------------------------------------------
    # Gates 12 to 14. Added 2026-08-05. The G2 checklist claimed figure
    # validation, widow and orphan detection, and a bottom-margin check for
    # months while AIOM_build.py performed none of them, so those sub-boxes
    # were ticked by hand and status_check.py accepted the tick. A gate that
    # reads green while nothing checked is worse than a gate that does not
    # exist, because it is trusted.
    # ----------------------------------------------------------------------

    # Shared line model. Characters grouped into lines by rounded baseline.
    # The main text column starts at the left margin; definition callouts are
    # floated into a narrow right column, so their lines are legitimately
    # short and must never be measured as body lines.
    BOTTOM = 640.0
    BODY_SIZE = 11.0
    X_TOL = 2.0

    def lines_of(page):
        rows = {}
        for c in page.chars:
            if c["text"].strip():
                rows.setdefault(round(c["top"], 0), []).append(c)
        return [(k, rows[k]) for k in sorted(rows)]

    # The design mirrors its margins for binding, so the main column starts at
    # a different x on recto and verso. A single hard-coded left edge silently
    # excludes every line on half the book: it made gate 14 analyse only even
    # pages, and it hid Figure 1.1's caption from gate 12 the moment the figure
    # moved to an odd page. Derive the edge per page instead of assuming it.
    page_left = {}
    for i, p in enumerate(pdf.pages):
        xs = [round(c["x0"], 1) for c in p.chars
              if round(c["size"], 1) == BODY_SIZE and 60 < c["top"] < BOTTOM]
        if xs:
            page_left[i] = min(Counter(xs).most_common(1)[0][0], min(xs))

    def in_main_column(page_no, row):
        left = page_left.get(page_no)
        return left is not None and abs(row[0]["x0"] - left) <= X_TOL

    def all_semibold(row):
        """A line set entirely in the semibold face at body size.

        That is a key-term name in the register, which is apparatus: the
        definition beneath it is 9.5pt and already excluded by size. Counted as
        prose, every term name reads as a one-line paragraph, so the first on a
        page scores as a widow and the last as an orphan. On Chapter 1 that
        produced exactly one phantom widow and one phantom orphan on the Key
        terms page, carried as CD7 and booked as real design work. Found at
        Stage 5, 2026-08-06.

        The whole line is tested, not its first character: body prose carries
        inline bold for a term at first use, so a line may legitimately open in
        semibold and still be prose. Every such line in Chapter 1 is mixed, and
        the six fully-semibold lines are all key-term names.
        """
        return all("Semi" in c["fontname"] for c in row)

    def is_body(page_no, row):
        return (round(row[0]["size"], 1) == BODY_SIZE
                and in_main_column(page_no, row)
                and "Jost" not in row[0]["fontname"]
                and not all_semibold(row))

    def width(row):
        return sum(c["width"] for c in row)

    # 12. Figures: captioned, numbered in order, each referenced in the text.
    # A caption is a caption-size line that OPENS with the figure label at the
    # left margin. An in-text reference is body size and mid-line. Matching on
    # the string alone counts every reference as a caption, which reads as a
    # duplicate figure number.
    CAP_SIZE = 9.0
    caps, refs = [], []
    for i, p in enumerate(pdf.pages):
        for _, row in lines_of(p):
            text = "".join(c["text"] for c in row)
            m = re.match(r"\s*Figure\s*(\d+\.\d+)", text)
            if m and round(row[0]["size"], 1) == CAP_SIZE \
                    and in_main_column(i, row):
                caps.append((m.group(1), i + 1))
            for r in re.finditer(r"Figure\s*(\d+\.\d+)", text):
                if not (m and r.start() == m.start()):
                    refs.append((r.group(1), i + 1))
    cap_nums = [n for n, _ in caps]
    ref_nums = {n for n, _ in refs}
    if not cap_nums:
        print("12. figures ............... none in this chapter")
    else:
        key = lambda s: [int(x) for x in s.split(".")]
        order_ok = cap_nums == sorted(cap_nums, key=key)
        dupes = sorted({n for n in cap_nums if cap_nums.count(n) > 1})
        unref = [n for n in cap_nums if n not in ref_nums]
        print(f"12. figures ............... {len(cap_nums)} captioned, "
              f"{'in order' if order_ok else 'OUT OF ORDER'}, "
              f"{len(refs)} in-text reference(s), {len(unref)} unreferenced")
        if not order_ok:
            fails.append(f"figure captions out of document order: {cap_nums}")
        if dupes:
            fails.append(f"figure number captioned more than once: {dupes}")
        if unref:
            fails.append(f"figure(s) captioned but never referenced in the "
                         f"text: {unref}")
    dangling = sorted(ref_nums - set(cap_nums))
    if dangling:
        fails.append(f"text references a figure that has no caption: "
                     f"{dangling}")

    # 13. Bottom margin. The folio sits below the text block by design, in its
    # own colour, so it is excluded by that signature rather than by position.
    FOLIO_COLOR = "#9B8F7C"
    below = []
    for i, p in enumerate(pdf.pages):
        for c in p.chars:
            if not c["text"].strip() or c["top"] <= BOTTOM + 1.5:
                continue
            if hexc(c.get("non_stroking_color")) == FOLIO_COLOR:
                continue                      # folio, legitimately below
            below.append((i + 1, round(c["top"], 1), c["text"]))
    print(f"13. bottom margin ......... {len(below)} character(s) below the "
          f"text block, folio excluded")
    if below:
        fails.append(f"text below the bottom margin: {below[:5]}")

    # 14. Widows, orphans, stranded heads. Body prose here is not indented, so
    # a paragraph start is marked by a larger-than-leading gap above the line,
    # and a paragraph end by a line that does not fill the measure.
    #   orphan  = a paragraph's FIRST line alone at the foot of a page
    #   widow   = a paragraph's LAST line alone at the head of a page
    # A short line at the foot of a page is NOT an orphan; it is an ordinary
    # paragraph ending where a page happens to end.
    body_rows = [(i, k, r) for i, p in enumerate(pdf.pages)
                 for k, r in lines_of(p) if is_body(i, r) and 60 < k < BOTTOM]
    widows, orphans, stranded = [], [], []
    if body_rows:
        measure = max(width(r) for _, _, r in body_rows)
        gaps = sorted(body_rows[n + 1][1] - body_rows[n][1]
                      for n in range(len(body_rows) - 1)
                      if body_rows[n + 1][0] == body_rows[n][0])
        leading = gaps[len(gaps) // 2] if gaps else 16.0

        by_page = {}
        for n, (pg, k, r) in enumerate(body_rows):
            by_page.setdefault(pg, []).append(n)

        def starts_para(n):
            if n == 0 or body_rows[n - 1][0] != body_rows[n][0]:
                return False        # first body line on its page: undecidable
            return (body_rows[n][1] - body_rows[n - 1][1]) > leading * 1.35

        def ends_para(n):
            """The line does not fill the measure, so it closes a paragraph."""
            return width(body_rows[n][2]) < measure * 0.98

        for pg, idxs in by_page.items():
            if len(idxs) < 2:
                continue
            if starts_para(idxs[-1]):
                orphans.append(pg + 1)
            # A widow needs the page's first line to be the LAST line of its
            # paragraph, which means the line after it opens a new paragraph.
            # A first line whose paragraph simply continues down the page is
            # ordinary carryover, not a widow.
            first, nxt = idxs[0], idxs[0] + 1
            para_ends_here = (nxt >= len(body_rows)
                              or body_rows[nxt][0] != pg
                              or starts_para(nxt))
            if pg > 0 and ends_para(first) and para_ends_here:
                widows.append(pg + 1)

    for i, p in enumerate(pdf.pages):
        rows = [(k, r) for k, r in lines_of(p) if 60 < k < BOTTOM]
        if rows and any("Jost" in c["fontname"] for c in rows[-1][1]):
            stranded.append(i + 1)

    print(f"14. widows and orphans .... {len(widows)} widow(s), "
          f"{len(orphans)} orphan(s), {len(stranded)} stranded head(s)")
    if stranded:
        fails.append(f"section head stranded at the foot of page(s): "
                     f"{stranded}")
    if widows:
        fails.append(f"widow: a paragraph's last line alone at the head of "
                     f"page(s) {widows}")
    if orphans:
        fails.append(f"orphan: a paragraph's first line alone at the foot of "
                     f"page(s) {orphans}")

    LAST_FAILS[:] = fails
    print("\nQA " + ("PASSED" if not fails else "FAILED"))
    for f in fails:
        print("   " + f)
    return not fails


def preflight():
    """Fail loudly and usefully when the toolchain is absent.

    A fresh session has none of these. Without the check, a missing module
    surfaces as a traceback partway through the gate run, which reads as a
    broken build rather than a missing dependency, and a gate that never ran
    is indistinguishable from a gate that passed.
    """
    missing = []
    for mod, pkg in [("weasyprint", "weasyprint"), ("pdfplumber", "pdfplumber"),
                     ("pdf2image", "pdf2image"), ("PIL", "pillow"),
                     ("fontTools", "fonttools")]:
        try:
            __import__(mod)
        except ImportError:
            missing.append(pkg)
    if not shutil.which("pdftoppm"):
        missing.append("poppler-utils (system)")

    if not missing:
        return True

    print("BUILD CANNOT RUN. Missing: " + ", ".join(missing))
    print()
    pips = [m for m in missing if "system" not in m]
    if pips:
        print("    pip install " + " ".join(pips))
    if any("system" in m for m in missing):
        print("    apt-get update -qq && apt-get install -y poppler-utils")
    print()
    print("Gates 9 and 14 need poppler; every gate needs pdfplumber. Do not")
    print("report a chapter as passing gates that did not run.")
    return False


if __name__ == "__main__":
    ap = argparse.ArgumentParser()
    ap.add_argument("html", nargs="?")
    ap.add_argument("--fonts", action="store_true", help="stage fonts and exit")
    ap.add_argument("--out", default=None)
    ap.add_argument("--url-policy", dest="url_policy", default="none",
                    choices=["none", "full"],
                    help="URLs in footnotes. Ruled: none.")
    a = ap.parse_args()
    if a.fonts:
        stage_fonts()
        sys.exit(0)
    if not a.html:
        ap.error("give a chapter HTML file, or --fonts")
    if not preflight():
        sys.exit(2)
    out = a.out or a.html.replace(".html", ".pdf")
    n = build(a.html, out, url_policy=a.url_policy)
    sys.exit(0 if qa(out, expected_footnotes=n) else 1)
