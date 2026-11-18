r"""
TIP102 | Week 5 | Session 1 | Problem Set Version 1 | Problem 11
Saharah

Source: statement reconstructed from the CodePath solution guide and written in our own words.
The original course page is behind a login, so wording and details may differ slightly.
Solution guide (only after you have tried!): https://github.com/codepath/compsci_guides/wiki/Saharah

PROBLEM
-------
Starting from the list built in the previous problems, remove the `tom_nook` node from the front of the list and add a new node `saharah` after `tommy`.

EXAMPLES (test cases from the solution guide)
---------------------------------------------
HAPPY CASE
Input: A linked list with nodes `tom_nook -> timmy -> tommy`
Output: A linked list with nodes `timmy -> tommy -> saharah`
Explanation: The `tom_nook` node is removed and the `saharah` node is added to the end.
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
