#!/usr/bin/env python3
"""
AIOM_build.py  |  version 6.0  |  2026-07-25

One command to stage fonts, render a chapter, and run every QA gate.

Usage:
    python3 AIOM_build.py --fonts            # stage fonts (run once per session)
    python3 AIOM_build.py AIOM_ch01.html     # render + QA
    python3 AIOM_build.py AIOM_ch01.html --out /mnt/user-data/outputs/Ch1.pdf
"""

import argparse, io, os, shutil, subprocess, sys, urllib.request, zipfile

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


def qa(path):
    """Every gate from section 8 of AIOM_DESIGN_SPEC.md. Returns True if all pass."""
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

    print("\nQA " + ("PASSED" if not fails else "FAILED"))
    for f in fails:
        print("   " + f)
    return not fails


if __name__ == "__main__":
    ap = argparse.ArgumentParser()
    ap.add_argument("html", nargs="?")
    ap.add_argument("--fonts", action="store_true", help="stage fonts and exit")
    ap.add_argument("--out", default=None)
    a = ap.parse_args()
    if a.fonts:
        stage_fonts()
        sys.exit(0)
    if not a.html:
        ap.error("give a chapter HTML file, or --fonts")
    out = a.out or a.html.replace(".html", ".pdf")
    render(a.html, out)
    sys.exit(0 if qa(out) else 1)
