r"""
TIP102 | Week 10 | Session 2 | Problem Set Version 2 | Problem 8
Celebrity Feuds

Source: statement reconstructed from the CodePath solution guide and written in our own words.
The original course page is behind a login, so wording and details may differ slightly.
Solution guide (only after you have tried!): https://github.com/codepath/compsci_guides/wiki/Celebrity-Feuds

PROBLEM
-------
There are `n` celebrities, and each [a, b] in `dislikes` means a and b cannot be in the same group. Write `can_split(n, dislikes)` that returns True if everyone can be split into two groups with no disliking pair together.

EXAMPLES (test cases from the solution guide)
---------------------------------------------
HAPPY CASE
Input: 
```python
dislikes_1 = [[1, 2], [1, 3], [2, 4]]
n = 4
```
Output:
```markdown
True
Explanation: The celebrities can be split into two groups: Group 1: [1, 4], Group 2: [2, 3]. No celebrity dislikes another celebrity in their own group.
```

EDGE CASE
Input: 
```python
dislikes_2 = [[1, 2], [1, 3], [2, 3]]
n = 3
```
Output:
```markdown
False
Explanation: It is impossible to split the celebrities into two groups such that no two celebrities in the same group dislike each other.
"""

# STATUS: not started    (not started | in progress | solved | solved with help)

"""
UNDERSTAND:
    * Input:
    * Output:

    * questions about the problem?

    * edge cases?


MATCH:    * similar problems?

PLAN
1.

IMPLEMENT:
-

REVIEW:


EVALUATE:
    * runtime and complexity?


"""

def can_split(n, dislikes):
    pass
