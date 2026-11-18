r"""
TIP102 | Week 7 | Session 2 | Problem Set Version 1 | Problem 2
Booking the Perfect Cruise Cabin

Source: statement reconstructed from the CodePath solution guide and written in our own words.
The original course page is behind a login, so wording and details may differ slightly.
Solution guide (only after you have tried!): https://github.com/codepath/compsci_guides/wiki/Booking-the-Perfect-Cruise-Cabin

PROBLEM
-------
`cabins` is a sorted list of deck numbers. Using recursive binary search between indices `left` and `right`, return the index of `preferred_deck` if present, otherwise the index where it would be inserted to keep the list sorted.

EXAMPLES (test cases from the solution guide)
---------------------------------------------
HAPPY CASE
Input: cabins = [1, 3, 5, 6], preferred_deck = 5
Output: 2
Explanation: The preferred deck is found at index 2.

Input: cabins = [1, 3, 5, 6], preferred_deck = 2
Output: 1
Explanation: The preferred deck is not found, but it should be inserted at index 1 to maintain sorted order.

EDGE CASE
Input: cabins = [1, 3, 5, 6], preferred_deck = 0
Output: 0
Explanation: The preferred deck is less than all the cabins, so it should be inserted at index 0.

Input: cabins = [1, 3, 5, 6], preferred_deck = 7
Output: 4
Explanation: The preferred deck is greater than all the cabins, so it should be inserted at the end.
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

def find_cabin_index(cabins, preferred_deck):
    pass
