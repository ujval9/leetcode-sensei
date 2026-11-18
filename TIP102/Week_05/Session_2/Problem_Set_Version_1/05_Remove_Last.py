r"""
TIP102 | Week 5 | Session 2 | Problem Set Version 1 | Problem 5
Remove Last

Source: statement reconstructed from the CodePath solution guide and written in our own words.
The original course page is behind a login, so wording and details may differ slightly.
Solution guide (only after you have tried!): https://github.com/codepath/compsci_guides/wiki/Remove-Last

PROBLEM
-------
Write `delete_tail(head)` that removes the last node of a linked list and returns the head. If the list is empty or has one node, return None.

EXAMPLES (test cases from the solution guide)
---------------------------------------------
HAPPY CASE
Input: Node("A") -> Node("B") -> Node("C")
Output: Node("A") -> Node("B")
Explanation: The last node "C" is removed.

EDGE CASE
Input: Node("A")
Output: None
Explanation: The only node is removed.
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


def delete_tail(head):
    pass
