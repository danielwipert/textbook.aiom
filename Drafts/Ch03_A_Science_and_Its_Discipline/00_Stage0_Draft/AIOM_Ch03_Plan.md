# Chapter 3 plan: A Science and Its Discipline

Process v4, step 1 (Decision 77). For Dan's sitting 1: approve, or redirect.
Source of the outline: Consolidated Spec, "CHAPTER 3" (lines 647 to 684). This
plan does not restate the outline; it adds what drafting needs and the decisions
only Dan can make.

## The chapter in one line

AI Business Economics is the science; AI Operations Management is the discipline
that acts on it. Competency C4 (read a formal claim). No anchor theorem; the THM-004
trace is the set piece. Closes Part I.

## Slots

| Slot | Content | Source or object |
|---|---|---|
| 1 Opening case | FinOps Foundation rewrites its mission, Feb 19, 2026: "value of cloud" to "value of technology"; 98% of practitioners manage AI spend, up from 31% two years earlier; 1,192 practitioners surveyed; practitioner quote "Is your AI providing value? No one can answer that question yet." Mission rewrite and arc only; the full FinOps treatment stays in Ch14. Dated. | State of FinOps 2026 report (data.finops.org) and the Foundation's Feb 19, 2026 press release. **Grade C**: search coverage converges on every figure; no primary read yet. Fact check A must read both. |
| 2 Teaching body | 3.1 why name a science; 3.2 the THM-004 trace (Figure 3.1, a tree); 3.3 how to read a formal claim (conditions, scope, non-claims, falsification; the "word games" objection); 3.4 the discipline and the five functions (Figure 3.2, two layers); 3.5 the four borders as a table; 3.6 the five Founding Questions, verbatim from the Workplan's canonical table | Registry: THM-004 (certified) and its parents, LEM-020 among them. Borders: each neighbor's own definition, cited (candidates below). |
| 3 Craft section | The trace procedure, six numbered steps, fully worked on the THM-004 chain | Registry statements, verbatim |
| 4 Summary | As the spec lists | none |
| 5 Key terms | As the spec lists; AI Business Economics terms come from `AIOM_Inherited_Vocabulary.md`, never re-explained | Registry definitions |
| 6 Questions and problems | Three discussion questions; P1 worked trace on THM-004; P2 completion trace (decision 4); P3 the "word games" reply; then the Part I cumulative case on Klarna, Feb 2024 announcement only | Klarna/OpenAI announcement, Feb 2024, primary, Grade A in the case bank |

**Border sources, to confirm at drafting (all Grade C until read):** AIOps, the
Gartner glossary definition; MLOps, Kreuzberger, Kühl and Hirschl, "Machine
Learning Operations (MLOps): Overview, Definition, and Architecture," *IEEE
Access* (2023); FinOps, the FinOps Foundation's own definition and framework;
regulatory AI governance, one fence sentence with no claim needing a source.

**Continuity promises this chapter pays** (`AIOM_Continuity_Ledger.md`):
- Ch1 to Ch3: where each neighboring subject ends and AIOM begins. Paid by 3.5.
- Ch2 to Ch3: THM-004 formalizes the economic consequence of the third flow's
  asymmetry and does not establish the taxonomy itself. Paid by 3.2 and 3.3.
- Ch2 to Ch3: Chapter 3 names the discipline that resolves the category error.
  Paid by 3.4.

**Promises it makes:** each Founding Question to its answering chapter (7, 8 and
9, 10, 11, 12); the FinOps treaty to Ch14; the THM-008 unseen trace to Ch7's
assessment; the Klarna reveal to Ch6.

**Length:** in line with Chapters 1 and 2, about 7,000 to 7,500 words. Two
figures and one table.

## Prerequisite from Dan before drafting

**The registry bundle.** The repository holds only the manifest (names and
hashes), never the statements or the edges. The trace in 3.2, the craft section
and P1 and P2 quote registry statements verbatim (rule 4a), so drafting those
parts needs the bundle at `dag.aiom` commit `9d7ee50` or a newer one. Everything
else can be drafted without it.

## Decisions for Dan, each with a recommendation

1. **Registry counts in the prose.** The spec says "200 propositions, 20 lemmas,
   8 theorems"; the registry now holds 201, 21 and 11 (194, 20 and 9 certified),
   and will move again. **Recommend:** describe the structure in body prose with
   no counts (fifty-year rule), and put the dated counts, with the registry
   version, in one dated box.
2. **"Neither can most organizations on earth" (spec, 3.6).** An unsourced
   frequency claim (Decision 78). **Recommend:** replace with the opener's own
   evidence, the practitioner line "No one can answer that question yet," which
   is sourced and says the same thing more strongly.
3. **The Part I cumulative case lives in Chapter 3's Slot 6**, as the spec
   places it, rather than running a separate lifecycle in `Case_Part_I/`.
   **Recommend:** yes. It is one page of evidence and the same fact check covers
   it, which saves a whole extra round of steps.
4. **P2's theorem.** **Recommend:** THM-002 (certified), the spec's candidate,
   so the completion problem previews Chapter 5.
