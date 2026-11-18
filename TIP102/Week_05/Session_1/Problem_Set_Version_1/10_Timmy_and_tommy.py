r"""
TIP102 | Week 5 | Session 1 | Problem Set Version 1 | Problem 10
Timmy and tommy

Source: statement reconstructed from the CodePath solution guide and written in our own words.
The original course page is behind a login, so wording and details may differ slightly.
Solution guide (only after you have tried!): https://github.com/codepath/compsci_guides/wiki/Timmy-and-tommy

PROBLEM
-------
Insert a new node (Timmy) between two existing nodes (Tom Nook and Tommy) by updating the `next` pointers.

EXAMPLES (test cases from the solution guide)
---------------------------------------------
HAPPY CASE
Input: 
tom_nook = Node("Tom Nook")
tommy = Node("Tommy")
timmy = Node("Timmy", tommy)
tom_nook.next = timmy
print(tom_nook.value) # Output: Tom Nook
print(tom_nook.next.value) # Output: Timmy
print(timmy.value) # Output: Timmy
print(timmy.next.value) # Output: Tommy
print(tommy.value) # Output: Tommy
print(tommy.next) # Output: None

Explanation: 
The linked list is correctly updated to include `timmy` between `tom_nook` and `tommy`.

EDGE CASE
Input: 
node1 = Node("Node 1")
node2 = Node("Node 2")
node1.next = node2
new_node = Node("New Node", node2)
node1.next = new_node
print(node1.value) # Output: Node 1
print(node1.next.value) # Output: New Node
print(new_node.value) # Output: New Node
print(new_node.next.value) # Output: Node 2

Explanation: 
The new node is correctly inserted between the two existing nodes.
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
