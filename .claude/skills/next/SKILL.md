---
name: next
description: Pick the next problem to practice from the TIP102 course and logic-building roadmap, based on progress files. Use when the user says "/next", "what should I do next", "give me a problem", or starts a session without saying what to work on.
---

# Next Problem

1. Run `python3 tools/progress.py --summary` to get fresh status.
2. Read `progress/weak-patterns.md` and the last few lines of `progress/log.md`.
3. Pick ONE problem, in this order of preference:
   - An **in progress** problem (finish what was started).
   - If a weak pattern is marked "Struggling", a not-started problem from a session that covers it (see the week topics in `progress/TIP102.md`).
   - Otherwise the **first not-started problem in order**: Week, then Session, then Version 1 before Version 2.
   - If the next week introduces recursion (Week 7) and Phase 3 of `logic-building/ROADMAP.md` is untouched, suggest a few Phase 3 warm-ups first.
4. Reply in 3 lines max: the file path, the topic, and one sentence on why this one. Then say: "Start with the UNDERSTAND section. Ask for `/hint` if you get stuck."
5. Do not explain the problem or hint at the approach unless asked.
