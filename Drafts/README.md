# Drafts

Working drafts for the manuscript, organized so every file has one obvious home.

This tree holds chapter draft files only. Build tooling (`AIOM_build.py`,
`place.py`), the design system (`AIOM_book.css`), and the project specs stay at
the repository root.

## Layout

```
Drafts/
  Ch01_The_Category_Error/
    00_Stage0_Draft/
    01_G1_Structural_Gate/
    02_Stage1_Content_Review/
    03_Stage2_Source_Fact_Check_1/
    04_Stage3_Voice_Check/
    05_Stage4_Design_Review/
    06_G2_Production_Gate/
    07_Stage5_Copy_Edit/
    08_Stage6_Final_Fact_Check_2/
    09_G3_Continuity_Gate/
    10_Stage7_Final_Read/
    11_Stage8_Locked/
  Ch02_The_Flow/
  ...
  Ch15_Standing_Up_the_Discipline/
  Case_Part_I/
  Case_Part_II/
  Case_Part_III/
```

Each chapter folder, and each Part cumulative-case folder, carries the same
twelve subfolders.

## The twelve steps

The subfolders follow the chapter lifecycle defined in `CLAUDE.md` section 8:
nine stages (0 through 8) with the three gates (G1, G2, G3) interleaved in
sequence. The two-digit prefix on each subfolder is a running step index, so the
folders always list in true lifecycle order rather than alphabetically.

| Prefix | Step | Owner |
|--------|------|-------|
| 00 | Stage 0, Draft | Claude |
| 01 | G1, Structural gate | Claude |
| 02 | Stage 1, Content review | Dan |
| 03 | Stage 2, Source and fact check 1 | Dan |
| 04 | Stage 3, Voice check | Claude |
| 05 | Stage 4, Design review | Claude |
| 06 | G2, Production gate | Claude |
| 07 | Stage 5, Copy edit | Dan |
| 08 | Stage 6, Final fact check 2 | Dan |
| 09 | G3, Continuity gate | Claude |
| 10 | Stage 7, Final read | Dan |
| 11 | Stage 8, Locked | Claude |

Gates are mechanical pass-or-fail checks, not editorial passes. Their folders
hold gate outputs: G1 structural findings, G2 render reports and QA logs, G3
continuity notes. A stage folder holds the working file as it stands after that
pass.

## Conventions

- The chapter draft moves forward through the folders. The current live version
  sits in the highest-numbered folder that owns it.
- Chapter folders are zero-padded (`Ch01` through `Ch15`) so they sort in reading
  order.
- The three Part cumulative cases run the same lifecycle and live in
  `Case_Part_I`, `Case_Part_II`, and `Case_Part_III`.
- Empty folders carry a `.gitkeep` so the structure persists in git. Remove a
  `.gitkeep` once a folder holds real files, or leave it; either is fine.
