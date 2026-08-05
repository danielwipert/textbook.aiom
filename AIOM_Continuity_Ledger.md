# AIOM Continuity Ledger

Owner: Dan (Chorus AI Systems). Maintained by `continuity.py`, the G3 gate.
Created 2026-08-05.

## What this is

The book is written one chapter at a time over a long period. Continuity drift
is therefore the default, not the exception: a term acquires a second definition
three chapters after its first, a promise made in Chapter 1 is never paid, a
lemma gloss is reworded because the earlier wording was not in front of the
drafter. Every one of those is cheap to prevent and expensive to discover at
manuscript integration, where the fix means reopening a locked chapter.

This ledger is the record G3 checks against. It holds, per chapter:

- **Terms owned.** The chapter that first defines a term owns it. A later
  chapter may use the term freely and may not redefine it.
- **Forward references made.** A promise that some later chapter will do
  something. Each is logged here when the promising chapter locks and marked
  paid when the promised chapter locks.
- **Registry glosses.** The wording used for a registry object. A recurring
  object is glossed identically every time.
- **Northmoor figures used**, so a figure can be diffed against generator
  output rather than trusted.
- **Founding Question and maturity-stage references**, checked verbatim against
  the canonical wording in section 2 below.

## Policy

1. **The ledger is appended at Stage 9, on lock, not at draft time.** A chapter
   still moving would write entries that later have to be retracted.
2. **G3 runs before lock and reads this file.** It fails on a redefinition, an
   unlogged forward reference, an unpaid promise assigned to the chapter under
   test, a reworded registry gloss, or a misquoted Founding Question or stage
   name.
3. **Entries are never edited to match a new chapter.** If a later chapter needs
   a different definition, that is a decision for Dan, recorded as a decision,
   and the earlier chapter is reopened. The ledger does not bend to make a gate
   pass.
4. **`continuity.py --update` writes the entries**, so the ledger reflects what
   the chapter actually contains rather than what someone remembered.

Usage:

```bash
python3 continuity.py <chapter.html> --chapter 1            # G3 check
python3 continuity.py <chapter.html> --chapter 1 --update   # append at lock
python3 continuity.py --pay 2                               # mark promises to Ch2 paid
```

---

## 1. Canonical invariants

These are copied from locked sources and are the reference G3 checks quotations
against. They are not editable here: change the source, then change this.

### The Founding Questions (locked, Decision 22; source: Workplan v5)

| # | Question | Function | Answered in | Maturity stage |
|---|----------|----------|-------------|----------------|
| 1 | Are you paying for capability you do not need, or starving work that needs more? | Sourcing | Ch7 | Governed |
| 2 | What do you expect the AI flow to consume next period, and how will you know when it deviates? | Planning and budgeting | Ch10 | Governed |
| 3 | Who consumed what last month, in service of which work? | Metering and attribution | Ch8, Ch9 | Visible, then Attributed |
| 4 | When capacity is constrained, who decides what runs first, and by what rule? | Allocation | Ch11 | Governed |
| 5 | Where, exactly, does this AI flow pay for itself, and who is on the hook for knowing? | Value boundary | Ch12 | Accountable |

Structural device: posed at the end of Ch3, resolved once each across Ch7 to
Ch12, instrumentalized as the diagnostic in Ch13, re-asked as the ninety-day
plan's targets in Ch15.

### The maturity ladder (locked; source: AIOM_Maturity_Model_v1.md)

| Stage | Name | One-line test |
|---|---|---|
| 1 | Unmanaged | No Founding Question answerable with records. |
| 2 | Visible | The first half of Question 3: who consumed what. |
| 3 | Attributed | Question 3 fully answerable: in service of which work. |
| 4 | Governed | Questions 1, 2, and 4 answerable with records. |
| 5 | Accountable | Question 5 answerable: the flow answers for itself. |

Stage names are used exactly as written. "Governed" is cost governance in
THM-004's sense, and Chapter 13 fences off regulatory AI governance in one
sentence.

---

## 2. Terms owned

One row per term, owned by the chapter that first defines it. The definition is
recorded as given, whitespace normalized. A later chapter using the term does
not appear here; only the owner does.

| Term | Owner | Definition as given |
|---|---|---|

<!-- CONTINUITY:TERMS -->

---

## 3. Forward references

A promise that a later chapter will do something. Logged when the promising
chapter locks; marked paid when the promised chapter locks and G3 confirms the
promise was kept.

| From | To | Promise | Status |
|---|---|---|---|

<!-- CONTINUITY:FORWARD -->

---

## 4. Registry glosses

The wording used for each registry object cited in prose. A recurring object is
glossed identically every time it appears, so the reader meets one statement of
it rather than three paraphrases. Verbatim registry statements are verified
separately by `aiom_registry.py` against Locked Registry v1.3; this table
tracks the surrounding prose gloss.

| Object | First used | Gloss as given |
|---|---|---|

<!-- CONTINUITY:REGISTRY -->

---

## 5. Northmoor figures used

Every Northmoor number that appears in a chapter, so it can be diffed against
generator output rather than trusted. The generator is `Northmoor/northmoor_gen.py`.

| Chapter | Figure | Value as printed | Source file |
|---|---|---|---|

<!-- CONTINUITY:NORTHMOOR -->

---

## 6. Chapter log

One line per chapter as it locks, so the ledger's own currency is visible.

| Chapter | Locked | Terms owned | Forward refs made | Registry objects |
|---|---|---|---|---|

<!-- CONTINUITY:LOG -->
