# LeetCode Sensei

My DSA practice repo: all 12 weeks of CodePath **TIP102** (372 problems) set up for the UMPIRE method, plus a Claude Code mentor ("Algo Sensei") that remembers my progress between sessions.

- **Language:** Python (with Swift notes, since I'm an iOS developer)
- **Progress:** see [`progress/TIP102.md`](progress/TIP102.md) and the checklist in [`TIP102/README.md`](TIP102/README.md)

## How a problem file looks

```
TIP102/Week_01/Session_1/Problem_Set_Version_1/01_Hundred_Acre_Wood.py

r"""  problem statement + examples + link to the solution guide  """
# STATUS: not started
"""  UNDERSTAND / MATCH / PLAN / IMPLEMENT / REVIEW / EVALUATE  """
def welcome():
    pass
if __name__ == "__main__":
    ...example usage...
```

Fill in UMPIRE top to bottom, write the code, run `python3 <file>`.

## Claude Code commands

| Command | What it does |
|---------|--------------|
| `/next` | Picks the next problem from my progress |
| `/tutor` | Explains a concept or problem from the ground up |
| `/hint` | 5-level progressive hints, never gives the answer away |
| `/review` | Reviews my solution: correctness, complexity, edge cases, UMPIRE |
| `/interview` | Mock interview with a written feedback report |
| `/pattern-mapper` | Teaches me to spot which pattern a problem uses |
| `/log-session` | Saves progress (STATUS, log, weak patterns) and offers to commit |
| `/syntax` | Python syntax for something you know how to do but forgot how to write (saves it to `progress/syntax-notes.md`; `/syntax quiz` to review) |

Swift notes are automatic: when Python and Swift differ on something in the problem, Claude adds one line about it.

## Memory

- `progress/` holds my profile, practice log, and weak patterns.
- Each problem's `# STATUS:` line is the source of truth for what's done.
- When Claude Code starts, a hook runs `tools/progress.py --summary`, so Claude knows what I solved, what's in progress, and what I struggle with.
- `/log-session` updates it all at the end. Commit and push to keep the history (and the contribution graph).

## Logic building

[`logic-building/ROADMAP.md`](logic-building/ROADMAP.md) maps the "Master Your Logic Building" problem list onto TIP102 weeks. You don't need to finish it first; use it as a warm-up and a gap filler.

## Typical session

```bash
cd leetcode-sensei
claude
> /next
# fill in UMPIRE and code in the file it points to
> /hint            # if stuck
> /review          # when done
> /log-session     # saves progress, offers to commit + push
```

## Sources

- Weeks 1 and 2 (Session 1) statements come from the CodePath TIP102 course pages.
- Other statements are reconstructed in my own words from the public [CodePath solution guide](https://github.com/codepath/compsci_guides/wiki/TIP102-Breakout-Problem-Solutions); each file links to its guide page.
