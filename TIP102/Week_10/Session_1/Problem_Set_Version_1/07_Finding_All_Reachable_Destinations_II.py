r"""
TIP102 | Week 10 | Session 1 | Problem Set Version 1 | Problem 7
Finding All Reachable Destinations II

Source: statement reconstructed from the CodePath solution guide and written in our own words.
The original course page is behind a login, so wording and details may differ slightly.
Solution guide (only after you have tried!): https://github.com/codepath/compsci_guides/wiki/Finding-All-Reachable-Destinations-II

PROBLEM
-------
Same as Finding All Reachable Destinations, but use depth-first search and return the cities in DFS order.

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
Output: ['Beijing', 'Mexico City', 'Sydney', 'Tokyo', 'Helsinki', 'Cairo', 'Reykjavik', 'New York']
Explanation: Starting from Beijing, the DFS visits all reachable destinations in the order they are visited.

EDGE CASE
Input: 
flights = {
    "Tokyo": ["Sydney"],
    "Sydney": ["Tokyo"]
}
start = "Tokyo"
Output: ['Tokyo', 'Sydney']
Explanation: From Tokyo, the DFS explores Sydney as the only destination and returns both airports.
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

def get_all_destinations(flights, start):
    pass
