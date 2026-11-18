r"""
TIP102 | Week 10 | Session 2 | Problem Set Version 1 | Problem 7
Expanding Flight Offerings

Source: statement reconstructed from the CodePath solution guide and written in our own words.
The original course page is behind a login, so wording and details may differ slightly.
Solution guide (only after you have tried!): https://github.com/codepath/compsci_guides/wiki/Expanding-Flight-Offerings

PROBLEM
-------
`flights` is an undirected adjacency dictionary of airports. Write `min_flights_to_expand(flights)` that returns the minimum number of new flights needed so that every airport can reach every other airport (number of separate groups minus one).

EXAMPLES (test cases from the solution guide)
---------------------------------------------
HAPPY CASE
Input: 
flights = {
    'JFK': ['LAX', 'SFO'],
    'LAX': ['JFK', 'SFO'],
    'SFO': ['JFK', 'LAX'],
    'ORD': ['ATL'],
    'ATL': ['ORD']
}

Output:
1
Explanation: The airports form two connected components: {'JFK', 'LAX', 'SFO'} and {'ORD', 'ATL'}. Only one flight is needed to connect the two components.

EDGE CASE
Input: 
flights = {}

Output:
0
Explanation: There are no airports, so there are zero components and no flights need to be added.
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

def min_flights_to_expand(flights):
    pass
