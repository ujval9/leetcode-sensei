r"""
TIP102 | Week 7 | Session 1 | Problem Set Version 1 | Problem 8
Merging Missions

Source: statement reconstructed from the CodePath solution guide and written in our own words.
The original course page is behind a login, so wording and details may differ slightly.
Solution guide (only after you have tried!): https://github.com/codepath/compsci_guides/wiki/Merging-Missions

PROBLEM
-------
Write a recursive `merge_missions(mission1, mission2)` that merges two sorted linked lists into one sorted linked list and returns its head.

EXAMPLES (test cases from the solution guide)
---------------------------------------------
HAPPY CASE
Input: mission1 = Node(1, Node(2, Node(4))), mission2 = Node(1, Node(3, Node(4)))
Output: 1 -> 1 -> 2 -> 3 -> 4 -> 4
Explanation: The merged linked list correctly combines the missions while maintaining sorted order.

EDGE CASE
Input: mission1 = None, mission2 = Node(1, Node(2, Node(3)))
Output: 1 -> 2 -> 3
Explanation: If one of the lists is empty, the merged list should just be the other list.

Input: mission1 = Node(5), mission2 = Node(1, Node(3, Node(7)))
Output: 1 -> 3 -> 5 -> 7
Explanation: Handles cases where the lists do not overlap in values.
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


# Helper for testing (provided)
def print_linked_list(head):
    current = head
    while current:
        print(current.value, end=" -> " if current.next else "\n")
        current = current.next


def merge_missions(mission1, mission2):
    pass
