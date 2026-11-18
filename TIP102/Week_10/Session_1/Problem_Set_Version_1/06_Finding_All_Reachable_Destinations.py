r"""
TIP102 | Week 10 | Session 1 | Problem Set Version 1 | Problem 6
Finding All Reachable Destinations

Source: statement reconstructed from the CodePath solution guide and written in our own words.
The original course page is behind a login, so wording and details may differ slightly.
Solution guide (only after you have tried!): https://github.com/codepath/compsci_guides/wiki/Finding-All-Reachable-Destinations

PROBLEM
-------
`flights` is an adjacency dictionary. Write `get_all_destinations(flights, start)` that returns every city reachable from `start` (by any number of flights) in breadth-first order, not including `start`.

EXAMPLES (test cases from the solution guide)
---------------------------------------------
HAPPY CASE
Input: 
flights = {
    "Tokyo": ["Sydney"],
    "Sydney": ["Tokyo", "Beijing"],
    "Beijing": ["Mexico City", "Helsinki"],
    "Helsinki": ["Cairo", "New York"],
    "Cairo": ["Helsinki", "Reykjavik"],
    "Reykjavik": ["Cairo", "New York"],
    "Mexico City": ["Sydney"]
}
start = "Beijing"
Output: ['Beijing', 'Mexico City', 'Helsinki', 'Sydney', 'Cairo', 'New York', 'Tokyo', 'Reykjavik']
Explanation: Starting from Beijing, you can reach all other destinations through direct and connecting flights.

EDGE CASE
Input: 
flights = {
    "Tokyo": ["Sydney"],
    "Sydney": ["Tokyo"]
}
start = "Tokyo"
Output: ['Tokyo', 'Sydney']
Explanation: Tokyo can only reach Sydney directly, and vice versa.
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


def get_all_destinations(flights, start):
    pass
