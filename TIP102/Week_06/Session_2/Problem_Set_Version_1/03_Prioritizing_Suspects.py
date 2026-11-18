r"""
TIP102 | Week 6 | Session 2 | Problem Set Version 1 | Problem 3
Prioritizing Suspects

Source: statement reconstructed from the CodePath solution guide and written in our own words.
The original course page is behind a login, so wording and details may differ slightly.
Solution guide (only after you have tried!): https://github.com/codepath/compsci_guides/wiki/Prioritizing-Suspects

PROBLEM
-------
Write `partition(suspect_ratings, threshold)` that rearranges a linked list so all nodes with values greater than `threshold` come before nodes with values less than or equal to it. Return the new head.

EXAMPLES (test cases from the solution guide)
---------------------------------------------
HAPPY CASE
Input: suspect_ratings = Node(1, Node(4, Node(3, Node(2, Node(5, Node(2)))))) 
       threshold = 3
Output: 4 -> 5 -> 1 -> 3 -> 2 -> 2
Explanation: The nodes with values greater than 3 come first, followed by nodes with values less than or equal to 3.

EDGE CASE
Input: suspect_ratings = Node(3, Node(3, Node(3)))
       threshold = 3
Output: 3 -> 3 -> 3
Explanation: All nodes have values equal to the threshold, so their order remains unchanged.
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


def partition(suspect_ratings, threshold):
    pass
