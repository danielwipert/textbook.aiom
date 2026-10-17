#!/usr/bin/env python3
"""The author pass in markdown instead of Word, for Chapter 3 (Dan, 2026-10-17).

Chapter-local on purpose: tooling is frozen while a chapter is in flight
(Decision 79), so this wraps the shared pair rather than changing it.
copyedit_export.extract() supplies the blocks and the manifest is written in
the exporter's own format; copyedit_import.main() does all the matching and
applying, with only its reader swapped for read_md(). Every refusal the
importer makes for Word it makes here: a structure change, a split paragraph,
a span it cannot place uniquely, a registry-bound block.

The file is one paragraph per block, "[KIND] text", blocks separated by a
blank line. Line breaks inside a paragraph are joined, so an editor that wraps
lines does no harm. A paragraph without a tag after the first tag is a
continuation (an added paragraph or a split), exactly as read_docx treats it.

Run from the repo root:
    python3 .../md_author_pass.py export <chapter.html> --out <name>
    python3 .../md_author_pass.py import <name>.md <name>.manifest.json <chapter.html> [--apply]
"""
import argparse
import hashlib
import json
import re
import sys
from pathlib import Path

ROOT = Path(__file__).resolve().parents[3]
sys.path.insert(0, str(ROOT))
import copyedit_export as ce  # noqa: E402
import copyedit_import as ci  # noqa: E402

HEAD = """# {title}: author pass

Edit the prose freely. Three things to keep:

1. The bracketed tag at the start of each paragraph, such as [BODY]. It tells
   the importer what the paragraph is.
2. One blank line between paragraphs, and the order of the paragraphs.
3. Plain text: no markdown formatting (no asterisks, no #). Typographic quotes
   and apostrophes are fine.

Splitting a paragraph, merging two, or adding a new one is fine: the importer
detects it and the change is made by hand. Blocks tagged THEOREM render a
locked registry statement; edits inside them are not applied. Footnotes carry
their source keys in parentheses after the tag; edit the footnote text, not the
keys. The source register is not in this file. Read the PDF beside this file
for layout and figures.

---
"""


def export(html, out, title):
    blocks, fig_strings = ce.extract(html)
    lines = [HEAD.format(title=title)]
    for b in blocks:
        src = f"({b['sources']}) " if b.get("sources") else ""
        lines.append(f"[{b['kind']}] {src}{b['text']}")
        lines.append("")
    Path(out + ".md").write_text("\n".join(lines), encoding="utf-8")
    manifest = {
        "source_html": html,
        "source_format": "markdown",
        "block_count": len(blocks),
        "excluded": ["<section id=\"aiom-sources\">, the Decision 51 source "
                     "register: machine-read apparatus, deliberately not exposed "
                     "to a copy edit"],
        "figure_text_counts": [len(f) for f in fig_strings],
        "blocks": [{"i": i, "kind": b["kind"], "class": b["class"],
                    "tag": b["tag"], "sources": b.get("sources"),
                    "figure": b.get("figure"), "string": b.get("string"),
                    "span": b["span"],
                    "sha1": hashlib.sha1(b["text"].encode()).hexdigest(),
                    "text": b["text"]}
                   for i, b in enumerate(blocks)],
    }
    Path(out + ".manifest.json").write_text(
        json.dumps(manifest, indent=1, ensure_ascii=False), encoding="utf-8")
    print(f"{len(blocks)} blocks; wrote {out}.md and {out}.manifest.json")


def read_md(path):
    """(kind, sources, text, continuations) per tagged paragraph, as read_docx."""
    raw = Path(path).read_text(encoding="utf-8")
    body = raw.split("\n---\n", 1)[1] if "\n---\n" in raw else raw
    out = []
    for para in re.split(r"\n\s*\n", body):
        t = re.sub(r"\s+", " ", para).strip()
        if not t:
            continue
        m = ci.TAG_RE.match(t)
        if not m:
            if out:
                out[-1][3].append(t)
            continue
        kind, rest, sources = m.group(1).strip(), m.group(2).strip(), ""
        if kind in ci.SOURCED_KINDS:
            s = ci.SOURCES_RE.match(rest)
            if s:
                sources, rest = s.group(1).strip(), s.group(2).strip()
        out.append((kind, sources, rest, []))
    return out


def main():
    if len(sys.argv) > 1 and sys.argv[1] == "import":
        ci.read_docx = read_md
        sys.argv = [sys.argv[0]] + sys.argv[2:]
        return ci.main()
    ap = argparse.ArgumentParser()
    ap.add_argument("cmd", choices=["export"])
    ap.add_argument("html")
    ap.add_argument("--out", required=True)
    ap.add_argument("--title", default="Chapter 3, A Science and Its Discipline")
    a = ap.parse_args()
    export(a.html, a.out, a.title)


if __name__ == "__main__":
    sys.exit(main())
