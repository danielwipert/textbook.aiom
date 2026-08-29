# Chapter 2, Stage 4. Second-model craft prompt

Built 2026-08-29. Dan runs this on a model that did not draft the chapter, and
rules on the result. **Claude's craft read was written by the model that drafted
this chapter and wrote the standard it grades against**, which is the self-marking
problem Decision 73 priced at Stage 1 and which the Stage 2 package answered the
same way.

## Attach exactly three files

    Drafts/Ch02_The_Flow/05_Stage4_Voice_And_Craft_Check/AIOM_Ch02_prose_for_craft_review.md
    Drafts/Ch02_The_Flow/05_Stage4_Voice_And_Craft_Check/ch02_craft_criteria_extract.md
    Drafts/Ch01_The_Category_Error/00_Stage0_Draft/AIOM_Ch01_redraft.html

**The third file is the exemplar, and attaching it is the change from Chapter 1's
version of this prompt.** The standard's band is measured from the locked Chapter 1
rather than from four journalists, so the reviewer can now calibrate against the
book's own prose instead of against an outside register.

**Do NOT attach this checklist and do not paste F1 through F7 into the
conversation.** The point is an independent read. Claude's findings are read after
the reviewer's own, never before.

## The prompt

> You are reviewing one chapter of an academic textbook against a written craft
> standard. Chapter 2 is the chapter under review. The standard's seven criteria,
> C1 through C7, are attached as a short extract. The third file is Chapter 1 of
> the same book, which is locked and published and is the exemplar the standard's
> numeric band was measured from.
>
> Three warnings about this task. First, **the standard was written partly by
> generalizing from Chapter 1's prose**, so calibrate against Chapter 1 and not
> against how closely Chapter 2 resembles itself. Second, on Chapter 1 the first
> review of this kind returned "meets all six criteria, no findings," and that
> verdict was withdrawn as confirmatory. Third, **Chapter 2 has an open fact-check
> step**, so sourcing, citation and whether any figure is true are OUT OF BOUNDS.
> Judge the prose.
>
> For each of the seven criteria, do not report whether the chapter meets it.
> Instead:
>
> 1. Quote the WEAKEST passage in Chapter 2 against that criterion, by section,
>    and say precisely what is wrong with it.
> 2. Quote the STRONGEST passage, so your calibration is visible.
> 3. State whether the weakest passage is a defect worth fixing, a deliberate
>    choice serving something else, or noise.
>
> Then answer four questions directly.
>
> a. Which single change would most improve this chapter's prose?
> b. Which criterion, if any, does the chapter fail outright at chapter level?
> c. **Where did you first stall?** Name the paragraph you had to read twice.
>    This is the question the drafter structurally cannot answer, because it has
>    read this chapter perhaps thirty times and can no longer be surprised by it.
> d. Is there any defect the seven criteria do not cover, which a serious reader
>    would notice?
>
> Finally, one comparison the criteria do not ask for. **Read Chapter 1 and
> Chapter 2 back to back and say whether they sound like the same book.** If they
> do not, say which one is the outlier and in which direction.
>
> Assume the chapter is good. Your job is not to praise it. Your job is to find
> what a hostile reviewer at a university press would find.

## What to expect, so it is not mistaken for a new finding

**The chapter is measurably heavier than Chapter 1** and a reviewer may report that
as a general impression. It is real and it is quantified in F4: mean sentence 15.8
words against 14.3, and the two closing slots are where the gap is widest. A
reviewer who names a DIFFERENT section as the heavy one is giving new information.

**The craft section's mapping is the book's own construct**, so a reviewer may
object that its two failure modes cannot have been observed. That is F2, it is
already raised, and it has been handed to Stage 3 as a standing rule 2 item.

## How to rule the result

Compare against F1 through F7 in the Stage 4 findings. Agreement raises confidence.
**A finding the second model raises that Claude missed is the more valuable output**
and goes in as F8 onward. Disagreement is Dan's to rule, and Claude rules none of it.
