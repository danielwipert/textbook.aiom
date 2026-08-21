> **STAGE 0 PLAN. Structure before content, per CLAUDE.md section 9.**
> Written 2026-08-21, before any prose. **One item blocks drafting and it is
> Dan's**: see section 7.

# Chapter 2: The Flow, Stage 0 plan

## 1. What the chapter must deliver

| | |
|---|---|
| Big idea | AI runs as three flows (usage, records, cost-and-value). Unmanaged flows degrade. Cost accrues by default, value only by design. |
| Competencies | **C2**: identify the three flows in any real deployment and diagnose which are unmanaged. **C3**: state the central asymmetry and derive its consequence, all of the cost and an unknown fraction of the value. |
| Anchor theorem | **THM-004**, "Scaled AI Deployment Requires Cost Governance for Economic Control". Certified in the pinned registry, hash `3ddd5475`. |
| Craft section | The three-flow mapping. **This is the chapter's most reused artifact**: the structure document marks it as a recurring diagnostic used across the book, so it is designed once here and interleaved later. |
| Word band | 6,500 to 7,500, Decision 33, whole rendered chapter less source register and SVG labels. |
| Owns | **"Flow"**. Chapter 1 deliberately does not define it, and G3 will hold Chapter 2 to defining it. |

## 2. What it inherits and may not redefine

Chapter 1 owns eight terms and `continuity.py` fails the build if Chapter 2
redefines any: category error, consumption event, resource consumption model,
software access model, access price, metered resource, flat-rate objection, meter
relocation.

**The consumption event is the hinge.** Chapter 1 established it as the basic unit.
Chapter 2's usage flow is the stream of those events, so the chapter builds on
Chapter 1's vocabulary rather than restating it. The prose standard's
inherited-vocabulary rule applies: placed once, used freely, never re-explained.

**One promise is outstanding.** The ledger records that problem sets begin reaching
back to earlier chapters in Chapter 2. The problem set must therefore include at
least one item that uses Chapter 1 material.

## 3. The six slots

**Slot 1, opening case.** A cited real deployment where the flows are visibly
uneven: usage running, records thin or absent, cost-and-value unreconciled.
**BLOCKED, see section 7.**

**Slot 2, teaching body.** In order, and the order matters because the coined term
must arrive after the mechanism per the prose standard:

1. What a flow is, built from the consumption event the reader already has.
2. The three flows, each shown before it is named: the work actually being done,
   the record of that work, and the money and value attached to it.
3. Why an unmanaged flow degrades rather than merely staying unmeasured.
4. The central asymmetry: cost accrues by default because the meter runs whether or
   not anyone watches, and value accrues only by design because nothing records it
   unless somebody builds the record.
5. The consequence, which is C3's teaching point: the organization carries **all**
   of the cost and an **unknown fraction** of the value. "Unknown" is the load
   bearing word, not "small".
6. THM-004 rendered as a structured conditional per Decision 56, with a plain
   English twin for every antecedent.

**Slot 3, craft section.** The three-flow mapping worksheet: a named deployment,
each flow traced, each diagnosed as managed, partly managed, or unmanaged, with the
evidence that settles it. Built here as an instrument, reused from Chapter 5 onward.

**Slot 4, chapter summary.**

**Slot 5, key terms.** Flow, usage flow, record flow, cost-and-value flow, and the
asymmetry term once named. Four to six terms, matching Chapter 1's density.

**Slot 6, discussion questions and problems.**
- The C2 assessment: a three-flow mapping on a cited real deployment, with a marked
  up flow diagram and a per-flow diagnosis.
- The C3 assessment, two parts: a prose derivation of why "unknown" is the damning
  word, and a spot-the-error on **three real quotes** of the claimed-as-realized,
  netting-against-access-price, and adoption-as-value types. **The three quotes
  need sourcing, see section 7.**
- At least one item reaching back to Chapter 1, per the ledger promise.

## 4. Figures

Two, provisionally. **Figure 2.1**, the three flows as parallel tracks over one
deployment, showing where each is instrumented and where it is not. **Figure 2.2**,
the asymmetry: cost accumulating continuously against value recorded only at the
points somebody built a record. Both must carry `.nb` on proper nouns and set their
labels in the print body family, which `tokenize_svg` remaps for the web.

## 5. What the chapter must carry from the first line

- `<html lang="en-US">`, never `lang="en"`. Decision 59, no CSS lever, no gate.
- `.nb` on every proper noun. Decision 58.
- The fixed six-slot skeleton, in order, no optional slots.
- A provenance line beneath the opening case title, dated or labelled constructed.
- **Concrete Management Prose from the first sentence**, not repaired at Stage 4.
  Business reality first, claim first, visible actors, ordinary business language,
  and every coined term after the mechanism it names.

## 6. What is different about drafting this chapter

Chapter 2 is the first chapter drafted with all of the following in force, and
**the proving question is whether they pay**:

- The prose standard binding from Stage 0, with the locked Chapter 1 as exemplar.
- Process v3, so the design review and G2 run after the copy edit, on frozen text.
- `chapter_check.py` holding every ticked step from the first commit.
- A registry check that verifies the THM-004 panel rather than trusting it.
- A ledger that can fail G3 on a redefined term or an unpaid promise.

Chapter 1 needed a full reopen from Stage 0 because its draft arrived in the wrong
voice. If Chapter 2 still needs a Stage 4 rewrite, the standard is not doing its
work at drafting time, and that is worth knowing on chapter two rather than nine.

## 7. What blocks drafting, and it is Dan's

**THE OPENING CASE IS NOT PROVISIONED, AND CLAUDE CANNOT SOURCE IT.**
`AIOM_Case_Bank_v1.md` carries shopping lists for Chapters 4, 5 and 6 and **none
for Chapter 2**. No source host is reachable from this environment, verified
against six hosts, so Stages 3 and 7 are structurally external and a new case
cannot be researched here.

Two entries in the bank are adjacent and neither is currently a Chapter 2 opening
case:

- **CASE 5.2, shadow AI and the invisible flow.** Its own note says the record
  flow's absence has a price and that unmetered activity is invisible to the
  management boundary. That is Chapter 2's argument almost exactly, but it is
  filed for Chapter 5 and is a pattern across sources rather than one deployment.
- **CASE 6.2, MIT NANDA, "The GenAI Divide".** Its placement line already reads
  "Ch2 or Ch6 teaching body", so it was anticipated as Chapter 2 material. It is a
  study rather than a deployment, so it can feed the teaching body but is a weak
  opening case for a chapter whose competency demands a named deployment.

**Three things are needed before Stage 0 prose begins:**

1. **The opening case.** A named, citable deployment where at least one flow is
   visibly unmanaged. Dan supplies it, or rules that CASE 5.2 or 6.2 is promoted,
   or rules the case constructed and labelled as constructed in the provenance line.
2. **The three real quotes** for the C3 spot-the-error problem, one of each error
   type. These are empirical claims and standing rule 2 applies to them.
3. **A ruling on whether the three flows are coined terms** with their own
   definitional callouts, or descriptive labels that need none. This changes the
   key-term count and the callout placement, so it is a structural question rather
   than a wording one.

Everything else in this plan can proceed on Claude's judgment.
