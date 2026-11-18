r"""
TIP102 | Week 6 | Session 1 | Problem Set Version 2 | Problem 6
Magic Loop

Source: statement reconstructed from the CodePath solution guide and written in our own words.
The original course page is behind a login, so wording and details may differ slightly.
Solution guide (only after you have tried!): https://github.com/codepath/compsci_guides/wiki/Magic-Loop

PROBLEM
-------
Write `loop_start(path_start)` that returns the value of the node where a cycle begins in a linked list, or None if there is no cycle.

EXAMPLES (test cases from the solution guide)
---------------------------------------------
HAPPY CASE
Input: path_start = Node("Mystic Falls"), with subsequent nodes leading to a cycle starting at "Troll's Bridge"
Output: "Troll's Bridge"
Explanation: The linked list has a cycle that begins at "Troll's Bridge".

EDGE CASE
Input: path_start = None
Output: None
Explanation: An empty list has no cycle.

EDGE CASE
Input: path_start = Node("Mystic Falls"), with no cycle
Output: None
Explanation: A list with no cycle should return None.
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

class Node:
    def __init__(self, value, next=None):
        self.value = value
        self.next = next


def loop_start(path_start):
    pass
