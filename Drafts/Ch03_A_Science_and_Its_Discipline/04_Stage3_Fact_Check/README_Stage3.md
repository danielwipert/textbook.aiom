# Chapter 3, fact check (v4 step 5). How to send it.

Built 2026-10-12 from the post-author-pass text (commit 56c830c), on a fresh
render. Nothing here is a verification: no source host is reachable from the
Claude environment.

## Send two checks, in separate sessions

| File | To | Notes |
|---|---|---|
| `AIOM_Ch03_Stage3_CheckA_package.md` | Model 1, **with web access** | Reads the sources. Carries the chapter and the claim packet. |
| `AIOM_Ch03_Stage3_CheckB_package.md` | Model 2, a different session | Reads only the chapter. No packet, on purpose. |

Each file is complete on its own: paste or attach it and say "follow the
instructions in this file". **Never show B the packet or A's output.** If
Model 1 says in its first line that it has no web access, stop: its report
cannot verify anything (Chapter 2's first check was redone for this reason).

Save the replies here as `AIOM_Ch03_Stage3_externalcheck_A.md` and
`AIOM_Ch03_Stage3_externalcheck_B.md`. Claude then builds the sitting 3
package: each finding put as a gate, the remedy judged apart from the finding.

## What else is in this folder

- `AIOM_Ch03_Stage3_render.pdf`: the render both packages were extracted from.
  It fails print gates 1, 4 and 8 on reflow; that is the design review's.
- `AIOM_Ch03_Stage3_packet.md`: the claim packet from `factcheck_packet.py`,
  with Table 3.1's three cited cells and two register entries added by hand
  (the tool reads paragraphs only).
