r"""
TIP102 | Week 3 | Session 2 | Problem Set Version 1 | Problem 4
Festival Booth Navigation

Source: statement reconstructed from the CodePath solution guide and written in our own words.
The original course page is behind a login, so wording and details may differ slightly.
Solution guide (only after you have tried!): https://github.com/codepath/compsci_guides/wiki/Festival-Booth-Navigation

PROBLEM
-------
Each clue is either a booth number (go to that booth) or "back" (return to the previous booth, undoing the last visit; ignore it if there is nothing to undo). Return the final list of booths in the order visited.
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

def booth_navigation(clues):
    pass


if __name__ == "__main__":
    # Example usage
    clues = [1, 2, "back", 3, 4]
    print(booth_navigation(clues))  # Output: [1, 3, 4]

    clues = [5, 3, 2, "back", "back", 7]
    print(booth_navigation(clues))  # Output: [5, 7]

    clues = [1, "back", 2, "back", "back", 3]
    print(booth_navigation(clues))  # Output: [3]
