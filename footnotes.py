"""footnotes.py

Build step. Replaces every <cite src="..."> element in a chapter with a
<span class="fn"> carrying a footnote generated from the chapter's own source
block, so the citation text has a single source of truth.

The <cite> element and its .ckey span remain the authored form: they carry the
source keys and the editorial gloss, and they are what the audit draft shows.
This step is what turns them into print footnotes.
"""
import re, json, html
import cite_format as cf

SRC_RE = re.compile(r'<pre id="aiom-sources-data">(.*?)</pre>', re.S)
CITE_RE = re.compile(r'<cite src="([^"]+)">(.*?)</cite>', re.S)
CKEY_RE = re.compile(r'<span class="ckey">.*?</span>', re.S)


def load_sources(chapter_html):
    m = SRC_RE.search(chapter_html)
    if not m:
        return {}
    src = json.loads(html.unescape(m.group(1)))
    src.pop("_README", None)
    return src


def inject(chapter_html, url_policy="full", hide_sources=True):
    """Return (html, report). Report lists every footnote built."""
    src = load_sources(chapter_html)
    report = []
    missing = []

    def repl(m):
        keys = [k.strip() for k in m.group(1).split(";") if k.strip()]
        for k in keys:
            if k not in src:
                missing.append(k)
        gloss = CKEY_RE.sub("", m.group(2))
        gloss = re.sub(r"\s+", " ", re.sub(r"<[^>]+>", "", gloss)).strip()
        text = cf.format_footnote(keys, src, gloss, url_policy)
        report.append((len(report) + 1, keys, len(text)))
        # U+2060 WORD JOINER, so the marker cannot be left on a line of its own.
        #
        # Added 2026-08-31 on Dan's ruling, after Chapter 2 Stage 5 found marker 8
        # stranded alone at the foot of a dated evidence box. There is no
        # whitespace between the sentence and the marker in the source, but
        # WeasyPrint takes the inline element boundary as a break opportunity, and
        # inside a box whose measure is narrower than the body's the line filled
        # exactly and the superscript wrapped.
        #
        # NO GATE SEES THIS. Gate 14 counts widows and orphans of PARAGRAPHS, and
        # a lone superscript is neither, so the render carried it past all fifteen.
        # It was found by rasterizing the page and reading it.
        #
        # The joiner is zero width and carries no advance, so it changes no
        # measure and no text a reader sees. It DOES enter the extracted text
        # stream, which is why voicecheck's terminal-punctuation check treats
        # zero-width formatting as transparent.
        return f'\u2060<span class="fn">{text}</span>'

    out = CITE_RE.sub(repl, chapter_html)

    if hide_sources:
        out = out.replace('<pre id="aiom-sources-data">',
                          '<pre id="aiom-sources-data" class="audit-only">')

    if missing:
        raise ValueError(f"cite keys with no source entry: {sorted(set(missing))}")
    return out, report


if __name__ == "__main__":
    import argparse
    ap = argparse.ArgumentParser()
    ap.add_argument("html")
    ap.add_argument("--url-policy", default="full", choices=["full", "none"])
    ap.add_argument("--out", required=True)
    a = ap.parse_args()
    text = open(a.html).read()
    out, rep = inject(text, a.url_policy)
    open(a.out, "w").write(out)
    print(f"{len(rep)} footnote(s) built, url_policy={a.url_policy}")
    for n, keys, ln in rep:
        print(f"   {n}. {len(keys)} source(s), {ln} chars")
