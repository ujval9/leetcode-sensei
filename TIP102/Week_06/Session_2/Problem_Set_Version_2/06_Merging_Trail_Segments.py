r"""
TIP102 | Week 6 | Session 2 | Problem Set Version 2 | Problem 6
Merging Trail Segments

Source: statement reconstructed from the CodePath solution guide and written in our own words.
The original course page is behind a login, so wording and details may differ slightly.
Solution guide (only after you have tried!): https://github.com/codepath/compsci_guides/wiki/Merging-Trail-Segments

PROBLEM
-------
The list starts and ends with 0, with 0s marking segment boundaries. Write `merge_trail(trailhead)` that replaces each segment between two 0s with a single node holding the sum of that segment, and removes all the 0s. Return the head.

EXAMPLES (test cases from the solution guide)
---------------------------------------------
HAPPY CASE
Input: trail1 = Node(0, Node(3, Node(1, Node(0, Node(4, Node(5, Node(2, Node(0))))))))
Output: 4 -> 11
Explanation: The modified list contains the sum of the segments between `0`s: 
- 3 + 1 = 4
- 4 + 5 + 2 = 11

EDGE CASE
Input: trail2 = Node(0, Node(1, Node(0, Node(3, Node(0, Node(2, Node(2, Node(0))))))))
Output: 1 -> 3 -> 4
Explanation: The modified list contains the sum of the segments between `0`s:
- 1 = 1
- 3 = 3
- 2 + 2 = 4
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


def merge_trail(trailhead):
    pass
