r"""
TIP102 | Week 6 | Session 2 | Problem Set Version 2 | Problem 4
Controlled Burns

Source: statement reconstructed from the CodePath solution guide and written in our own words.
The original course page is behind a login, so wording and details may differ slightly.
Solution guide (only after you have tried!): https://github.com/codepath/compsci_guides/wiki/Controlled-Burns

PROBLEM
-------
Write `selective_trail_clearing(trailhead, m, n)` that keeps the first `m` nodes, removes the next `n`, and repeats this pattern to the end of the list. Return the head.

EXAMPLES (test cases from the solution guide)
---------------------------------------------
HAPPY CASE
Input: trailhead = Node(1, Node(2, Node(3, Node(4, Node(5, Node(6, Node(7, Node(8, Node(9, Node(10))))))))))
       m = 2
       n = 3
Output: 1 -> 2 -> 6 -> 7
Explanation: The function keeps the first 2 nodes (1, 2), deletes the next 3 nodes (3, 4, 5), keeps the next 2 nodes (6, 7), and deletes the remaining 3 nodes (8, 9, 10).

EDGE CASE
Input: trailhead = Node(1, Node(2, Node(3)))
       m = 1
       n = 2
Output: 1
Explanation: The function keeps the first node, deletes the next 2 nodes, and stops as it reaches the end of the list.
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


def selective_trail_clearing(trailhead, m, n):
    pass
