r"""
TIP102 | Week 10 | Session 1 | Problem Set Version 1 | Problem 4
Converting Flight Representations

Source: statement reconstructed from the CodePath solution guide and written in our own words.
The original course page is behind a login, so wording and details may differ slightly.
Solution guide (only after you have tried!): https://github.com/codepath/compsci_guides/wiki/Converting-Flight-Representations

PROBLEM
-------
`flights` is a list of [a, b] pairs, each a two-way flight. Write `get_adj_dict(flights)` that returns an adjacency dictionary mapping each city to the list of cities it connects to.

EXAMPLES (test cases from the solution guide)
---------------------------------------------
HAPPY CASE
Input: flights = [['Cape Town', 'Addis Ababa'], ['Cairo', 'Lagos'], ['Lagos', 'Addis Ababa'], ['Nairobi', 'Cairo'], ['Cairo', 'Cape Town']]
Output: {
            'Cape Town': ['Addis Ababa', 'Cairo'],
            'Addis Ababa': ['Cape Town', 'Lagos'],
            'Lagos': ['Cairo', 'Addis Ababa'],
            'Cairo': ['Lagos', 'Nairobi', 'Cape Town'],
            'Nairobi': ['Cairo']
        }
Explanation: The list of flights is converted into an adjacency dictionary, representing the bidirectional connections.

EDGE CASE
Input: flights = []
Output: {}
Explanation: There are no flights, so the output is an empty dictionary.
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

def get_adj_dict(flights):
    pass
