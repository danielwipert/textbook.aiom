# Stage 7 render verification, 2026-08-11

What Claude can and cannot do at this step. No source host is reachable from the
Claude environment, verified 2026-08-06 against six of them, so the source half of
external check 1 is recorded as received and is NOT confirmed here. What follows
is everything in that check that is decidable inside the repo: the two production
flags, the register-versus-prose diffs, and the arithmetic.

## The render

`AIOM_Ch1_Stage7_FactCheck_Input.pdf` in this folder, built 2026-08-11 from
`00_Stage0_Draft/AIOM_Ch01_redraft.html` at the post-CE2 state. 25 pages.

**All fourteen gates pass.** This also discharges a real exposure: G2 was ticked
2026-08-10 against the pre-CE1 state, and CE1 and CE2 are copy edits, which
re-run G2 under the scoped re-run matrix. The committed G2 render dated 2026-08-08
predates both. The gate suite has now run clean on the text as it actually stands.

```
1. right-margin overflow ... 0          8. footnotes ... 6 called, all on the calling page
2. em / en dashes ......... 0          9. dated evidence boxes ... 2 labelled, 2 rules
3. heads and folios ....... checked   10. problem labels ... 3 found, all with title
4. callout splits ......... 0         11. theorem panel ... 1 panel, 1 label, intact
5. font faces ............. 5         12. figures ... 2 captioned, in order, 2 referenced
6. key terms .............. 8 / 8     13. bottom margin ... 0 characters below
7. provenance ............. present   14. widows/orphans/stranded heads ... 0 / 0 / 0
```

## Production flag A, theorem conditions. PHANTOM.

All four antecedents render on page 9, inside the theorem panel, roman-numbered
(i) through (iv), in the structured-conditional form standing rule 6 requires. The
panel is unsplit and gate 11 passes.

The source carries them as `<ol class="ante">` with four `<li>` items at lines 188
to 193. The checker's HTML-to-text extraction dropped the `<li>` contents, leaving
"if:" butted against "then", which is exactly the reported symptom.

**This is the second independent tool to exhibit `<li>` blindness.** The first is
`copyedit_export.py`, where it is already logged as an open Stage 6 defect: "any
prose inside `<li>` is invisible to Stage 6." Two tools, one blind spot, and the
lines it eats are theorem antecedents, which under standing rule 4a are the least
paraphrasable content in the book. Treat this as a property of HTML text
extraction generally, not a quirk of one script. Consequence for Chapters 2 to 15:
never hand a fact checker the HTML.

## Production flag B, P3 table alignment. PHANTOM.

The table renders correctly on page 25. Four columns in the intended order, and
the student-blank column is the first one, under "EVENT TYPE", drawn as three fill
rules at x0 68.4 to 126.4, one per row. Confirmed three ways: the source carries
`<td class="blank"></td>` opening all three rows; the rendered body text begins at
x0 144.0, which is the "RESOURCE DRIVERS" column origin, not the "EVENT TYPE"
origin at x0 68.4; and the rasterized page shows the three blanks.

The checker wrote this flag as a conditional, asking whether the blank cells were
in the first column. They are.

**Caution for the next checker.** This flag would reproduce against the PDF too
under naive text extraction, because an empty cell contributes no text and the row
collapses leftward. It is disproved only by reading the page or the geometry.
Page 25 is also short by design: that is DR3a, the accepted cost of holding the
inventory table whole, already recorded and not a new defect.

## Flag 2, SF3. CONFIRMED REGRESSION.

Against the render:

- ruled at SF3 (2026-08-06): "began enforcing monthly premium-request allowances
  and letting customers pay for usage beyond them"  ABSENT
- current prose: "began charging Copilot customers for premium requests that
  exceeded a monthly allowance"  PRESENT

The register note quotes the ruled sentence verbatim and adds "Do not restore the
prior-state contrast without a pre-2025-06-18 GitHub pricing or documentation
artifact." The current sentence is a partial restoration of it.

**Same defect as SF8, on a second vendor.** SF8 was the copy edit reintroducing
"Cursor billed each additional request at API rates", an automatic-continuation
mechanism no source establishes. This reintroduces automatic charging on the
GitHub side, where the changelog says allowances were enforced and overage
required a spending limit defaulting to zero. The copy edit reaches for "the
vendor began charging" because it is shorter than "began enforcing allowances and
offered a paid overage", and it has now smuggled in an unsupported billing
mechanism twice. Both sources are scheduled for reuse in Chapters 4 and 11.

## Sweep of every ruled sentence quoted in the register. SF3 IS ALONE.

Run against body prose only, with the register block excluded so the notes cannot
self-match. Four ruled sentences are quoted in the register:

| Ruled sentence | In prose |
| :-- | :-- |
| "because subscribers used them more than the price had assumed" | yes |
| "began enforcing monthly premium-request allowances and letting customers pay for usage beyond them" (SF3) | **NO** |
| "On January 28, 2026, four months before that change, the company told investors..." | yes |
| "after which additional usage was priced at the same rates" (SF8) | yes |

So the repair of 2026-08-10 caught SF8, SF9 and SF10 and missed SF3, and nothing
else of this exact shape is outstanding. **RECOMMENDED AS A GATE.** Every instance
of this failure so far was recoverable only because a register note quoted the
ruled sentence, and the control has now failed once by being run by hand. The
check is about fifteen lines and generalizes to all fifteen chapters.

**The limit of that control, stated so it is not overestimated.** It sees only
claims that were once ruled with a quoted sentence. Flags 3, 4 and 5 below are
prose drifting broader than a register note on claims never ruled, and no
mechanical sweep can find them.

## Flags 3, 4 and 5. All present in the render, all decidable against the register.

- **Flag 3.** Prose: "annual subscribers kept their existing terms until their
  subscriptions expired". Register note for `github-2026-credits`: annual Pro and
  Pro+ subscribers "remain on premium-request pricing until their terms expire".
  The prose generalizes "premium-request pricing" to "existing terms". The
  checker's proposed fix is the register's own wording. The model-multiplier
  exception the checker cites is not in the register note and needs the source.
- **Flag 4.** Prose: "for every subscriber, regardless of renewal date". The
  register note for `techcrunch-2025-anthropic-limits` carries the August 28
  effective date and the Max overage and says nothing about renewal. Unsourced
  empirical claim under standing rule 2.
- **Flag 5.** Prose: "Customers on the highest-priced plan". Register: "Max
  subscribers". "Highest-priced plan" is an editorial characterization, and Max
  spans two price points.

**Flags 3 and 4 are coupled and must be ruled together.** Both clauses serve one
contrast: GitHub carved out its annual subscribers, Anthropic carved out nobody.
Narrowing flag 3 weakens the GitHub side and cutting flag 4 weakens the Anthropic
side, so ruling them independently could dissolve a contrast the paragraph is
built on.

## Flag 1. A prose defect before it is a source question.

The paragraph at page 12 describes what subscribers encountered and carries no
date in prose. The next paragraph opens "Eleven days later". The only date anchor
near it is inside the citation gloss and the "Dated: July 2025" box label, so a
reader is asked to count eleven days from nothing stated. That half is decidable
here and is a real defect.

The source half is not decidable here. Whether July 17 is the encounter or the
report of it requires the Brandom piece. Noted, though: the register for
`techcrunch-2025-anthropic-tightening` already records that Anthropic confirmed
the reports and declined to confirm a change, "which is why the chapter attributes
the tightening to what subscribers encountered rather than to a company action the
company acknowledged." If the encounter has no company-confirmed date, the chapter
is counting from a report and should say so.

Of the checker's two proposed remedies, "eleven days after the first reports"
keeps the precision and supplies the missing antecedent; "two weeks later" blurs
both. Judge the remedy separately from the finding, per Stage 3.

## Arithmetic re-verified

| Item | Result |
| :-- | :-- |
| 5,000 x 40 x 6 x 21 generations | 25,200,000 |
| retrievals, one per drafted reply | 25,200,000 |
| close operations, 5,000 x 40 x 21 | 4,200,000 |
| total | 54,600,000 |
| per seat, divided by 5,000 | 10,920, stated as "about 10,900" |
| June 16 to July 4, 2025 | 18 days, "less than three weeks" holds |
| June 16 to June 18, 2025 | 2 days, "two days after" holds |
| July 17 to July 28, 2025 | 11 days |
| July 14 to July 28, 2025 | 14 days, the checker's alternative anchor |
| Jan 28 to June 1, 2026 | 124 days, "four months before" holds |

## Standing recommendations

1. **A second external check on a different prompt before Stage 7 is ticked.**
   Stage 3 established that two checks on different prompts beat one thorough
   check and that the disagreement is the value. SF3 exists because two checks
   disagreed. This is one check.
2. **Hand the checker the render, never the HTML.** Stage 3 fed PDFs. This run fed
   HTML and produced two phantom flags out of seven items.
3. **Route the applied findings through the outstanding Stage 6 round.** Flags 1
   through 5 are body-prose or citation-adjacent changes, and round 5 is
   unstaled. An edit to the live text invalidates the current export, and the
   re-export is part of applying the edit.
4. Nothing in the chapter has been edited on the strength of this check. All five
   flags await Dan's ruling.
