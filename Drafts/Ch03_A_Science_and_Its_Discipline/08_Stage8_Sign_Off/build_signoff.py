#!/usr/bin/env python3
"""Assemble the Chapter 3 sign-off package (Sitting 4): the render and a diff.

Stage 8 of Process v4: "Claude sends the render plus a short diff of
everything that changed since the author pass." The diff is taken block by
block (the same extraction the author pass used), between the commit that
closed the author pass and the current text, and split by the step that made
each change, so every change can be traced to a ruling.

Run from the repo root:
    python3 Drafts/Ch03_A_Science_and_Its_Discipline/08_Stage8_Sign_Off/build_signoff.py
"""
import difflib
import shutil
import subprocess
import sys
import tempfile
from pathlib import Path

ROOT = Path(__file__).resolve().parents[3]
sys.path.insert(0, str(ROOT))
import copyedit_export as ce  # noqa: E402

HERE = Path(__file__).resolve().parent
LIVE = "Drafts/Ch03_A_Science_and_Its_Discipline/00_Stage0_Draft/AIOM_Ch03_draft.html"
PLACE_KINDS = {"SLOT", "CASE TITLE", "SECTION HEAD", "PROBLEM TITLE"}

# (commit that ends the phase, name, where its rulings are recorded)
PHASES = [
    ("b56819c", None, None),
    ("ae64f47", "Sitting 3, fact check",
     "checklist S3 lines; 04_Stage3_Fact_Check/AIOM_Ch03_Sitting3_rulings.md"),
    ("3599687", "Scoped re-review",
     "checklist SR lines; 02_Stage4_Review/AIOM_Ch03_Scoped_review_rulings.md"),
    (None, "Production (Stage 5, G2, G3)", "checklist P, G2 and G3 lines"),
]


def blocks_at(rev):
    if rev is None:
        r = ce.extract(str(ROOT / LIVE))
    else:
        raw = subprocess.run(["git", "show", f"{rev}:{LIVE}"], cwd=ROOT, check=True,
                             capture_output=True, text=True).stdout
        with tempfile.NamedTemporaryFile("w", suffix=".html", delete=False,
                                         encoding="utf-8") as f:
            f.write(raw)
        r = ce.extract(f.name)
    return [b for b in (r[0] if isinstance(r, tuple) else r) if b["kind"] != "FIGURE TEXT"]


def place(blocks, i):
    for j in range(min(i, len(blocks) - 1), -1, -1):
        if blocks[j]["kind"] in PLACE_KINDS:
            return blocks[j]["text"]
    return "Chapter opening"


def diff(old, new):
    out = []
    sm = difflib.SequenceMatcher(a=[b["text"] for b in old], b=[b["text"] for b in new],
                                 autojunk=False)
    for op, i1, i2, j1, j2 in sm.get_opcodes():
        if op != "equal":
            out.append((place(new, j1), old[i1:i2], new[j1:j2]))
    # A passage removed in one place and inserted unchanged in another moved
    # (place.py swaps a paragraph with a definition box); no words changed, so
    # it is reported as a move, not as an edit.
    removed = [x["text"] for _, b, _ in out for x in b]
    added = [x["text"] for _, _, a in out for x in a]
    moved = set(removed) & set(added)
    kept = []
    for sec, b, a in out:
        b = [x for x in b if x["text"] not in moved]
        a = [x for x in a if x["text"] not in moved]
        if b or a:
            kept.append((sec, b, a))
    return kept, len(moved)


def main():
    snaps = [blocks_at(rev) for rev, _, _ in PHASES]
    parts, total = [], 0
    for k in range(1, len(PHASES)):
        _, name, where = PHASES[k]
        changes, n_moved = diff(snaps[k - 1], snaps[k])
        total += len(changes)
        lines = [f"## {k}. {name}: {len(changes)} change(s)", "",
                 f"Rulings recorded in: {where}.", ""]
        if n_moved:
            lines += [f"Also {n_moved} passage(s) moved with no words changed "
                      "(a paragraph swapped order with a definition box).", ""]
        for n, (sec, before, after) in enumerate(changes, 1):
            kinds = sorted({x["kind"] for x in before + after})
            lines += [f"**{k}.{n}  {sec}**  ({', '.join(kinds).lower()})", ""]
            lines += ["Before:", ""] + [f"> {x['text']}" for x in before] + [""]
            lines += ["After:", ""] + [f"> {x['text']}" for x in after] + [""]
        parts.append("\n".join(lines))

    shutil.copy(ROOT / "build/Ch03.pdf", HERE / "AIOM_Ch03_Signoff_render.pdf")
    body = HEAD.format(total=total) + "\n\n".join(parts)
    for bad in ("\u2014", "\u2013"):
        assert bad not in body, "a dash in the package"
    out = HERE / "AIOM_Ch03_Signoff_diff.md"
    out.write_text(body, encoding="utf-8")
    print(f"wrote {out.name}: {total} changes; copied the render")


HEAD = """# Chapter 3 sign-off (Sitting 4): what changed since your author pass

Two files: this diff, and `AIOM_Ch03_Signoff_render.pdf`, the final 27-page
render (all fifteen print gates and all seventeen web gates pass).

Your author pass closed at commit b56819c. Since then, {total} passages
changed, every one by a ruling you made at a gate. They are listed below in
three groups, by the step that made them, each passage BEFORE and AFTER.
Layout-only changes (a definition box moved, Figure 3.2 moved and moved back,
two CSS rules) change no words and are not listed; they are in the checklist.

What you decide: approve the chapter as a whole, or name ONE structural
reason, and the chapter returns to the step that owns it. The full read
already happened in your author pass, so this is a check of the changes and
the render, not a second read.

"""


if __name__ == "__main__":
    main()
