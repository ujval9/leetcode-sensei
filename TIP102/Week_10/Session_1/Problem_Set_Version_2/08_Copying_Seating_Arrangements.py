r"""
TIP102 | Week 10 | Session 1 | Problem Set Version 2 | Problem 8
Copying Seating Arrangements

Source: statement reconstructed from the CodePath solution guide and written in our own words.
The original course page is behind a login, so wording and details may differ slightly.
Solution guide (only after you have tried!): https://github.com/codepath/compsci_guides/wiki/Copying-Seating-Arrangements

PROBLEM
-------
Each `Node` is a guest with a `val` (name) and a `neighbors` list of the guests sitting next to them (an undirected graph). Write `copy_seating(seat)` that returns a deep copy of the whole connected seating graph, starting from `seat`.

EXAMPLES (test cases from the solution guide)
---------------------------------------------
HAPPY CASE
Input: 
lily = Node("Lily Gladstone")
mark = Node("Mark Ruffalo")
cillian = Node("Cillian Murphy")
danielle = Node("Danielle Brooks")
lily.neighbors.extend([mark, danielle])
mark.neighbors.extend([lily, cillian])
cillian.neighbors.extend([danielle, mark])
danielle.neighbors.extend([lily, cillian])
Output: A deep copy of the seating arrangement graph starting from `lily`.

EDGE CASE
Input: 
lily = Node("Lily Gladstone")
lily.neighbors = []
Output: A copy of the node `lily` with no neighbors.
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

class Node():
    def __init__(self, val = 0, neighbors = None):
        self.val = val
        self.neighbors = neighbors if neighbors is not None else []


def copy_seating(seat):
    pass
