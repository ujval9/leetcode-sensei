r"""
TIP102 | Week 10 | Session 2 | Problem Set Version 1 | Problem 8
Get Flight Itinerary

Source: statement reconstructed from the CodePath solution guide and written in our own words.
The original course page is behind a login, so wording and details may differ slightly.
Solution guide (only after you have tried!): https://github.com/codepath/compsci_guides/wiki/Get-Flight-Itinerary

PROBLEM
-------
`flights` maps each airport to the airports reachable by direct flight. Write `get_itinerary(flights, source, dest)` that returns any valid path from `source` to `dest` as a list of airports.

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
source = 'LAX'
dest = 'MIA'

Output:
['LAX', 'SFO', 'ORD', 'MIA']
Explanation: The path LAX -> SFO -> ORD -> MIA is valid, though LAX -> SFO -> ERW -> ORD -> MIA is also valid.
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

def get_itinerary(flights, source, dest):
    pass
