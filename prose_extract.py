#!/usr/bin/env python3
"""Chapter HTML to reviewer-readable prose, for a second-model review package.

Stage 1, Stage 2 and the bias check each need the chapter as plain prose that a
reviewer can read and quote. That extraction had been written from scratch three
times, and the first version invented a slot label the chapter does not carry.
This is the committed version, on the same reasoning that promoted
factcheck_packet.py to the root: work that comes due on every chapter at three
separate steps is not throwaway work.

What it emits is the chapter's own text and nothing else. The source register is
excluded, because its notes are the fact checkers' working record and carry
superseded ruled forms beside current ones. Citation markers are excluded, because
a developmental or structural reviewer is reading prose rather than checking it.
Figures are named and their captions kept; the drawn geometry cannot survive the
conversion and the extract says so at each figure rather than dropping it silently.

    python3 prose_extract.py <chapter.html> [--out FILE]
"""

import argparse
import html
import re
import sys
from html.parser import HTMLParser

# Blocks whose text is dropped whole.
DROP_SECTIONS = ('aiom-sources',)


def strip_dropped(doc):
    """Remove the source register, the SVG geometry and the citation notes."""
    for sid in DROP_SECTIONS:
        doc = re.sub(
            r'<p class="slot-label">Sources for this chapter</p>\s*'
            r'<section id="%s">.*?</section>' % re.escape(sid),
            '', doc, flags=re.S)
        doc = re.sub(r'<section id="%s">.*?</section>' % re.escape(sid),
                     '', doc, flags=re.S)
    doc = re.sub(r'<svg\b.*?</svg>', '', doc, flags=re.S)
    doc = re.sub(r'<cite\b.*?</cite>', '', doc, flags=re.S)
    return doc


class Inline(HTMLParser):
    """Flatten an element's inner HTML to markdown-ish plain text."""

    # Spans that carry a label butted straight against the text that follows it:
    # the markup relies on CSS for the gap, so the gap has to be restored here.
    LABEL_SPANS = ('mk', 'num', 'fignum', 'kt-t', 'dq-n')

    def __init__(self):
        super().__init__(convert_charrefs=True)
        self.out = []
        self.spans = []

    def handle_starttag(self, tag, attrs):
        if tag in ('b', 'strong'):
            self.out.append('**')
        elif tag in ('em', 'i'):
            self.out.append('*')
        elif tag == 'span':
            cls = dict(attrs).get('class', '').split()
            self.spans.append(any(c in self.LABEL_SPANS for c in cls))

    def handle_endtag(self, tag):
        if tag in ('b', 'strong'):
            self.out.append('**')
        elif tag in ('em', 'i'):
            self.out.append('*')
        elif tag == 'span':
            if self.spans and self.spans.pop():
                self.out.append(' ')

    def handle_data(self, data):
        self.out.append(data)

    def text(self):
        return re.sub(r'\s+', ' ', ''.join(self.out)).strip()


def inline(fragment):
    p = Inline()
    p.feed(fragment)
    return p.text()


def find_block(doc, start, tag):
    """Return (inner, end) for the balanced element opening at start."""
    opener = re.compile(r'<%s\b[^>]*>' % tag)
    m = opener.match(doc, start)
    if not m:
        return None, start
    depth = 1
    pos = m.end()
    token = re.compile(r'<(/?)%s\b[^>]*>' % tag)
    while depth:
        t = token.search(doc, pos)
        if not t:
            return doc[m.end():], len(doc)
        depth += -1 if t.group(1) else 1
        pos = t.end()
    close = doc.rfind('</%s' % tag, 0, pos)
    return doc[m.end():close], pos


def class_of(open_tag):
    m = re.search(r'class="([^"]*)"', open_tag)
    return m.group(1).split() if m else []


def convert(doc):
    doc = strip_dropped(doc)
    body = doc[doc.find('<body>') + len('<body>'):doc.find('</body>')]
    out = []
    pos = 0
    tag_re = re.compile(r'<(h1|h2|h3|p|aside|div|figure|section|ol)\b[^>]*>')
    while True:
        m = tag_re.search(body, pos)
        if not m:
            break
        tag = m.group(1)
        classes = class_of(m.group(0))
        inner, end = find_block(body, m.start(), tag)
        pos = end

        if tag == 'section':
            # Containers only: re-scan their contents in place.
            pos = m.end()
            continue
        if tag == 'ol':
            continue

        if tag == 'h1':
            out.append('# %s' % inline(inner))
        elif tag == 'h2':
            out.append('## %s' % inline(inner))
        elif tag == 'h3':
            num = re.search(r'<span class="num">([^<]*)</span>', inner)
            text = inline(re.sub(r'<span class="num">[^<]*</span>', '', inner))
            out.append('### %s' % ('%s %s' % (num.group(1), text) if num else text))
        elif tag == 'figure':
            cap = re.search(r'<figcaption[^>]*>(.*?)</figcaption>', inner, re.S)
            label = re.search(r'<span class="fignum">([^<]*)</span>', inner)
            body_text = inline(re.sub(r'<span class="fignum">[^<]*</span>', '',
                                      cap.group(1))) if cap else ''
            name = label.group(1) if label else 'Figure'
            out.append('[%s. Drawn figure, not reproduced here.]\n\n**%s.** %s'
                       % (name.upper(), name, body_text))
        elif tag == 'aside' and 'definition' in classes:
            term = re.search(r'<p class="term">(.*?)</p>', inner, re.S)
            paras = re.findall(r'<p(?![^>]*class="(?:lab|term)")[^>]*>(.*?)</p>',
                               inner, re.S)
            out.append('> **DEFINITION CALLOUT · %s**\n>\n> %s'
                       % (inline(term.group(1)) if term else '',
                          '\n>\n> '.join(inline(p) for p in paras)))
        elif tag == 'div' and 'theorem' in classes:
            lab = re.search(r'<p class="lab">(.*?)</p>', inner, re.S)
            stmt = re.search(r'<p class="stmt">(.*?)</p>', inner, re.S)
            cond = re.search(r'<p class="cond">(.*?)</p>', inner, re.S)
            ante = re.findall(r'<li[^>]*>(.*?)</li>', inner, re.S)
            conseq = re.search(r'<p class="conseq">(.*?)</p>', inner, re.S)
            lines = ['> **THEOREM PANEL · %s**' % (inline(lab.group(1)) if lab else '')]
            if stmt:
                lines.append('> *%s*' % inline(stmt.group(1)))
            if cond:
                lines.append('> %s' % inline(cond.group(1)))
            for a in ante:
                lines.append('>   %s' % inline(a))
            if conseq:
                lines.append('> %s' % inline(conseq.group(1)))
            out.append('\n>\n'.join(lines))
        elif tag == 'div' and 'dated' in classes:
            # The device the fifty-year rule depends on: perishable specifics are
            # quarantined here, so an extract that flattened it would hide the one
            # thing a reader of the extract most needs to see about this material.
            date = re.search(r'<p class="date">(.*?)</p>', inner, re.S)
            paras = re.findall(r'<p(?![^>]*class="date")[^>]*>(.*?)</p>', inner, re.S)
            out.append('> **DATED EVIDENCE BOX · %s**\n>\n> %s'
                       % (inline(date.group(1)) if date else '',
                          '\n>\n> '.join(inline(x) for x in paras)))
        elif tag == 'div' and 'kt' in classes:
            term = re.search(r'<span class="kt-t">(.*?)</span>', inner, re.S)
            paras = re.findall(r'<p[^>]*>(.*?)</p>', inner, re.S)
            out.append('**%s.** %s' % (inline(term.group(1)) if term else '',
                                       ' '.join(inline(p) for p in paras)))
        elif tag == 'div' and 'dq' in classes:
            n = re.search(r'<div class="dq-n">(.*?)</div>', inner, re.S)
            paras = re.findall(r'<p[^>]*>(.*?)</p>', inner, re.S)
            out.append('**%s.** %s' % (inline(n.group(1)) if n else '',
                                       ' '.join(inline(p) for p in paras)))
        elif tag == 'div' and 'problem' in classes:
            # Walked in document order rather than by first match, because a
            # problem div can hold MORE THAN ONE problem. Chapter 2's P4 has no
            # wrapper of its own and sits inside P3's, and taking the first plab
            # in the block dropped P4's label and title silently. A second model
            # reading the extract reported the missing label as a chapter defect,
            # which sent a real markup fault to the author through the wrong door.
            for chunk in re.findall(r'<p[^>]*>.*?</p>', inner, re.S):
                cls = class_of(chunk[:chunk.find('>') + 1])
                text = inline(re.sub(r'\A<p[^>]*>|</p>\Z', '', chunk))
                if 'plab' in cls:
                    out.append('**%s.**' % text)
                elif 'ptitle' in cls:
                    out[-1] = '%s %s' % (out[-1], text)
                elif 'pnote' in cls:
                    out.append('*%s*' % text)
                elif text:
                    out.append(text)
        elif tag == 'div':
            # Layout container: re-scan its contents in place.
            pos = m.end()
            continue
        elif tag == 'p':
            if 'slot-label' in classes:
                out.append('## [%s]' % inline(inner).upper())
            elif 'provenance' in classes:
                out.append('*%s*' % inline(inner))
            elif 'part-label' in classes:
                out.append('%s' % inline(inner))
            elif 'pnote' in classes:
                out.append('*%s*' % inline(inner))
            else:
                text = inline(inner)
                if text:
                    out.append(text)
    return '\n\n'.join(out) + '\n'


def main(argv=None):
    ap = argparse.ArgumentParser(description=__doc__)
    ap.add_argument('chapter')
    ap.add_argument('--out', help='write here instead of stdout')
    args = ap.parse_args(argv)

    doc = open(args.chapter, encoding='utf-8').read()
    text = convert(doc)
    prose = '\n'.join(l for l in text.splitlines()
                      if l and not l[0] in '#>*[')
    words = len(re.findall(r'\S+', prose))
    if args.out:
        open(args.out, 'w', encoding='utf-8').write(text)
        print('%s  %d characters, about %d words of body prose'
              % (args.out, len(text), words))
    else:
        sys.stdout.write(text)
    return 0


if __name__ == '__main__':
    sys.exit(main())
