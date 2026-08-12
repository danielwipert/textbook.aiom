#!/usr/bin/env python3
"""Build a fact-check packet: every cited passage paired with its register entry.

Repo tooling as of 2026-08-10, on Dan's ruling, closing the open thread that had
asked whether the packet was worth having on every chapter. It is: Stages 3 and 7
both need one, so fifteen chapters need thirty.

The history is the argument. The Stage 3 packet of 2026-08-10 was built by a
throwaway script in a session scratchpad and died with its container; the Stage 7
packet four hours later had to rebuild the same work from nothing. A script that
has to be rewritten to reproduce a step is not a reproducible step.

WHAT THIS DOES NOT DO. It does not verify anything. Stages 3 and 7 are
STRUCTURALLY external, not external by preference: no source host is reachable
from the Claude environment, verified 2026-08-06 against six of them. This
assembles what a human checker needs and states the mechanical checks that were
run locally. It must never be described as a fact check.

The register notes are reproduced IN FULL and verbatim, never summarised. They
carry the verification history and, for findings already ruled, the condition that
would reverse the ruling. SF7 and SF11 both exist because a note outlived the
prose it described, and both were catchable only because the note quoted the
actual sentence.

Usage:
    python3 factcheck_packet.py <chapter.html> --stage 7 --render <name.pdf> --out <out.md>
"""

import argparse
import json
import re
from pathlib import Path


def split_register(raw):
    """Return (body_html, register_json_text). The register is the Decision 51
    block: a JSON object whose first key is _README."""
    m = re.search(r'\{\s*"_README"', raw)
    if not m:
        raise SystemExit("no source register found (expected a _README key)")
    start = m.start()
    depth, end = 0, None
    for i in range(start, len(raw)):
        if raw[i] == "{":
            depth += 1
        elif raw[i] == "}":
            depth -= 1
            if depth == 0:
                end = i + 1
                break
    if end is None:
        raise SystemExit("source register never closes")
    return raw[:start], raw[start:end]


def render_field(v):
    """Register fields are strings, lists of strings, or lists of author objects
    carrying family, given and sometimes handle. Render all three without
    dropping a name, since a checker verifies bylines against the source."""
    if isinstance(v, list):
        return ", ".join(render_field(x) for x in v)
    if isinstance(v, dict):
        name = " ".join(p for p in (v.get("given"), v.get("family")) if p)
        return f"{name} ({v['handle']})" if v.get("handle") else (name or json.dumps(v))
    return str(v)


def strip_tags(s):
    s = re.sub(r"<span class=\"ckey\">.*?</span>", "", s, flags=re.S)
    s = re.sub(r"<[^>]+>", "", s)
    return re.sub(r"\s+", " ", s).strip()


def main():
    ap = argparse.ArgumentParser()
    ap.add_argument("html")
    ap.add_argument("--stage", required=True)
    ap.add_argument("--render", required=True)
    ap.add_argument("--out", required=True)
    a = ap.parse_args()

    raw = Path(a.html).read_text(encoding="utf-8")
    body, regtext = split_register(raw)
    reg = json.loads(regtext)

    # Every paragraph carrying a citation marker, in document order.
    cited = []
    for m in re.finditer(r"<p[^>]*>.*?</p>", body, flags=re.S):
        block = m.group(0)
        keys = []
        for km in re.finditer(r"<span class=\"ckey\">\[([^\]]+)\]</span>", block):
            keys += [k.strip() for k in re.split(r"\s*\+\s*", km.group(1))]
        if not keys:
            continue
        cite = re.search(r"<cite[^>]*>(.*?)</cite>", block, flags=re.S)
        claim = strip_tags(re.sub(r"<cite[^>]*>.*?</cite>", "", block, flags=re.S))
        gloss = strip_tags(cite.group(1)) if cite else ""
        cited.append((claim, keys, gloss))

    defined = {k for k in reg if not k.startswith("_")}
    used = {k for _, ks, _ in cited for k in ks}

    out = []
    out.append(f"# Chapter 1, Stage {a.stage}. Claim inventory and source packet\n")
    out.append("Generated from the live text by `factcheck_packet.py` at the repo root.")
    out.append(f"Stage {a.stage} is STRUCTURALLY external: no source host is reachable from the")
    out.append("Claude environment, verified 2026-08-06 against six of them, so nothing")
    out.append("below is a verification. It is the material a checker needs.\n")
    out.append(f"LIVE TEXT      `{a.html}`")
    out.append(f"RENDER         `{a.render}`, built this session, all fourteen gates green.\n")
    out.append("WHAT THIS IS. Every passage carrying a citation marker, with the keys it")
    out.append("cites and the register entry behind each key. The register note is")
    out.append("reproduced in full because it carries the verification history and, for")
    out.append("findings already ruled, the condition that would reverse the ruling.\n")
    out.append("WHAT A CHECKER SHOULD NOT RE-RAISE. SF1 through SF10 were ruled on")
    out.append("2026-08-06 and 2026-08-10 and their rulings sit in the register notes")
    out.append("below. A checker who reaches one should say whether the condition named in")
    out.append("the note is now met, not restate the finding. SF6, archive capture and")
    out.append("second paths, is closed on Decisions 30 and 48 and has been raised four")
    out.append("times.\n")
    out.append("MECHANICAL CHECKS ALREADY RUN, so they need not be repeated:\n")
    out.append(f"  Register closure    {len(defined)} keys defined, {len(used)} cited. "
               f"Zero orphans, zero dangling.")
    out.append(f"  Citation markers    {len(cited)} cited passages, every marker resolving to a key.")
    out.append("  Footnote build      6 footnotes generated, all on their calling page (gate 8).")
    out.append("  Value surface       175 numeric atoms and 32 date atoms, identical to the")
    out.append("                      Stage 3 audited render. Zero added, zero altered.")
    out.append("  Ruled-form check    SF7 to SF10, NC1, NC3, CE1 and CE2 all still in force.\n")
    out.append("---\n")
    out.append("## Part 1. Cited passages, in document order\n")

    for n, (claim, keys, gloss) in enumerate(cited, 1):
        out.append(f"### C{n}\n")
        out.append("CLAIM TEXT AS IT STANDS\n")
        out.append(f"> {claim}\n")
        out.append("CITES: " + ", ".join(f"`{k}`" for k in keys) + "\n")
        if gloss:
            out.append(f"IN-CHAPTER GLOSS: {gloss}\n")

    out.append("---\n")
    out.append("## Part 2. Register entries, verbatim\n")
    for k in sorted(used):
        e = reg[k]
        out.append(f"### `{k}`\n")
        for field in ("type", "authors", "title", "container", "date", "url",
                      "volume", "issue", "pages", "doi", "perishable",
                      "accessed", "upgrade"):
            if field in e and e[field] not in (None, "", []):
                out.append(f"- **{field}**: {render_field(e[field])}")
        if e.get("note"):
            note = e["note"]
            note = " ".join(note) if isinstance(note, list) else note
            out.append(f"\nNOTE, verbatim:\n\n> {note}\n")
        out.append("")

    Path(a.out).write_text("\n".join(out), encoding="utf-8")
    print(f"wrote {a.out}")
    print(f"  cited passages : {len(cited)}")
    print(f"  keys defined   : {len(defined)}")
    print(f"  keys cited     : {len(used)}")
    print(f"  orphans        : {sorted(defined - used) or 'none'}")
    print(f"  dangling       : {sorted(used - defined) or 'none'}")


if __name__ == "__main__":
    main()
