# Chapter 3, sitting 2b: the external reviews, one list

Built 2026-10-06 from two independent reviews of `AIOM_Ch03_Review_package.md`:
the second model (`AIOM_Ch03_Review_secondmodel_review.md`, 26 findings, "E-n" below)
and a Sonnet subagent (`AIOM_Ch03_Review_thirdmodel_sonnet.md`, 24 findings, "S-n"
below, plus a second pass of 22 cited as "S2-n"). 72 findings merge into the items here. Claude checked each against the live
chapter before listing it. Dan rules; Claude applies in one commit.

## Part 1. Dismissed or already ruled (no action, listed so nothing is lost)

| Findings | Why no action |
|---|---|
| E-2, E-3, S-4 | Table 3.1 is in the chapter, all four rows. The extractor dropped it (fix-between list). |
| E-1 (first half), S-1 (first half) | Ruled at sitting 2: registry private, Appendix A reaches lemma level. Residual is item B2. |
| E-8 | P1 on LEM-020: ruled at sitting 2 (R-16). |
| E-10 | P2's preview of Part II: ruled earlier (ruling 4). |
| S-9 | "Part III takes them in a different order": Dan added it at sitting 2 (R-10). |
| E-3, S-17 | Regulatory governance in one sentence: standing ruling, and Table 3.1 now carries its "lacks" cell. |
| E-11, E-12 | "Not yet checked" provenance note and anonymous practitioner: the fact check settles both. The note is required until then. |
| S-23 | Aphorism; reviewer rated it noise. |

## Part 2. Decisions for Dan

| # | Findings | Question | Recommendation |
|---|---|---|---|
| A1 | E-13, E-14, S-3 (both reviewers' top three) | What does "meeting a condition" mean? 3.3 says a deployment with no instruments installed can meet all four; the craft section says a team that cannot cap its costs does not meet the third. | **Authority is scope, not a condition.** Keep 3.3's reading of the conditions. Rewrite craft step 4: a team that cannot cap its costs falls outside LEM-020's scope, so the theorem says nothing about it. Same logic as the pilot that fails condition (i). Two sentences change; no registry text changes. |
| A2 | E-16, E-23, S-12 | 3.1 is heavy: five object kinds, certification, validator and the dated box before any example. You ruled "keep" at sitting 2 (R-27), but both outside reviewers raised it. | **Keep your ruling, move only the dated six-number box** to the end of 3.2, where the reader has just seen the graph it counts. |
| A3 | E-17, E-26, S-16 | The fifth function ("holds value to account at a boundary") has no example and "boundary" is never defined. | **Add one constructed example, labelled as such, with no figures** (one deployment, one scope, one period, the question it must answer) **and a Key terms entry for value boundary.** |
| A4 | E-18, S-14 | The falsifying case and the answer to the "word games" objection are stated abstractly. | **Add one worked contrast** in 3.3: "big deployments need cost controls" applied to a one-team pilot, against what the formal conditions make the reader check first. |
| A5 | E-19, S-15 | THM-004 is walked three times (3.2, 3.3, craft section). | **Keep.** The outline orders it, and the chapter sits at about 6,400 words against a 6,000 floor. Put the authority finding first in the craft section. |

## Part 3. Plain fixes Claude applies as one batch (approve the batch)

| # | Findings | Fix |
|---|---|---|
| B1 | E-4, S-10 | In 3.2, show how LEM-020's three quoted propositions combine into its result (about four sentences), so the trace visibly produces something. |
| B2 | E-1, S-1, E-7 | Split the 3.1 sentence on tracing levels; give LEM-021's statement in P2 so the problem can be done from the chapter; note in the checklist that assessment 4 must supply THM-008's propositions. |
| B3 | E-15, S-13 (both chose it to cut first) | Cut the "One further limit is this book's" tail of the non-claims paragraph; keep "it does not establish the three-flow taxonomy". |
| B4 | E-6, S-5 | Key terms: add Proposition and Dependency (required and contextual). |
| B5 | E-5, S-7 | Trace procedure step 2: "State the scope, then restate each condition in plain words," so the rule matches the worked run. |
| B6 | E-20, S-11 | Say once what the validator checks (every dependency present, no circular chain) and what it does not (that each proposition is true). Accuracy, not style. |
| B7 | S-2 | "The registry records them for every claim, so a reader does not have to guess" assumes registry access. Rewrite so the reader derives non-claims from the statement. |
| B8 | S-6 | Cut "Diligence from the people running the deployment is no longer enough." THM-004 does not say it. |
| B9 | S-22, E-12, S2-9, S2-11 | FinOps border: derive it from what FinOps was built for (cloud billing). The practitioner quotation is used five times; keep it in the opening case and Table 3.1 only. |
| B10 | E-24, S-20, S-21 | Three paragraphs that close on a cross-reference or a vague line close on their own point instead; name the "two disciplines" in the Chapter 14 pointer. |
| B11 | E-21 | One sentence on what the five functions cover between them (a unit of capacity bought, budgeted, recorded, routed, judged). |
| B12 | E-22, E-25, S-24, E-26, S-18 | Voice: lead 3.3's necessity paragraph with the misreading; replace "formalizes the economic consequence of the third flow's asymmetry" (cut by B3 anyway); open 3.3 and the 3.5 set-aside paragraph on a business statement. |
| B13 | E-9, S-8, S-19 | Keep the set-asides and the parallel function openings (sitting 2 R-34); tighten the set-asides by a sentence each if B1 to B11 push the length up. |

| B14 | S2-3 | Question 4 (match flows to functions): tag each function in 3.4 with the flow it manages, one clause each, so the question tests something taught. |
| B15 | S2-4, E-6 | Give one contextual dependency as a worked line in the craft section, so P2 step 5 has a model. |
| B16 | S2-10 | "This is the hardest of the five" is unsupported: cut "hardest". "The FinOps practitioners ... could not yet perform" becomes what one practitioner reported. |
| B17 | S2-13, S2-16 | 3.1's "two managers hold opposite beliefs" is anchored to Chapter 1's Cursor buyer; 3.2's second paragraph leads with its business claim. |
| B18 | S2-19, S2-22 | "Nobody designed it to manage AI" is a historical claim about FinOps: it goes to the fact check with the founding date as its support, or is rewritten as "It was designed before AI spending existed at scale." Cut the ironic "speaking from inside the discipline" sentence. |
| noted | S2-6 | "Theorem 2" beside THM-002 in P2: noise; left for the production step. |

After the batch: the mechanical suite and `freqsweep.py` re-run, the review extract
is regenerated (with the table), Stage 4 closes, and the author pass begins.
