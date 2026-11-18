r"""
TIP102 | Week 12 | Session 2 | Problem Set Version 2 | Problem 5
Number of Provinces

Source: statement reconstructed from the CodePath solution guide and written in our own words.
The original course page is behind a login, so wording and details may differ slightly.
Solution guide (only after you have tried!): https://github.com/codepath/compsci_guides/wiki/Number-of-Provinces

PROBLEM
-------
`is_connected` is an n x n matrix where `is_connected[i][j] == 1` means cities i and j are directly connected. A province is a group of directly or indirectly connected cities. Write `num_provinces(is_connected)` that returns the number of provinces.

EXAMPLES (test cases from the solution guide)
---------------------------------------------
HAPPY CASE
Input: is_connected = [[1,1,0],[1,1,0],[0,0,1]]
Output: 2
Explanation: The first two cities are connected to each other, forming one province. The third city is isolated, forming another province.

Input: is_connected = [[1,0,0],[0,1,0],[0,0,1]]
Output: 3
Explanation: Each city is isolated, so there are 3 provinces.
EDGE CASE
Input: is_connected = [[1]]
Output: 1
Explanation: A single city is its own province.

Input: is_connected = [[1,1],[1,1]]
Output: 1
Explanation: Both cities are connected, forming one province.
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

def num_provinces(is_connected):
    pass
