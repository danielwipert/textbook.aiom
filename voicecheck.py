#!/usr/bin/env python3
"""
Stage 4 voice and craft check, plus the Stage 6 house-style counts. AIOM.

    python3 voicecheck.py <chapter.html>               everything
    python3 voicecheck.py <chapter.html> --voice-only  Stage 4 half only

THREE HALVES NOW, WHICH IS THE POINT OF THE FLAG. The mechanical checks below
are Stage 4 and decide that step. The HOUSE STYLE block is prose style guide
Part 8, ported 2026-08-12, and belongs to the STAGE 6 copy edit, not to Stage 4.
It is printed by default because a defect nobody prints is a defect nobody
fixes, and suppressed by --voice-only when running Stage 4 on work in progress.
The two verdicts print on separate lines and are never merged.

MECHANICAL (pass or fail). Magisterial register, testable parts:
  - zero em dashes
  - zero contractions
  - zero question marks outside discussion prompts
  - third person in body prose; first or second person only inside
    marked voiced material (Decision 42)

CRAFT METRICS (advisory, always). Proxies for four of the six craft criteria
in AIOM_Voice_and_Craft_v1.md:
  - sentence length distribution and longest uniform run   -> C4 rhythm
  - throat-clearing openers                                -> C3 economy
  - concrete-particular density                            -> C1 particulars
  - copula rate and nominalization density                 -> C3 economy
  - paragraphs closing on a trailing qualifier             -> C5 close

One printed number is NOT a proxy: the chapter word count, printed first under
the craft metrics. It is the Decision 33 measure, named at Ch1 DE6 on 2026-08-09,
and it is the only figure here that answers to a ruled band (6,500 to 7,500 for
Chapters 1 and 2). It is printed rather than enforced, because the band is
editorial judgment and G1 owns it.

These numbers never fail a run and never will. They are proxies, and a proxy
optimized against has stopped measuring. They inform the Stage 4 read; the
checklist criteria decide it. C2 (context and stakes) and C6 (the guard) have
no proxy here and are enforced by reading alone.

Chapter 1 sets the baseline band. Later chapters are read against it rather
than against an absolute threshold, because a craft-heavy chapter and a
proof-heavy chapter do not carry the same numbers.

Voiced material is marked either by a block class (model, dq, problem)
or by enclosing quotation marks. It is excluded from the craft metrics.

Usage: python3 voicecheck.py AIOM_ch01.html
"""
import html
import re
import statistics
import sys

VOICED_CLASSES = ("model", "dq", "dq-b", "dq-n", "dq-list", "problem")

# Paragraph classes exempt from the QUESTION-MARK ban only. They stay subject to
# every other prohibition, including the person check.
#
# The standing rule bans RHETORICAL questions, asked for effect with the answer
# implied and not expected. This check tests for a question mark outside a
# discussion block, which is a proxy for that rule and not the rule. Chapter 1
# section 1.4 sets out five diagnostic questions an organization must literally
# answer, introduced as "leaders must be able to answer five questions:". They
# are not rhetorical and the proxy could not tell the difference.
#
# Ruled 2026-08-08. The class carries NO CSS rules, so rendering is unchanged and
# no design-system re-run is triggered. The point is to narrow what the check
# reads as a violation by making the author's intent explicit IN THE SOURCE,
# never to widen what it tolerates: the ban still holds everywhere a paragraph
# does not carry one of these classes.
QUESTION_EXEMPT_P_CLASSES = ("diagnostic",)
EXEMPT_P_RE = re.compile(
    r'<p[^>]*\bclass="(?:[^"]*\s)?(?:%s)(?:\s[^"]*)?"'
    % "|".join(QUESTION_EXEMPT_P_CLASSES))

# Apparatus blocks whose inner paragraphs carry no class of their own, so
# SKIP_CLASSES cannot see them. A theorem's formal conditional is one sentence
# of stated antecedents and a consequent; it is a proof object, not running
# prose, and counting it as prose reports any section holding a theorem as
# rhythmically heavy. Found at Chapter 1 Stage 4, 2026-08-06, where it put
# section 1.3 at a mean of 23.1 words against a chapter mean of 17.6 on the
# strength of one 61-word sentence. Every chapter carries theorems, so the
# misreport would have travelled to all fifteen.
#
# The same defect class covers <aside class="definition"> bodies and key-term
# entries, which are also unclassed paragraphs inside a classed container.
# Those are NOT excluded here: extending the set moves the baseline band that
# Chapters 2 to 15 are read against, which is Dan's ruling to make, not a side
# effect of this fix. Adding "definition" and "kt" below is the whole change if
# he rules that way.
APPARATUS_BLOCKS = ("theorem",)

# SENTENCE-INITIAL FIRST AND SECOND PERSON WAS INVISIBLE UNTIL 2026-08-29.
# The pattern was case-sensitive and listed lowercase forms only, so "We know
# that..." and "You should record..." passed while "as we know" failed. That is
# backwards: the START of a sentence is the likeliest place for second person to
# appear in an instruction. Found while scoping these bans away from the source
# register, by a control that turned out to be passing for the wrong reason.
# CAPITALISED FORMS ARE LISTED EXPLICITLY RATHER THAN USING re.I, because
# case-insensitive \bus\b matches "US" in "the US market" and would fail a
# chapter for naming a country.
PERSON = re.compile(r"\b(I|we|our|us|you|your|yours|ourselves|yourself"
                    r"|We|Our|Us|You|Your|Yours|Ourselves|Yourself)\b")
CONTRACTION = re.compile(
    r"\b(don|doesn|didn|isn|aren|wasn|weren|can|couldn|wouldn|shouldn|won"
    r"|hasn|haven|hadn|it|that|there|he|she|they|we|you|I|who|what)"
    r"['\u2019](t|s|re|ve|ll|d|m)\b",
    re.I,
)
EMDASH = re.compile(r"\u2014|&mdash;|&#8212;")

# Known false positives: part labels, cited titles, italic tags.
FP = re.compile(r"Part I\b|Clarifying our pricing|Clarifying Our Pricing")


def voiced_spans(text):
    """Character ranges inside double quotation marks."""
    spans = []
    marks = [m.start() for m in re.finditer(r'["\u201c\u201d]', text)]
    for a, b in zip(marks[::2], marks[1::2]):
        spans.append((a, b))
    return spans


def in_span(pos, spans):
    return any(a <= pos <= b for a, b in spans)


def block_lines(lines, classes):
    """Which lines sit inside a block of one of `classes`, tracked by depth.

    Depth counts <div> and <aside> together, because the design system uses
    both as block containers: voiced material is div-based, definition
    callouts are asides.
    """
    inside = [False] * (len(lines) + 1)
    depth = 0
    marked_at = None
    for i, line in enumerate(lines, 1):
        opens = re.findall(r"<(?:div|aside)\b[^>]*>", line)
        closes = len(re.findall(r"</(?:div|aside)>", line))
        for tag in opens:
            cls = re.search(r'class="([^"]+)"', tag)
            depth += 1
            if marked_at is None and cls and cls.group(1) in classes:
                marked_at = depth
        inside[i] = marked_at is not None
        depth -= closes
        if marked_at is not None and depth < marked_at:
            marked_at = None
    return inside


def voiced_lines(lines):
    """Which lines sit inside a voiced block. Used by the prohibitions.

    Voiced material is exempt from the person check only. It is NOT exempt
    from the dash, contraction, or question-mark bans, which hold everywhere.
    """
    return block_lines(lines, VOICED_CLASSES)


def register_lines(lines):
    """1-indexed set: which lines fall inside the Decision 51 source register.

    THE PROSE BANS DO NOT APPLY TO THE REGISTER AND THE EM DASH BAN DOES. Added
    2026-08-29 after Chapter 2 quoted a real speaker verbatim in a `note` field
    and voicecheck failed the chapter on his contractions and his first person.
    **The note is the fact checkers' working record, not body prose**, and
    CLAUDE.md rules that quoting the source sentence in it is a CONTROL rather
    than a convenience: a checker that bans contractions there forbids quoting
    any human being who used one.

    **CHAPTER 1 PASSED THIS FOR MONTHS BY LUCK.** Its notes quote the BOOK's own
    sentences, and body prose bans contractions, so quoting it introduced none.
    Chapter 2 is the first chapter to quote an external speaker.

    Standing rule 1 is absolute and stays absolute: em dashes are still checked
    inside the register, which also matters because a register entry's page range
    must store a hyphen and `cite_format` turns these fields into footnotes a
    reader reads.
    """
    inside, depth = {}, 0
    for i, line in enumerate(lines, 1):
        if '<section id="aiom-sources"' in line:
            depth += 1
        inside[i] = depth > 0
        if depth > 0 and "</section>" in line:
            depth = 0
    return inside


def analyse(path):
    raw = open(path, encoding="utf-8").read()
    lines = raw.split("\n")
    inside = voiced_lines(lines)
    in_register = register_lines(lines)

    findings = {"emdash": [], "contraction": [], "question": [], "person": []}

    for i, line in enumerate(lines, 1):
        text = re.sub(r"(?s)<[^>]+>", "", line)
        if not text.strip():
            continue

        for m in EMDASH.finditer(text):
            findings["emdash"].append((i, m.group(0), text[:90]))

        if not in_register[i]:
            for m in CONTRACTION.finditer(text):
                findings["contraction"].append((i, m.group(0), text[:90]))

        if ("?" in text and not inside[i] and not in_register[i]
                and not EXEMPT_P_RE.search(line)):
            findings["question"].append((i, "?", text[:90]))

        if inside[i] or in_register[i]:
            continue
        spans = voiced_spans(text)
        for m in PERSON.finditer(text):
            if in_span(m.start(), spans):
                continue
            window = text[max(0, m.start() - 40): m.end() + 40]
            if FP.search(window):
                continue
            findings["person"].append((i, m.group(0), window.strip()))

    return findings


# --------------------------------------------------------------------------
# Craft metrics. Advisory only. See the module docstring.
# --------------------------------------------------------------------------

# Paragraphs shorter than this are apparatus (definition asides, captions,
# key-term glosses, stubs) rather than teaching prose, and are not measured.
MIN_PARA_WORDS = 20

THROAT = re.compile(
    r"^(it is (important|worth) (to note|noting)|it should be noted"
    r"|it is worth noting|note that|it is clear that|it is interesting"
    r"|in this (section|chapter)|this (section|chapter) (will|examines|looks)"
    r"|as (we|the reader) (will|shall) see|before (we|turning)"
    r"|there (is|are) (a|an|no|some|several|many)\b"
    r"|one (might|could|may) (say|argue|note))",
    re.I,
)

# A closing clause that lets the air out of the paragraph: the final
# comma-clause opens on a subordinator, a concessive, or a participle.
TRAILING_QUALIFIER = re.compile(
    r",\s+(which|although|though|while|since|because|unless|whereas|albeit"
    r"|however|except|given that|rather than|if\s|assuming|depending"
    r"|\w+ing)\b[^,]*[.!?]?$",
    re.I,
)

# A paragraph closing on apparatus rather than argument: a figure, chapter, or
# part cross-reference in the final sentence. Found by the Chapter 1 craft audit
# of 2026-08-05, which the TRAILING_QUALIFIER proxy was blind to because a
# cross-reference is not a subordinate clause. Cross-references are legitimate;
# ending a paragraph on one usually is not, because the reader is handed a
# pointer instead of the point.
XREF_CLOSE = re.compile(
    r"\b(Figure\s+\d+(\.\d+)?|Chapter\s+\d+|Part\s+[IVX]+)\b"
    r"[^.!?]*(\.\d+[^.!?]*)?[.!?]?$",
    re.I,
)

# Apparatus paragraph classes: labels, terms, provenance lines, and the like.
# Measured prose excludes them.
SKIP_CLASSES = {
    "lab", "term", "stmt", "date", "provenance", "slot-label", "part-label",
    "mlab", "plab", "ptitle", "pnote", "caption", "figcap",
}

COPULA = re.compile(r"\b(is|are|was|were|be|been|being)\b", re.I)
NOMINAL = re.compile(r"\b\w{4,}(tion|tions|ment|ments|ance|ence|ity|ities)\b",
                     re.I)
NUMERAL = re.compile(r"\b\d[\d,.]*\b")
# Capitalized word not opening a sentence: a proper-noun proxy.
PROPER = re.compile(r"(?<![.!?]\s)(?<!^)\b[A-Z][a-z]{2,}\b")

ABBREV = re.compile(r"\b(No|Dr|Mr|Ms|Mrs|Prof|St|vs|etc|Fig|Ch|pp|Inc|Co|Ltd"
                    r"|e\.g|i\.e)\.$")


def body_paragraphs(path):
    """Teaching-prose paragraphs as (section, text), apparatus removed.

    Sectioned, because a chapter-level average hides a weak section. The
    Chapter 1 audit of 2026-08-05 found a summary running at twice the
    chapter's mean sentence length with no short sentences at all, invisible
    in the chapter total.
    """
    raw = open(path, encoding="utf-8").read()
    lines = raw.split("\n")
    voiced = voiced_lines(lines)
    apparatus = block_lines(lines, APPARATUS_BLOCKS)
    kept = [ln for i, ln in enumerate(lines, 1)
            if not voiced[i] and not apparatus[i]]
    doc = "\n".join(kept)
    doc = re.sub(r"(?s)<(script|style|svg)\b.*?</\1>", " ", doc)
    # Footnote apparatus. A <cite> body becomes a numbered footnote at build
    # time, so it is not body prose and must not be measured as such: left in,
    # it reports a paragraph as closing on whatever the footnote closes on.
    doc = re.sub(r"(?s)<cite\b[^>]*>.*?</cite>", " ", doc)

    paras = []
    section = "(chapter opening)"
    for m in re.finditer(r"(?s)<(h[1-4]|p)\b([^>]*)>(.*?)</\1>", doc):
        tag, attrs, inner = m.group(1), m.group(2), m.group(3)
        text = re.sub(r"(?s)<[^>]+>", " ", inner)
        text = html.unescape(text)
        text = re.sub(r"\[[a-z0-9\-+ ]+\]", " ", text)   # citation keys
        text = re.sub(r"\s+", " ", text).strip()
        if not text:
            continue
        if tag != "p":
            section = text[:34]
            continue
        cls = re.search(r'class="([^"]*)"', attrs)
        cls = cls.group(1).strip() if cls else ""
        if cls in SKIP_CLASSES:
            continue
        if len(text.split()) >= MIN_PARA_WORDS:
            paras.append((section, text))
    return paras


def sentences(text):
    """Split on terminal punctuation, protecting decimals and abbreviations."""
    t = re.sub(r"(\d)\.(\d)", lambda m: m.group(1) + "\x00" + m.group(2), text)
    parts = re.split(r"(?<=[.!?])\s+", t)
    out, buf = [], ""
    for part in parts:
        cand = (buf + " " + part).strip() if buf else part
        if ABBREV.search(part.rstrip()):
            buf = cand
            continue
        buf = ""
        out.append(cand.replace("\x00", "."))
    if buf:
        out.append(buf.replace("\x00", "."))
    return [s.strip() for s in out if s.strip()]


def longest_uniform_run(lengths, spread=4):
    """Longest stretch of consecutive sentences within `spread` words."""
    best = best_at = 0
    start = 0
    for i in range(1, len(lengths) + 1):
        window = lengths[start:i]
        if max(window) - min(window) > spread:
            start += 1
            while max(lengths[start:i]) - min(lengths[start:i]) > spread:
                start += 1
        run = i - start
        if run > best:
            best, best_at = run, start
    return best, best_at


def section_table(paras):
    """Per-section rhythm, so a weak section cannot hide in a chapter average."""
    order, groups = [], {}
    for section, text in paras:
        if section not in groups:
            order.append(section)
            groups[section] = []
        groups[section].append(text)

    print("  [by section] a chapter average hides a weak section")
    print(f"         {'section':<34}{'par':>4}{'sent':>5}{'mean':>6}"
          f"{'stdev':>7}{'short%':>8}")
    for section in order:
        lens = [len(s.split()) for t in groups[section] for s in sentences(t)]
        if not lens:
            continue
        short = 100.0 * sum(1 for n in lens if n < 12) / len(lens)
        flag = ""
        if statistics.mean(lens) >= 28 or (short == 0 and len(lens) >= 4):
            flag = "  <- uniform and long"
        print(f"         {section[:34]:<34}{len(groups[section]):>4}"
              f"{len(lens):>5}{statistics.mean(lens):>6.1f}"
              f"{statistics.pstdev(lens):>7.1f}{short:>7.0f}%{flag}")


def chapter_words(path):
    """The Decision 33 measure, amended 2026-08-09 at Ch1 DE6.

    The whole chapter as rendered, excluding only the Decision 51 source
    register block and SVG label text. Citation notes ARE counted, because
    sources.py turns them into numbered footnotes the reader reads.

    This exists because the band was unusable without it. Decision 33 named a
    number and no measure, and Chapter 1 produced four defensible counts, two of
    which put it on opposite sides of the band. A hand-computed check is exactly
    the condition under which a green reading measures nothing.
    """
    src = open(path, encoding="utf-8").read()
    src = re.sub(r'(?s)<section id="aiom-sources">.*?</section>', " ", src)
    src = re.sub(r"(?s)<svg.*?</svg>", " ", src)
    src = re.sub(r"(?s)<head>.*?</head>", " ", src)
    return len(re.sub(r"<[^>]+>", " ", src).split())


def craft_metrics(path):
    paras = body_paragraphs(path)
    if not paras:
        print("CRAFT METRICS: no teaching-prose paragraphs found; skipped.")
        return

    sents, lengths = [], []
    for _, p in paras:
        for s in sentences(p):
            sents.append(s)
            lengths.append(len(s.split()))

    words = sum(lengths)
    per_k = lambda n: round(1000.0 * n / words, 1) if words else 0.0

    print("CRAFT METRICS (advisory, never a pass or fail)")
    print(f"  chapter: {chapter_words(path)} words "
          f"(Decision 33 measure: whole chapter less source register and SVG)")
    print(f"  corpus: {len(paras)} paragraphs, {len(sents)} sentences, "
          f"{words} words  (craft prose only, NOT the Decision 33 measure)")

    # C4, rhythm.
    run, at = longest_uniform_run(lengths)
    print("  [C4 rhythm]")
    print(f"         sentence words  mean {statistics.mean(lengths):.1f}  "
          f"median {statistics.median(lengths):.0f}  "
          f"stdev {statistics.pstdev(lengths):.1f}  "
          f"min {min(lengths)}  max {max(lengths)}")
    short = sum(1 for n in lengths if n < 12)
    long_ = sum(1 for n in lengths if n > 35)
    print(f"         short (<12w) {100.0*short/len(lengths):.0f}%   "
          f"long (>35w) {100.0*long_/len(lengths):.0f}%")
    print(f"         longest uniform run: {run} consecutive sentences "
          f"within 4 words")
    if run >= 6:
        print(f"           starts: {sents[at][:70]}")

    # C3, economy.
    throat = [s for s in sents if THROAT.match(s)]
    copulas = sum(len(COPULA.findall(s)) for s in sents)
    nominals = sum(len(NOMINAL.findall(s)) for s in sents)
    print("  [C3 economy]")
    print(f"         throat-clearing openers: {len(throat)}")
    for s in throat[:5]:
        print(f"           {s[:70]}")
    print(f"         copulas per 100 words: {100.0*copulas/words:.1f}")
    print(f"         nominalizations per 1,000 words: {per_k(nominals)}")

    # C1, concrete particulars.
    numerals = sum(len(NUMERAL.findall(s)) for s in sents)
    propers = sum(len(PROPER.findall(s)) for s in sents)
    print("  [C1 particulars]")
    print(f"         numerals per 1,000 words: {per_k(numerals)}")
    print(f"         proper nouns per 1,000 words: {per_k(propers)}")

    # C5, paragraph close. Two proxies: a trailing qualifier, and a close on
    # apparatus (a figure or chapter cross-reference) instead of on argument.
    weak, xref = [], []
    for i, (_, p) in enumerate(paras):
        ss = sentences(p)
        if not ss:
            continue
        if TRAILING_QUALIFIER.search(ss[-1]):
            weak.append((i, ss[-1]))
        if XREF_CLOSE.search(ss[-1]):
            xref.append((i, ss[-1]))
    print("  [C5 close]")
    print(f"         closing on a trailing qualifier: {len(weak)} of "
          f"{len(paras)}   (over-reports on causal closes)")
    for i, s in weak[:4]:
        print(f"           P{i}  ...{s[-66:]}")
    print(f"         closing on a cross-reference: {len(xref)} of {len(paras)}"
          f"   (hands the reader a pointer, not the point)")
    for i, s in xref[:4]:
        print(f"           P{i}  ...{s[-66:]}")

    print()
    section_table(paras)

    print("  [C2 context and stakes] no proxy exists. Read for it.")
    print("  [C6 the guard]          no proxy exists. Read for it.")


# --------------------------------------------------------------------------
# HOUSE STYLE, prose style guide Part 8.
#
# Ported 2026-08-12 from claude/chapter-1-prose-style-x0bzze, where these were
# written on 2026-08-05 against a 262-line version of this script and then
# stranded. This file is now 470 lines, so they were ported check by check
# rather than merged, and each one was verified by a NEGATIVE TEST: an injected
# violation must make it fail. A check that has only ever read green is not
# evidence that it measures anything, which this repo has now learned four
# times.
#
# These are SOURCE-level checks. Typography of the RENDERED artifact is gate 15
# in AIOM_build.py and reads the PDF, because the chapter's source register is
# JSON and legitimately carries straight quotes, and because footnotes are
# generated at build time. The two do not overlap: this one catches a straight
# quote a drafter types into prose, gate 15 catches one that reaches the page
# from the apparatus.
# --------------------------------------------------------------------------

PARA_MAX_WORDS = 150          # guide 8.3
FIGURE_BUDGET = 3             # guide 8.2
# "It is not X. It is Y", the chapter's signature antithesis.
ANTITHESIS = re.compile(
    r"(?:is|was|are|were|do(?:es)?|did)\s+not\b[^.]{0,90}\.\s*"
    r"(?:It|They|That|These)\s+(?:is|was|are|were)\b")
STRAIGHT = re.compile(r"['\"]")


def hs_strip(s):
    return re.sub(r"\s+", " ", re.sub(r"(?s)<[^>]+>", " ", html.unescape(s))
                  ).strip()


def prose_regions(raw):
    """Drop everything that is not running body prose.

    The source register, the problems section with its voiced material, model
    answers, the theorem panel, definition callouts, key terms, figure captions,
    SVG labels and citation apparatus all come out.
    """
    for pat in (r'(?s)<section id="aiom-sources">.*?</section>',
                r'(?s)<section class="problems-sec">.*?</section>',
                r'(?s)<section class="keyterms">.*?</section>',
                r'(?s)<div class="model">.*?</div>',
                r'(?s)<div class="theorem">.*?</div>',
                r'(?s)<aside class="definition">.*?</aside>',
                r"(?s)<figcaption>.*?</figcaption>",
                r"(?s)<svg.*?</svg>",
                r"(?s)<cite\b.*?</cite>"):
        raw = re.sub(pat, "", raw)
    return raw


def housestyle(path):
    raw = open(path, encoding="utf-8").read()
    body = prose_regions(raw)
    craft_at = body.find('<p class="slot-label">Craft section</p>')
    if craft_at < 0:
        craft_at = len(body)

    out = {"quotes": [], "longpara": [], "figure": [], "reader": [],
           "terminvar": [], "unstopped": []}

    # A prose block that does not close with terminal punctuation.
    #
    # Added 2026-08-31 at Chapter 2 Stage 5, after TWO full stops were lost in
    # the Stage 6 copy edit and reached the render. They survived the 195-block
    # import control, the Stage 7 packet and two external checks.
    #
    # THE IMPORT CONTROL COULD NOT SEE THEM AND THAT IS THE LESSON. It compares
    # the chapter against the returned .docx, and the .docx had dropped the
    # periods too, so the chapter matched its proof exactly. A control that
    # proves two artifacts agree is blind to a defect they share.
    #
    # Key-term NAMES and the dated box's own label are labels rather than
    # sentences, so they are excluded by requiring a verb-bearing length: a
    # block of fewer than five words is a label, not a sentence.
    for m in re.finditer(r"(?s)<p>(.*?)</p>", body):
        text = hs_strip(m.group(1))
        if len(text.split()) < 5:
            continue
        # Zero-width formatting characters are transparent to this test. A word
        # joiner is legitimately the last character of a block when it holds a
        # footnote marker to the sentence it belongs to, which is the Chapter 2
        # DR-C fix, and it is not punctuation.
        tail = text.rstrip("\u2060\u200b\ufeff")
        if tail and tail[-1] not in ".?!:;\u201d\u2019)":
            out["unstopped"].append(tail[-58:])

    # Body prose paragraphs carry no class attribute.
    for m in re.finditer(r"(?s)<p>(.*?)</p>", body):
        text = hs_strip(m.group(1))
        if len(text.split()) < 15:
            continue
        if len(text.split()) > PARA_MAX_WORDS:
            out["longpara"].append((len(text.split()), text[:70]))
        for q in STRAIGHT.finditer(text):
            out["quotes"].append(
                (q.group(0), text[max(0, q.start() - 32):q.start() + 28]))
        # "the reader" is permitted in the craft section, which addresses one.
        if m.start() < craft_at:
            for r in re.finditer(r"\bthe reader\b", text, re.I):
                out["reader"].append(text[max(0, r.start() - 30):
                                          r.start() + 45])
        # Scanned per paragraph, NEVER across the stripped body. Stripping
        # wholesale runs a heading into the paragraph beneath it and invents
        # sentence pairs that are not on the page.
        for a in ANTITHESIS.finditer(text):
            out["figure"].append(a.group(0).strip()[:78])

    # A defined term must read IDENTICALLY in its callout and its key term.
    # This is the check that would have caught CE3 on 2026-08-12, where "Meter
    # relocation" carried two different definitions past every gate. Gate 6
    # counts entries and header bands and read 8 and 8 throughout.
    defs = {}
    for d in re.finditer(r'(?s)<aside class="definition">(.*?)</aside>', raw):
        blk = d.group(1)
        t = re.search(r'<p class="term">(.*?)</p>', blk)
        ps = re.findall(r"(?s)<p>(.*?)</p>", blk)
        if t and ps:
            defs[hs_strip(t.group(1)).lower()] = hs_strip(ps[-1])
    for k in re.finditer(r'(?s)<div class="kt">(.*?)</div>\s*<p>(.*?)</p>',
                         raw):
        t = re.search(r'<span class="kt-t">(.*?)</span>', k.group(1))
        if not t:
            continue
        term = hs_strip(t.group(1)).lower()
        kt = hs_strip(k.group(2))
        if term in defs and defs[term] != kt:
            out["terminvar"].append((term, defs[term][:58], kt[:58]))
    return out


def report_housestyle(h):
    rows = [
        ("quotes", "Straight quotes or apostrophes in chapter prose", None),
        ("longpara", f"Paragraphs over {PARA_MAX_WORDS} words", None),
        ("figure", f"Antithesis figure (budget {FIGURE_BUDGET})",
         FIGURE_BUDGET),
        ("reader", "'the reader' in the teaching body", None),
        ("terminvar", "Defined terms differing from their key term", None),
        ("unstopped", "Prose blocks not closing with terminal punctuation", None),
    ]
    failed = False
    print("HOUSE STYLE (prose style guide Part 8)")
    for key, label, budget in rows:
        hits = h[key]
        over = len(hits) > budget if budget is not None else bool(hits)
        failed = failed or over
        print(f"[{'FAIL' if over else 'PASS'}] {label}: {len(hits)}")
        for item in hits[:6]:
            print(f"         {item}")
        if len(hits) > 6:
            print(f"         ... and {len(hits) - 6} more")
    return failed


def main():
    path = sys.argv[1] if len(sys.argv) > 1 else "AIOM_ch01.html"
    f = analyse(path)
    labels = {
        "emdash": "Em dashes",
        "contraction": "Contractions",
        "question": "Question marks outside discussion prompts",
        "person": "First or second person in unmarked body prose",
    }
    failed = False
    for key, label in labels.items():
        hits = f[key]
        status = "PASS" if not hits else "FAIL"
        if hits:
            failed = True
        print(f"[{status}] {label}: {len(hits)}")
        for line_no, token, ctx in hits:
            print(f"         L{line_no}  [{token}]  {ctx}")
    print()
    print("STAGE 4 MECHANICAL:", "FAIL" if failed else "PASS")
    print()
    # --voice-only suppresses the house-style half for work in progress, per
    # prose style guide 8.7. The Stage 4 mechanical result above is unaffected.
    if "--voice-only" not in sys.argv:
        hs_failed = report_housestyle(housestyle(path))
        failed = failed or hs_failed
        print()
        print("HOUSE STYLE:", "FAIL" if hs_failed else "PASS")
        print()
    craft_metrics(path)
    print()
    print("Craft criteria C1 to C6 are ruled on the Stage 4 checklist, not "
          "here.")
    return 1 if failed else 0


if __name__ == "__main__":
    sys.exit(main())
