r"""
TIP102 | Week 10 | Session 2 | Problem Set Version 1 | Problem 3
Number of Flights

Source: statement reconstructed from the CodePath solution guide and written in our own words.
The original course page is behind a login, so wording and details may differ slightly.
Solution guide (only after you have tried!): https://github.com/codepath/compsci_guides/wiki/Number-of-Flights

PROBLEM
-------
`flights` is an adjacency matrix of direct flights. Write `counting_flights(flights, start, destination)` that returns the minimum number of flights needed to get from `start` to `destination`, or -1 if it is impossible.

EXAMPLES (test cases from the solution guide)
---------------------------------------------
HAPPY CASE
Input: flights = [
                  [0, 1, 0, 0],  # Airport 0
                  [0, 0, 1, 0],  # Airport 1
                  [0, 0, 0, 1],  # Airport 2
                  [0, 0, 0, 0]   # Airport 3
                 ]
start = 0
destination = 3
Output: 3
Explanation: The shortest path from airport 0 to airport 3 requires 3 flights (0 -> 1 -> 2 -> 3).

EDGE CASE
Input: flights = [
                  [0, 0, 0, 0],  # Airport 0
                  [0, 0, 1, 0],  # Airport 1
                  [0, 0, 0, 1],  # Airport 2
                  [0, 0, 0, 0]   # Airport 3
                 ]
start = 0
destination = 3
Output: -1
Explanation: There is no valid path from airport 0 to airport 3.
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


def counting_flights(flights, start, destination):
    pass
