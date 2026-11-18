r"""
TIP102 | Week 5 | Session 1 | Problem Set Version 2 | Problem 9
Tom and Jerry

Source: statement reconstructed from the CodePath solution guide and written in our own words.
The original course page is behind a login, so wording and details may differ slightly.
Solution guide (only after you have tried!): https://github.com/codepath/compsci_guides/wiki/Tom-and-Jerry

PROBLEM
-------
Create a linked list where a node with value "Tom" points to a node with value "Jerry".

EXAMPLES (test cases from the solution guide)
---------------------------------------------
HAPPY CASE
Input: Node("Tom") -> Node("Jerry")
Output:
Tom
<__main__.Node object at 0x...>
Jerry
Jerry
None
Explanation: The "Tom" node points to the "Jerry" node, and "Jerry" is the last node in the list, so its `next` is `None`.

EDGE CASE
Input: Node("Tom") -> None
Output:
Tom
None
Explanation: If "Tom" has no next node, its `next` should be `None`.
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
