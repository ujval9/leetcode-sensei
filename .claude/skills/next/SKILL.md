---
name: next
description: Pick the next problem to practice from the TIP102 course and logic-building roadmap, based on progress files. Use when the user says "/next", "what should I do next", "give me a problem", or starts a session without saying what to work on.
---

# Next Problem

1. Run `python3 tools/progress.py --summary` to get fresh status.
2. **Reconcile stale STATUS lines before picking.** For any problem marked `not started` or `in progress` that has code written under the starter stub, check it yourself: run the file and read the UMPIRE block. Then update the `# STATUS:` line without asking:
   - code runs and produces the expected output, UMPIRE filled in -> `solved`
   - correct only after you gave away the approach or the answer -> `solved with help`
   - code present but wrong, incomplete, or UMPIRE mostly empty -> `in progress`
   Rerun `python3 tools/progress.py` after any change. Say in one line what you flipped and why. Never flip a problem to solved without running it first. Do not touch the learner's code, only the STATUS line.
3. Read `progress/weak-patterns.md` and the last few lines of `progress/log.md`.
4. Pick ONE problem, in this order of preference:
   - An **in progress** problem (finish what was started).
   - If a weak pattern is marked "Struggling", a not-started problem from a session that covers it (see the week topics in `progress/TIP102.md`).
   - Otherwise the **first not-started problem in order**: Week, then Session, then Version 1 before Version 2.
   - If the next week introduces recursion (Week 7) and Phase 3 of `logic-building/ROADMAP.md` is untouched, suggest a few Phase 3 warm-ups first.
5. **Open the chosen file in the editor** so the learner does not have to navigate to it: run `code <path>` if the `code` CLI is on PATH, otherwise `open -a "Visual Studio Code" <path>`. Do not wait for confirmation.
6. Reply in 3 lines max: the file path, the topic, and one sentence on why this one. Then say: "Start with the UNDERSTAND section. Ask for `/hint` if you get stuck."
7. Do not explain the problem or hint at the approach unless asked.
