> **STATUS: PROPOSED, NOT ADOPTED. AWAITING DAN'S RULING.**
>
> Would become **Decision 72**; `AIOM_Workplan_v5.md` is the numbering authority
> and settles it. Nothing here binds until ruled. Filed at the repository root
> because it is a live proposal, with this banner so a root file does not read as
> adopted.
>
> **Every number in this memo was computed from the bundle Dan supplied on
> 2026-08-19**, `dag.aiom` at `9d7ee504dfebdac70b5fbb8087177946e4cc4cdd`, not from
> the summary in CLAUDE.md. Where the two disagree, the bundle wins and the
> disagreement is named.

# Reconnecting the book to the AI Business Economics registry

Author: Claude, 2026-08-19. Third of three proposals raised this week, after the
Process v3 reorder and the continuous suite.

---

## 1. The headline: nothing published is wrong

**Chapter 1 cites exactly one registry ID, THM-009, and its panel is still
faithful.** Comparing the panel against the new `formal_statement`: four
antecedents, same order, same content, scope boundary rendered first per Decision
56. No antecedent added, dropped, merged, split, weakened or strengthened. THM-009
is certified in the new registry and its name is unchanged.

**The project's entire exposure is 28 IDs and 27 of them are certified.** Every one
resolves in the new registry. Nothing referenced anywhere in the repository has
been deleted or renumbered.

**All eight chapter anchor theorems exist and are certified**, including THM-004,
which Chapter 2 anchors on and which could have blocked drafting.

This is the result that determines urgency. **The registry change is additive, not
corrective.** No chapter must be repaired. What follows is about apparatus and
opportunity.

---

## 2. What actually changed

| | Locked Registry v1.3 | dag.aiom @ 9d7ee50 |
|---|---|---|
| Total nodes | 228 | **413** |
| Definitions | not modelled | **140** |
| Axioms | not modelled | **35** |
| Propositions | 200 | 201 |
| Lemmas | 20 | 21 |
| Theorems | 8 | **11** |
| Evidence | not modelled | **5** |
| Edges | a dependency graph, unversioned | **1,777, typed and weighted** |
| Status model | "Locked", asserted | **"Certified", derived by `validate.py`** |
| Identity | a workbook filename | **a git repo and a commit SHA** |

**The registry is now a versioned repository rather than a workbook.** The bundle
carries `source_repo` and `source_commit`. This is the single most useful change
for the book, because the version identity that never existed now exists for free.

**"Certified" replaces "locked", and it is DERIVED rather than asserted.** The
bundle's own contract says so: "No node carries a lock status. Certification under
`_computed` is derived by `scripts/validate.py` from the graph and is a snapshot at
`source_commit`." Uncertified nodes carry machine-readable blockers. THM-001 and
THM-003 both read "excluded from the proof graph (review_status provisional)".

**Uncertified across the corpus:** 2 theorems, 1 lemma, 7 propositions, 1 axiom,
and all 5 evidence nodes.

---

## 3. Four things the book has no apparatus for

### 3.1 Certification

The book's apparatus knows "Locked". It does not know "certified", it does not know
that certification is derived, and it cannot express a blocker. **Rendering an
uncertified object as "Theorem n" would claim more than the science claims.**

### 3.2 One hundred and forty definitions

These are the science's own vocabulary, not the book's coined terms: Cost, Fixed
cost, Marginal cost, Token, Input token, Seat-based pricing, Access pricing,
Consumption pricing, Metered pricing, and 131 more. **None of Chapter 1's four key
terms has a registry definition**, checked directly, so there is no collision.

**There is adjacency worth an editorial look.** The book coins "access price"
beside DEF-102 "Access pricing"; "software access model" beside DEF-108
"Seat-based pricing"; "resource consumption model" beside DEF-109 "Consumption
pricing" and DEF-110 "Metered pricing". Teaching terms that differ from the
science's terms are a legitimate choice. They should be a choice rather than an
accident, and nothing currently records which they are.

### 3.3 An evidence-need register

The five evidence nodes are not citations. They are a register of claims the
science says still need empirical support, with `status`, `blocking`,
`claim_supported`, `linked_node_id` and `suggested_source_types`. Two are BLOCKING.

**This couples the registry to the book's fact-check lane for the first time.**
Standing rule 2 requires every empirical claim to be cited, rewritten as a formal
conditional, or cut. The registry now states, in machine-readable form, which of
its own claims are not yet evidenced. A chapter leaning on one of those is leaning
on something the science itself has flagged.

### 3.4 A complete, typed dependency graph

1,777 edges: 1,082 `supports`, 500 `defines`, 194 `grounds`, 1 `requires_evidence`,
with necessity and weight on each. **Every trace is now generable.** THM-004 has
four direct parents (LEM-016, LEM-002, LEM-020, LEM-006) and 205 nodes within three
levels.

**This retires a recorded constraint.** CLAUDE.md says the registry ships a
pre-built trace for THM-005 only, that THM-005 is a Chapter 6 asset rather than
THM-004, and that Chapter 3's trace set piece "must be built separately". Figure
3.1 is now generable from the edge list like any other trace.

---

## 4. Findings that need attention

**4.1 LEM-015 is present and uncertified, not retired and absent.** CLAUDE.md
instructs: "LEM-015 is retired. Skip it explicitly. IDs run LEM-001 through LEM-021
with LEM-015 absent." In the new registry LEM-015 exists and is the corpus's one
uncertified lemma. **The operational instruction stays right and its stated reason
becomes wrong.** Under a certified-only rule it is skipped for a reason the build
can check, rather than by a note somebody has to remember.

**4.2 Chapter 1 makes a directional claim adjacent to an uncertified theorem, and
this is the most interesting finding in the bundle.** THM-001, "AI Pricing Tends
Toward Metered or Constrained Access", is uncertified and provisional. EVID-002 is
BLOCKING against it and its `claim_supported` reads: "AI access models tend toward
metering, caps, throttling, price increases, or cost reallocation under usage
pressure." Chapter 1's locked prose says: "The method may vary, but the direction
does not: what the customer receives becomes more closely tied to what the customer
consumes."

**Nothing is formally broken.** Chapter 1 does not cite THM-001, it cites THM-009,
which is about the character of the activity and is certified. The chapter derives
its directional sentence from the flat-rate mechanism it has just explained rather
than from the registry. **But the book is asserting in prose approximately what the
science currently marks provisional and unevidenced**, and no check in either
system can see that. This belongs to Dan and to the fact-check lane, not to Claude,
and it is raised here rather than acted on.

**Chapter 4 is the chapter most exposed to it.** Chapter 1 promises that "Chapter 4
examines these instruments in detail", and pricing trajectory is THM-001's
territory. Chapter 4 anchors on THM-007, which is certified, so the exposure is in
the surrounding argument rather than in the anchor.

**4.3 Appendix A's scope has moved.** It was specified as the 28 theorems and
lemmas reproduced in full, with the 200 propositions cited by ID. There are now 11
theorems and 21 lemmas, so 32 objects, or 29 if only certified ones are
reproduced. The 140 definitions and 35 axioms are a separate question the appendix
was never designed for.

**4.4 THM-011 is new, certified, and unassigned.** "Pilot Economics Do Not
Establish Production Economics." No chapter anchors on it. THM-003, "Frontier
Capability Does Not Imply Frontier Economic Suitability", is also unassigned and
is uncertified.

---

## 5. Track 1: connect and pin

Mechanical, and mostly collapsed by the bundle already carrying a commit SHA.

**5.1 Pin the version.** Record `source_repo` and `source_commit` in the repository.
This is the identity that has never existed, and without it no later session can
answer "which registry is this book built against".

**5.2 Derive a manifest, and do NOT commit the bundle.** Per object: ID, type,
certification, blockers, and a hash of the canonical statement. A few hundred lines,
diffable, and checkable offline.

**The bundle itself stays out of the repository, and the reason is rule 4a.** The
registry is upstream and the book is an interpretation of it. Committing 1.6MB of
registry into the book's repo creates a second copy of the authority, which is the
Decision 50 hazard with the added problem that the two are SUPPOSED to diverge
between bundle refreshes. A hash manifest can never be mistaken for the authority
because it does not contain the statements.

**5.3 Build the gate rule 4a always implied.** For every registry object the book
renders, compare the rendered panel against the registry statement, and fail when
the book renders an object that is uncertified or absent. **This is possible for
the first time**, and it closes the project's largest unguarded surface: the panel
promises a reader that the ID leads to the verbatim form, and until now nothing
checked that promise.

**5.4 Strike an obsolete constraint from CLAUDE.md.** Rule 4a states that the
workbook "is NOT in this repo, so no panel wording can be verified from a Claude
session". That was true when written. The Drive connector reads the project Drive
and Dan can supply a bundle directly, so it is now false, and it is the sentence
that has justified the absence of this gate.

---

## 6. Track 2: diff and replan

Judgment, and smaller than the object counts suggest.

**6.1 The blast radius is 28 IDs and it is fully enumerated in section 1.** Most of
a 413-node registry is invisible to the book, which cites by ID and renders almost
nothing. "The registry changed" is not "the book changed".

**6.2 Classify each future delta by what it forces**, which is the durable part of
this process and should outlive this particular bundle:

| Class | Remedy |
|---|---|
| Object the book never renders or cites | Nothing |
| A gloss in the continuity ledger moves | Ledger update, G3 check 4 owns it |
| A rendered panel's statement moves, chapter locked | `amend.py`, chapter stays Stage 9, Decision 56 governs the form |
| A chapter's anchor is retired or decertified | Chapter PLAN changes, never its structure. Rule 4 |
| The registry contradicts the book's argument | The only class that forces rethinking content |

**6.3 Nothing in this bundle falls in the last row.** That is worth stating plainly,
because it is the class everyone fears when a foundation moves.

**6.4 The replan is therefore about apparatus and opportunity**, in this order: the
certified-only rule, Appendix A's scope, whether the definitions become the
inherited-vocabulary source, whether THM-011 earns a home, and whether Chapter 4
needs to be planned around THM-001's provisional status.

---

## 7. What I recommend ruling

**A. The book renders certified objects only, and "certified" replaces "locked"
throughout.** Recommended. It is derived rather than asserted, it is mechanically
checkable, and it gives LEM-015 a reason a build can enforce instead of a note a
person must remember.

**B. Appendix A reproduces the certified theorems and lemmas**, which is 9 plus 20,
with uncertified objects listed by ID and status rather than reproduced.
Recommended, but it is a scope decision and the alternative of reproducing all 32
with status shown is defensible.

**C. The inherited-vocabulary source becomes the registry's 140 definitions.**
Recommended, and it closes a question already open from this morning: the
placed-vocabulary ledger sitting unadopted in `archive/` was meant to track exactly
this vocabulary by hand. Generating it from the registry is better than adopting
that file, because it cannot drift.

**D. Build the manifest and the panel gate now, before Chapter 2.** Recommended.
Chapter 2 anchors on THM-004 and will presumably render it in a panel as Chapter 1
rendered THM-009, which would make it the first chapter whose panel is checked
rather than trusted.

**E. Chapter 1's directional sentence and THM-001's provisional status go to the
fact-check lane**, not to an amendment made on Claude's reading. Recommended as a
referral, with Chapter 4's plan flagged at the same time.

---

## 8. What this proposal does not do

- **It does not touch the registry.** Rule 4a stands: a registry object is never
  edited to suit a chapter, and if a statement is wrong that is an AI Business
  Economics change, upstream of the book.
- **It does not restructure any chapter.** Rule 4 stands: the registry justifies
  the book and does not organize it.
- **It does not verify any empirical claim.** The evidence register says which
  claims the science still needs sources for. Sourcing them remains external, per
  the standing rule that no source host is reachable from this environment.
- **It cannot detect a restatement that preserves meaning**, nor one that changes
  meaning while the hash changes for innocent reasons such as punctuation. The
  manifest reports that a statement moved; a human rules what the move meant.

---

## 9. Reversal conditions

- **If the bundle turns out not to be the authority**, and the workbook lineage
  continues in parallel, the manifest pins the wrong thing and this should be
  re-derived from whichever artifact Dan rules canonical.
- **If certification proves unstable across bundles**, meaning objects flip
  certified and uncertified between commits for reasons unrelated to the book, then
  rule A gates the book on a moving target and should become advisory.
- **If the certified-only rule would exclude an object a chapter genuinely needs**,
  that is a signal to raise the object upstream, never to weaken the rule.
