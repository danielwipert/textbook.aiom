#!/usr/bin/env python3
"""web_build.py  |  the web edition renderer  |  Phases W1 and W2

Adopted by Decision 62. Companion to AIOM_build.py, reading the SAME locked
chapter HTML. The web is a second PRESENTATION of the book, never a second text.

The pipeline is deliberately shaped so that equivalence is structural rather
than hoped for. Both artifacts descend from one call to footnotes.inject():

    source HTML
        |
        +-- footnotes.inject()  <-- the SAME call the print build makes
                |
                +-- print HTML --> WeasyPrint --> PDF        (AIOM_build.py)
                |
                +-- web transform --> web HTML               (this file)

The web transform does four things and nothing else: it lifts the body, it turns
each <span class="fn"> into a numbered sidenote, it adds id attributes for
anchors, and it wraps each inventory table in a scroll box. Everything else is
copied through byte for byte. Every one of the four adds elements or attributes
and NO TEXT, which is the test for whether a presentation change belongs here.
Gate W1 then proves the transform preserved the text, which is a check on this
file rather than a check on the author.

Six gates. W1 text equivalence, W2 lock status, W3 typographic marks, W4
structure and links, W5 document attributes, W6 horizontal overflow across a
width sweep. W6 needs a headless browser and is the only optional one; it reports
SKIPPED and is never counted as passed.

Citation text is never reimplemented here. It comes from footnotes.py and
cite_format.py, which is the whole reason this is Python.

Usage:
    python3 web_build.py Drafts/Ch01_The_Category_Error/00_Stage0_Draft/AIOM_Ch01_redraft.html
    python3 web_build.py <chapter.html> --out build/web --preview
    python3 web_build.py <chapter.html> --no-browser   # skip gate W6
"""
import argparse
import glob
import os
import re
import shutil
import sys
from html.parser import HTMLParser

import book_structure
import footnotes
import status_check

# URLs are ruled out of print footnotes, and the web matches print so that
# gate W1's note comparison is exact. The URL is not lost: it lives in the
# chapter source register, which becomes the per-chapter sources page in
# Phase W4. See AIOM_Web_Edition_Plan_v1.0.md section 4.
URL_POLICY = "none"

VOID = {"area", "base", "br", "col", "embed", "hr", "img", "input", "link",
        "meta", "param", "source", "track", "wbr"}

SVG_RE = re.compile(r"<svg\b.*?</svg>", re.S)
BODY_RE = re.compile(r"<body[^>]*>(.*)</body>", re.S)
TITLE_RE = re.compile(r"<title>(.*?)</title>", re.S)
LANG_RE = re.compile(r"<html[^>]*\blang=\"([^\"]*)\"")
AUDIT_RE = re.compile(r'<section id="aiom-sources">.*?</section>', re.S)
PARTLABEL_RE = re.compile(r'<p class="part-label">(.*?)</p>', re.S)
CHTITLE_RE = re.compile(r'<h1 class="chapter-title">(.*?)</h1>', re.S)
FIGNUM_RE = re.compile(r'<span class="fignum">\s*Figure\s+([\d.]+)\s*</span>')
FIGCAP_RE = re.compile(r"<figcaption>.*?</figcaption>", re.S)
ID_ATTR_RE = re.compile(r'\bid="([^"]+)"')
HREF_RE = re.compile(r'\bhref="#([^"]+)"')

# The six-slot skeleton. CLAUDE.md section 3 fixes it for all fifteen chapters,
# but the chapter HTML does not mark all six the same way: three carry a
# p.slot-label, two open a semantic <section>, and the teaching body is not
# labelled at all and is detected from the first numbered section head. Anchors
# are ADDED here, never text: adding a visible label would change the body text
# and gate W1 would fail, correctly.
SLOTS = [
    ("opening-case",  "Opening case",
     re.compile(r'<p class="slot-label">Opening case</p>')),
    ("teaching-body", "Teaching body", None),
    ("craft-section", "Craft section",
     re.compile(r'<p class="slot-label">Craft section</p>')),
    ("summary",       "Chapter summary",
     re.compile(r'<section class="summary-sec">')),
    ("key-terms",     "Key terms",
     re.compile(r'<section class="keyterms">')),
    ("problems",      "Discussion questions and problems",
     re.compile(r'<section class="problems-sec">')),
]


# ---------------------------------------------------------------- text extract

class TextExtract(HTMLParser):
    """Concatenate the text of a document, skipping designated subtrees.

    Used for gate W1 and for gates W3 and W4, so every check reads the text the
    same way. Whitespace is normalized by `text()`, and nothing else is
    normalized: no dehyphenation, no case folding, no punctuation smoothing.
    A check that normalizes away the thing it measures is this repository's
    signature failure, so the comparison is exact by construction.
    """

    # <head> carries a <title> whose text is not chapter prose. Skipping it is
    # not cosmetic: the print side is not scoped to an element, so without this
    # the title joined the front of the prose and gate W1a failed at char 0.
    SKIP_TAGS = {"head", "title", "script", "style", "template"}

    def __init__(self, skip_ids=(), skip_classes=(), skip_attrs=(),
                 only_within_id=None):
        super().__init__(convert_charrefs=True)
        self.skip_ids = set(skip_ids)
        self.skip_classes = set(skip_classes)
        self.skip_attrs = set(skip_attrs)
        self.only_within_id = only_within_id
        self.stack = []
        self.skip_at = None
        self.collect_at = None if only_within_id else 0
        self.parts = []

    def _skips(self, tag, attrs):
        if tag in self.SKIP_TAGS:
            return True
        a = dict(attrs)
        if a.get("id") in self.skip_ids:
            return True
        if self.skip_classes & set((a.get("class") or "").split()):
            return True
        return bool(self.skip_attrs & set(a))

    def handle_starttag(self, tag, attrs):
        if tag in VOID:
            return
        self.stack.append(tag)
        if self.collect_at is None:
            if dict(attrs).get("id") == self.only_within_id:
                self.collect_at = len(self.stack)
            return
        if self.skip_at is None and self._skips(tag, attrs):
            self.skip_at = len(self.stack)

    def handle_startendtag(self, tag, attrs):
        return

    def handle_endtag(self, tag):
        if tag in VOID or tag not in self.stack:
            return
        while self.stack:
            if self.stack.pop() == tag:
                break
        if self.skip_at is not None and len(self.stack) < self.skip_at:
            self.skip_at = None
        if self.collect_at is not None and self.only_within_id \
                and len(self.stack) < self.collect_at:
            self.collect_at = None

    def handle_data(self, data):
        if self.collect_at is not None and self.skip_at is None:
            self.parts.append(data)

    def text(self):
        return re.sub(r"\s+", " ", "".join(self.parts)).strip()


def extract_text(doc, **kw):
    """Text of a document with <svg> stripped first.

    SVG is removed rather than skipped in the parser because figure markup is
    XML inside an HTML document and is not worth asking html.parser to walk.
    The figures are copied through byte for byte, so they are identical on both
    sides by construction and contribute nothing to the comparison.
    """
    p = TextExtract(**kw)
    p.feed(SVG_RE.sub("", doc))
    p.close()
    return p.text()


# ------------------------------------------------------------ balanced spans

SPAN_EDGE = re.compile(r"<span\b|</span>")


def find_spans(doc, opener):
    """Locate every span matching `opener`, counting nested spans properly.

    Returns (start, end, inner) for each, where start is at the opening tag and
    end is past the matching close.

    A non-greedy regex is wrong here and it is wrong twice over. A footnote
    built with url_policy="full" contains <span class="url">, so the first
    </span> closes the wrong element and the note is silently truncated. That
    case does not arise at the ruled url_policy, which is exactly why it would
    have survived until someone changed the policy.

    This is ONE function used for both the print side and the web side
    deliberately. The first draft had a balanced scanner for print footnotes and
    a non-greedy regex for web sidenotes, which is the failure CLAUDE.md records
    against the hyphenation scan: a check rewritten from memory reacquiring the
    defect the original was fixed for. The self-test caught it.
    """
    out = []
    for m in re.finditer(opener, doc):
        i, depth = m.end(), 1
        while depth:
            nxt = SPAN_EDGE.search(doc, i)
            if not nxt:
                raise ValueError(f"unclosed span for {opener!r}")
            depth += 1 if nxt.group(0) == "<span" else -1
            i = nxt.end()
        out.append((m.start(), i, doc[m.end():i - len("</span>")]))
    return out


FN_OPEN = re.escape('<span class="fn">')
NOTE_OPEN = r'<span class="note" id="fn-\d+"[^>]*>'


def find_fn_spans(doc):
    """Every print footnote, in document order."""
    return find_spans(doc, FN_OPEN)


# ------------------------------------------------------------------ transform

def add_anchors(body):
    """Add id attributes for the slot rail and the numbered sections.

    Adds attributes only. No element is created, moved or renamed, and no text
    is introduced, so the body text is unchanged by construction.

    Sections are numbered FIRST and the slots read the result. The other order
    was tried and was wrong: the teaching-body slot has no label of its own and
    anchors on the first numbered section head, so numbering afterwards
    overwrote the slot id with the section id and the rail linked to a target
    that no longer existed. Gate W4c caught it, which is the gate working.
    """
    sections = []

    def sec(m):
        num = m.group(1)
        sid = "sec-" + num.replace(".", "-")
        sections.append({"num": num, "title": re.sub(r"<[^>]+>", "", m.group(2)),
                         "id": sid})
        return (f'<h3 class="section" id="{sid}">'
                f'<span class="num">{num}</span>{m.group(2)}</h3>')

    body = re.sub(
        r'<h3 class="section">'
        r'<span class="num">([\d.]+)</span>(.*?)</h3>', sec, body, flags=re.S)

    slots = []
    for key, label, pat in SLOTS:
        if pat is None:
            # The teaching body is not labelled in the chapter HTML. It opens at
            # the first numbered section, so it reuses that anchor rather than
            # gaining a second id on one element.
            if sections:
                slots.append({"key": key, "label": label, "id": sections[0]["id"]})
            continue
        m = pat.search(body)
        if not m:
            continue
        tag = m.group(0)
        body = body[:m.start()] + tag[:-1] + f' id="slot-{key}"' + tag[-1:] \
            + body[m.end():]
        slots.append({"key": key, "label": label, "id": f"slot-{key}"})
    return body, slots, sections


def to_sidenotes(body):
    """Turn each print footnote into a numbered web sidenote.

    The marker and the note body both carry data-note, which is how gate W1
    tells prose from apparatus. The note text itself is untouched: it arrives
    from footnotes.inject() and is placed, not rewritten.
    """
    spans = find_fn_spans(body)
    notes = []
    out, prev = [], 0
    for n, (start, end, inner) in enumerate(spans, 1):
        out.append(body[prev:start])
        out.append(
            f'<a class="fnref" id="fnref-{n}" href="#fn-{n}" data-note="ref" '
            f'aria-describedby="fn-{n}"><sup>{n}</sup></a>'
            f'<span class="note" id="fn-{n}" data-note="body" role="note">'
            f'<a class="note-n" href="#fnref-{n}">{n}</a> {inner}</span>')
        notes.append(inner)
        prev = end
    out.append(body[prev:])
    return "".join(out), notes


TABLE_RE = re.compile(r'<table class="inv">.*?</table>', re.S)


def wrap_tables(body):
    """Put each inventory table in its own horizontally scrollable box.

    Found by the gate W6 width sweep, not by eye: the four-column P3 table
    cannot fit below about 390px and was forcing the whole PAGE to scroll
    sideways, which breaks every other block on the phone rather than just the
    table. Scrolling the table inside its own box confines the problem to the
    element that has it.

    This adds an element and no text, so gate W1 is unaffected, which is the
    test for whether a presentation change belongs in this transform at all.
    """
    return TABLE_RE.sub(
        lambda m: f'<div class="table-scroll">{m.group(0)}</div>', body)


def transform(print_html):
    """Print HTML to web body HTML, plus everything the template needs."""
    m = BODY_RE.search(print_html)
    if not m:
        raise ValueError("no <body> in the print HTML")
    body = m.group(1)

    audit = AUDIT_RE.search(body)
    body = AUDIT_RE.sub("", body)

    part = PARTLABEL_RE.search(body)
    title = CHTITLE_RE.search(body)
    body = PARTLABEL_RE.sub("", body, count=1)
    body = CHTITLE_RE.sub("", body, count=1)

    body, slots, sections = add_anchors(body)
    body, notes = to_sidenotes(body)
    body = wrap_tables(body)

    figures = []
    for fm in FIGNUM_RE.finditer(body):
        figures.append(fm.group(1))

    tm = TITLE_RE.search(print_html)
    num = ""
    if tm:
        nm = re.search(r"Chapter\s+(\d+)", tm.group(1))
        num = nm.group(1) if nm else ""

    # Reading metadata for the rail. This is CHROME and lives outside
    # <article id="chapter-text">, so it cannot reach gate W1. Counted from the
    # transformed body rather than stated by hand, because a hand-kept count is
    # a claim that goes stale silently.
    prose = extract_text(body, skip_attrs=("data-note",))
    words = len(prose.split())
    meta_counts = {
        "words": words,
        # 230 wpm is a common estimate for adult non-fiction reading. It is a
        # rounded estimate and is labelled as one in the rail, not presented as
        # a measurement of this text.
        "minutes": max(1, round(words / 230)),
        "key_terms": len(re.findall(r'<div class="kt">', body)),
        "figures": len(figures),
        "problems": len(re.findall(r'<div class="problem">', body)),
        "questions": len(re.findall(r'<div class="dq">', body)),
    }

    return {
        "body": body.strip(),
        "slots": slots,
        "sections": sections,
        "notes": notes,
        "figures": figures,
        "counts": meta_counts,
        "part_label": re.sub(r"<[^>]+>", "", part.group(1)).strip() if part else "",
        "chapter_title": re.sub(r"<[^>]+>", "", title.group(1)).strip() if title else "",
        "chapter_number": num,
        "audit_block": audit.group(0) if audit else "",
        # Carried through from the source rather than hardcoded in the template.
        # A template that always emitted en-US would make gate W5 a check that
        # measures nothing: a chapter whose source omits Decision 59 would still
        # pass. This way the defect propagates to where the gate can see it.
        "lang": lm.group(1) if (lm := LANG_RE.search(print_html)) else "",
    }


# ---------------------------------------------------------------------- gates

def gate_w1(print_html, web_html):
    """Text equivalence. Two channels, both exact, no tolerance.

    Channel A, prose: the chapter's body text with all footnote apparatus
    removed from both sides. Catches a transform that drops, reorders or
    mangles prose.

    Channel B, notes: the ordered list of footnote texts. Catches a transform
    that drops a note, renumbers, or truncates one. Both sides descend from the
    same footnotes.inject() call, so this measures the web transform rather
    than comparing two implementations of citation formatting, which would
    measure nothing.

    Excluded on BOTH sides and stated so the exclusion is on the record:
    <svg> figure internals, which are copied through byte for byte; and
    <section id="aiom-sources">, the audit block, which print also drops
    because AIOM_book.css sets #aiom-sources to display:none.
    """
    fails = []
    print_prose = extract_text(
        print_html, skip_ids=("aiom-sources", "aiom-sources-data"),
        skip_classes=("fn", "ckey"))
    web_prose = extract_text(
        web_html, skip_attrs=("data-note",), only_within_id="chapter-text")

    if print_prose == web_prose:
        print(f"W1a. prose text ........... identical, {len(web_prose):,} chars")
    else:
        fails.append("W1a: web prose text differs from print prose text")
        _report_first_divergence(print_prose, web_prose)

    pn = [_plain(i) for _, _, i in find_fn_spans(print_html)]
    wn = [_plain(re.sub(r'<a class="note-n".*?</a>', "", i, flags=re.S))
          for _, _, i in find_spans(web_html, NOTE_OPEN)]
    if pn == wn:
        print(f"W1b. footnote text ........ identical, {len(wn)} note(s)")
    else:
        fails.append(f"W1b: {len(pn)} print note(s) vs {len(wn)} web note(s), "
                     f"or text differs")
        for i, (a, b) in enumerate(zip(pn, wn), 1):
            if a != b:
                fails.append(f"    note {i} print: {a[:90]}")
                fails.append(f"    note {i} web  : {b[:90]}")
                break
    return fails


def _plain(frag):
    return re.sub(r"\s+", " ", re.sub(r"<[^>]+>", "", frag)).strip()


def _report_first_divergence(a, b):
    n = min(len(a), len(b))
    i = next((k for k in range(n) if a[k] != b[k]), n)
    print(f"     first divergence at char {i}")
    print(f"     print: ...{a[max(0, i - 60):i + 60]!r}")
    print(f"     web  : ...{b[max(0, i - 60):i + 60]!r}")


def is_locked(chapter_dir):
    """Does this chapter's checklist report Stage 9 passed?

    One reading of lock status, used by gate W2 and by the navigation, so the
    site cannot link a chapter the gate would refuse to publish.
    """
    found = sorted(glob.glob(os.path.join(chapter_dir, "AIOM_Ch*_Checklist*.md")))
    if not found:
        return False, None
    steps = status_check.parse(found[-1])
    lock = next((s for s in steps if s["id"] == "Stage 9"), None)
    return bool(lock and lock["status"]), found[-1]


def locked_chapters():
    """Chapter numbers reporting Stage 9, scanned from the Drafts tree."""
    out = {}
    for d in sorted(glob.glob("Drafts/Ch[0-9][0-9]_*")):
        m = re.search(r"Ch(\d\d)_", os.path.basename(d))
        if not m:
            continue
        locked, path = is_locked(d)
        if locked:
            out[int(m.group(1))] = path
    return out


def gate_w2(chapter_path, preview):
    """Lock status. Decision 64: locked chapters only, and a machine says so."""
    chdir = os.path.dirname(os.path.dirname(os.path.abspath(chapter_path)))
    found = sorted(glob.glob(os.path.join(chdir, "AIOM_Ch*_Checklist*.md")))
    if not found:
        return [f"W2: no checklist found in {chdir}, cannot establish lock status"]
    steps = status_check.parse(found[-1])
    lock = next((s for s in steps if s["id"] == "Stage 9"), None)
    name = os.path.basename(found[-1])
    if lock and lock["status"]:
        print(f"W2. lock status ........... LOCKED, {name}, {lock['date']}")
        return []
    if preview:
        print(f"W2. lock status ........... not locked, PREVIEW build ({name})")
        return []
    return [f"W2: {name} does not report Stage 9 passed. Locked chapters only "
            f"(Decision 64). Use --preview for a local noindex build."]


def gate_pages(pages):
    """Run the page-level gates over EVERY emitted page, not just the chapter.

    Added at W3, and it closed a real hole rather than a theoretical one. Gates
    W3 and W5 had only ever been handed the chapter, so the landing page was
    ungated from the moment it existed, and it shipped four straight apostrophes
    that gate W3 would have failed instantly had it been looking. A suite that
    checks one of two artifacts is evidence about one of two artifacts.
    """
    fails = []
    for label, html in pages:
        fails += gate_w3(html, label)
        fails += gate_w5(html, None, label)
        fails += gate_w4_links(html, label)
    return fails


def gate_w4_links(html, label):
    """Anchor uniqueness and internal link resolution, for any page."""
    fails = []
    ids = ID_ATTR_RE.findall(html)
    dupes = sorted({i for i in ids if ids.count(i) > 1})
    if dupes:
        fails.append(f"W4 [{label}]: duplicate id attribute(s): {dupes}")
    dead = sorted({h for h in HREF_RE.findall(html) if h not in set(ids)})
    if dead:
        fails.append(f"W4 [{label}]: internal link(s) with no target: {dead}")
    if not fails:
        print(f"W4f. {label} links ....... {len(ids)} unique id(s), all "
              f"internal links resolve")
    return fails


def gate_w3(web_html, label="chapter"):
    """Typographic marks. Ports print gates 2 and 15 to the web output.

    Both are properties of the text, so both apply. Run against the extracted
    text rather than the markup, because attribute values legitimately carry
    straight quotes and a check that failed on those would be noise.

    Scoped to the WHOLE page rather than to the article, so navigation labels,
    the footer and any other chrome are covered too. The standing rule bans the
    em dash in every file in this repository, and chrome is not an exemption.
    Script and style are skipped by the extractor, so JavaScript string quotes
    do not register as typewriter marks in prose.

    <title> is added back explicitly. The extractor skips <head> because the
    print side is not scoped to an element and the title would otherwise join
    the front of the prose, but the title is chapter-derived text that a reader
    sees in the browser tab, so it is checked here rather than exempted. The
    self-test found this hole: four mark controls landed in the title and none
    of them fired.
    """
    text = extract_text(web_html)
    tm = TITLE_RE.search(web_html)
    if tm:
        text += " " + tm.group(1)
    fails = []
    for ch, name, code in (("\u2014", "em dash", "U+2014"),
                           ("\u2013", "en dash", "U+2013"),
                           ('"', "straight quotation mark", "U+0022"),
                           ("'", "straight apostrophe", "U+0027")):
        hits = [m.start() for m in re.finditer(re.escape(ch), text)]
        if hits:
            fails.append(f"W3 [{label}]: {len(hits)} {name} ({code}) in the "
                         f"text, first at char {hits[0]}: "
                         f"{text[max(0, hits[0] - 40):hits[0] + 40]!r}")
    if not fails:
        print(f"W3. typographic marks ..... {label}: no em dash, en dash, or "
              f"straight mark")
    return fails


def gate_w4(web_html, meta):
    """Structure, anchors, links, figures."""
    fails = []

    got = {s["key"] for s in meta["slots"]}
    missing = [label for key, label, _ in SLOTS if key not in got]
    if missing:
        fails.append(f"W4: slot not found in the chapter: {', '.join(missing)}")
    else:
        print(f"W4a. six-slot skeleton .... all {len(SLOTS)} slots anchored")

    ids = ID_ATTR_RE.findall(web_html)
    dupes = sorted({i for i in ids if ids.count(i) > 1})
    if dupes:
        fails.append(f"W4: duplicate id attribute(s): {dupes}")
    else:
        print(f"W4b. anchors .............. {len(ids)} unique id(s)")

    targets = set(ids)
    dead = sorted({h for h in HREF_RE.findall(web_html) if h not in targets})
    if dead:
        fails.append(f"W4: internal link(s) with no target: {dead}")
    else:
        print("W4c. internal links ....... all resolve")

    prose = extract_text(web_html, skip_attrs=("data-note",),
                         only_within_id="chapter-text")
    body_no_caps = FIGCAP_RE.sub("", meta["body"])
    ref_text = extract_text(body_no_caps)
    unref = [n for n in meta["figures"] if f"Figure {n}" not in ref_text]
    if unref:
        fails.append(f"W4: figure(s) captioned but never referenced in the "
                     f"prose: {unref}")
    elif meta["figures"]:
        print(f"W4d. figures .............. {len(meta['figures'])} captioned "
              f"and referenced ({', '.join(meta['figures'])})")

    if not meta["notes"]:
        fails.append("W4: no footnotes built, which means no <cite> resolved")
    else:
        print(f"W4e. citations ............ {len(meta['notes'])} note(s) built "
              f"from the chapter register")
    return fails


def gate_w5(web_html, meta, label="chapter"):
    """Document attributes. Decision 59 is invisible when omitted."""
    fails = []
    lang = LANG_RE.search(web_html)
    if not lang or lang.group(1) != "en-US":
        fails.append(f"W5: lang is {lang.group(1) if lang else 'absent'!r}, "
                     f"must be 'en-US' (Decision 59). In Pyphen 'en' is an "
                     f"alias for en_GB.")
    if not TITLE_RE.search(web_html):
        fails.append("W5: no <title>")
    if 'name="viewport"' not in web_html:
        fails.append("W5: no viewport meta, the page will not be responsive")
    if 'charset="utf-8"' not in web_html.lower():
        fails.append("W5: no charset declaration")
    if meta is not None and not meta["chapter_number"]:
        fails.append("W5: chapter number not derivable from the source <title>")
    fails = [f.replace("W5:", f"W5 [{label}]:") for f in fails]
    if not fails:
        print(f"W5. document attributes ... {label}: lang=en-US, title, "
              f"viewport, charset")
    return fails


def gate_w7(meta, book):
    """The book spine, and the one place it can silently drift.

    The site's navigation is parsed from AIOM_Structure_v1.md rather than retyped,
    so the structural checks below are what stand between a changed heading and a
    site quietly missing a quarter of the book.

    The second half matters more. A chapter's published title comes from its own
    locked HTML, and the navigation's comes from the structure document. Those two
    can disagree, and nothing else in this repository would notice: the chapter
    would render correctly, the nav would render correctly, and they would name
    different chapters. That is this repository's signature failure with a new
    surface, so it fails the build.
    """
    fails = ["W7: " + f for f in book_structure.check(book)]
    if not fails:
        print(f"W7a. book spine ........... {len(book)} parts, "
              f"{len(book_structure.flat(book))} chapters, parsed from "
              f"{book_structure.STRUCTURE}")

    num = int(meta["chapter_number"]) if meta["chapter_number"] else None
    entry = next((c for c in book_structure.flat(book) if c["number"] == num), None)
    if entry is None:
        fails.append(f"W7: chapter {num} is not in the book structure")
    elif entry["title"] != meta["chapter_title"]:
        fails.append(
            f"W7: chapter {num} title disagrees. "
            f"{book_structure.STRUCTURE} says {entry['title']!r}, "
            f"the locked chapter HTML says {meta['chapter_title']!r}")
    else:
        print(f"W7b. title agreement ...... chapter {num} matches the structure "
              f"document")
    return fails


WIDTHS = [320, 360, 390, 414, 480, 620, 768, 900, 1024, 1180, 1240, 1300,
          1366, 1411, 1440, 1441, 1512, 1600, 1920, 2560]


def gate_w6(page_path):
    """Horizontal overflow across a width sweep. The web analogue of print gate 1.

    Print gate 1 fails a page whose content exceeds the measure, because an
    unbreakable string or an oversized table runs off the paper. The web has the
    same defect with a different symptom: the document scrolls sideways and every
    block on the page is dragged with it, not just the one that overflowed.

    Requires a headless browser, which the build does not otherwise need, so it
    is OPTIONAL. It reports SKIPPED and is counted as skipped, never as passed.
    A gate that did not run is not a gate that passed, and an optional gate that
    quietly reports success is the exact failure this repository keeps finding in
    its own suite.

    Returns (fails, ran).
    """
    try:
        from playwright.sync_api import sync_playwright
    except ImportError:
        print("W6. horizontal overflow .. SKIPPED, playwright not installed")
        return [], False

    exe = next((p for p in glob.glob("/opt/pw-browsers/chromium-*/chrome-linux/chrome")
                if os.path.exists(p)), None)
    fails = []
    try:
        with sync_playwright() as p:
            kw = {"args": ["--no-sandbox"]}
            if exe:
                kw["executable_path"] = exe
            b = p.chromium.launch(**kw)
            pg = b.new_page(viewport={"width": 1512, "height": 900})
            url = "file://" + os.path.abspath(page_path)
            for w in WIDTHS:
                pg.set_viewport_size({"width": w, "height": 900})
                pg.goto(url)
                pg.wait_for_timeout(120)
                # An element inside an overflow-x container legitimately
                # extends past the viewport and is NOT the cause of a page
                # scroll. Reporting it sends the reader after the wrong element,
                # which is the defect already recorded against print gate 12's
                # failure message. Those ancestors are excluded.
                r = pg.evaluate(
                    "() => {const d=document.documentElement; const o=[];"
                    "const clipped = e => {for (let n=e.parentElement; n && n!==d;"
                    "  n=n.parentElement) {const ox=getComputedStyle(n).overflowX;"
                    "  if (ox==='auto'||ox==='scroll'||ox==='hidden') return true;}"
                    "  return false;};"
                    "document.querySelectorAll('body *').forEach(e=>{"
                    "  if (e.getBoundingClientRect().right > d.clientWidth + 1"
                    "      && !clipped(e))"
                    "    o.push(e.tagName + '.' + (e.className||''));});"
                    "return {sw:d.scrollWidth, cw:d.clientWidth,"
                    "        over:[...new Set(o)].slice(0,3)};}")
                if r["sw"] > r["cw"] + 1:
                    fails.append(f"W6: page scrolls sideways at {w}px "
                                 f"({r['sw']} > {r['cw']}), widest: {r['over']}")
            b.close()
    except Exception as exc:
        print(f"W6. horizontal overflow .. SKIPPED, browser unavailable ({exc.__class__.__name__})")
        return [], False

    if not fails:
        print(f"W6. horizontal overflow .. clean at {len(WIDTHS)} widths, "
              f"{WIDTHS[0]}px to {WIDTHS[-1]}px")
    return fails, True


# ----------------------------------------------------------------------- build

def _env():
    # Autoescape on, explicitly rather than by extension guess: the templates
    # are named .j2 and select_autoescape would have left it OFF. Only `body`
    # and `audit_block` are marked safe in a template, and both are chapter HTML
    # that arrived from footnotes.inject().
    from jinja2 import Environment, FileSystemLoader
    return Environment(loader=FileSystemLoader("web_templates"),
                       autoescape=True, trim_blocks=True, lstrip_blocks=True)


def render(chapter_path, outdir, preview=False):
    src = open(chapter_path, encoding="utf-8").read()
    print_html, _ = footnotes.inject(src, url_policy=URL_POLICY)
    meta = transform(print_html)

    book = book_structure.load_book()
    locked = locked_chapters()
    nav = []
    for p in book:
        nav.append({
            "numeral": p["numeral"], "name": p["name"],
            # First sentence only, and typographically corrected. The rest of a
            # Purpose line is production talk. See book_structure.public_purpose.
            "purpose": book_structure.public_purpose(p["purpose"]),
            "chapters": [{
                "number": c["number"],
                "title": book_structure.curl(c["title"]),
                "short": book_structure.curl(book_structure.short_title(c["title"])),
                "slug": f"ch{c['number']:02d}",
                # A chapter is a LINK only if it is locked. Decision 64 is
                # enforced by gate W2 at build time; this is the same rule at
                # navigation time, so the site cannot offer a door that the gate
                # would refuse to open.
                "locked": c["number"] in locked,
            } for c in p["chapters"]],
        })
    meta["book"] = nav
    meta["locked_count"] = len(locked)

    web_html = _env().get_template("chapter.html.j2").render(
        preview=preview, **meta)

    slug = f"ch{int(meta['chapter_number']):02d}" if meta["chapter_number"] else "ch"
    meta["slug"] = slug
    meta["structure"] = book
    chdir = os.path.join(outdir, slug)
    os.makedirs(chdir, exist_ok=True)
    os.makedirs(os.path.join(outdir, "assets", "fonts"), exist_ok=True)
    open(os.path.join(chdir, "index.html"), "w", encoding="utf-8").write(web_html)
    shutil.copyfile("AIOM_web.css", os.path.join(outdir, "assets", "aiom_web.css"))
    for f in glob.glob("fonts/use/*.ttf"):
        shutil.copyfile(f, os.path.join(outdir, "assets", "fonts",
                                        os.path.basename(f)))
    return print_html, web_html, meta, os.path.join(chdir, "index.html")


def render_index(outdir, meta):
    """The front door. Phase W3.

    Copy on this page is DRAFT and marked so in the plan. What is here comes from
    ruled material and nothing else: the two named layers are CLAUDE.md section 1
    verbatim, and each part's description is its Purpose line from
    AIOM_Structure_v1.md. Nothing on this page is invented, and no chapter's "Big
    idea" line appears, because those are internal planning shorthand and later
    chapters withhold things deliberately.
    """
    first = next((c for p in meta["book"] for c in p["chapters"] if c["locked"]),
                 None)
    out = _env().get_template("index.html.j2").render(
        book=meta["book"], locked_count=meta["locked_count"],
        chapter_count=sum(len(p["chapters"]) for p in meta["book"]),
        first_locked=first)
    open(os.path.join(outdir, "index.html"), "w", encoding="utf-8").write(out)
    return os.path.join(outdir, "index.html")


def main():
    ap = argparse.ArgumentParser(description="Build the AIOM web edition.")
    ap.add_argument("chapter", help="path to the locked chapter HTML")
    ap.add_argument("--out", default="build/web", help="output directory")
    ap.add_argument("--preview", action="store_true",
                    help="build an unlocked chapter to a local noindex page")
    ap.add_argument("--no-browser", action="store_true",
                    help="skip gate W6, the width sweep, which needs a browser")
    a = ap.parse_args()

    if not os.path.exists("web_templates/chapter.html.j2"):
        sys.exit("web_build.py must run from the repository root "
                 "(web_templates/ not found)")

    print_html, web_html, meta, path = render(a.chapter, a.out, a.preview)
    index = render_index(a.out, meta)
    print(f"\nChapter {meta['chapter_number']}: {meta['chapter_title']}")
    print(f"  {meta['part_label']}")
    print(f"  wrote {path}")
    print(f"  wrote {index}\n")

    fails = []
    fails += gate_w1(print_html, web_html)
    fails += gate_w2(a.chapter, a.preview)
    fails += gate_w3(web_html)
    fails += gate_w4(web_html, meta)
    fails += gate_w5(web_html, meta)
    fails += gate_w7(meta, meta["structure"])
    fails += gate_pages([("index", open(index, encoding="utf-8").read())])
    w6_fails, w6_ran = ([], False) if a.no_browser else gate_w6(path)
    fails += w6_fails

    verdict = "PASSED" if not fails else "FAILED"
    # The skip is stated in the verdict line rather than buried above it. Five of
    # this repository's recorded defects are a check that was believed to have
    # run and had not, so an optional gate has to be noisy about not running.
    if not w6_ran:
        verdict += ", W6 NOT RUN"
    print(f"\nWEB GATES {verdict}")
    for f in fails:
        print("   " + f)
    return 0 if not fails else 1


if __name__ == "__main__":
    sys.exit(main())
