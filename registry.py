#!/usr/bin/env python3
"""
registry.py

The book's connection to the AI Business Economics registry. Decision 72.

WHAT THIS IS FOR. Rule 4a calls the registry the third rail: the book is an
interpretation of it, a registry object is never edited to suit a chapter, and the
ID in a theorem panel is a promise to the reader that they can follow it to the
verbatim form. Until 2026-08-21 nothing checked that promise, because the registry
lived upstream and no session could read it. That is now false, and this is the
check the rule always implied.

THE BUNDLE IS NEVER COMMITTED, AND THE MANIFEST IS. The registry is upstream and
committing it would put the authority in this repository twice, which is the
Decision 50 hazard with the added problem that the two are SUPPOSED to diverge
between refreshes. What is committed is a MANIFEST: per object, its ID, type,
certification, blockers, name, and a hash of its canonical statement. A manifest
carries no statements, so it can never be mistaken for the authority, and it is
enough to answer the only questions the book needs answered:

  1. Does every object a chapter renders or cites actually exist?
  2. Is it CERTIFIED? Decision 72 rules that the book renders certified objects
     only, because rendering a provisional one as "Theorem n" claims more than the
     science claims.
  3. Is the rendered theorem NAME character-identical to the registry's?
  4. Has the statement MOVED since the manifest was pinned?

CHECK 4 REPORTS, IT DOES NOT RULE. A statement hash changes for innocent reasons,
punctuation among them, and it changes for load-bearing ones. The manifest can say
that a statement moved; only a human can say what the move meant. This follows the
snapshot divergence warning's precedent.

Usage:
    python3 registry.py --bundle <bundle.json> --write-manifest
    python3 registry.py --bundle <bundle.json> --write-vocabulary
    python3 registry.py --check                 # every chapter, against the manifest
    python3 registry.py --check Ch01
"""

import argparse
import datetime
import glob
import hashlib
import json
import os
import re
import sys

MANIFEST = "AIOM_Registry_Manifest.json"
VOCABULARY = "AIOM_Inherited_Vocabulary.md"

ID_RE = re.compile(r"\b(THM|LEM|PROP|DEF|AX|EVID)-\d+\b")
# The theorem panel, as Decision 56 sets it: a label carrying the ID and a
# statement line carrying the registry's own name for the object.
PANEL_RE = re.compile(
    r'<p class="lab">(?P<lab>[^<]*?)</p>\s*<p class="stmt">(?P<stmt>.*?)</p>', re.S)


def canonical(node):
    """The statement a hash is taken over. Falls back down the layers so every
    node type hashes something rather than silently hashing nothing."""
    for k in ("formal_statement", "plain_statement", "definition_text",
              "claim_supported"):
        v = node.get(k)
        if v:
            return v.strip()
    return ""


def build_manifest(bundle_path):
    b = json.load(open(bundle_path, encoding="utf-8"))
    objects = {}
    for layer, items in b["nodes"].items():
        for x in items:
            comp = x.get("_computed") or {}
            stmt = canonical(x)
            objects[x["id"]] = {
                "type": layer,
                "certified": bool(comp.get("certified")),
                "blockers": comp.get("blockers") or [],
                "name": (x.get("name") or x.get("term") or
                         x.get("evidence_name") or "").strip(),
                "statement_sha256": hashlib.sha256(
                    stmt.encode("utf-8")).hexdigest() if stmt else "",
            }
    return {
        "manifest_version": 1,
        "note": "Derived from the registry bundle. Carries no registry "
                "statements: hashes only, so this file can never be mistaken "
                "for the authority. The registry is upstream (rule 4a).",
        "source_repo": b.get("source_repo"),
        "source_commit": b.get("source_commit"),
        "bundle_contract": b.get("contract"),
        "counts": b.get("counts"),
        "certified_counts": b.get("certified_counts"),
        "objects": dict(sorted(objects.items())),
    }


def load_manifest():
    if not os.path.exists(MANIFEST):
        sys.exit("no %s. Build it with --bundle <path> --write-manifest" % MANIFEST)
    return json.load(open(MANIFEST, encoding="utf-8"))


def chapter_files(target=None):
    out = []
    for d in sorted(glob.glob("Drafts/Ch*")):
        if target and not os.path.basename(d).startswith(target):
            continue
        stage0 = os.path.join(d, "00_Stage0_Draft")
        live = [p for p in glob.glob(os.path.join(stage0, "*.html"))
                if not os.path.basename(p).startswith(("DRAFT-", "_"))
                and not p.endswith(".print.html")]
        if live:
            out.append((os.path.basename(d), live[0]))
    return out


def cited_ids(html):
    """Every registry ID the chapter names, with the source register excluded so
    a bibliographic note cannot masquerade as a rendering."""
    body = re.sub(r'<div class="src-register".*?</div>\s*$', "", html, flags=re.S)
    return sorted(set(m.group(0) for m in ID_RE.finditer(body)))


def rendered_panels(html):
    """(id, rendered name) for each theorem panel."""
    out = []
    for m in PANEL_RE.finditer(html):
        ids = ID_RE.findall(m.group("lab"))
        if not ids:
            continue
        full = ID_RE.search(m.group("lab")).group(0)
        name = re.sub(r"<[^>]+>", "", m.group("stmt"))
        out.append((full, re.sub(r"\s+", " ", name).strip()))
    return out


def check(target=None):
    man = load_manifest()
    objs = man["objects"]
    print("Registry manifest: %s @ %s"
          % (man.get("source_repo"), (man.get("source_commit") or "")[:12]))
    print("  %d objects, %s certified"
          % (len(objs), sum(1 for o in objs.values() if o["certified"])))

    failures = []
    for chapter, path in chapter_files(target):
        html = open(path, encoding="utf-8").read()
        ids = cited_ids(html)
        panels = rendered_panels(html)
        print("\n%s  %d registry ID(s), %d panel(s)" % (chapter, len(ids), len(panels)))

        for i in ids:
            o = objs.get(i)
            if not o:
                failures.append((chapter, "%s is not in the registry" % i))
                print("  %-10s MISSING from the registry" % i)
                continue
            mark = "certified" if o["certified"] else "UNCERTIFIED"
            print("  %-10s %-11s %s" % (i, mark, o["name"][:52]))
            if not o["certified"]:
                # Decision 72: the book renders certified objects only. A citation
                # in prose is held to the same rule, because a reader following an
                # ID cannot tell rendering from citation.
                failures.append((chapter, "%s is uncertified (%s)"
                                 % (i, "; ".join(o["blockers"]) or "no blocker given")))

        for pid, name in panels:
            o = objs.get(pid)
            if not o:
                continue
            if name != o["name"]:
                failures.append((chapter,
                                 "panel %s renders a name the registry does not "
                                 "carry.\n      panel:    %s\n      registry: %s"
                                 % (pid, name, o["name"])))
            else:
                print("  panel %s name matches the registry exactly" % pid)

    if failures:
        print("\n" + "=" * 70)
        print("REGISTRY CHECK FAILED")
        print("=" * 70)
        for ch, msg in failures:
            print("  %s: %s" % (ch, msg))
        return 1
    print("\nREGISTRY CHECK PASSED")
    return 0


def write_vocabulary(bundle_path):
    """The inherited-vocabulary source, Decision 72 rule C.

    Generated from the registry's definition layer rather than maintained by
    hand. The style standard places an inherited term once, on first load-bearing
    use, and never re-explains it, which only works across fifteen chapters if
    something records what the science already names. That something is this, and
    generating it means it cannot drift from the registry.
    """
    b = json.load(open(bundle_path, encoding="utf-8"))
    defs = sorted(b["nodes"]["definition"],
                  key=lambda x: x.get("canonical_order") or x["id"])
    lines = [
        "> **GENERATED from the registry by `registry.py --write-vocabulary`.",
        "> Do not edit by hand.** Decision 72.",
        "",
        "# AIOM Inherited Vocabulary",
        "",
        "The registry's definition layer: the vocabulary AI Business Economics",
        "already owns. **These are not the book's coined terms.** A coined term",
        "lives in a definitional callout and in the key-term list; an inherited",
        "term is glossed in line once, at its first load-bearing use in the book,",
        "and then used freely and never re-explained.",
        "",
        "**Placement is recorded per chapter as chapters lock**, so a drafter can",
        "see what has already been placed. The column is empty until then, which",
        "is correct rather than incomplete: no chapter has placed anything yet.",
        "",
        "Source: `%s` @ `%s`." % (b.get("source_repo"), b.get("source_commit")),
        "",
        "| ID | Term | Tier | Placed in |",
        "|---|---|---|---|",
    ]
    for x in defs:
        lines.append("| %s | %s | %s |  |"
                     % (x["id"], x.get("term", ""), x.get("tier_name") or ""))
    open(VOCABULARY, "w", encoding="utf-8").write("\n".join(lines) + "\n")
    print("wrote %s: %d inherited terms" % (VOCABULARY, len(defs)))


def main():
    ap = argparse.ArgumentParser(description=__doc__)
    ap.add_argument("--bundle", help="path to a registry bundle JSON")
    ap.add_argument("--write-manifest", action="store_true")
    ap.add_argument("--write-vocabulary", action="store_true")
    ap.add_argument("--check", nargs="?", const="", metavar="ChNN")
    a = ap.parse_args()

    if not os.path.exists("web_templates/chapter.html.j2"):
        sys.exit("registry.py must run from the repository root")

    if a.write_manifest or a.write_vocabulary:
        if not a.bundle:
            sys.exit("--bundle is required to write the manifest or vocabulary")
        if a.write_manifest:
            man = build_manifest(a.bundle)
            # Stamped after the build rather than inside it, so the file is a
            # pure function of the bundle apart from this one line.
            man["generated"] = datetime.date.today().isoformat()
            open(MANIFEST, "w", encoding="utf-8").write(
                json.dumps(man, indent=1, ensure_ascii=False) + "\n")
            print("wrote %s: %d objects from %s @ %s"
                  % (MANIFEST, len(man["objects"]), man["source_repo"],
                     (man["source_commit"] or "")[:12]))
        if a.write_vocabulary:
            write_vocabulary(a.bundle)
        return 0

    if a.check is not None:
        return check(a.check or None)
    ap.error("give --check, --write-manifest or --write-vocabulary")


if __name__ == "__main__":
    sys.exit(main())
