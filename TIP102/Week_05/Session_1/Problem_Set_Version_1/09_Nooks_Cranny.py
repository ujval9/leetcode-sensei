r"""
TIP102 | Week 5 | Session 1 | Problem Set Version 1 | Problem 9
Nook's Cranny

Source: statement reconstructed from the CodePath solution guide and written in our own words.
The original course page is behind a login, so wording and details may differ slightly.
Solution guide (only after you have tried!): https://github.com/codepath/compsci_guides/wiki/Nook's-Cranny

PROBLEM
-------
Using the given `Node` class, create nodes for the shop owners and link them with `next` pointers to build the described linked list (e.g. Tom Nook -> Tommy).

EXAMPLES (test cases from the solution guide)
---------------------------------------------
HAPPY CASE
Input: 
tom_nook = Node("Tom Nook")
tommy = Node("Tommy")
tom_nook.next = tommy
print(tom_nook.value) # Output: Tom Nook
print(tom_nook.next.value) # Output: Tommy
print(tommy.value) # Output: Tommy
print(tommy.next) # Output: None

Explanation: 
The linked list is created correctly, with `tom_nook` pointing to `tommy`.

EDGE CASE
Input: 
node1 = Node("Node 1")
print(node1.value) # Output: Node 1
print(node1.next) # Output: None

Explanation: 
A single node without a next node should have its `next` attribute set to `None`.
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
