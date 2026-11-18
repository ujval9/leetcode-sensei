r"""
TIP102 | Week 5 | Session 1 | Problem Set Version 1 | Problem 12
Print Players Linked List

Source: statement reconstructed from the CodePath solution guide and written in our own words.
The original course page is behind a login, so wording and details may differ slightly.
Solution guide (only after you have tried!): https://github.com/codepath/compsci_guides/wiki/Print-Players-Linked-List

PROBLEM
-------
Write `print_list(head)` that prints the values of a linked list separated by " -> " (for example: "Isabelle -> Saharah -> C.J.").

EXAMPLES (test cases from the solution guide)
---------------------------------------------
HAPPY CASE
Input: A linked list with nodes `isabelle -> saharah -> cj`
Output: `"Isabelle -> Saharah -> C.J."`
Explanation: The values of the nodes are concatenated with the `"->"` separator.

EDGE CASE
Input: An empty linked list.
Output: `""`
Explanation: There are no values to concatenate, so the result is an empty string.
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


def print_list(head):
    pass


if __name__ == "__main__":
    # Example Usage:
    isabelle = Node("Isabelle")
    saharah = Node("Saharah")
    cj = Node("C.J.")

    isabelle.next = saharah
    saharah.next = cj

    print(print_list(isabelle))  # Output: "Isabelle -> Saharah -> C.J."
