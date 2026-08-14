#!/usr/bin/env python3
"""web_build.py  |  the web edition renderer and site build  |  Phases W1 to W5

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

FIFTEEN gates, W1 through W15. A gate is one W-number: sub-lettered checks are
parts of their gate, never gates of their own. This list had said "eleven" and
stopped at W10 since Phase W5, which is the count drift CLAUDE.md records; it is
derived from the build's own output rather than copied forward.

W1 text equivalence with print, W2 lock status, W3 typographic marks, W4
structure, anchors and links, W5 document attributes, W6 horizontal overflow
across a width sweep, W7 the book spine, W8 the reference layer against the
chapter, W9 the landing page quoted verbatim and no register note published,
W10 deploy readiness, W11 no third-party request, W12 figure colours are tokens,
W13 colour contrast in both themes, W14 claim preservation, W15 in-page
navigation.

W6 and W15 need a headless browser and are the only optional gates. Each reports
SKIPPED, the verdict line gains "W6 AND W15 NOT RUN", and neither is ever
counted as passed.

W14 is the only gate that reads MEANING. W15 is the only one that EXERCISES the
site rather than measuring it, and it exists because two rail anchors were dead
for six phases while every other gate reported the navigation sound.

Citation text is never reimplemented here. It comes from footnotes.py and
cite_format.py, which is the whole reason this is Python.

Usage:
    python3 web_build.py --site                    # every LOCKED chapter, discovered
    python3 web_build.py --site --base-url https://example.org
    python3 web_build.py <chapter.html>            # one chapter
    python3 web_build.py <chapter.html> --preview  # unlocked, noindex, local only
    python3 web_build.py --site --no-browser       # skip gate W6
"""
import argparse
import glob
import contextlib
import functools
import http.server
import socketserver
import tempfile
import threading
import os
import re
import shutil
import sys
from html.parser import HTMLParser

import book_structure
import footnotes
import ledger
import status_check
import claimcheck
import snapshot

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


class AnchorCollector(HTMLParser):
    """Collect ids the way a browser does: from START TAGS only.

    A regex over the raw HTML is NOT equivalent and the difference is a whole
    class of dead link. `\\bid="x"` matches inside `</p id="x">`, which is an
    attribute on a closing tag; every parser discards it, so the id is in the
    file and never in the DOM. Gates W4b and W4c used the regex and therefore
    counted two dead anchors as live targets and reported "all resolve" for two
    rail links that did nothing when clicked. Found 2026-08-13, by Dan clicking
    one, which is the only check that had ever actually followed the link.
    """

    def __init__(self):
        super().__init__(convert_charrefs=True)
        self.ids = []

    def handle_starttag(self, tag, attrs):
        for k, v in attrs:
            if k == "id" and v:
                self.ids.append(v)


def anchor_ids(html):
    p = AnchorCollector()
    p.feed(html)
    return p.ids

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
_EDGE_CACHE = {}


def _edge(tag):
    if tag not in _EDGE_CACHE:
        _EDGE_CACHE[tag] = re.compile(rf"<{tag}\b|</{tag}>")
    return _EDGE_CACHE[tag]


def find_spans(doc, opener, tag="span"):
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
    edge, close = _edge(tag), f"</{tag}>"
    out = []
    for m in re.finditer(opener, doc):
        i, depth = m.end(), 1
        while depth:
            nxt = edge.search(doc, i)
            if not nxt:
                raise ValueError(f"unclosed <{tag}> for {opener!r}")
            depth += 1 if nxt.group(0) != close else -1
            i = nxt.end()
        out.append((m.start(), i, doc[m.end():i - len(close)]))
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
        # THE id GOES IN THE OPENING TAG, AND WHICH CHARACTER THAT IS DEPENDS ON
        # THE PATTERN. Three SLOTS patterns match a bare opening tag
        # (`<section class="keyterms">`) and two match a WHOLE element
        # (`<p class="slot-label">Craft section</p>`), because that is the only
        # way to tell one slot label from another. Writing the attribute before
        # the last character of the match assumed the first shape, so for the
        # other two it produced `</p id="slot-craft-section">`: an attribute on
        # a CLOSING tag, which every HTML parser discards. The id was in the
        # file and never in the DOM, so the Opening case and Craft section rail
        # links did nothing when clicked. Cutting at the first ">" is correct
        # for both shapes.
        cut = tag.index(">")
        body = (body[:m.start()] + tag[:cut] + f' id="slot-{key}"' + tag[cut:]
                + body[m.end():])
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

DEF_OPEN_RE = re.compile(
    r'<aside class="definition">\s*<p class="lab">Definition</p>\s*'
    r'<p class="term">(.*?)</p>', re.S)
KT_OPEN_RE = re.compile(
    r'<div class="kt"><div class="kt-h"><span class="kt-t">(.*?)</span>', re.S)
BOLD_RE = re.compile(r"<b>(.*?)</b>", re.S)

# The design system's colours, by value. Chapter figures carry literal hex, as
# AIOM_book.css section 2 records, because print needs no indirection.
FIGURE_TOKENS = {
    "#F4ECDD": "paper", "#16314F": "navy", "#B4551F": "amber",
    "#C0521A": "amber-fig", "#0E7A72": "teal", "#2B2620": "ink",
    "#9B8F7C": "folio", "#6E6353": "axis", "#EDE3D0": "tint-def",
    "#F7EDE2": "tint-thm", "#E7DECB": "tint-fig", "#DCCFB4": "hairline",
}
FIG_COLOUR_RE = re.compile(
    r'\b(fill|stroke|stop-color)="(#[0-9A-Fa-f]{3,8})"')


def tokenize_svg(body):
    """Replace literal hex in chapter figures with the token that owns it.

    Phase W6. The chapter HTML is the LOCKED source shared with print, so it is
    never edited: this is a presentation transform on the way to the web, and it
    adds attributes and no text, which is the test for whether a transform
    belongs here at all. Gate W1 is unaffected.

    Verified before being relied on rather than assumed: var() DOES resolve in an
    SVG presentation attribute and DOES follow a theme change, checked in a
    headless browser against computed style in both colour schemes.

    A colour the design system does not own is left alone and reported by gate
    W12, because silently rewriting an unknown colour would hide exactly the
    drift the gate exists to catch.
    """
    def repl(m):
        attr, hexv = m.group(1), m.group(2).upper()
        token = FIGURE_TOKENS.get(hexv)
        return f'{attr}="var(--{token})"' if token else m.group(0)

    def do_svg(sm):
        return FIG_COLOUR_RE.sub(repl, sm.group(0))

    return SVG_RE.sub(do_svg, body)


def figure_colours(body):
    """Every literal colour still present in a figure, with its context."""
    out = []
    for sm in SVG_RE.finditer(body):
        for m in FIG_COLOUR_RE.finditer(sm.group(0)):
            out.append(m.group(2).upper())
    return out


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


def term_key(text):
    """Normalize a term for matching a bold run against a defined term.

    Case is folded, whitespace collapsed, and ONE leading article dropped,
    because the chapter writes "the consumption event" in prose and
    "Consumption event" on the callout, and both name the same object.

    TRAILING PUNCTUATION IS DELIBERATELY NOT STRIPPED. The craft section sets
    "Meter:" in bold as a worksheet label, and stripping the colon would let it
    match a term named Meter and turn a form field into a definition link. The
    cost of leaving it is that a term genuinely written with trailing
    punctuation goes unlinked, which is a missing link rather than a wrong one.
    """
    t = re.sub(r"<[^>]+>", "", text)
    t = re.sub(r"\s+", " ", t).strip().lower()
    return re.sub(r"^(the|a|an) ", "", t)


def slugify(text):
    s = re.sub(r"[^a-z0-9]+", "-", term_key(text)).strip("-")
    return s or "term"


def link_terms(body):
    """Make a bolded key term a link to the definition that owns it.

    Two passes. Definition callouts and key-term entries gain an id, then every
    bold run whose normalized text names one of them is wrapped in an anchor.
    A bold run that names nothing is left exactly as it was, which is most of
    them: the craft section sets its worksheet labels in bold, and those are
    form fields rather than terms.

    THE DEFINITION CALLOUT WINS OVER THE KEY-TERM ENTRY when a term has both,
    because the callout sits beside the prose that introduces the term and the
    key-term list sits at the end of the chapter. A term that has only a
    key-term entry still links, to that, since the alternative is a page where
    four bolded terms are links and a fifth identical-looking one is not.

    Adds attributes and an element, and no text, so gate W1 is unaffected. That
    is the test for whether a presentation change belongs in this transform.
    """
    targets, used = {}, set()

    def anchor(match, tag_len, prefix, name):
        slug = f"{prefix}-{slugify(name)}"
        n, base = 2, slug
        while slug in used:
            slug, n = f"{base}-{n}", n + 1
        used.add(slug)
        key = term_key(name)
        # Definitions are registered first, so they are never overwritten here.
        targets.setdefault(key, slug)
        head = match.group(0)
        return head[:tag_len] + f' id="{slug}"' + head[tag_len:]

    body = DEF_OPEN_RE.sub(
        lambda m: anchor(m, len("<aside class=\"definition\""), "def", m.group(1)),
        body)
    body = KT_OPEN_RE.sub(
        lambda m: anchor(m, len("<div class=\"kt\""), "kt", m.group(1)), body)

    linked = []

    def bold(m):
        slug = targets.get(term_key(m.group(1)))
        if not slug:
            return m.group(0)
        linked.append(m.group(1))
        return (f'<a class="termlink" href="#{slug}">{m.group(0)}</a>')

    body = BOLD_RE.sub(bold, body)
    return body, linked, targets


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
    body = tokenize_svg(body)
    body, termlinks, termtargets = link_terms(body)
    # A silent zero here is the shape this repository keeps finding: the
    # chapter rewords a term, nothing matches, every link disappears, and no
    # gate notices because a missing anchor breaks nothing. Report, do not fail.
    if termtargets and not termlinks:
        print("  WARNING: term linking matched nothing, though "
              f"{len(termtargets)} defined term(s) exist. Has a term been "
              "reworded in the chapter?")

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
        # The opener tolerates attributes: link_terms() gives every .kt block
        # an id, so a pattern demanding an immediate ">" would count zero here
        # and report a chapter with no key terms.
        "key_terms": len(re.findall(r'<div class="kt"[^>]*>', body)),
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
        "termlinks": termlinks,
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


def gate_w14(chapter_path):
    """Claim preservation. Does the chapter still say what the checks ruled?

    THE ONLY GATE IN EITHER SUITE THAT READS MEANING RATHER THAN FORM, and it
    exists because meaning is where this project's damage happens. SF8, SF9 and
    SF10 were reverted during a copy edit with every date and figure intact, so
    nothing that checks values could see it; FC2 repeated the shape, and the case
    bank carried a withdrawn claim for seventy days. Five instances, none visible
    to any check that existed.

    The ruled sentences live in AIOM_Claim_Ledger.md rather than being scraped
    from the register notes, for a reason worth keeping in front of whoever
    edits this: a note holds SUPERSEDED ruled forms beside current ones, so the
    obvious implementation demands sentences the chapter is right not to have.
    claimcheck.py's docstring carries the full account.
    """
    chapter = claimcheck.chapter_id_for(chapter_path)
    fails = claimcheck.check(chapter_path, chapter=chapter)
    n_rul, n_req, n_forb, n_rev = claimcheck.summary(chapter_path, chapter=chapter)
    if fails:
        return fails
    if n_rul == 0:
        # Not a failure: a chapter can legitimately carry no rulings yet. But it
        # must never read as a pass, because a deleted ledger section looks
        # exactly like a chapter nobody has ruled on.
        print(f"W14. claim preservation .. {chapter}: NO RULINGS IN THE LEDGER, "
              f"nothing was checked")
        return []
    print(f"W14. claim preservation .. {chapter}: {n_rul} ruling(s) hold, "
          f"{n_req} required present, {n_forb} withdrawn absent"
          + (f", {n_rev} review-only NOT mechanical" if n_rev else ""))
    return []


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
    # Parsed rather than regexed, for the reason in AnchorCollector: an id on a
    # closing tag satisfies the regex and reaches no DOM. Both id readers moved
    # together deliberately, because a hardened chapter gate beside a soft
    # page gate would leave the landing page carrying the defect the chapter is
    # now protected from.
    ids = anchor_ids(html)
    stringy = set(ID_ATTR_RE.findall(html)) - set(ids)
    if stringy:
        fails.append(f"W4 [{label}]: id attribute(s) in the markup but not on "
                     f"any element: {sorted(stringy)}")
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

    # Parsed, not regexed. See AnchorCollector: an id written into a CLOSING
    # tag matches the regex and never reaches the DOM, which is exactly the
    # defect this gate passed twice.
    ids = anchor_ids(web_html)
    stringy = set(ID_ATTR_RE.findall(web_html)) - set(ids)
    if stringy:
        fails.append(f"W4: id attribute(s) present in the markup but not on any "
                     f"element, so no link can reach them: {sorted(stringy)}")
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

    # W4g. THE CHAPTER PAGE CARRIES NO SPOT MARK. Ruled 2026-08-13: the marks
    # live in chrome only, because the chapter is a reading surface and anything
    # competing with the prose is a cost. Stated as a rule this would be an
    # intention, and an intention that reads as a control is this repository's
    # signature failure. GATE W1 CANNOT COVER IT: a mark is an SVG carrying no
    # text, so text equivalence with print stays perfect while the page fills up
    # with ornament.
    marks = web_html.count('class="mark"')
    if marks:
        fails.append(f"W4g: the chapter page carries {marks} spot mark(s). Marks "
                     f"are chrome only (ruled 2026-08-13); the chapter is a "
                     f"reading surface.")
    else:
        print("W4g. chapter ornament ..... none, marks are chrome only")

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


# A chapter's live text is the ONE html in its Stage 0 folder. Decision 50
# permits exactly one per chapter. Chapter 1's folder held a stale superseded
# fork (DRAFT-AIOM_ch01.html: lang="en", no source register) until it was
# removed on 2026-08-13; the guard stays because the hazard is structural, not
# specific to that file, and the next chapter can reintroduce it. Auto discovery
# must never be able to choose such a fork, so excluded prefixes are named here
# and gate W10 reports every file it skipped on every build.
LIVE_EXCLUDE = ("DRAFT-", "_")
LIVE_EXCLUDE_SUFFIX = (".print.html",)


def discover_chapters(root="Drafts"):
    """Find the live text of every LOCKED chapter, in book order.

    Returns (chapters, notes) where chapters is [(number, path)] and notes
    records what was skipped and why, so a silent choice is never made.
    """
    found, notes = [], []
    for d in sorted(glob.glob(os.path.join(root, "Ch[0-9][0-9]_*"))):
        m = re.search(r"Ch(\d\d)_", os.path.basename(d))
        if not m:
            continue
        num = int(m.group(1))
        locked, _ = is_locked(d)
        if not locked:
            continue
        stage0 = os.path.join(d, "00_Stage0_Draft")
        cands, skipped = [], []
        for f in sorted(glob.glob(os.path.join(stage0, "*.html"))):
            base = os.path.basename(f)
            if base.startswith(LIVE_EXCLUDE) or base.endswith(LIVE_EXCLUDE_SUFFIX):
                skipped.append(base)
            else:
                cands.append(f)
        for s in skipped:
            notes.append(f"chapter {num}: skipped {s} (excluded by name)")
        if len(cands) != 1:
            notes.append(f"chapter {num}: FAIL, {len(cands)} candidate live "
                         f"texts in {stage0}: {[os.path.basename(c) for c in cands]}. "
                         f"Decision 50 permits exactly one per chapter.")
            continue
        found.append((num, cands[0]))
        notes.append(f"chapter {num}: {os.path.basename(cands[0])}")
    return found, notes


SUBRESOURCE_RE = re.compile(
    r'<(?:script|img|iframe|video|audio|source|embed|track)\b[^>]*\bsrc="([^"]+)"'
    r"|<link\b[^>]*\bhref=\"([^\"]+)\""
    r"|url\(\s*['\"]?([^)'\"]+)", re.I)


def gate_w12(pages):
    """Every colour in every SVG on every page is a design token. Phase W6.

    Chapter figures are drawn with literal hex, which print needs and the web
    cannot theme; tokenize_svg() maps each value to the token that owns it, and
    anything it could not map is still literal when this runs. That is either a
    colour outside the design system or a token nobody registered, and both are
    drift worth failing on.

    IT SCANS EVERY PAGE, and the first version did not. It looked only at the
    chapter body, so the landing page's hero figure kept literal hex and rendered
    in light-mode colours on the dark ground while the gate reported green. That
    is the same failure already recorded against gates W3 and W5 in Phase W3: a
    gate handed one page is evidence about one page.
    """
    fails = []
    for label, html in pages:
        left = figure_colours(html)
        if left:
            counts = {c: left.count(c) for c in sorted(set(left))}
            fails.append(f"W12: the {label} page uses SVG colour(s) outside the "
                         f"design system: {counts}. Register the value in "
                         f"FIGURE_TOKENS or use var(--token) in the figure.")
    if not fails:
        print(f"W12. figure colours ...... every SVG colour on {len(pages)} "
              f"page(s) is a design token and follows the theme")
    return fails


# The group is the BARE token name. It captured "--folio" while every
# lookup used "folio", so `fg not in pal` was true for all of them and the
# contrast loop skipped every pair while the gate printed a pass. The
# self-test control caught it on its first run, which is the entire reason
# the controls exist.
TOKEN_RE = re.compile(r"^\s*--([a-z-]+):\s*(#[0-9A-Fa-f]{6})\s*;", re.M)
AA_NORMAL = 4.5


def _lum(hexv):
    hexv = hexv.lstrip("#")
    parts = [int(hexv[i:i + 2], 16) / 255 for i in (0, 2, 4)]
    f = lambda c: c / 12.92 if c <= 0.03928 else ((c + 0.055) / 1.055) ** 2.4
    r, g, b = (f(c) for c in parts)
    return 0.2126 * r + 0.7152 * g + 0.0722 * b


def contrast(a, b):
    la, lb = _lum(a), _lum(b)
    hi, lo = max(la, lb), min(la, lb)
    return (hi + 0.05) / (lo + 0.05)


FOREGROUNDS = ("ink", "navy", "amber", "amber-fig", "teal", "folio", "axis")
SURFACES = ("paper", "tint-def", "tint-thm", "tint-fig")


def gate_w13(css_path="AIOM_web.css"):
    """Colour contrast in BOTH themes, and the two dark blocks agreeing.

    Phase W6. Dark mode doubles the palette, and a second palette is a second
    place for an accessibility regression to hide. Every foreground token is
    checked against every surface token at the WCAG AA floor for normal text.
    The check is conservative: some pairs never co-occur, so passing it is
    stronger than the design strictly needs, which is the right direction.

    It also compares the two dark blocks. CSS cannot declare them once, so they
    are written twice and will drift the first time someone edits one of them.
    """
    css = open(css_path, encoding="utf-8").read()
    fails = []

    def block(pattern):
        m = re.search(pattern, css, re.S)
        return dict(TOKEN_RE.findall(m.group(1))) if m else {}

    light = block(r":root \{(.*?)\n\}")
    dark_media = block(r'@media \(prefers-color-scheme: dark\) \{\s*'
                       r':root:not\(\[data-theme="light"\]\) \{(.*?)\n  \}')
    dark_attr = block(r':root\[data-theme="dark"\] \{(.*?)\n\}')

    if not light or not dark_media or not dark_attr:
        return ["W13: could not parse the token blocks from " + css_path]
    if dark_media != dark_attr:
        diff = {k for k in set(dark_media) | set(dark_attr)
                if dark_media.get(k) != dark_attr.get(k)}
        fails.append(f"W13: the two dark token blocks disagree on {sorted(diff)}. "
                     f"They must be identical; CSS cannot declare them once.")

    for name, pal in (("light", light), ("dark", dark_media)):
        for fg in FOREGROUNDS:
            for bg in SURFACES:
                if fg not in pal or bg not in pal:
                    continue
                r = contrast(pal[fg], pal[bg])
                if r < AA_NORMAL:
                    fails.append(f"W13: {name} theme, --{fg} on --{bg} is "
                                 f"{r:.2f}:1, below the AA floor of {AA_NORMAL}")
        for pair in (("invert-fg", "invert-bg"), ("invert-muted", "invert-bg"),
                     ("invert-accent", "invert-bg")):
            if all(k in pal for k in pair):
                r = contrast(pal[pair[0]], pal[pair[1]])
                if r < AA_NORMAL:
                    fails.append(f"W13: {name} theme, --{pair[0]} on "
                                 f"--{pair[1]} is {r:.2f}:1, below AA")
    if not fails:
        print(f"W13. colour contrast .... both themes clear AA for normal text "
              f"across {len(FOREGROUNDS)}x{len(SURFACES)} pairs, dark blocks agree")
    return fails


def gate_w11(outdir):
    """No third-party requests from any page. Decisions 66 and 62.

    Decision 66 rules out analytics, and the build has always self-hosted its
    fonts rather than calling a CDN. Both are currently true because nobody has
    added anything, which is an intention rather than a control. This is the
    control: every SUBRESOURCE the site fetches must be same-origin.

    Anchor hrefs are deliberately NOT checked. The sources page links out to every
    cited source, and that is the point of a bibliography: a link a reader chooses
    to follow is not a request the page makes on their behalf.
    """
    fails = []
    scanned = 0
    for path in sorted(glob.glob(os.path.join(outdir, "**", "*.html"),
                                 recursive=True)) + \
            sorted(glob.glob(os.path.join(outdir, "**", "*.css"), recursive=True)):
        scanned += 1
        text = open(path, encoding="utf-8").read()
        for m in SUBRESOURCE_RE.finditer(text):
            url = next((g for g in m.groups() if g), "")
            if re.match(r"https?://|//", url.strip()):
                fails.append(f"W11: {os.path.relpath(path, outdir)} fetches a "
                             f"third-party subresource: {url[:70]}")
    if not fails:
        print(f"W11. third-party requests  none across {scanned} file(s). "
              f"No analytics, no CDN, fonts self-hosted")
    return fails


def gate_w10(outdir, metas, notes, preview):
    """Deploy readiness. Is what is about to be published complete and correct?"""
    fails = [n for n in notes if "FAIL" in n]
    fails = [f"W10: {f}" for f in fails]

    locked = set(locked_chapters())
    built = {int(m["chapter_number"]) for m in metas if m["chapter_number"]}
    missing = sorted(locked - built)
    if missing:
        fails.append(f"W10: chapter(s) {missing} are locked but were not built, "
                     f"so the deploy would silently omit them")

    for m in metas:
        page = os.path.join(outdir, m["slug"], "index.html")
        if not os.path.exists(page):
            fails.append(f"W10: {page} was not written")

    # A publish build must carry no noindex page. A preview build must carry
    # nothing else.
    for path in sorted(glob.glob(os.path.join(outdir, "**", "*.html"),
                                 recursive=True)):
        has = 'name="robots"' in open(path, encoding="utf-8").read()
        if has and not preview:
            fails.append(f"W10: {path} carries a robots noindex tag in a "
                         f"publish build")

    for req in ("index.html", "robots.txt", "sitemap.xml", "404.html",
                "search-index.json", "assets/aiom_web.css"):
        if not os.path.exists(os.path.join(outdir, req)):
            fails.append(f"W10: {req} is missing from the built site")

    sm = os.path.join(outdir, "sitemap.xml")
    if os.path.exists(sm):
        xml = open(sm, encoding="utf-8").read()
        for m in metas:
            if f"/{m['slug']}/" not in xml:
                fails.append(f"W10: chapter {m['chapter_number']} is not in "
                             f"the sitemap")
    if not fails:
        print(f"W10. deploy readiness .... {len(metas)} chapter page(s), "
              f"sitemap, robots, 404, assets all present")
    return fails


def write_deploy_files(outdir, metas, base_url, base_path=""):
    """robots.txt, sitemap.xml, 404.html, and CNAME when a domain is set.

    base_url is empty until Dan rules the domain. The sitemap then emits
    site-relative paths, which are valid and become absolute the moment a domain
    is supplied. Nothing here invents a hostname.
    """
    pages = ["", "search/", "glossary/", "sources/", "objects/"] + \
            [m["slug"] + "/" for m in metas]
    root = base_url.rstrip("/") if base_url else ""
    urls = "\n".join(
        f"  <url><loc>{root}/{p}</loc></url>" for p in pages)
    open(os.path.join(outdir, "sitemap.xml"), "w", encoding="utf-8").write(
        '<?xml version="1.0" encoding="UTF-8"?>\n'
        '<urlset xmlns="http://www.sitemaps.org/schemas/sitemap/0.9">\n'
        f"{urls}\n</urlset>\n")

    open(os.path.join(outdir, "robots.txt"), "w", encoding="utf-8").write(
        "User-agent: *\n"
        "Allow: /\n"
        + (f"Sitemap: {root}/sitemap.xml\n" if root else "Sitemap: /sitemap.xml\n"))

    open(os.path.join(outdir, "404.html"), "w", encoding="utf-8").write(
        _env().get_template("404.html.j2").render(base=base_path))

    if base_url:
        host = re.sub(r"^https?://", "", base_url).strip("/")
        open(os.path.join(outdir, "CNAME"), "w", encoding="utf-8").write(host + "\n")



W15_FOLLOW = r"""
(href) => {
  const id = decodeURIComponent(href.slice(1));
  const target = document.getElementById(id);
  const link = document.querySelector('a[href="' + CSS.escape(href).replace(/\\#/, '#') + '"]')
            || [...document.querySelectorAll('a[href^="#"]')]
                 .find(a => a.getAttribute('href') === href);
  if (!target) return {dead: true};
  if (!link) return {nolink: true};
  // The hash must be cleared first. Clicking a link whose hash is ALREADY
  // current is a no-op in every browser, so without this a second visit to the
  // same anchor would measure the previous landing and call it a pass.
  history.replaceState(null, '', location.pathname);
  window.scrollTo(0, 0);
  link.click();
  return {clicked: true};
}
"""

W15_MEASURE = r"""
(href) => {
  const el = document.getElementById(decodeURIComponent(href.slice(1)));
  const r = el.getBoundingClientRect();
  const doc = document.documentElement;
  return {
    top: Math.round(r.top),
    bottom: Math.round(r.bottom),
    scrollY: Math.round(window.scrollY),
    viewport: doc.clientHeight,
    atEnd: Math.ceil(window.scrollY + doc.clientHeight) >= doc.scrollHeight - 2,
    hidden: el.offsetParent === null && getComputedStyle(el).position !== 'fixed',
  };
}
"""

# How far below the top of the window a target may land and still count as
# arrived. The sticky bar plus scroll-padding puts every correct landing near
# 165px at the shipped type size, and the root size is fluid, so the band is
# generous at the bottom and tight at the top.
W15_BAND = (-8, 320)



@contextlib.contextmanager
def _serve(outdir, base_path=""):
    """Serve the built tree over HTTP at the prefix it deploys to.

    ADDED 2026-08-13, ON DAN'S RULING, AFTER A DEFECT THAT ONLY EXISTS UNDER A
    PREFIX. The 404 page linked its stylesheet as `/assets/aiom_web.css`. Loaded
    from `file://` that is merely odd; served from a GitHub Pages PROJECT site at
    `/textbook.aiom/` it resolves to the ROOT of the user site, so the live 404
    page came up unstyled with every link leading out of the book. Nothing saw
    it: W10 checks the asset exists, W11 checks it is same-origin, and the gates
    had never loaded a page over HTTP at the deployed prefix.

    The tree is mounted UNDER the prefix rather than served at the root, because
    serving at the root is exactly the configuration that hides this class of
    bug. A symlink is used so nothing is copied.
    """
    root = tempfile.mkdtemp(prefix="aiom-serve-")
    prefix = "/" + base_path.strip("/") if base_path.strip("/") else ""
    try:
        if prefix:
            mount = os.path.join(root, *prefix.strip("/").split("/"))
            os.makedirs(os.path.dirname(mount), exist_ok=True)
            os.symlink(os.path.abspath(outdir), mount)
            docroot = root
        else:
            docroot = os.path.abspath(outdir)

        class _Quiet(http.server.SimpleHTTPRequestHandler):
            # The default handler logs every request to stderr, which would bury
            # the gate output it is serving.
            def log_message(self, *a, **kw):
                pass

        handler = functools.partial(_Quiet, directory=docroot)
        # Port 0 lets the OS pick a free one, so concurrent runs cannot collide.
        httpd = socketserver.TCPServer(("127.0.0.1", 0), handler)
        httpd.daemon_threads = True
        thread = threading.Thread(target=httpd.serve_forever, daemon=True)
        thread.start()
        try:
            yield f"http://127.0.0.1:{httpd.server_address[1]}{prefix}"
        finally:
            httpd.shutdown()
            httpd.server_close()
            thread.join(timeout=5)
    finally:
        shutil.rmtree(root, ignore_errors=True)

def gate_w15(outdir, base_path=""):
    """Navigation navigates. Follow every in-page link in a real browser.

    ADDED 2026-08-13, ON DAN'S RULING, AFTER TWO RAIL ANCHORS WERE DEAD FOR SIX
    PHASES. The id for the Opening case and Craft section slots was written into
    a CLOSING tag, which every parser discards, so the anchor was in the file and
    never in the DOM. W4 read ids with a regex, counted both as live targets, and
    reported that every internal link resolved. Two gates agreed, twice per
    build, about links that went nowhere. Dan found them by clicking one.

    W4 now parses start tags and would catch that exact fault. This gate exists
    because the class is larger than the fault: an anchor can also be present and
    unreachable, on an element that is display:none, inside a collapsed rail, or
    under a handler that swallows the click, and no amount of reading the markup
    settles any of those. **The only check that answers "does this link work" is
    following the link.**

    Runs with reduced motion so the scroll is instantaneous and the measurement
    is deterministic. That is a shipped configuration rather than a test-only
    one, since the stylesheet honours prefers-reduced-motion.

    OPTIONAL, exactly like W6 and for the same reason: it needs a headless
    browser that nothing else in the build requires. It reports SKIPPED and is
    counted as skipped, never as passed.
    """
    try:
        from playwright.sync_api import sync_playwright
    except ImportError:
        print("W15. in-page navigation .. SKIPPED, playwright not installed")
        return [], False

    exe = next((p for p in glob.glob("/opt/pw-browsers/chromium-*/chrome-linux/chrome")
                if os.path.exists(p)), None)
    pages = sorted(glob.glob(os.path.join(outdir, "**", "*.html"), recursive=True))
    fails, followed = [], 0
    try:
        with _serve(outdir, base_path) as origin, sync_playwright() as pw:
            kw = {"args": ["--no-sandbox"]}
            if exe:
                kw["executable_path"] = exe
            b = pw.chromium.launch(**kw)
            pg = b.new_page(viewport={"width": 1512, "height": 900},
                            reduced_motion="reduce")
            bad_res = []
            pg.on("response",
                  lambda r: bad_res.append((r.url, r.status)) if r.status >= 400
                  else None)
            for path in pages:
                label = os.path.relpath(path, outdir)
                bad_res.clear()
                pg.goto(origin + "/" + label.replace(os.sep, "/"),
                        wait_until="networkidle")
                pg.wait_for_timeout(80)
                for u, s in bad_res:
                    # Chromium requests /favicon.ico on its own, unprompted by
                    # the page. The site ships none, so that 404 is not a defect
                    # in anything the build emitted. Excluded explicitly rather
                    # than left to chance: it happened not to surface on the run
                    # that found this gate's first real defect, and relying on
                    # that would be relying on luck.
                    if u.endswith("/favicon.ico"):
                        continue
                    fails.append(
                        f"W15 [{label}]: a subresource returned {s} when the "
                        f"page is served at {base_path or chr(47)}: "
                        f"{u.split(chr(47) + chr(47), 1)[-1].split(chr(47), 1)[-1]}")
                hrefs = pg.eval_on_selector_all(
                    'a[href^="#"]',
                    'els => [...new Set(els.map(e => e.getAttribute("href")))]')
                for href in hrefs:
                    if href == "#":
                        fails.append(f"W15 [{label}]: a link with a bare '#' "
                                     f"href, which navigates nowhere")
                        continue
                    r = pg.evaluate(W15_FOLLOW, href)
                    if r.get("dead"):
                        fails.append(f"W15 [{label}]: {href} has no target "
                                     f"element, so the link does nothing")
                        continue
                    if r.get("nolink"):
                        continue
                    pg.wait_for_timeout(60)
                    m = pg.evaluate(W15_MEASURE, href)
                    followed += 1
                    if m["hidden"]:
                        fails.append(f"W15 [{label}]: {href} targets an element "
                                     f"that is not rendered")
                        continue
                    lo, hi = W15_BAND
                    if lo <= m["top"] <= hi:
                        continue
                    # A target near the foot of the document cannot reach the top
                    # of the window, because there is nothing left to scroll. It
                    # has arrived if the page is at its end and the target is on
                    # screen. Without this the last anchor on every page fails.
                    if m["atEnd"] and m["bottom"] > 0 and m["top"] < m["viewport"]:
                        continue
                    fails.append(
                        f"W15 [{label}]: {href} did not arrive. After the click "
                        f"the target sits {m['top']}px from the top of the "
                        f"window (expected {lo} to {hi}), scrollY={m['scrollY']}")
            b.close()
    except Exception as exc:
        print(f"W15. in-page navigation .. SKIPPED, browser unavailable "
              f"({exc.__class__.__name__})")
        return [], False

    if not fails:
        print(f"W15. navigation and load . {followed} link(s) followed, "
              f"{len(pages)} page(s) served at {base_path or chr(47)}, every "
              f"link arrives and every subresource resolves")
    return fails, True

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


def gate_w8(ref, meta, web_html):
    """The reference layer against the chapter it claims to describe.

    Three joints, each of which can drift silently:

    W8a. The GLOSSARY is built from the continuity ledger, and the chapter sets
    its own key terms. Those are two records of one definition. CLAUDE.md already
    records that a ruled claim narrowing was reverted four times with every date
    and figure intact, and a definition is exactly that kind of text: it can be
    reworded without any value changing. So the ledger's definition must match
    the chapter's key-term text, character for character.

    W8b. The SOURCES page must carry every key the chapter actually cites. A
    bibliography missing an entry the prose points at is a broken promise to the
    reader, and it is invisible to every other check.

    W8c. The OBJECT INDEX must not exceed what chapters invoke. The Locked
    Registry workbook is not in this repository (CLAUDE.md rule 4a), so the site
    cannot claim objects it has never seen a chapter render.
    """
    fails = []

    # W8a. Key terms as the chapter sets them, name to definition.
    # Balanced scan, not a non-greedy regex. A .kt block contains a nested
    # .kt-h div, so `<div class="kt">(.*?)</div>` closes on the WRONG div and
    # swallows the neighbouring terms. That was written and it failed here, which
    # is the third time in this file that a hand-rolled non-greedy match over
    # nested elements has been the defect. find_spans now takes a tag.
    chapter_terms = {}
    # The opener tolerates attributes for the same reason the count above does.
    # link_terms() adds an id to every .kt block, and an opener demanding an
    # immediate ">" would match nothing, leaving W8a comparing an EMPTY set of
    # chapter terms against the ledger and reporting a pass. A gate that
    # measures nothing is this repository's signature failure, so the two
    # openers must move together.
    #
    # AND THE OPENER MUST CONSUME THE WHOLE TAG, not just enough to identify it.
    # find_spans returns the text after the opener MATCH, so a `[ >]` opener
    # left the remainder of the tag, id and all, inside the block. W8a then
    # reported all eight terms as differing from the ledger. That was this gate
    # doing its job on the change that broke it, and it is the reason the
    # pattern is `[^>]*>` rather than the shorter thing that looked equivalent.
    for _, _, inner in find_spans(web_html, r'<div class="kt"[^>]*>', "div"):
        head = find_spans(inner, r'<div class="kt-h">', "div")
        if not head:
            continue
        name = re.search(r'<span class="kt-t">(.*?)</span>', head[0][2], re.S)
        if not name:
            continue
        body = inner[:head[0][0]] + inner[head[0][1]:]
        chapter_terms[_plain(name.group(1))] = _plain(body)

    num = int(meta["chapter_number"]) if meta["chapter_number"] else None
    checked = 0
    for t in ref["terms"]:
        if t["chapter"] != num:
            continue
        got = chapter_terms.get(t["term"])
        if got is None:
            fails.append(f"W8a: ledger says chapter {num} owns {t['term']!r}, "
                         f"but the chapter sets no such key term")
            continue
        checked += 1
        if got != t["definition"]:
            fails.append(
                f"W8a: {t['term']!r} differs between the ledger and the chapter.\n"
                f"       ledger:  {t['definition'][:100]}\n"
                f"       chapter: {got[:100]}")
    if not fails and checked:
        print(f"W8a. glossary agreement ... {checked} term(s) identical in the "
              f"ledger and the chapter")

    # W8b. Every cited key is on the sources page.
    on_page = {s["key"] for s in ref["sources"]}
    missing = sorted({s["key"] for s in ref["sources"] if s["cited"]} - on_page)
    cited = sorted(s["key"] for s in ref["sources"] if s["cited"])
    if missing:
        fails.append(f"W8b: cited source(s) absent from the sources page: {missing}")
    else:
        print(f"W8b. sources coverage ..... {len(cited)} cited of "
              f"{len(on_page)} in the register, all listed")

    # W8c. No object claimed that no chapter has rendered.
    rendered = set(re.findall(r"\b((?:THM|LEM|PROP)-\d+)\b", web_html))
    claimed = {o["id"] for o in ref["objects"] if o["chapter"] == num}
    extra = sorted(claimed - rendered)
    if extra:
        fails.append(f"W8c: object index claims {extra} for chapter {num}, "
                     f"which the chapter does not render")
    elif claimed:
        print(f"W8c. object index ......... {len(claimed)} object(s), each "
              f"rendered by the chapter that invokes it")
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
    print(f"  term links: {len(meta['termlinks'])} bolded term(s) linked to "
          f"the definition that owns them")

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


def build_specimens(meta, chapter_html):
    """Lift real material out of the locked chapter for the landing page.

    THE FRONT PAGE QUOTES THE BOOK. IT NEVER PARAPHRASES IT. A marketing surface
    that restates a theorem in plainer words is the exact failure CLAUDE.md rule
    4a forbids inside a chapter, and it is worse on the front page, because that
    is where a reader forms their idea of what the book says. Everything returned
    here is lifted verbatim from the chapter or from its own register, and gate
    W9 fails the build if the landing page and the chapter ever disagree.

    Returns the theorem panel, one specimen paragraph with its sidenote, and the
    register note that produced that sidenote.
    """
    body = meta["body"]

    thm = find_spans(body, r'<div class="theorem">', "div")
    theorem = body[thm[0][0]:thm[0][1]] if thm else ""

    # The paragraph that calls the first sidenote, taken whole with its note.
    spec_para, note_text = "", ""
    for s, e, inner in find_spans(body, r"<p>", "p"):
        if 'id="fnref-1"' in inner:
            spec_para = body[s:e]
            n = find_spans(spec_para, NOTE_OPEN, "span")
            if n:
                note_text = _plain(re.sub(r'<a class="note-n".*?</a>', "",
                                          n[0][2], flags=re.S))
            break

    # The register entry behind that note, from the chapter's own Decision 51
    # block. The editorial note is what makes the sourcing discipline visible:
    # it records what the source does and does not support.
    src = footnotes.load_sources(chapter_html)
    key = ""
    m = re.search(r'<cite src="([^";]+)', chapter_html)
    if m:
        key = m.group(1).strip()
    entry = src.get(key, {})
    # THE REGISTER'S `note` FIELD IS NEVER PUBLISHED. It is internal audit prose:
    # it carries fact-check finding IDs, instructions to future checkers, and,
    # decisively, VERBATIM QUOTATIONS OF SENTENCES THE BOOK HAS CUT. The note on
    # this very entry quotes the SF2 continuation mechanism and the FC9
    # absorbed-cost inference, both retracted. Putting it on the landing page
    # would publish the book's retracted claims on its most public surface.
    # Gate W9b enforces this rather than leaving it to whoever writes the next
    # template. Only the bibliographic fields, which are reader-facing and
    # already on the sources page, are carried.
    import cite_format
    return {
        "theorem": theorem,
        "spec_para": spec_para,
        "spec_note": note_text,
        "reg_key": key,
        "reg_title": entry.get("title", ""),
        "reg_url": entry.get("url", ""),
        "reg_accessed": entry.get("accessed", ""),
        "reg_cite": cite_format.format_note(entry, url_policy="full") if entry else "",
        "reg_has_note": bool((entry.get("note") or "").strip()),
    }


def gate_w9(spec, meta, index_html):
    """The landing page against the chapter it advertises.

    Same shape as gate W8, one surface further out. The front page carries the
    theorem and a specimen paragraph, and both must be present in the chapter
    character for character. A marketing page that drifts from the book is how a
    reader ends up quoting a sentence the book does not contain.
    """
    fails = []
    chapter_text = extract_text(meta["body"], skip_attrs=("data-note",))
    idx_text = extract_text(index_html)

    checks = [("theorem", extract_text(spec["theorem"])),
              ("specimen paragraph",
               extract_text(spec["spec_para"], skip_attrs=("data-note",)))]
    for label, text in checks:
        if not text:
            fails.append(f"W9: no {label} could be lifted from the chapter")
        elif text not in chapter_text:
            fails.append(f"W9: the {label} is not present verbatim in the chapter")
        elif text not in idx_text:
            fails.append(f"W9: the {label} was lifted but is not on the landing "
                         f"page, so the page and the chapter disagree")
    if spec["spec_note"] and spec["spec_note"] not in idx_text:
        fails.append("W9: the specimen sidenote text is not on the landing page")
    if not fails:
        print(f"W9a. landing specimens ... theorem and specimen paragraph "
              f"verbatim from chapter {meta['chapter_number']}")
    return fails


def gate_w9b(chapter_html, pages):
    """No register note text on any published page.

    The register's `note` field is the fact checkers' working record. It carries
    finding IDs, instructions to later checkers, and VERBATIM QUOTATIONS OF
    SENTENCES THE BOOK HAS CUT: the note behind Chapter 1's first citation quotes
    both the SF2 continuation mechanism and the FC9 absorbed-cost inference, each
    of which was retracted on Dan's ruling.

    Publishing any of it would put the book's retracted claims on its most public
    surface. This was nearly done: a first draft of the landing page printed the
    note in full, and gate W3 caught it only because the note contains straight
    apostrophes, which is luck rather than a check. This is the check.
    """
    src = footnotes.load_sources(chapter_html)
    fails = []
    for key, entry in src.items():
        note = re.sub(r"\s+", " ", (entry.get("note") or "")).strip()
        if len(note) < 40:
            continue
        probe = note[:60]
        for label, html in pages:
            if probe in re.sub(r"\s+", " ", extract_text(html)):
                fails.append(f"W9b: register note for {key!r} is published on the "
                             f"{label} page. Notes are internal and quote cut "
                             f"claims; only bibliographic fields may be published.")
    if not fails:
        print(f"W9b. register notes ...... none of {len(src)} internal notes "
              f"appear on any published page")
    return fails


def build_reference(outdir, meta, chapter_html):
    """Glossary, sources, and object index. Phase W4.

    Every page here is generated from a record that already exists and is already
    enforced somewhere else:

      glossary  <- AIOM_Continuity_Ledger.md, the G3 record, appended at lock
      sources   <- the chapter's own Decision 51 register, via cite_format
      objects   <- the ledger's registry glosses

    None of it is assembled by scraping the rendered chapter, which would have
    made the reference layer a second reading of the book.

    THE OBJECT INDEX IS AN APPENDIX, NEVER THE SPINE. CLAUDE.md rule 4: the
    registry justifies the book, it does not organize it. This page is reached
    from a chapter, no chapter is laid out around it, and it carries only what
    chapters have actually invoked. The Locked Registry workbook is not in this
    repository (rule 4a), so a full 228-object index cannot be built here and is
    not pretended at.
    """
    import cite_format
    led = ledger.load_ledger()
    locked = set(locked_chapters())

    def ch_link(n):
        return f"../ch{n:02d}/" if n in locked else None

    terms = sorted(
        ({"term": t["term"], "definition": t["definition"],
          "chapter": ledger.chapter_of(t["owner"]),
          "href": ch_link(ledger.chapter_of(t["owner"]))}
         for t in led["terms"]),
        key=lambda t: t["term"].lower())

    # Sources come from the chapter register with url_policy FULL. Print rules
    # URLs out of footnotes; a bibliography is where they belong, and this is the
    # bibliography. Gate W1 is unaffected because it compares the CHAPTER, and
    # this page is not the chapter.
    src = footnotes.load_sources(chapter_html)
    cited = set()
    for m in re.finditer(r'<cite src="([^"]+)">', chapter_html):
        cited.update(k.strip() for k in m.group(1).split(";") if k.strip())
    sources = sorted(
        ({"key": k, "cited": k in cited,
          "text": cite_format.format_note(src[k], url_policy="full"),
          "url": src[k].get("url") or (
              f'https://doi.org/{src[k]["doi"]}' if src[k].get("doi") else "")}
         for k in src),
        key=lambda s: s["text"].lower())

    objects = sorted(
        ({"id": o["object"], "gloss": o["gloss"],
          "chapter": ledger.chapter_of(o["first_used"]),
          "href": ch_link(ledger.chapter_of(o["first_used"]))}
         for o in led["registry"]),
        key=lambda o: o["id"])

    forward = [{"frm": ledger.chapter_of(f["frm"]), "to": ledger.chapter_of(f["to"]),
                "promise": f["promise"], "status": f["status"]}
               for f in led["forward"]]

    env = _env()
    pages = {}
    for name, tpl, ctx in (
        ("glossary", "glossary.html.j2", {"terms": terms}),
        ("sources", "sources.html.j2",
         {"sources": sources, "chapter_title": meta["chapter_title"],
          "chapter_number": meta["chapter_number"]}),
        ("objects", "objects.html.j2", {"objects": objects, "forward": forward}),
    ):
        html = env.get_template(tpl).render(book=meta["book"], **ctx)
        d = os.path.join(outdir, name)
        os.makedirs(d, exist_ok=True)
        open(os.path.join(d, "index.html"), "w", encoding="utf-8").write(html)
        pages[name] = html
    return pages, {"terms": terms, "sources": sources, "objects": objects}


def build_search(outdir, meta, chapter_html, ref):
    """A prebuilt JSON index, queried client side.

    The whole book at fifteen chapters of roughly seven thousand words is small
    enough to ship in one request, so there is no server and nothing to operate.
    Chapter prose is indexed per SECTION rather than per chapter, so a hit lands
    the reader on the passage instead of at the top of a 25,000 pixel page.
    """
    docs = []
    for t in ref["terms"]:
        docs.append({"t": t["term"], "k": "term",
                     "b": t["definition"],
                     "u": f"glossary/#term-{slugify(t['term'])}"})
    for s in ref["sources"]:
        docs.append({"t": _plain(s["text"])[:90], "k": "source",
                     "b": _plain(s["text"]),
                     "u": f"sources/#src-{slugify(s['key'])}"})
    for o in ref["objects"]:
        docs.append({"t": o["id"], "k": "object", "b": o["gloss"],
                     "u": f"objects/#obj-{slugify(o['id'])}"})

    # Chapter prose, split at the numbered section heads.
    body = meta["body"]
    marks = [(m.start(), m.group(1), m.group(2))
             for m in re.finditer(
                 r'<h3 class="section" id="([^"]+)">'
                 r'<span class="num">([\d.]+)</span>', body)]
    bounds = [m[0] for m in marks] + [len(body)]
    slug = meta["slug"]
    for i, (_, sec_id, num) in enumerate(marks):
        chunk = body[bounds[i]:bounds[i + 1]]
        text = extract_text(chunk, skip_attrs=("data-note",))
        head_text = SEC_NUM_RE.sub("", text[:70])
        docs.append({"t": f"{num} {head_text}",
                     "k": f"Chapter {meta['chapter_number']}",
                     "b": text, "u": f"{slug}/#{sec_id}"})
    head = extract_text(body[:bounds[0]] if marks else body,
                        skip_attrs=("data-note",))
    docs.append({"t": meta["chapter_title"], "k": f"Chapter {meta['chapter_number']}",
                 "b": head, "u": f"{slug}/"})

    import json
    path = os.path.join(outdir, "search-index.json")
    open(path, "w", encoding="utf-8").write(
        json.dumps({"docs": docs}, ensure_ascii=False, separators=(",", ":")))
    html = _env().get_template("search.html.j2").render(book=meta["book"],
                                                        count=len(docs))
    d = os.path.join(outdir, "search")
    os.makedirs(d, exist_ok=True)
    open(os.path.join(d, "index.html"), "w", encoding="utf-8").write(html)
    return html, len(docs), os.path.getsize(path)


# No trailing space is required. The heading markup is
# <span class="num">1.5</span>What this book is not, so the extracted text
# is "1.5What this book is not" and a pattern needing a space left the
# number in, printing it twice in the search result title.
SEC_NUM_RE = re.compile(r"^[\d.]+\s*")


def slugify(s):
    return re.sub(r"[^a-z0-9]+", "-", s.lower()).strip("-")


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
        first_locked=first, spec=meta["spec"], counts=meta["counts"])
    open(os.path.join(outdir, "index.html"), "w", encoding="utf-8").write(out)
    return os.path.join(outdir, "index.html")


def build_site(chapter_paths, outdir, preview=False, no_browser=False,
               base_url="", notes=(), base_path=""):
    """Build the whole site from every chapter given, then gate it.

    W5 turned this from a one-chapter command into a site build. The gates that
    are per-chapter run per chapter; the gates that are properties of the site
    run once over every emitted page. A chapter that fails does not stop the
    others being reported, because a deploy needs the full list of what is wrong
    rather than the first thing that is wrong.
    """
    metas, pages, fails = [], [], []
    first_index = None

    for path in chapter_paths:
        src = open(path, encoding="utf-8").read()
        print_html, web_html, meta, page = render(path, outdir, preview)
        meta["spec"] = build_specimens(meta, src)
        metas.append(meta)
        pages.append(("chapter " + meta["slug"], web_html))
        print(f"  chapter {meta['chapter_number']}: {meta['chapter_title']} "
              f"-> {page}")

        fails += gate_w1(print_html, web_html)
        fails += gate_w2(path, preview)
        fails += gate_w4(web_html, meta)
        fails += gate_w5(web_html, meta, "chapter " + meta["slug"])
        fails += gate_w7(meta, meta["structure"])
        fails += gate_w9b(src, [("chapter " + meta["slug"], web_html)])
        fails += gate_w14(path)
        if not no_browser:
            w6, ran = gate_w6(page)
            fails += w6

    if not metas:
        return ["W10: no chapters were built, so there is nothing to publish"], []

    lead = metas[0]
    index = render_index(outdir, lead)
    ref_pages, ref = build_reference(
        outdir, lead, open(chapter_paths[0], encoding="utf-8").read())
    search_html, docs, bytes_ = build_search(
        outdir, lead, chapter_paths[0], ref)
    write_deploy_files(outdir, metas, base_url, base_path)
    print(f"  reference and search: {docs} search docs, {bytes_ / 1024:.1f} kB")
    print(f"  deploy files: sitemap, robots, 404"
          + (f", CNAME for {base_url}" if base_url else ", no CNAME (no domain set)"))

    index_html = open(index, encoding="utf-8").read()
    site_pages = ([("index", index_html), ("search", search_html)]
                  + [(n, h) for n, h in ref_pages.items()])

    fails += gate_w8(ref, lead, pages[0][1])
    fails += gate_w9(lead["spec"], lead, index_html)
    fails += gate_w9b(open(chapter_paths[0], encoding="utf-8").read(), site_pages)
    fails += gate_pages(site_pages)
    if not no_browser:
        w6, _ = gate_w6(index)
        fails += w6
    fails += gate_w10(outdir, metas, notes, preview)
    # W15 walks the finished tree, so it runs after W10 has confirmed the tree
    # is complete. Following a link on a page that was never emitted would fail
    # for the wrong reason and send the reader after the wrong defect.
    if not no_browser:
        w15, _ = gate_w15(outdir, base_path)
        fails += w15
    fails += gate_w11(outdir)
    fails += gate_w12(pages + site_pages)
    fails += gate_w13()
    return fails, metas


def main():
    ap = argparse.ArgumentParser(description="Build the AIOM web edition.")
    ap.add_argument("chapter", nargs="*",
                    help="chapter HTML to build; omit with --site to discover")
    ap.add_argument("--site", action="store_true",
                    help="build every LOCKED chapter, discovered from Drafts/")
    ap.add_argument("--out", default="build/web", help="output directory")
    ap.add_argument("--preview", action="store_true",
                    help="build an unlocked chapter to a local noindex page")
    ap.add_argument("--no-browser", action="store_true",
                    help="skip gates W6 and W15, which need a headless browser")
    ap.add_argument("--base-path", default="",
                    help="the path the site is served under, e.g. /textbook.aiom "
                         "for a GitHub Pages project site. Empty for the root.")
    ap.add_argument("--from-worktree", action="store_true",
                    help="build --site from the working tree instead of each "
                         "chapter's last lock. Local preview of edits in "
                         "flight; CI never uses it.")
    ap.add_argument("--base-url", default="",
                    help="site origin, e.g. https://example.org. Sets CNAME and "
                         "absolute sitemap URLs. Unset until Dan rules the domain.")
    a = ap.parse_args()

    if not os.path.exists("web_templates/chapter.html.j2"):
        sys.exit("web_build.py must run from the repository root "
                 "(web_templates/ not found)")

    notes = []
    if a.site:
        # WHAT PUBLISHES IS THE LAST LOCK, NOT THE WORKING TREE. Ruled
        # 2026-08-13. Before this, reopening a locked chapter failed the whole
        # site build and held CI red for the length of a revision, which made
        # editing a published chapter an event. snapshot.py materializes each
        # chapter's locked state into a Drafts-shaped tree, so discovery, W2,
        # the checklist lookup and claimcheck all run unchanged against it.
        root = "Drafts"
        if not a.from_worktree:
            snap_chapters, snap_notes = snapshot.materialize(root, "build/_snapshots")
            notes.extend(snap_notes)
            if not snap_chapters:
                print("Discovering locked chapters:")
                for n in snap_notes:
                    print("  " + n)
                print(chr(10) + "WEB GATES FAILED"
                      + chr(10) + "   W10: no chapter has ever locked, "
                      "nothing to publish")
                return 1
            for name, still_locked, changed in snapshot.divergence(root, snap_chapters):
                if still_locked:
                    notes.append(
                        "WARNING %s: text changed since it locked but its "
                        "checklist still reports Stage 9. An edit to a locked "
                        "chapter should reopen it." % name)
                else:
                    notes.append(
                        "%s: revision in flight, %d file(s) differ from the "
                        "published lock. The site keeps serving the lock."
                        % (name, len(changed)))
            root = "build/_snapshots"
        found, disc_notes = discover_chapters(root)
        notes.extend(disc_notes)
        chapters = [p for _, p in found]
        print("Discovering locked chapters:")
        for n in notes:
            print("  " + n)
        if not chapters:
            print(chr(10) + "WEB GATES FAILED"
                  + chr(10) + "   W10: no locked chapter found to build")
            return 1
    elif a.chapter:
        chapters = a.chapter
    else:
        ap.error("give a chapter path, or --site to build every locked chapter")

    # THE DEPLOY PREFIX. A GitHub Pages PROJECT site serves at /<repo>/, and the
    # 404 page is the one page that cannot use a relative path to reach an asset,
    # because Pages serves it for any missing address at any depth. --base-path
    # states that prefix; when it is not given it is taken from --base-url's own
    # path, so supplying a domain that already carries a subdirectory does not
    # need the same fact stated twice. Empty means the site is served at the root,
    # which is what a custom domain gives.
    base_path = a.base_path
    if not base_path and a.base_url:
        base_path = re.sub(r"^https?://[^/]+", "", a.base_url)
    base_path = "/" + base_path.strip("/") if base_path.strip("/") else ""

    print(f"{chr(10)}Building {len(chapters)} chapter(s) into {a.out}")
    fails, metas = build_site(chapters, a.out, a.preview, a.no_browser,
                              a.base_url, notes, base_path)

    verdict = "PASSED" if not fails else "FAILED"
    # The skip is stated in the verdict line rather than buried above it. Five of
    # this repository's recorded defects are a check that was believed to have
    # run and had not, so an optional gate has to be noisy about not running.
    if a.no_browser:
        verdict += ", W6 AND W15 NOT RUN"
    print(f"{chr(10)}WEB GATES {verdict}")
    for f in fails:
        print("   " + f)
    return 0 if not fails else 1


if __name__ == "__main__":
    sys.exit(main())
