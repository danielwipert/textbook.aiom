#!/usr/bin/env python3
"""continuity.py  |  Gate G3, the continuity gate

G3 catches chapter-to-chapter drift here rather than at manuscript integration,
where the fix would mean reopening a locked chapter. It reads
AIOM_Continuity_Ledger.md and checks a chapter against it.

Checks, matching the G3 sub-boxes in the generated checklist:

  1. No term redefined that an earlier chapter already owns.
  2. Every forward reference this chapter makes is logged.
  3. Every forward reference assigned to this chapter is paid.
  4. Registry IDs logged; recurring glosses worded identically.
  5. Founding Question references match the canonical table exactly.
  6. Maturity ladder language consistent with the locked five-stage model.
  7. Northmoor figures diffed against generator output.

The ledger is the authority. When a chapter and the ledger disagree, the gate
fails and Dan rules; the gate never edits the ledger to make itself pass. The
one writing path is --update, run at Stage 9 on a chapter that has locked.

Usage:
    python3 continuity.py <chapter.html> --chapter 1
    python3 continuity.py <chapter.html> --chapter 1 --update
    python3 continuity.py --pay 2
"""
import argparse
import html as htmlmod
import os
import re
import sys

LEDGER = "AIOM_Continuity_Ledger.md"
NORTHMOOR_DIR = "Northmoor"

MARKERS = {
    "terms": "<!-- CONTINUITY:TERMS -->",
    "forward": "<!-- CONTINUITY:FORWARD -->",
    "registry": "<!-- CONTINUITY:REGISTRY -->",
    "northmoor": "<!-- CONTINUITY:NORTHMOOR -->",
    "log": "<!-- CONTINUITY:LOG -->",
}


def norm(s):
    """Collapse whitespace. Nothing else changes, matching aiom_registry.norm."""
    return re.sub(r"\s+", " ", str(s or "")).strip()


def strip_tags(s):
    return norm(htmlmod.unescape(re.sub(r"(?s)<[^>]+>", " ", s)))


# --------------------------------------------------------------------------
# Reading the ledger
# --------------------------------------------------------------------------

def read_ledger(path=LEDGER):
    if not os.path.exists(path):
        print(f"FATAL: {path} does not exist. G3 cannot run without it.")
        sys.exit(2)
    text = open(path, encoding="utf-8").read()

    def rows_above(marker):
        """Table rows sitting between the header rule and the marker."""
        i = text.index(marker)
        block = text[:i].rsplit("|---", 1)[-1]
        out = []
        for line in block.split("\n"):
            line = line.strip()
            if line.startswith("|") and not line.startswith("|--"):
                cells = [c.strip() for c in line.strip("|").split("|")]
                if any(cells):
                    out.append(cells)
        return out

    led = {k: rows_above(m) for k, m in MARKERS.items()}

    # Canonical invariants, parsed from section 1 rather than hard-coded, so
    # the ledger stays the single place they live.
    fq = {}
    for m in re.finditer(r"^\|\s*([1-5])\s*\|\s*([^|]+?)\s*\|", text, re.M):
        fq[int(m.group(1))] = norm(m.group(2))
    stages = {}
    for m in re.finditer(r"^\|\s*([1-5])\s*\|\s*(Unmanaged|Visible|Attributed"
                         r"|Governed|Accountable)\s*\|", text, re.M):
        stages[int(m.group(1))] = m.group(2)
    led["_fq"] = fq
    led["_stages"] = stages
    led["_text"] = text
    return led


# --------------------------------------------------------------------------
# Reading a chapter
# --------------------------------------------------------------------------

def read_chapter(path):
    raw = open(path, encoding="utf-8").read()
    raw = re.sub(r"(?s)<(script|style|svg)\b.*?</\1>", " ", raw)
    body = strip_tags(raw)

    # Key terms: the Slot 5 register is the authoritative list of what a
    # chapter defines. Inline definition callouts repeat a subset of it.
    terms = []
    for m in re.finditer(
            r'(?s)<div class="kt">.*?<span class="kt-t">(.*?)</span>.*?'
            r"<p>(.*?)</p>", raw):
        terms.append((strip_tags(m.group(1)), strip_tags(m.group(2))))

    # Forward references: a sentence naming a later chapter is a promise.
    forwards = []
    for sent in re.split(r"(?<=[.!?])\s+", body):
        for m in re.finditer(r"Chapter\s+(\d+)", sent):
            forwards.append((int(m.group(1)), norm(sent)))

    registry = sorted(set(re.findall(r"\b((?:THM|LEM|PROP)-\d{3})\b", body)))

    # Founding Questions and maturity stages, as quoted.
    fq_quotes = re.findall(r"Question\s+([1-5])\b", body)
    stage_words = re.findall(
        r"\b(Unmanaged|Visible|Attributed|Governed|Accountable)\b", body)

    numbers = re.findall(r"\b\d[\d,]*(?:\.\d+)?\b", body)

    return {"terms": terms, "forwards": forwards, "registry": registry,
            "fq": fq_quotes, "stages": stage_words, "numbers": numbers,
            "body": body}


def northmoor_values():
    """Every numeric literal the generated Northmoor data actually contains."""
    vals = set()
    if not os.path.isdir(NORTHMOOR_DIR):
        return vals
    for name in os.listdir(NORTHMOOR_DIR):
        if not name.endswith((".csv", ".md")):
            continue
        try:
            text = open(os.path.join(NORTHMOOR_DIR, name),
                        encoding="utf-8", errors="replace").read()
        except OSError:
            continue
        for tok in re.findall(r"\b\d[\d,]*(?:\.\d+)?\b", text):
            vals.add(tok.replace(",", ""))
    return vals


# --------------------------------------------------------------------------
# The gate
# --------------------------------------------------------------------------

def check(path, chapter, led):
    ch = read_chapter(path)
    fails, notes = [], []

    owned = {norm(r[0]).lower(): (r[1], norm(r[2]))
             for r in led["terms"] if len(r) >= 3}
    print(f"G3 continuity, Chapter {chapter}, against {LEDGER}")
    print(f"  ledger holds {len(owned)} owned term(s), "
          f"{len(led['forward'])} forward reference(s), "
          f"{len(led['registry'])} registry gloss(es)")

    # 1. Term redefinition.
    redefined = 0
    for term, definition in ch["terms"]:
        prior = owned.get(term.lower())
        if prior is None:
            continue
        prior_owner, prior_def = prior
        if str(prior_owner).strip() in (str(chapter), f"Ch{chapter}"):
            continue                       # this chapter already owns it
        if norm(definition) != prior_def:
            redefined += 1
            fails.append(
                f"term redefined: {term!r} is owned by chapter {prior_owner} "
                f"and is redefined here\n"
                f"       ledger:  {prior_def[:90]}\n"
                f"       chapter: {norm(definition)[:90]}")
        else:
            notes.append(f"{term!r} restated verbatim from chapter "
                         f"{prior_owner}; owner unchanged")
    print(f"  1. term redefinition ...... {redefined}")

    # 2. Forward references made are logged.
    logged = {(str(r[0]).strip(), norm(r[2])) for r in led["forward"]
              if len(r) >= 3}
    made = {(t, s) for t, s in ch["forwards"] if t != chapter}
    unlogged = [(t, s) for t, s in sorted(made)
                if (str(chapter), s) not in logged]
    print(f"  2. forward refs made ...... {len(made)}, {len(unlogged)} "
          f"not yet logged")
    if unlogged:
        notes.append("unlogged forward references are expected before lock; "
                     "run --update at Stage 9 to record them")
        for t, s in unlogged[:6]:
            notes.append(f"  to Ch{t}: {s[:88]}")

    # 3. Forward references assigned TO this chapter are paid.
    owed = [r for r in led["forward"]
            if len(r) >= 4 and str(r[1]).strip() in (str(chapter),
                                                     f"Ch{chapter}")
            and norm(r[3]).lower() != "paid"]
    print(f"  3. promises owed by Ch{chapter} ... {len(owed)} unpaid")
    for r in owed:
        fails.append(f"unpaid promise from chapter {r[0]}: {norm(r[2])[:100]}")

    # 4. Registry glosses.
    glossed = {norm(r[0]).upper(): norm(r[2]) for r in led["registry"]
               if len(r) >= 3}
    drift = 0
    for oid in ch["registry"]:
        if oid not in glossed:
            notes.append(f"{oid} cited, no gloss recorded yet; --update at lock")
            continue
        if glossed[oid].startswith("(gloss to be recorded"):
            drift += 1
            fails.append(f"{oid} carries the placeholder gloss in the ledger. "
                         f"--update wrote the row; a human writes the wording. "
                         f"Record the gloss as it appears in the chapter that "
                         f"first used it, then this gate checks later chapters "
                         f"against it.")
            continue
        if glossed[oid] and glossed[oid].lower() not in ch["body"].lower():
            drift += 1
            fails.append(f"{oid} gloss drift: the recorded wording does not "
                         f"appear in this chapter\n"
                         f"       ledger: {glossed[oid][:100]}")
    print(f"  4. registry glosses ....... {len(ch['registry'])} object(s), "
          f"{drift} drifted")

    # 5. Founding Questions quoted verbatim.
    fq_bad = 0
    for n, canonical in led["_fq"].items():
        if not canonical or canonical.lower().startswith("question"):
            continue
        stem = canonical.rstrip("?").split(",")[0]
        if len(stem) > 25 and stem.lower() in ch["body"].lower():
            if canonical.lower() not in ch["body"].lower():
                fq_bad += 1
                fails.append(
                    f"Founding Question {n} appears but not verbatim\n"
                    f"       canonical: {canonical}")
    print(f"  5. Founding Questions ..... {fq_bad} misquoted")

    # 6. Maturity ladder language.
    canonical_stages = set(led["_stages"].values())
    stray = sorted({s for s in ch["stages"]} - canonical_stages)
    print(f"  6. maturity ladder ........ {len(set(ch['stages']))} stage "
          f"name(s) used, {len(stray)} outside the locked five")
    for s in stray:
        fails.append(f"maturity stage name not in the locked five: {s!r}")

    # 7. Northmoor figures.
    nm = northmoor_values()
    if not nm:
        print("  7. Northmoor figures ...... generator data not found, skipped")
        notes.append("Northmoor/ not readable; figure diff did not run")
    else:
        # Only chapters that name Northmoor carry its figures.
        if re.search(r"\bNorthmoor\b", ch["body"], re.I):
            printed = {n.replace(",", "") for n in ch["numbers"]}
            unknown = sorted(printed - nm, key=len, reverse=True)[:10]
            print(f"  7. Northmoor figures ...... {len(printed)} number(s), "
                  f"{len(unknown)} not found in generator output")
            for u in unknown:
                fails.append(f"number {u} printed in a Northmoor chapter but "
                             f"absent from generator output")
        else:
            print("  7. Northmoor figures ...... chapter cites no Northmoor "
                  "data")

    print()
    for n in notes:
        print("  NOTE  " + n)
    for f in fails:
        print("  FAIL  " + f)
    print("\nG3 " + ("PASSED" if not fails else "FAILED"))
    return not fails


# --------------------------------------------------------------------------
# Writing the ledger, at lock only
# --------------------------------------------------------------------------

def insert(text, marker, rows):
    i = text.index(marker)
    return text[:i] + "".join(r + "\n" for r in rows) + text[i:]


def update(path, chapter, led, date):
    ch = read_chapter(path)
    text = led["_text"]

    owned = {norm(r[0]).lower() for r in led["terms"] if r}
    new_terms = [f"| {t} | {chapter} | {d} |"
                 for t, d in ch["terms"] if t.lower() not in owned]

    logged = {(str(r[0]).strip(), norm(r[2])) for r in led["forward"]
              if len(r) >= 3}
    new_fwd = [f"| {chapter} | {t} | {s} | open |"
               for t, s in sorted({(t, s) for t, s in ch["forwards"]
                                   if t != chapter})
               if (str(chapter), s) not in logged]

    glossed = {norm(r[0]).upper() for r in led["registry"] if r}
    new_reg = [f"| {oid} | Ch{chapter} | (gloss to be recorded) |"
               for oid in ch["registry"] if oid not in glossed]

    log_row = (f"| {chapter} | {date} | {len(new_terms)} | {len(new_fwd)} | "
               f"{len(ch['registry'])} |")

    text = insert(text, MARKERS["terms"], new_terms)
    text = insert(text, MARKERS["forward"], new_fwd)
    text = insert(text, MARKERS["registry"], new_reg)
    text = insert(text, MARKERS["log"], [log_row])
    open(LEDGER, "w", encoding="utf-8").write(text)

    print(f"ledger updated for chapter {chapter}: {len(new_terms)} term(s), "
          f"{len(new_fwd)} forward reference(s), {len(new_reg)} registry "
          f"object(s)")
    if new_reg:
        print("  record the gloss wording by hand for each registry object; "
              "the placeholder is deliberate, not a default to leave in place")
    return True


def pay(chapter, led):
    text = led["_text"]
    out, n = [], 0
    for line in text.split("\n"):
        stripped = line.strip()
        if stripped.startswith("|") and not stripped.startswith("|--"):
            cells = [c.strip() for c in stripped.strip("|").split("|")]
            if (len(cells) == 4 and cells[1] in (str(chapter), f"Ch{chapter}")
                    and cells[3].lower() == "open"):
                cells[3] = "paid"
                line = "| " + " | ".join(cells) + " |"
                n += 1
        out.append(line)
    open(LEDGER, "w", encoding="utf-8").write("\n".join(out))
    print(f"{n} promise(s) to chapter {chapter} marked paid")
    return True


def main():
    ap = argparse.ArgumentParser()
    ap.add_argument("chapter_html", nargs="?")
    ap.add_argument("--chapter", type=int, help="chapter number under test")
    ap.add_argument("--update", action="store_true",
                    help="append this chapter's entries; run at Stage 9 only")
    ap.add_argument("--pay", type=int, metavar="N",
                    help="mark promises owed by chapter N as paid")
    ap.add_argument("--date", default=None)
    a = ap.parse_args()

    led = read_ledger()

    if a.pay is not None:
        return 0 if pay(a.pay, led) else 1

    if not a.chapter_html or a.chapter is None:
        ap.error("give a chapter HTML file and --chapter N, or use --pay")

    if a.update:
        date = a.date
        if date is None:
            import datetime
            date = datetime.date.today().isoformat()
        return 0 if update(a.chapter_html, a.chapter, led, date) else 1

    return 0 if check(a.chapter_html, a.chapter, led) else 1


if __name__ == "__main__":
    sys.exit(main())
