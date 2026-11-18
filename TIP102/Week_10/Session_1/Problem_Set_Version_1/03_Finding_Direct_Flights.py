r"""
TIP102 | Week 10 | Session 1 | Problem Set Version 1 | Problem 3
Finding Direct Flights

Source: statement reconstructed from the CodePath solution guide and written in our own words.
The original course page is behind a login, so wording and details may differ slightly.
Solution guide (only after you have tried!): https://github.com/codepath/compsci_guides/wiki/Finding-Direct-Flights

PROBLEM
-------
`flights` is an adjacency matrix where `flights[i][j] == 1` means a direct flight from i to j. Write `get_direct_flights(flights, source)` that returns a list of all destinations reachable directly from `source`.

EXAMPLES (test cases from the solution guide)
---------------------------------------------
HAPPY CASE
Input: flights = [
                   [0, 1, 1, 0],
                   [1, 0, 0, 0],
                   [1, 1, 0, 1],
                   [0, 0, 0, 0]
                 ], source = 2
Output: [0, 1, 3]
Explanation: From destination 2, there are direct flights to destinations 0, 1, and 3.

EDGE CASE
Input: flights = [
                   [0, 1, 1, 0],
                   [1, 0, 0, 0],
                   [1, 1, 0, 1],
                   [0, 0, 0, 0]
                 ], source = 3
Output: []
Explanation: Destination 3 has no outgoing flights, so the result is an empty list.
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

def get_direct_flights(flights, source):
    pass
