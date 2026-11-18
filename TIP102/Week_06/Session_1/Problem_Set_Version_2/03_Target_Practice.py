r"""
TIP102 | Week 6 | Session 1 | Problem Set Version 2 | Problem 3
Target Practice

Source: statement reconstructed from the CodePath solution guide and written in our own words.
The original course page is behind a login, so wording and details may differ slightly.
Solution guide (only after you have tried!): https://github.com/codepath/compsci_guides/wiki/Target-Practice

PROBLEM
-------
Write `find_middle_potion(potions)` that returns the value of the middle node of a linked list. If there are two middle nodes, return the second one.

EXAMPLES (test cases from the solution guide)
---------------------------------------------
HAPPY CASE
Input: potions1 = Node("Poison Antidote", Node("Shrinking Solution", Node("Trollblood Tincture")))
Output: "Shrinking Solution"
Explanation: "Shrinking Solution" is the middle potion in the list.

HAPPY CASE
Input: potions2 = Node("Elixir of Life", Node("Sleeping Draught", Node("Babbling Beverage", Node("Aging Potion"))))
Output: "Babbling Beverage"
Explanation: "Babbling Beverage" is the second middle potion in the list with an even number of nodes.

EDGE CASE
Input: potions = None
Output: None
Explanation: If the list is empty, return None.
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
    def __init__(self, potion, next=None):
        self.potion = potion
        self.next = next


def find_middle_potion(potions):
    pass
