#!/usr/bin/env python3
"""
Stage 3 voice check. AIOM.

Magisterial register, mechanically testable parts:
  - zero em dashes
  - zero contractions
  - zero question marks outside discussion prompts
  - third person in body prose; first or second person only inside
    marked voiced material (Decision 42)

Voiced material is marked either by a block class (model, dq, problem)
or by enclosing quotation marks.

Usage: python3 voicecheck.py AIOM_ch01.html
"""
import re
import sys

VOICED_CLASSES = ("model", "dq", "dq-b", "dq-n", "dq-list", "problem")

PERSON = re.compile(r"\b(I|we|our|us|you|your|yours|ourselves|yourself)\b")
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


def analyse(path):
    raw = open(path, encoding="utf-8").read()
    lines = raw.split("\n")

    # Track whether each line sits inside a voiced block, by div depth.
    inside = [False] * (len(lines) + 1)
    depth = 0
    voiced_at = None
    for i, line in enumerate(lines, 1):
        opens = re.findall(r"<div\b[^>]*>", line)
        closes = len(re.findall(r"</div>", line))
        for tag in opens:
            cls = re.search(r'class="([^"]+)"', tag)
            depth += 1
            if voiced_at is None and cls and cls.group(1) in VOICED_CLASSES:
                voiced_at = depth
        inside[i] = voiced_at is not None
        depth -= closes
        if voiced_at is not None and depth < voiced_at:
            voiced_at = None

    findings = {"emdash": [], "contraction": [], "question": [], "person": []}

    for i, line in enumerate(lines, 1):
        text = re.sub(r"(?s)<[^>]+>", "", line)
        if not text.strip():
            continue

        for m in EMDASH.finditer(text):
            findings["emdash"].append((i, m.group(0), text[:90]))

        for m in CONTRACTION.finditer(text):
            findings["contraction"].append((i, m.group(0), text[:90]))

        if "?" in text and not inside[i]:
            findings["question"].append((i, "?", text[:90]))

        if inside[i]:
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
    print("STAGE 3 MECHANICAL:", "FAIL" if failed else "PASS")
    return 1 if failed else 0


if __name__ == "__main__":
    sys.exit(main())
