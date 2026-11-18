r"""
TIP102 | Week 10 | Session 2 | Problem Set Version 1 | Problem 5
Get Flight Cost

Source: statement reconstructed from the CodePath solution guide and written in our own words.
The original course page is behind a login, so wording and details may differ slightly.
Solution guide (only after you have tried!): https://github.com/codepath/compsci_guides/wiki/Get-Flight-Cost

PROBLEM
-------
`flights` maps each location to a list of (destination, cost) tuples. Write `calculate_cost(flights, start, dest)` that returns the total cost of any valid route from `start` to `dest`, or -1 if there is no route.

EXAMPLES (test cases from the solution guide)
---------------------------------------------
HAPPY CASE
Input: 
flights = {
    'LAX': [('SFO', 50)],
    'SFO': [('LAX', 50), ('ORD', 100), ('ERW', 210)],
    'ERW': [('SFO', 210), ('ORD', 300)],
    'ORD': [('ERW', 300), ('SFO', 100), ('MIA', 400)],
    'MIA': [('ORD', 400)]
}
start = 'LAX'
dest = 'MIA'

Output:
550
Explanation: One possible path is LAX -> SFO -> ORD -> MIA with total cost 50 + 100 + 400 = 550.

EDGE CASE
Input: 
flights = {
    'LAX': [('SFO', 50)],
    'SFO': [('LAX', 50)],
    'MIA': []
}
start = 'LAX'
dest = 'MIA'

Output:
-1
Explanation: There is no possible path from 'LAX' to 'MIA'.
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

def calculate_cost(flights, start, dest):
    pass
