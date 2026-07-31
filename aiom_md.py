#!/usr/bin/env python3
"""
aiom_md.py  |  version 1.0  |  2026-07-30

Enriched-markdown parser for the AIOM textbook.

The canonical source for a chapter is AIOM_chNN.md. This module turns one
chapter file into semantic HTML plus a manifest. It knows nothing about print
or web: the two Jinja2 templates and the two stylesheets carry that difference.

    from aiom_md import parse_chapter
    doc = parse_chapter("AIOM_ch01.md")
    doc.html       # semantic HTML for the templates
    doc.slots      # the six chapter slots, each as HTML
    doc.manifest   # cited objects, figures, problems
    doc.errors     # build blockers; an empty list means clean
"""

import re
import sys
import json
from dataclasses import dataclass, field

from markdown_it import MarkdownIt
from mdit_py_plugins.footnote import footnote_plugin
from mdit_py_plugins.deflist import deflist_plugin

# The fixed six-slot chapter skeleton. Detected from the H2 text, so the
# author never writes a directive for a slot.
SLOTS = [
    ("opening_case",  "Opening case"),
    ("teaching_body", "Teaching body"),
    ("craft_section", "Craft section"),
    ("summary",       "Chapter summary"),
    ("key_terms",     "Key terms"),
    ("problems",      "Discussion questions and problems"),
]

# Registry object directives and the ID prefix each one requires.
REGISTRY_KINDS = {"theorem": "THM", "lemma": "LEM", "proposition": "PROP"}
PLAIN_KINDS    = {"figure", "definition", "evidence", "problem", "provenance"}
DIRECTIVES     = set(REGISTRY_KINDS) | PLAIN_KINDS

FENCE = re.compile(r"^(```|~~~)")
OPEN  = re.compile(r"^:::[ \t]*([a-z]+)[ \t]*(.*?)[ \t]*$")
CLOSE = re.compile(r"^:::[ \t]*$")
ATTR  = re.compile(r"^([a-z_]+):[ \t]*(.*)$")


@dataclass
class Node:
    """A run of ordinary prose, or one ::: directive block."""
    kind: str            # "prose" or a directive name
    arg: str = ""        # the text after the directive name, e.g. "THM-009"
    body: str = ""       # raw markdown inside the block
    line: int = 0        # 1-based source line, for error messages


@dataclass
class Chapter:
    number: str = ""
    title: str = ""
    html: str = ""
    slots: dict = field(default_factory=dict)
    manifest: dict = field(default_factory=dict)
    errors: list = field(default_factory=list)


def scan(text):
    """Split source into prose runs and directive blocks. Fenced code is skipped."""
    lines = text.split("\n")
    nodes, buf, i, in_fence = [], [], 0, False

    def flush(at):
        if buf and "".join(buf).strip():
            nodes.append(Node("prose", body="\n".join(buf), line=at))
        buf.clear()

    while i < len(lines):
        line = lines[i]
        if FENCE.match(line):
            in_fence = not in_fence
        m = OPEN.match(line) if not in_fence else None
        if m:
            kind, arg, start = m.group(1), m.group(2), i + 1
            body, i = [], i + 1
            while i < len(lines) and not CLOSE.match(lines[i]):
                body.append(lines[i])
                i += 1
            flush(start)
            nodes.append(Node(kind, arg, "\n".join(body).strip(), start))
            i += 1
            continue
        buf.append(line)
        i += 1
    flush(len(lines))
    return nodes


def split_attrs(body):
    """Peel leading `key: value` lines off a directive body."""
    attrs, lines, k = {}, body.split("\n"), 0
    while k < len(lines):
        s = lines[k].strip()
        if not s:
            break
        m = ATTR.match(s)
        if not m:
            break
        attrs[m.group(1)] = m.group(2).strip()
        k += 1
    return attrs, "\n".join(lines[k:]).strip()


def split_head(body):
    """First paragraph is the title, the remainder is the statement."""
    parts = body.split("\n\n", 1)
    head = parts[0].strip().replace("\n", " ")
    rest = parts[1].strip() if len(parts) > 1 else ""
    return head, rest


def slug(s):
    return re.sub(r"[^a-z0-9]+", "-", s.lower()).strip("-")


def make_md():
    md = MarkdownIt("commonmark", {"typographer": True})
    md.enable(["table", "smartquotes"])
    md.use(footnote_plugin)
    md.use(deflist_plugin)
    return md


MD = make_md()


def block(src):
    return MD.render(src).strip() if src.strip() else ""


def inline(src):
    return MD.renderInline(src).strip() if src.strip() else ""


def render_registry(node, kind, errors, manifest):
    prefix = REGISTRY_KINDS[kind]
    oid = node.arg.strip().upper()
    if not oid:
        errors.append(f"line {node.line}: ::: {kind} has no object ID")
        return ""
    if not oid.startswith(prefix + "-"):
        errors.append(
            f"line {node.line}: ::: {kind} {oid} mismatched, "
            f"{kind} requires the {prefix}- prefix")
        return ""
    title, statement = split_head(node.body)
    if not statement:
        errors.append(f"line {node.line}: {oid} has a title but no statement")
    manifest["objects"].append(
        {"id": oid, "kind": kind, "title": title, "statement": statement})
    return (
        f'<section class="aiom-object aiom-{kind}" id="{oid.lower()}" '
        f'data-object="{oid}">\n'
        f'  <p class="aiom-object-label">'
        f'<span class="aiom-object-id">{oid}</span> '
        f'<span class="aiom-object-title">{inline(title)}</span></p>\n'
        f'  <div class="aiom-object-statement">{block(statement)}</div>\n'
        f'</section>')


def render_figure(node, errors, manifest):
    attrs, desc = split_attrs(node.body)
    num = node.arg.strip()
    if not num:
        errors.append(f"line {node.line}: ::: figure has no number")
        return ""
    cap, src = attrs.get("caption", ""), attrs.get("src", "")
    if not cap:
        errors.append(f"line {node.line}: figure {num} has no caption")
    manifest["figures"].append(
        {"number": num, "caption": cap, "src": src, "placed": bool(src)})
    inner = (f'<img src="{src}" alt="{cap}">' if src else
             f'<div class="aiom-figure-placeholder">{block(desc)}</div>')
    return (
        f'<figure class="aiom-figure" id="fig-{slug(num)}" data-figure="{num}">\n'
        f'  {inner}\n'
        f'  <figcaption><span class="aiom-figure-number">Figure {num}.</span> '
        f'{inline(cap)}</figcaption>\n'
        f'</figure>')


def render_definition(node, errors, manifest):
    term = node.arg.strip()
    if not term:
        errors.append(f"line {node.line}: ::: definition has no term")
        return ""
    manifest["definitions"].append(term)
    return (
        f'<aside class="aiom-definition" id="def-{slug(term)}" '
        f'data-term="{term}">\n'
        f'  <p class="aiom-definition-term">{inline(term)}</p>\n'
        f'  <div class="aiom-definition-body">{block(node.body)}</div>\n'
        f'</aside>')


def render_evidence(node, errors, manifest):
    attrs, body = split_attrs(node.body)
    tag, date = attrs.get("tag", ""), attrs.get("date", "")
    if not tag:
        errors.append(f"line {node.line}: ::: evidence has no tag")
    manifest["evidence"].append({"tag": tag, "date": date})
    return (
        f'<aside class="aiom-evidence" data-tag="{tag}" data-date="{date}">\n'
        f'  <p class="aiom-evidence-label">'
        f'<span class="aiom-evidence-tag">{inline(tag)}</span>'
        + (f' <span class="aiom-evidence-date">{date}</span>' if date else "")
        + f'</p>\n  <div class="aiom-evidence-body">{block(body)}</div>\n</aside>')


def render_problem(node, errors, manifest):
    label = node.arg.strip().upper()
    if not re.match(r"^P\d+$", label):
        errors.append(
            f"line {node.line}: ::: problem label {label or '(missing)'} "
            f"must look like P1")
        return ""
    title, body = split_head(node.body)
    manifest["problems"].append({"label": label, "title": title})
    return (
        f'<div class="aiom-problem" id="{label.lower()}" data-problem="{label}">\n'
        f'  <p class="aiom-problem-label">{label}</p>\n'
        f'  <p class="aiom-problem-title">{inline(title)}</p>\n'
        f'  <div class="aiom-problem-body">{block(body)}</div>\n'
        f'</div>')


def render_provenance(node, manifest):
    manifest["provenance"] += 1
    return f'<p class="aiom-provenance">{inline(node.body)}</p>'


H2 = re.compile(r"^##[ \t]+(.*)$")


def slot_for(heading):
    h = heading.strip().lower()
    for key, label in SLOTS:
        if h.startswith(label.lower()):
            return key
    return None


def parse_chapter(path, registry=None):
    text = open(path, encoding="utf-8").read()
    manifest = {"objects": [], "figures": [], "definitions": [],
                "evidence": [], "problems": [], "provenance": 0}
    errors = []
    doc = Chapter(manifest=manifest, errors=errors)

    m = re.search(r"^#[ \t]+(.*)$", text, re.M)
    if not m:
        errors.append("no H1 chapter title found")
    else:
        head = m.group(1).strip()
        mm = re.match(r"Chapter[ \t]+(\d+)\.?[ \t]*(.*)$", head, re.I)
        doc.number, doc.title = (mm.group(1), mm.group(2).strip()) if mm else ("", head)

    parts = {k: [] for k, _ in SLOTS}
    stream, current = [], None

    def emit(frag):
        if not frag:
            return
        stream.append(frag)
        if current:
            parts[current].append(frag)

    for node in scan(text):
        if node.kind == "prose":
            buf = []
            for line in node.body.split("\n"):
                hm = H2.match(line)
                key = slot_for(hm.group(1)) if hm else None
                if key:
                    emit(block("\n".join(buf)))
                    buf, current = [], key
                buf.append(line)
            emit(block("\n".join(buf)))
        elif node.kind in REGISTRY_KINDS:
            emit(render_registry(node, node.kind, errors, manifest))
        elif node.kind == "figure":
            emit(render_figure(node, errors, manifest))
        elif node.kind == "definition":
            emit(render_definition(node, errors, manifest))
        elif node.kind == "evidence":
            emit(render_evidence(node, errors, manifest))
        elif node.kind == "problem":
            emit(render_problem(node, errors, manifest))
        elif node.kind == "provenance":
            emit(render_provenance(node, manifest))
        else:
            errors.append(f"line {node.line}: unknown directive ::: {node.kind}")

    for key, label in SLOTS:
        if not parts[key]:
            errors.append(f"missing required slot: {label}")

    def dupes(vals):
        seen, out = set(), []
        for v in vals:
            if v in seen:
                out.append(v)
            seen.add(v)
        return sorted(set(out))

    for d in dupes([f["number"] for f in manifest["figures"]]):
        errors.append(f"duplicate figure number: {d}")
    for d in dupes([p["label"] for p in manifest["problems"]]):
        errors.append(f"duplicate problem label: {d}")

    if registry and manifest["objects"]:
        from aiom_registry import load_registry, verify
        errors.extend(verify(manifest["objects"], load_registry(registry)))

    doc.html = "\n\n".join(stream)
    doc.slots = {k: "\n\n".join(v) for k, v in parts.items()}
    return doc


if __name__ == "__main__":
    if len(sys.argv) < 2:
        sys.exit("usage: python3 aiom_md.py AIOM_chNN.md "
                 "[--registry registry.xlsx] [--html out.html]")
    reg = (sys.argv[sys.argv.index("--registry") + 1]
           if "--registry" in sys.argv else None)
    d = parse_chapter(sys.argv[1], registry=reg)
    mf = d.manifest
    print(f"Chapter {d.number}: {d.title}")
    print(f"  slots present ..... {sum(1 for k in d.slots if d.slots[k])}/6")
    print(f"  registry objects .. {len(mf['objects'])}"
          + (f"  {[o['id'] for o in mf['objects']]}" if mf["objects"] else ""))
    placed = sum(1 for f in mf["figures"] if f["placed"])
    print(f"  figures ........... {len(mf['figures'])} "
          f"({placed} placed, {len(mf['figures']) - placed} awaiting art)")
    print(f"  definitions ....... {len(mf['definitions'])}")
    print(f"  evidence boxes .... {len(mf['evidence'])}")
    print(f"  problems .......... {len(mf['problems'])}")
    print(f"  provenance lines .. {mf['provenance']}")
    print(f"  registry gate ..... "
          + ("verified against locked registry" if reg else "SKIPPED, no --registry"))
    print("\nPARSE " + ("PASSED" if not d.errors else "FAILED"))
    for e in d.errors:
        print("   " + e)
    if "--html" in sys.argv:
        out = sys.argv[sys.argv.index("--html") + 1]
        open(out, "w", encoding="utf-8").write(d.html)
        print(f"\nwrote {out}")
        open(out.replace(".html", ".manifest.json"), "w").write(
            json.dumps(mf, indent=2))
    sys.exit(0 if not d.errors else 1)
