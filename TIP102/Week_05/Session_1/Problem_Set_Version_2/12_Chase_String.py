r"""
TIP102 | Week 5 | Session 1 | Problem Set Version 2 | Problem 12
Chase String

Source: statement reconstructed from the CodePath solution guide and written in our own words.
The original course page is behind a login, so wording and details may differ slightly.
Solution guide (only after you have tried!): https://github.com/codepath/compsci_guides/wiki/Chase-String

PROBLEM
-------
Write `chase_list(head)` that returns a string of all values in the linked list joined by " chases " (e.g. "Spike chases Tom chases Jerry"). Return an empty string for an empty list.

EXAMPLES (test cases from the solution guide)
---------------------------------------------
HAPPY CASE
Input: dog -> cat -> mouse -> cheese
Output: "Spike chases Tom chases Jerry chases Gouda"
Explanation: The values of the nodes are concatenated with "chases" as the separator.

EDGE CASE
Input: (empty list)
Output: ""
Explanation: The list is empty, so the function returns an empty string.
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


def chase_list(head):
    pass


if __name__ == "__main__":
    # Example usage
    dog = Node("Spike")
    cat = Node("Tom")
    mouse = Node("Jerry")
    cheese = Node("Gouda")

    dog.next = cat
    cat.next = mouse
    mouse.next = cheese

    print(chase_list(dog))  # Output: "Spike chases Tom chases Jerry chases Gouda"
