r"""
TIP102 | Week 10 | Session 2 | Problem Set Version 1 | Problem 6
Fixing Flight Booking Software

Source: statement reconstructed from the CodePath solution guide and written in our own words.
The original course page is behind a login, so wording and details may differ slightly.
Solution guide (only after you have tried!): https://github.com/codepath/compsci_guides/wiki/Fixing-Flight-Booking-Software

PROBLEM
-------
`flights` maps each location to a list of locations with direct flights. Write `find_shortest_path(flights, source, destination)` that returns the list of locations on a shortest route (fewest flights) from `source` to `destination`, or an empty list if there is none.

EXAMPLES (test cases from the solution guide)
---------------------------------------------
HAPPY CASE
Input: 
flights = {
    'LAX': ['SFO'],
    'SFO': ['LAX', 'ORD', 'ERW'],
    'ERW': ['SFO', 'ORD'],
    'ORD': ['ERW', 'SFO', 'MIA'],
    'MIA': ['ORD']
}
start = 'LAX'
destination = 'MIA'

Output:
['LAX', 'SFO', 'ORD', 'MIA']
Explanation: The path LAX -> SFO -> ORD -> MIA is the shortest path with the least layovers.

EDGE CASE
Input: 
flights = {
    'LAX': ['SFO'],
    'SFO': ['LAX'],
    'MIA': []
}
start = 'LAX'
destination = 'MIA'

Output:
[]
Explanation: There is no possible path from LAX to MIA.
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


def find_shortest_path(flights, source, destination):
    pass
