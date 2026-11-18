r"""
TIP102 | Week 5 | Session 1 | Problem Set Version 2 | Problem 5
Add Special Item

Source: statement reconstructed from the CodePath solution guide and written in our own words.
The original course page is behind a login, so wording and details may differ slightly.
Solution guide (only after you have tried!): https://github.com/codepath/compsci_guides/wiki/Add-Special-Item

PROBLEM
-------
Add a method `add_item(self, item_name)` to `Player` that appends `item_name` to the player's `items` list only if it is one of the valid special items.

EXAMPLES (test cases from the solution guide)
---------------------------------------------
HAPPY CASE
Input: add_item("red shell")
Output: items = ["red shell"]
Explanation: The `item_name` "red shell" is valid, so it is added to the `items` list.

EDGE CASE
Input: add_item("super smash")
Output: items = ["red shell"]
Explanation: The `item_name` "super smash" is not valid, so it is not added to the `items` list.
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

class Player():

    def __init__(self, character, kart):
        self.character = character
        self.kart = kart
        self.items = []

    def add_item(self, item_name):
        pass
