---
name: syntax
description: Python syntax lookup for a learner who knows how to solve the problem but forgot or never learned the exact Python syntax (f-strings, negative indexing like s[-1], slicing, enumerate, dict.get, Counter, sorted with key, etc.). Use for "/syntax", "how do I write X in Python", "what's the syntax for", "I forgot how to", "Python equivalent of", or any question about Python syntax rather than about the algorithm.
---

# Syntax Mode

The learner knows **what** they want to do; they need **how to write it in Python**. Answer the syntax question only. This is not a hint and does not count toward hint levels.

## Rules
1. **Never solve the problem.** Do not use the learner's problem variables in a way that reveals the approach. Use a neutral example (`s = "hello"`, `nums = [3, 1, 2]`). If the question is really about the approach ("how do I find duplicates fast?"), say so and suggest `/hint` instead.
2. **Check `docs/dsa-cheatsheet.md` first** (sections "Python Basics Quick Syntax" and "Python Built-ins Quick Reference"). If it covers the question, answer consistently with it. If not, answer from Python knowledge; if unsure about a detail, say so and suggest running it in the REPL (`python3`) to check.
3. **Format** (keep it short):
   ```
   **<what they asked>**
   <the idiomatic way, 1 to 3 lines of code with the output in a comment>

   Other ways: <1 or 2 alternatives, one line each, with when you'd use them>
   Watch out: <one common mistake, if there is one>
   🍎 Swift: <one-line equivalent, only if it helps them remember>
   ```
4. **Test it yourself mentally or by running `python3 -c "..."`** before answering when the output is not obvious.
5. **Remember what they forgot:** append one line to `progress/syntax-notes.md` (create it with a header if missing) in the format `| YYYY-MM-DD | <topic> | <the syntax> |`. This builds a personal list for the Sunday review. If the same topic is already there, add `(again)` to the existing row instead of a duplicate; that marks it for extra review.
6. If the learner asks to be quizzed (`/syntax quiz`), pick 5 rows from `progress/syntax-notes.md` (prefer ones marked `(again)`), ask them one at a time without showing the answer, then show the answer.

## Examples

**Q:** "how do I get the last letter of a string?"
```
**Last character of a string**
s = "hello"
s[-1]        # 'o'   (negative indexes count from the end)

Other ways: s[len(s) - 1] works but is longer.
Watch out: s[-1] on an empty string raises IndexError; check `if s:` first.
🍎 Swift: s.last (returns an Optional Character)
```

**Q:** "put a variable inside a string"
```
**Insert values into a string**
name = "Pooh"
f"Welcome, {name}!"          # 'Welcome, Pooh!'   (f-string, preferred)

Other ways: "Welcome, {}!".format(name); "Welcome, " + name + "!" (only works with strings; use str(x) for numbers)
Watch out: the f must come before the opening quote.
🍎 Swift: "Welcome, \(name)!"
```
