r"""
TIP102 | Week 5 | Session 2 | Problem Set Version 1 | Problem 2
Linked Up

Source: statement reconstructed from the CodePath solution guide and written in our own words.
The original course page is behind a login, so wording and details may differ slightly.
Solution guide (only after you have tried!): https://github.com/codepath/compsci_guides/wiki/Linked-Up

PROBLEM
-------
Using the `Node` class, build the linked list described in the problem (e.g. Isabelle -> Saharah -> C.J.) and print it with `print_linked_list(head)`.

EXAMPLES (test cases from the solution guide)
---------------------------------------------
HAPPY CASE
Input: Nodes with values "K.K. Slider", "Harriet", "Saharah", "Isabelle"
Output: "K.K. Slider -> Harriet -> Saharah -> Isabelle"
Explanation: The nodes are linked in the correct order.

EDGE CASE
Input: A single node with value "Isabelle"
Output: "Isabelle"
Explanation: The list contains only one node.
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


def print_linked_list(head):
    pass


if __name__ == "__main__":
    kk_slider = Node("K.K. Slider")
    harriet = Node("Harriet")
    saharah = Node("Saharah")
    isabelle = Node("Isabelle")

    # Link the nodes to form the linked list
    kk_slider.next = harriet
    harriet.next = saharah
    saharah.next = isabelle

    # Example Usage:
    print_linked_list(kk_slider)  # Output: "K.K. Slider -> Harriet -> Saharah -> Isabelle"
