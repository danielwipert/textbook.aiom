#!/usr/bin/env python3
"""Type specimen: set the book's own prose in candidate faces, side by side.

WHY THIS EXISTS. A face is judged by rendering the book's own prose at the size
it ships at, never by reading a description of the face or by reasoning about its
letterforms. That is the same rule already in force for the drawn marks, and it
came from the same failure: three of the nine marks were redrawn only after a
contact sheet was rendered at both sizes.

WHAT IT PRODUCES. One self-contained HTML page, every face embedded as a subset
data URI so it needs no network and can be opened anywhere, with the book's own
paper, ink and display face around it. A 17px/20px toggle reproduces the two
stops of the section 3 clamp, and a blind mode hides the names so a face can be
picked on shape before it is picked on reputation.

IT ALSO PRINTS THE TWO NUMBERS THAT DECIDE MOST OF IT. Set width against the
current body face, which is what moves the measure, and x-height, which is what
decides whether a face holds presence at 17px without spending weight to do it.
A candidate that takes the measure outside the 45 to 75 band is reported as such.

    python3 specimen.py --face "Fira Sans=/tmp/FiraSans-Regular.ttf" \
                        --face "Archivo=/tmp/Archivo-Regular.ttf"

A --face needs only the roman to be compared. Give it the italic and the heavier
weights, as NAME=roman,italic,medium,semibold, to see the whole ladder set, which
is what actually ships. FONT HOSTS ARE BLOCKED FROM THE BUILD CONTAINER: the npm
registry is not, and @expo-google-fonts/<family> ships the upstream Google Fonts
TTFs with the OFL unmodified, which is the only font route that works from here.
"""
import argparse
import base64
import html
import io
import os
import re

from fontTools import subset
from fontTools.ttLib import TTFont

# The current web body face, and the print face beside it. Every candidate is
# reported against the first of these, because that is the one being replaced.
STAGED = [
    ("Archivo, current web body", "fonts/use/Archivo-Regular.ttf,"
     "fonts/use/Archivo-Italic.ttf,fonts/use/Archivo-Medium.ttf,"
     "fonts/use/Archivo-SemiBold.ttf"),
    ("IBM Plex Sans Text, print body", "fonts/use/IBMPlexSans-Text.ttf,"
     "fonts/use/IBMPlexSans-Italic.ttf,fonts/use/IBMPlexSans-Medium.ttf,"
     "fonts/use/IBMPlexSans-SemiBold.ttf"),
]
DISPLAY = ("fonts/use/Jost-Medium.ttf", "fonts/use/Jost-SemiBold.ttf")

DEFAULT_CHAPTER = ("Drafts/Ch01_The_Category_Error/00_Stage0_Draft/"
                   "AIOM_Ch01_redraft.html")
# A fixed string, so a number from one run is comparable with a number from the
# next. It is prose from this book rather than a pangram, because a pangram's
# letter frequencies are nothing like a page of text.
PROBE = "The consumption event is the unit of account in AI operations management."
BAND = (45, 75)          # the readable measure, in characters
MEASURE_CH = 73          # what the shipping measure holds in the current face


def chapter_paragraphs(path, count=3, floor=300):
    """The chapter's own body prose, which is the only fair specimen text."""
    src = open(path, encoding="utf-8").read()
    body = src.split('id="slot-teaching-body"', 1)[-1]
    out = []
    for para in re.findall(r"<p[^>]*>(.*?)</p>", body, re.S):
        text = html.unescape(re.sub(r"\s+", " ", re.sub(r"<[^>]+>", "", para))).strip()
        if len(text) > floor and not text.startswith("Figure"):
            out.append(text)
        if len(out) == count:
            break
    if not out:
        raise SystemExit(f"no body paragraphs over {floor} characters in {path}")
    return out


def ascii_safe(text):
    """Entities rather than raw bytes, so the page reads under any charset. A
    specimen that renders the curly apostrophe as mojibake is a specimen of the
    wrong thing."""
    return "".join(c if ord(c) < 128 else f"&#{ord(c)};" for c in text)


def embed(path, text):
    """The face, subset to what this page sets, as a base64 woff2."""
    font = TTFont(path)
    sub = subset.Subsetter(subset.Options(layout_features=["*"], notdef_outline=True,
                                          recommended_glyphs=True, name_IDs=["*"]))
    sub.populate(text=text)
    sub.subset(font)
    buf = io.BytesIO()
    font.flavor = "woff2"
    font.save(buf)
    return base64.b64encode(buf.getvalue()).decode("ascii")


def advance(path, text):
    """Set width of a string in em, summed from the font's own metrics."""
    font = TTFont(path)
    upm = font["head"].unitsPerEm
    cmap = font.getBestCmap()
    hmtx = font["hmtx"]
    return sum(hmtx[cmap[ord(c)]][0] for c in text if ord(c) in cmap) / upm


def metrics(path):
    font = TTFont(path)
    upm = font["head"].unitsPerEm
    os2 = font["OS/2"]
    return os2.usWeightClass, os2.sxHeight / upm, os2.sxHeight / os2.sCapHeight


def parse_face(spec):
    """NAME=roman[,italic,medium,semibold] into a name and up to four paths."""
    if "=" not in spec:
        raise SystemExit(f"--face wants NAME=path, got {spec!r}")
    name, paths = spec.split("=", 1)
    files = [p.strip() for p in paths.split(",") if p.strip()]
    for path in files:
        if not os.path.exists(path):
            raise SystemExit(f"no such font file: {path}")
    return name.strip(), files


CSS = """
:root {
  --paper:#F4ECDD; --navy:#16314F; --amber:#9E4B1B; --ink:#2B2620;
  --hairline:#DCCFB4; --folio:#7A6A55; --measure:32rem; --grain:0.13;
}
@media (prefers-color-scheme: dark) {
  :root:not([data-theme="light"]) {
    --paper:#0F1D2B; --navy:#F2F7FB; --amber:#E08A55; --ink:#E3E9EF;
    --hairline:#2C4459; --folio:#8FA6BC; --grain:0.08;
  }
}
:root[data-theme="dark"] {
  --paper:#0F1D2B; --navy:#F2F7FB; --amber:#E08A55; --ink:#E3E9EF;
  --hairline:#2C4459; --folio:#8FA6BC; --grain:0.08;
}
*,*::before,*::after { box-sizing:border-box; }
html { font-size:clamp(17px, 8px + 0.625vw, 20px); background:var(--paper); }
html.size-1440 { font-size:17px; }
html.size-1920 { font-size:20px; }
body {
  margin:0; background:var(--paper); color:var(--ink); line-height:1.62;
  font-family:"face0", system-ui, sans-serif; font-weight:400;
  text-rendering:optimizeLegibility; font-kerning:normal;
}
body::before {
  content:""; position:fixed; inset:0; z-index:-1; pointer-events:none;
  opacity:var(--grain); background-size:120px 120px;
  background-image:url("data:image/svg+xml,%3Csvg%20xmlns='http://www.w3.org/2000/svg'%20width='120'%20height='120'%3E%3Cfilter%20id='g'%3E%3CfeTurbulence%20type='fractalNoise'%20baseFrequency='0.9'%20numOctaves='4'%20stitchTiles='stitch'/%3E%3C/filter%3E%3Crect%20width='120'%20height='120'%20filter='url%28%23g%29'/%3E%3C/svg%3E");
}
.bar {
  position:sticky; top:0; z-index:10; display:flex; flex-wrap:wrap; gap:1rem;
  align-items:baseline; justify-content:space-between;
  padding:0.7rem clamp(1rem,4vw,3rem);
  background:color-mix(in srgb, var(--paper) 88%, transparent);
  backdrop-filter:blur(8px); border-bottom:1px solid var(--hairline);
}
.bar h1 {
  font-family:"Jost",sans-serif; font-weight:600; font-size:0.78rem;
  letter-spacing:0.11em; text-transform:uppercase; color:var(--navy); margin:0;
}
.bar h1 span { color:var(--folio); font-weight:500; letter-spacing:0.06em; text-transform:none; }
.controls { display:flex; gap:0.5rem; flex-wrap:wrap; }
button {
  font-family:"Jost",sans-serif; font-weight:500; font-size:0.7rem;
  letter-spacing:0.06em; text-transform:uppercase; padding:0.35rem 0.7rem;
  border:1px solid var(--hairline); border-radius:2px; background:transparent;
  color:var(--folio); cursor:pointer;
}
button:hover { border-color:var(--amber); color:var(--amber); }
button[aria-pressed="true"] { background:var(--navy); border-color:var(--navy); color:var(--paper); }
:focus-visible { outline:2px solid var(--amber); outline-offset:3px; }
main { padding:0 clamp(1rem,4vw,3rem) 6rem; max-width:60rem; margin:0 auto; }
.spec { padding:3rem 0; border-bottom:1px solid var(--hairline); scroll-margin-top:4.5rem; }
.spec:last-of-type { border-bottom:0; }
.eyebrow { display:flex; align-items:center; gap:0.6rem; }
.eyebrow::after { content:""; flex:1; height:1px; background:var(--hairline); }
.letter {
  font-family:"Jost",sans-serif; font-weight:600; font-size:0.68rem;
  letter-spacing:0.08em; color:var(--paper); background:var(--navy);
  width:1.5rem; height:1.5rem; display:grid; place-items:center; border-radius:50%;
}
.name { font-family:"Jost",sans-serif; font-weight:600; font-size:0.92rem; color:var(--navy); }
.metrics { display:flex; flex-wrap:wrap; gap:0 1.6rem; margin:0.7rem 0 0; }
.metrics div { display:flex; gap:0.35rem; align-items:baseline; }
.metrics dt {
  font-family:"Jost",sans-serif; font-weight:500; font-size:0.62rem;
  letter-spacing:0.09em; text-transform:uppercase; color:var(--folio);
}
.metrics dd {
  margin:0; font-family:"Jost",sans-serif; font-weight:600; font-size:0.72rem;
  color:var(--navy); font-variant-numeric:tabular-nums;
}
.metrics dd.out { color:var(--amber); }
.reading { max-width:var(--measure); font-family:var(--face), system-ui, sans-serif; }
.reading p { margin:0 0 1.05em; text-align:justify; hyphens:auto; }
.reading p:last-child { margin-bottom:0; }
.reading b { font-weight:600; color:var(--navy); }
body.blind .name, body.blind .metrics { visibility:hidden; }
@media (prefers-reduced-motion:reduce) { html { scroll-behavior:auto; } }
"""

SCRIPT = """
const root=document.documentElement, b=document.body;
const s14=document.getElementById('s1440'), s19=document.getElementById('s1920');
function size(w){
  root.classList.toggle('size-1440', w===14);
  root.classList.toggle('size-1920', w===19);
  s14.setAttribute('aria-pressed', w===14); s19.setAttribute('aria-pressed', w===19);
}
s14.onclick=()=>size(root.classList.contains('size-1440')?0:14);
s19.onclick=()=>size(root.classList.contains('size-1920')?0:19);
size(14);
const blind=document.getElementById('blind');
blind.onclick=()=>{
  const on=b.classList.toggle('blind');
  blind.setAttribute('aria-pressed', on);
  blind.textContent = on ? 'Show names' : 'Hide names';
};
"""


def main():
    ap = argparse.ArgumentParser(description=__doc__,
                                 formatter_class=argparse.RawDescriptionHelpFormatter)
    ap.add_argument("--face", action="append", default=[], metavar="NAME=PATH[,PATH...]",
                    help="a candidate: roman, or roman,italic,medium,semibold")
    ap.add_argument("--chapter", default=DEFAULT_CHAPTER,
                    help="chapter HTML to take the specimen prose from")
    ap.add_argument("--out", default="build/specimen.html")
    ap.add_argument("--no-staged", action="store_true",
                    help="omit the faces already in fonts/use/")
    args = ap.parse_args()

    faces = [] if args.no_staged else [parse_face(f"{n}={p}") for n, p in STAGED]
    faces += [parse_face(f) for f in args.face]
    if not faces:
        raise SystemExit("nothing to compare: pass --face, or drop --no-staged")

    paras = chapter_paragraphs(args.chapter)
    # The subset has to cover the prose, the labels and the whole ASCII range, or
    # a face is judged on glyphs the page happens not to set.
    corpus = "".join(paras) + "".join(n for n, _ in faces) + PROBE + "".join(
        chr(c) for c in range(32, 127)) + "’“”…"

    base = advance(faces[0][1][0], PROBE)
    css_faces, panels, rows = [], [], []
    for i, (name, files) in enumerate(faces):
        styles = [("400", "normal"), ("400", "italic"), ("500", "normal"), ("600", "normal")]
        for path, (weight, style) in zip(files, styles):
            css_faces.append(f'@font-face{{font-family:"face{i}";font-weight:{weight};'
                             f'font-style:{style};font-display:block;'
                             f'src:url(data:font/woff2;base64,{embed(path, corpus)}) '
                             f'format("woff2");}}')
        wclass, xh, xcap = metrics(files[0])
        adv = advance(files[0], PROBE)
        chars = MEASURE_CH * base / adv
        panels.append((i, name, chars, (adv / base - 1) * 100, xh, xcap))
        rows.append((name, wclass, len(files), chars, (adv / base - 1) * 100, xh))

    for weight, path in zip(("500", "600"), DISPLAY):
        css_faces.append(f'@font-face{{font-family:"Jost";font-weight:{weight};'
                         f'font-display:block;'
                         f'src:url(data:font/woff2;base64,{embed(path, corpus)}) '
                         f'format("woff2");}}')

    body = "".join(f"<p>{ascii_safe(p)}</p>" for p in paras)
    blocks = []
    for i, name, chars, delta, xh, xcap in panels:
        out = "" if BAND[0] <= chars <= BAND[1] else " class='out'"
        blocks.append(f"""
<section class="spec" id="face{i}" style="--face:'face{i}'">
  <header>
    <div class="eyebrow"><span class="letter">{chr(65 + i)}</span>
      <span class="name">{html.escape(name)}</span></div>
    <dl class="metrics">
      <div><dt>measure</dt><dd{out}>{chars:.1f} ch</dd></div>
      <div><dt>set width</dt><dd>{delta:+.1f}%</dd></div>
      <div><dt>x-height</dt><dd>{xh:.3f} em</dd></div>
      <div><dt>x / cap</dt><dd>{xcap:.2f}</dd></div>
    </dl>
  </header>
  <div class="reading">{body}</div>
</section>""")

    page = (f"<title>Chapter Face Specimen</title>\n<style>\n"
            f"{chr(10).join(css_faces)}\n{CSS}</style>\n"
            '<div class="bar"><h1>Chapter face specimen '
            "<span>web edition only, print unchanged</span></h1>"
            '<div class="controls">'
            '<button id="s1440" aria-pressed="true">17px / at 1440</button>'
            '<button id="s1920" aria-pressed="false">20px / at 1920</button>'
            '<button id="blind" aria-pressed="false">Hide names</button>'
            f"</div></div>\n<main>{''.join(blocks)}</main>\n<script>{SCRIPT}</script>\n")

    os.makedirs(os.path.dirname(args.out) or ".", exist_ok=True)
    open(args.out, "w", encoding="utf-8").write(page)

    print(f"{args.out}  {os.path.getsize(args.out) / 1024:.0f} kB, "
          f"{len(faces)} face(s), prose from {args.chapter}")
    print(f"{'face':32s} {'wc':>4s} {'ladder':>7s} {'measure':>9s} {'set':>7s} {'x-ht':>6s}")
    for name, wclass, count, chars, delta, xh in rows:
        flag = "" if BAND[0] <= chars <= BAND[1] else f"  <- outside the {BAND[0]}-{BAND[1]} band"
        ladder = f"{count}/4" if count < 4 else "full"
        print(f"{name[:32]:32s} {wclass:4d} {ladder:>7s} {chars:6.1f} ch "
              f"{delta:+6.1f}% {xh:6.3f}{flag}")
    print("\nA face is judged by reading this page at the size it ships at. The "
          "numbers rule candidates out; they do not pick one.")


if __name__ == "__main__":
    main()
