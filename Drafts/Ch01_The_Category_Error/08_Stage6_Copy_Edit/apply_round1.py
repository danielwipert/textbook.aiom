#!/usr/bin/env python3
"""Apply the Stage 6 round-1 copy-edit return to the chapter HTML.

Run 2026-08-08. Kept as the record of HOW the return was applied, because the
return changed 59 of 155 blocks and copyedit_import.py refused 162 spans, so
this pass replaced it for one round. Method: span substitution against the
manifest. Blocks whose returned text matches the live text are skipped entirely,
so their inline markup survives; only changed blocks are rewritten, each into a
recorded character span. Nothing outside those spans can move, which is what
keeps the source register, both SVGs, and every structural wrapper provably
untouched.

  python3 Drafts/Ch01_The_Category_Error/08_Stage6_Copy_Edit/apply_round1.py [--apply]

Run from the repository root. Without --apply it writes a dry run beside itself.
"""
import sys, re, json, difflib, importlib.util, os

HERE = os.path.dirname(os.path.abspath(__file__))
ROOT = os.path.abspath(os.path.join(HERE, "..", "..", ".."))
DOCX = os.path.join(HERE, "AIOM_Ch1_CopyEdit_round1_returned.docx")
MAN  = os.path.join(HERE, "AIOM_Ch1_CopyEdit.manifest.json")
DRY  = os.path.join(HERE, "round1_dryrun.html")

spec = importlib.util.spec_from_file_location("ce", os.path.join(ROOT, "copyedit_export.py"))
ce = importlib.util.module_from_spec(spec); spec.loader.exec_module(ce)

TAG = re.compile(r"^\[([A-Z][A-Z ]+)\]\s*(?:\(([^)]*)\)\s*)?(.*)$", re.S)


def parse_docx():
    """Returned blocks, keeping the untagged continuation paragraphs.

    copyedit_import.py drops them, which is why a split paragraph loses
    everything after its first line there. This pass keeps them.
    """
    from docx import Document
    out = []
    for p in Document(DOCX).paragraphs:
        t = re.sub(r"\s+", " ", p.text).strip()
        if not t:
            continue
        m = TAG.match(t)
        if m:
            out.append({"kind": m.group(1).strip(), "sources": (m.group(2) or "").strip(),
                        "paras": [m.group(3).strip()] if m.group(3).strip() else []})
        elif out:
            out[-1]["paras"].append(t)
    return out


def load_manifest():
    man = json.load(open(MAN, encoding="utf-8"))
    man["source_html"] = os.path.join(ROOT, man["source_html"])
    return man

# ---------------------------------------------------------------- corrections
# Applied to returned paragraph text before it is written back. Every entry is
# asserted to hit exactly once, so a silent miss is impossible.
FIXES = [
    # grammar
    ("It cannot measure cost reliably; however, because one task",
     "It cannot, however, measure cost reliably, because one task"),
    ("It follows from Theorum 1: Deployed AI is a resource consuming operating activity, not merely access to software.",
     "It follows from Theorem 1: deployed AI is a resource-consuming operating activity, not merely software access."),
    ("Total consumption rises with the volume of work and as a deployment succeeds,",
     "Total consumption rises with the volume of work, and as a deployment succeeds,"),
    ("Anysphere (owner of Cursor) chief executive Michael Truell apologized and promised refunds",
     "Michael Truell, chief executive of Anysphere, the company behind Cursor, apologized and promised refunds"),
    ("These five practices are not unique to manufacturing.",
     "These practices are not unique to manufacturing."),
    ("and Chapter 3 explains where each ends and AI operations management begins.",
     "and Chapter 3 explains where each ends and AI Operations Management begins."),
    # missing terminal stops
    ("It does not include additional costs based on how much AI the organization actually uses",
     "It does not include additional costs based on how much AI the organization actually uses."),
    ("It is to reveal the work, consumption, and cost drivers that cannot be seen from the seat count alone",
     "It is to reveal the work, consumption, and cost drivers that cannot be seen from the seat count alone."),
    # claim scope, restoring Stage 3 approved wording (SF2)
    ("The change therefore fell hardest on the customers who used the product most, and many received very surprising and very large invoices.",
     "The change therefore fell hardest on the customers who used the product most, and charges arrived that they had not planned for."),
    # soft superlative, same shape as the Stage 3 SF1 cut
    ("OpenAI provided one of the clearest examples.",
     "OpenAI provided an early example."),
    # the chapter's owned term must be named in the prose that teaches it
    ("Flat pricing relocates the meter from the buyer to the provider. It does not abolish it.",
     "Flat pricing relocates the meter from the buyer to the provider. It does not abolish it. This is meter relocation."),
    # numeral style: prose spells out, arithmetic keeps numerals
    ("an AI coding assistant for 500 employees", "an AI coding assistant for five hundred employees"),
    ("The 500 employees do not consume", "The five hundred employees do not consume"),
    ("Two companies may each purchase 500 seats", "Two companies may each purchase five hundred seats"),
    ("The company buys 500 seats", "The company buys five hundred seats"),
    ("an AI coding assistant to 300 developers", "an AI coding assistant to three hundred developers"),
]
FIXES_MULTI = {  # substitutions permitted to hit more than once
    "It does not include additional costs based on how much AI the organization actually uses": 2,
}

# Key-term register name, corrected to sentence case.
KEYTERM_FIX = {"Metered Resource": "Metered resource"}

# Inline bold, by live block index: the exact substring to wrap on first use.
BOLD = {
    20:  ["access price"],
    21:  ["The software access model"],
    27:  ["the consumption event"],
    57:  ["meter relocation"],
    89:  ["The consumption-event inventory"],
    90:  ["Step 1: Enumerate the event types.", "Step 2: Identify the resource drivers.",
          "Step 3: Locate the meter.", "Step 4: State what the seat count conceals."],
    135: ["Event types:"],
    136: ["Resource drivers:"],
    137: ["Meter:"],
    138: ["What the seat count conceals:"],
}

# A <cite> element is nested INSIDE its body paragraph's span, so rewriting the
# paragraph destroys it. Each one is carried across and re-attached to the
# paragraph that now carries its claim. Default is the last paragraph of the
# block, which is where five of the six sat; live[10] is the exception, where
# the citation documents the execution contrast in the first paragraph.
CITE_TO_PARA = {10: 0}

# Ruled 2026-08-08: keep the live Decision 56 panel and its four registry
# antecedents. These live blocks are not overwritten from the return.
THEOREM_KEEP = {59, 60, 61, 62}

# The gloss the return added inside the consequent, relocated to its own
# paragraph after the panel, per the same ruling.
THEOREM_GLOSS = ("Software access describes how the buyer obtains the right to use the "
                 "capability. It does not describe how much of the underlying resource the "
                 "organization consumes or what that consumption costs.")


def norm(s):
    s = s.replace('’', "'").replace('‘', "'")
    s = s.replace('“', '"').replace('”', '"')
    return re.sub(r'\s+', ' ', s).strip()


def esc(s):
    return s.replace('&', '&amp;').replace('<', '&lt;').replace('>', '&gt;')


def main(apply=False):
    man = load_manifest()
    path = man['source_html']
    src = open(path, encoding='utf-8').read()
    live, _ = ce.extract(path)
    ret = parse_docx()

    # align returned blocks to manifest blocks by kind sequence
    sm = difflib.SequenceMatcher(a=[b['kind'] for b in man['blocks']],
                                 b=[b['kind'] for b in ret], autojunk=False)
    pairs = []
    for op, i1, i2, j1, j2 in sm.get_opcodes():
        if op == 'equal':
            pairs += list(zip(range(i1, i2), range(j1, j2)))
        elif op == 'delete':
            pairs += [(i, None) for i in range(i1, i2)]
        else:
            sys.exit(f"unexpected alignment op {op}; refusing to guess")

    # manifest index -> live index (live gained one block when Decision 56
    # split the theorem into p.cond + ol.ante + p.conseq)
    def L(i):
        return i if i < 61 else i + 1

    # This pass is a one-shot against the state the proof was exported from.
    # Once round 1 is applied the spans no longer describe the file, so refuse
    # rather than rewrite a chapter against stale offsets. Kept as the record of
    # how round 1 landed, not as a repeatable pass.
    drift = [i for i, b in enumerate(man['blocks'])
             if i != 61 and b['text'] != live[L(i)]['text']]
    if drift:
        sys.exit(f"refusing: {len(drift)} manifest block(s) no longer match the chapter. "
                 "Round 1 has already been applied (2026-08-08); re-export a fresh "
                 "proof with copyedit_export.py for the next round.")

    edits = []          # (start, end, replacement)
    report = []
    fixes_hit = {a: 0 for a, _ in FIXES}

    for i, j in pairs:
        li = L(i)
        blk = live[li]
        a, z = blk['span']

        if j is None:                                   # deleted block
            # widen to the whole element plus its blank line
            open_tag = src.rfind('<', 0, a)
            close_end = src.find('>', src.find('</', z)) + 1
            start = open_tag
            while start > 0 and src[start - 1] == '\n':
                start -= 1
            edits.append((start, close_end, ''))
            report.append(f"DELETE   live[{li}] {blk['kind']}: {blk['text'][:70]}")
            continue

        if li in THEOREM_KEEP:
            report.append(f"KEEP     live[{li}] {blk['kind']} (Decision 56 panel, ruled)")
            continue
        if blk['kind'] == 'FOOTNOTE':
            continue

        paras = list(ret[j]['paras'])

        if blk['kind'] == 'KEY TERM':
            paras = [KEYTERM_FIX.get(p, p) for p in paras]

        # apply corrections
        for k, p in enumerate(paras):
            for old, new in FIXES:
                if old in p:
                    paras[k] = p = p.replace(old, new)
                    fixes_hit[old] += 1

        if norm(' '.join(paras)) == norm(blk['text']):
            continue                                     # unchanged: keep live markup

        # figure captions keep their <span class="fignum"> and drop the
        # returned "Figure 1.N." prefix, so gate 12 still sees the number
        if blk['kind'] == 'FIGURE CAPTION':
            fignum = re.match(r'(Figure \d+\.\d+)', blk['text']).group(1)
            body = re.sub(r'^Figure \d+\.\d+\.?\s*', '', paras[0])
            inner = f'<span class="fignum">{fignum}</span>{esc(norm(body))}'
            edits.append((a, z, inner))
            report.append(f"CAPTION  live[{li}]")
            continue

        parts = [esc(norm(p)) for p in paras]

        cites = re.findall(r'(?s)<cite [^>]*>.*?</cite>', src[a:z])
        if cites:
            target = CITE_TO_PARA.get(li, len(parts) - 1)
            parts[target] = parts[target] + ''.join(cites)

        for phrase in BOLD.get(li, []):
            done = False
            for k, p in enumerate(parts):
                if phrase in p:
                    parts[k] = p.replace(phrase, f'<b>{phrase}</b>', 1)
                    done = True
                    break
            if not done:
                sys.exit(f"bold phrase not found in live[{li}]: {phrase!r}")

        if len(parts) == 1:
            inner = parts[0]
        else:
            cls = f' class="{blk["class"]}"' if blk['class'] else ''
            inner = f'</p>\n\n<p{cls}>'.join(parts)
        edits.append((a, z, inner))
        report.append(f"REWRITE  live[{li}] {blk['kind']} ({len(parts)} para)")

    # insert the relocated theorem gloss after the panel's closing </div>
    div_end = src.find('</div>', live[62]['span'][1])
    assert div_end > 0
    ins = div_end + len('</div>')
    edits.append((ins, ins, f'\n\n<p>{THEOREM_GLOSS}</p>'))
    report.append("INSERT   theorem gloss paragraph after panel")

    # verify every correction landed
    bad = [a for a, n in fixes_hit.items() if n != FIXES_MULTI.get(a, 1)]
    if bad:
        for a in bad:
            print(f"FIX MISS ({fixes_hit[a]}x): {a[:80]}")
        sys.exit("refusing to write: a correction did not land as expected")

    edits.sort(key=lambda e: e[0], reverse=True)
    for s, e, rep in edits:
        assert not (s < live[62]['span'][1] < e) or rep == '', "edit straddles theorem"
        src = src[:s] + rep + src[e:]

    print('\n'.join(report))
    print(f"\n{len(edits)} edits")
    if apply:
        open(path, 'w', encoding='utf-8').write(src)
        print(f"written: {path}")
    else:
        open(DRY, 'w', encoding='utf-8').write(src)
        print(f"dry run written to {DRY}")


if __name__ == '__main__':
    main(apply='--apply' in sys.argv)
