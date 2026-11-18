r"""
TIP102 | Week 11 | Session 2 | Problem Set Version 1 | Problem 4
Escape the Infected Zone

Source: statement reconstructed from the CodePath solution guide and written in our own words.
The original course page is behind a login, so wording and details may differ slightly.
Solution guide (only after you have tried!): https://github.com/codepath/compsci_guides/wiki/Escape-the-Infected-Zone

PROBLEM
-------
`safety` is a grid of safety levels. The Pacific zone touches the top and left edges and the Atlantic zone touches the bottom and right edges. Survivors can move to an adjacent cell only if its safety level is less than or equal to the current one. Write `escape_subzones(safety)` that returns every cell from which survivors can reach both zones.

EXAMPLES (test cases from the solution guide)
---------------------------------------------
HAPPY CASE
Input: safety = [
    [1, 2, 2, 3, 5],
    [3, 2, 3, 4, 4],
    [2, 4, 5, 3, 1],
    [6, 7, 1, 4, 5],
    [5, 1, 1, 2, 4]
]
Output: [[0, 4], [1, 3], [1, 4], [2, 2], [3, 0], [3, 1], [4, 0]]
Explanation: These zones allow survivors to escape to both the Pacific and Atlantic Safety Zones.

EDGE CASE
Input: safety = [
    [2, 1],
    [1, 2]
]
Output: [[0, 0], [0, 1], [1, 0], [1, 1]]
Explanation: All four zones allow survivors to escape to both safety zones. Zones `[0, 1]` and `[1, 0]` border both safety zones directly, zone `[0, 0]` can reach the second safety zone through `[0, 1]`, and zone `[1, 1]` can reach the first safety zone through `[0, 1]` or `[1, 0]`.
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

def escape_subzones(safety):
    pass
