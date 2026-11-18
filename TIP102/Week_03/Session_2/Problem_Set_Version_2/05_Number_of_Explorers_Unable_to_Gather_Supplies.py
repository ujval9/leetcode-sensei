r"""
TIP102 | Week 3 | Session 2 | Problem Set Version 2 | Problem 5
Number of Explorers Unable to Gather Supplies

Source: statement reconstructed from the CodePath solution guide and written in our own words.
The original course page is behind a login, so wording and details may differ slightly.
Solution guide (only after you have tried!): https://github.com/codepath/compsci_guides/wiki/Number-of-Explorers-Unable-to-Gather-Supplies

PROBLEM
-------
Supplies form a stack (supplies[0] on top) and explorers form a queue. The front explorer takes the top supply if it matches their preference; otherwise they move to the back of the queue. Stop when nobody in the queue wants the top supply. Return how many explorers are left without supplies.
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

from collections import deque


def count_explorers(explorers, supplies):
    pass


if __name__ == "__main__":
    # Example usage
    print(count_explorers([1, 1, 0, 0], [0, 1, 0, 1]))  # Output: 0
    print(count_explorers([1, 1, 1, 0, 0, 1], [1, 0, 0, 0, 1, 1]))  # Output: 3
