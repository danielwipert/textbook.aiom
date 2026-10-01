# Chapter 3 review: second-model prompt (Process v4, Decision 77)

Built 2026-10-01, before sitting 2. **Dan runs this on a model that did not draft
the chapter**, then rules every finding from both reviews in one sitting. Claude's
own findings are in `AIOM_Ch03_Review_claude_findings.md`. **Do not attach or paste
them**: the second read is independent, and Claude's findings are read after it,
never before.

## Attach exactly three files

    Drafts/Ch03_A_Science_and_Its_Discipline/02_Stage4_Review/AIOM_Ch03_prose_for_review.md
    Drafts/Ch03_A_Science_and_Its_Discipline/02_Stage4_Review/ch03_reference_extract.md
    Drafts/Ch03_A_Science_and_Its_Discipline/02_Stage4_Review/ch01_prose_exemplar.md

Both chapters went through the same extractor, `prose_extract.py`, so they compare
directly. Neither carries its source register.

## The prompt

> You are reviewing one chapter of an academic textbook for business graduate
> students. Chapter 3 is under review. The second file holds what the chapter is
> meant to do (its structure entry, its competency, its outline, the author's
> rulings on its plan) and the book's seven craft criteria, C1 to C7. The third
> file is Chapter 1 of the same book, locked and published, which is the exemplar
> the craft standard was measured from. Calibrate against Chapter 1, not against
> how closely Chapter 3 resembles itself.
>
> Three warnings. First, sourcing and whether any figure is true are OUT OF BOUNDS:
> a separate fact check reads the sources later. You may still flag a sentence
> that makes an empirical claim with no visible support. Second, quoted statements
> of theorems, lemmas and propositions are verbatim from a formal registry and are
> not to be judged as prose; judge the prose around them. Third, a review that
> returns "meets the criteria, no findings" will be discarded as confirmatory.
>
> Review in three separate sections. In every section, do not report whether
> something is met. Quote the WEAKEST evidence, say precisely what is wrong, and
> say whether it is a defect, a deliberate choice serving something else, or noise.
>
> **Section A, structure.** Does every slot serve the chapter's stated purpose?
> Is competency C4 DELIVERED, meaning a reader could actually perform it after this
> chapter, unaided, on a theorem they have not seen? Is the trace load-bearing or
> decorative? Does the chapter front-run anything a later chapter is meant to
> reveal? Does anything in the outline go missing, and does anything appear that
> the outline does not call for?
>
> **Section B, teaching.** Where would a sceptical, busy MBA-level reader stall,
> lose the thread, or stop believing the argument? Judge clarity, pacing,
> cognitive load, example fitness, and transitions. Name the single paragraph you
> would cut first and the single place most in need of a concrete example.
>
> **Section C, voice and craft.** One finding per criterion, C1 to C7, quoting the
> weakest passage by section and the strongest, so your calibration is visible.
>
> Number your findings S-1, S-2, and so on across all three sections, one line
> each, and finish with the three you would fix first.

## After the review

Save the reply as `AIOM_Ch03_Review_secondmodel_review.md` in this folder. Claude
merges both sets of findings into ONE decision list for sitting 2, each with a
recommendation, and applies Dan's rulings in one commit (Decision 81).
