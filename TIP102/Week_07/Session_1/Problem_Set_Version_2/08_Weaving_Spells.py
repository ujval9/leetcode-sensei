r"""
TIP102 | Week 7 | Session 1 | Problem Set Version 2 | Problem 8
Weaving Spells

Source: statement reconstructed from the CodePath solution guide and written in our own words.
The original course page is behind a login, so wording and details may differ slightly.
Solution guide (only after you have tried!): https://github.com/codepath/compsci_guides/wiki/Weaving-Spells

PROBLEM
-------
Write a recursive `weave_spells(spell_a, spell_b)` that interleaves two linked lists by alternating nodes (a1, b1, a2, b2, ...). If one list runs out, attach the rest of the other. Return the new head.

EXAMPLES (test cases from the solution guide)
---------------------------------------------
HAPPY CASE
Input: 
spell_a = Node('A', Node('C', Node('E')))
spell_b = Node('B', Node('D', Node('F')))
Output: A -> B -> C -> D -> E -> F
Explanation: The nodes from both linked lists are alternated to create the resulting list.

EDGE CASE
Input: spell_a = Node('A'), spell_b = None
Output: A
Explanation: If one list is empty, the other list should be returned as it is.
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


def weave_spells(spell_a, spell_b):
    pass
