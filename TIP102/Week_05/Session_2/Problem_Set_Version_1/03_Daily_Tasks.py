r"""
TIP102 | Week 5 | Session 2 | Problem Set Version 1 | Problem 3
Daily Tasks

Source: statement reconstructed from the CodePath solution guide and written in our own words.
The original course page is behind a login, so wording and details may differ slightly.
Solution guide (only after you have tried!): https://github.com/codepath/compsci_guides/wiki/Daily-Tasks

PROBLEM
-------
Write `add_task(head, task)` that adds a new node with value `task` to the front of a linked list of tasks and returns the new head.

EXAMPLES (test cases from the solution guide)
---------------------------------------------
HAPPY CASE
Input: head = Node("shake tree") -> Node("dig fossils") -> Node("catch bugs"), task = "check turnip prices"
Output: Node("check turnip prices") -> Node("shake tree") -> Node("dig fossils") -> Node("catch bugs")
Explanation: The new task is added to the front of the task list.

EDGE CASE
Input: head = None, task = "start new task"
Output: Node("start new task")
Explanation: When the initial task list is empty, the new task becomes the head.
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


def add_task(head, task):
    pass
