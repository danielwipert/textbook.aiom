#!/usr/bin/env python3
"""
freqsweep.py  |  the frequency-claim sweep, Decision 78

Lists every sentence in a chapter that says how often something happens:
"organizations usually...", "most buyers...", "vendors rarely...". Each one is
an empirical claim, so standing rule 2 applies to it like any other: it is
cited, rewritten as a formal conditional, or cut.

WHY A LIST RATHER THAN A READ. On Chapter 2 no step owned these sentences. They
were swept at Stages 1, 4, 6 and 7, five times in all, and the render-only fact
check still found about a dozen, every one present since the draft. A reader
forgets a sentence; a list does not. Process v4 gives the sweep to the DRAFT
step: Claude clears the whole list before Dan sees the chapter, and runs it
again after the author pass, before the fact check.

IT REPORTS AND NEVER FAILS. Accurate qualification is not hedging (Prose
Standard section 13): "usage usually rises with headcount" can be required
precision rather than an unsourced claim. The list says where to look; the
disposition of each sentence is a judgment, and Dan rules it.

WHAT IT READS. Paragraphs, list items, table cells and block quotes, with the
Decision 51 source register, SVG, scripts, styles and footnote bodies removed.
Voiced material (case dialogue) is KEPT, because a quoted executive asserting
what "most firms" do is still a claim the chapter prints. Short blocks are kept
too: a one-line key-term definition can carry a frequency claim.

Usage:
    python3 freqsweep.py <chapter.html>
    python3 freqsweep.py <chapter.html> --count      # the number only
"""
import html
import re
import sys

import voicecheck as vc

# Words that assert a frequency or a prevalence. Deliberately broad: a false
# positive costs a glance, a false negative is the Chapter 2 failure.
FREQ = re.compile(
    r"\b("
    r"usually|commonly|often|oftentimes|frequently|typically|generally|"
    r"normally|routinely|ordinarily|customarily|habitually|"
    r"rarely|seldom|hardly ever|infrequently|occasionally|sometimes|"
    r"(?:almost|nearly|virtually) (?:always|never|every|all|no)|always|never|"
    r"tends? to|tended to|as a rule|in practice|in most cases|in many cases|"
    r"(?<!the )most|(?<!the )many|(?<!a )few|majority|minority|"
    r"common(?:ly)?|commonest|uncommon|rare|rarer|rarest|widespread|prevalent|pervasive|"
    r"standard practice|the norm|increasingly|more and more"
    r")\b", re.I)

BLOCK = re.compile(r"(?s)<(p|li|td|th|blockquote|h[1-4])\b([^>]*)>(.*?)</\1>")


def blocks(path):
    """(section, text) for every prose block, register and apparatus removed."""
    raw = open(path, encoding="utf-8").read()
    lines = raw.split("\n")
    in_register = vc.register_lines(lines)
    doc = "\n".join(ln for i, ln in enumerate(lines, 1) if not in_register[i])
    doc = re.sub(r"(?s)<(script|style|svg)\b.*?</\1>", " ", doc)
    doc = re.sub(r"(?s)<cite\b[^>]*>.*?</cite>", " ", doc)

    section = "(chapter opening)"
    for m in BLOCK.finditer(doc):
        tag, inner = m.group(1), m.group(3)
        text = html.unescape(re.sub(r"(?s)<[^>]+>", " ", inner))
        text = re.sub(r"\[[a-z0-9\-+ ]+\]", " ", text)      # citation keys
        text = re.sub(r"\s+", " ", text).strip()
        if not text:
            continue
        if tag.startswith("h"):
            section = text[:40]
            continue
        yield section, text


def sweep(path):
    """[(n, section, sentence, [matched words])] in reading order."""
    hits, n = [], 0
    for section, text in blocks(path):
        for s in vc.sentences(text):
            words = sorted({w.group(0).lower() for w in FREQ.finditer(s)})
            if words:
                n += 1
                hits.append((n, section, s, words))
    return hits


def main(argv):
    if not argv or argv[0].startswith("-"):
        print(__doc__)
        return 2
    hits = sweep(argv[0])
    if "--count" in argv:
        print(len(hits))
        return 0
    print("FREQUENCY SWEEP (Decision 78): %d sentence(s) to dispose of" % len(hits))
    print("Each is cited, rewritten as a formal conditional, or cut; or kept as")
    print("accurate qualification, which Dan rules. This list never fails.\n")
    for n, section, s, words in hits:
        print("F%-3d [%s]  %s" % (n, section, ", ".join(words)))
        print("      %s\n" % s)
    return 0


if __name__ == "__main__":
    sys.exit(main(sys.argv[1:]))
