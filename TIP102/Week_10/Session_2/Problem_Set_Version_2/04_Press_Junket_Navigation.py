r"""
TIP102 | Week 10 | Session 2 | Problem Set Version 2 | Problem 4
Press Junket Navigation

Source: statement reconstructed from the CodePath solution guide and written in our own words.
The original course page is behind a login, so wording and details may differ slightly.
Solution guide (only after you have tried!): https://github.com/codepath/compsci_guides/wiki/Press-Junket-Navigation

PROBLEM
-------
`venue_map` is an adjacency list where `venue_map[i]` lists the rooms connected to room i by a hallway. Starting from room 0, write `find_path(venue_map, target)` that returns any list of rooms leading to `target`.

EXAMPLES (test cases from the solution guide)
---------------------------------------------
HAPPY CASE
Input: 
```python
venue_map = [
    [1, 2],
    [0, 3],
    [0, 4],
    [1, 5],
    [2],
    [3]
]
target = 5
```
Output:
```markdown
[0, 1, 3, 5]
Explanation: The path from room 0 to room 5 is 0 -> 1 -> 3 -> 5. This is one valid solution, though other paths may also exist.
```

EDGE CASE
Input: 
```python
venue_map = [
    [1],
    [0],
]
target = 1
```
Output:
```markdown
[0, 1]
Explanation: Room 1 is directly connected to room 0, so the path is simply [0, 1].
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

def find_path(venue_map, target):
    pass
