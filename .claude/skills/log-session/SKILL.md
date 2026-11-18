---
name: log-session
description: Save practice progress (the repo's memory) at the end of a problem or session. Use when the user says "log this", "save progress", "/log-session", "done for today", or right after a problem is solved or abandoned.
---

# Log Session

This repo is the memory. Claude Code starts every session fresh, so anything worth remembering must be written to files and committed.

For each problem worked on this session:

1. **Update the `# STATUS:` line** at the top of the problem file to one of: `in progress`, `solved`, `solved with help` (used any hint at level 3 or higher, or saw a solution).
2. **Append one row to `progress/log.md`:**
   `| YYYY-MM-DD | Week W S# V# #N Name | Easy/Medium/Hard | Pattern | Mode | Solved / Solved with help / Not solved | hint level 0-5 | one short note |`
   Use today's real date. The note should be specific ("forgot to move slow pointer", not "struggled").
3. **Update `progress/weak-patterns.md`** if a pattern caused trouble: add or update a row with the specific sticking point. Status values: Struggling / Improving / Solid. Mark "Solid" only after two clean solves of that pattern with hint level 0-1.
4. **Logic-building roadmap:** if they practiced a problem from `logic-building/ROADMAP.md`, change its `- [ ]` to `- [x]`.
5. **Learner profile:** update `progress/learner-profile.md` only if level, language, or learning style clearly changed.
6. Run `python3 tools/progress.py` to refresh `progress/TIP102.md` and `TIP102/README.md`.
7. Show a one-line summary (e.g. "Logged 2 problems, 14/372 solved, weak spot: sliding window") and offer to commit and push:
   `git add -A && git commit -m "practice: W1S1 Hundred Acre Wood, Greeting (functions)" && git push`
   Committing daily is what builds the GitHub contribution graph the learner wants.

Only record what actually happened in this session. Never invent results, hint levels, or problems that were not attempted.
