r"""
TIP102 | Week 10 | Session 2 | Problem Set Version 2 | Problem 5
Gossip Chain

Source: statement reconstructed from the CodePath solution guide and written in our own words.
The original course page is behind a login, so wording and details may differ slightly.
Solution guide (only after you have tried!): https://github.com/codepath/compsci_guides/wiki/Gossip-Chain

PROBLEM
-------
There are `n` celebrities and each [u, v] in `connections` means u tells the rumor to v. Starting a DFS at `start`, record for each celebrity the time they first hear the rumor (arrival) and the time they finish spreading it (departure). Return these times.

EXAMPLES (test cases from the solution guide)
---------------------------------------------
HAPPY CASE
Input: 
connections = [
    ["Amber Gill", "Greg O'Shea"],
    ["Amber Gill", "Molly-Mae Hague"],
    ["Greg O'Shea", "Molly-Mae Hague"],
    ["Greg O'Shea", "Tommy Fury"],
    ["Molly-Mae Hague", "Tommy Fury"],
    ["Tommy Fury", "Ovie Soko"],
    ["Curtis Pritchard", "Maura Higgins"]
]
n = 7
start = "Amber Gill"

Output:
{
    "Amber Gill": (1, 10),
    "Greg O'Shea": (2, 9),
    "Molly-Mae Hague": (3, 8),
    "Tommy Fury": (4, 7),
    "Ovie Soko": (5, 6),
    "Curtis Pritchard": (-1, -1),
    "Maura Higgins": (-1, -1)
}
Explanation: The rumor starts with "Amber Gill" and spreads to other connected celebrities. "Curtis Pritchard" and "Maura Higgins" never hear the rumor.

EDGE CASE
Input: 
connections = [
    ["Amber Gill", "Greg O'Shea"],
    ["Amber Gill", "Molly-Mae Hague"]
]
n = 4
start = "Molly-Mae Hague"
Output:
{
    "Amber Gill": (-1, -1),
    "Greg O'Shea": (-1, -1),
    "Molly-Mae Hague": (1, 2)
}
Explanation: The rumor only starts with "Molly-Mae Hague" and does not reach the other celebrities.
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

from collections import defaultdict


def rumor_spread_times(connections, n, start):
    pass
