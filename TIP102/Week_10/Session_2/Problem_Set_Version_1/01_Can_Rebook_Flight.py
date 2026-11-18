r"""
TIP102 | Week 10 | Session 2 | Problem Set Version 1 | Problem 1
Can Rebook Flight

Source: statement reconstructed from the CodePath solution guide and written in our own words.
The original course page is behind a login, so wording and details may differ slightly.
Solution guide (only after you have tried!): https://github.com/codepath/compsci_guides/wiki/Can-Rebook-Flight

PROBLEM
-------
`flights` is an adjacency matrix where `flights[i][j] == 1` means a direct flight from i to j. Write `can_rebook(flights, source, dest)` that returns True if you can get from `source` to `dest` using any number of flights, using BFS.

EXAMPLES (test cases from the solution guide)
---------------------------------------------
HAPPY CASE
Input: 
flights = [
    [0, 1, 0],  # Flight 0
    [0, 0, 1],  # Flight 1
    [0, 0, 0]   # Flight 2
]
source = 0
dest = 2

Output:
True
Explanation: There is a path from location 0 to 2 through location 1.

EDGE CASE
Input: 
flights = [
    [0, 0],
    [0, 0]
]
source = 0
dest = 1

Output:
False
Explanation: There is no flight available from location 0 to location 1.
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

from collections import deque


def can_rebook(flights, source, dest):
    pass
