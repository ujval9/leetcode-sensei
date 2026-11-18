r"""
TIP102 | Week 5 | Session 1 | Problem Set Version 1 | Problem 5
Add Furniture

Source: statement reconstructed from the CodePath solution guide and written in our own words.
The original course page is behind a login, so wording and details may differ slightly.
Solution guide (only after you have tried!): https://github.com/codepath/compsci_guides/wiki/Add-Furniture

PROBLEM
-------
Add a method `add_item(self, item_name)` to `Villager`. If `item_name` is one of "acoustic guitar", "ironwood kitchenette", "rattan armchair", "kotatsu", or "cacao tree", append it to the villager's `furniture` list; otherwise do nothing.

EXAMPLES (test cases from the solution guide)
---------------------------------------------
HAPPY CASE
Input: 
alice = Villager("Alice", "Koala", "Normal", "guvnor")
alice.add_item("acoustic guitar")
print(alice.furniture)

Output: 
["acoustic guitar"]

Explanation: 
The `item_name` is valid, so it is added to the `furniture` attribute of `alice`.

EDGE CASE
Input: 
alice = Villager("Alice", "Koala", "Normal", "guvnor")
alice.add_item("nintendo switch")
print(alice.furniture)

Output: 
Invalid item
[]

Explanation: 
The `item_name` is invalid, so it is not added to the `furniture` attribute of `alice`, and an error message is printed.
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

class Villager:

    def __init__(self, name, species, personality, catchphrase):
        self.name = name
        self.species = species
        self.personality = personality
        self.catchphrase = catchphrase
        self.furniture = []

    def add_item(self, item_name):
        pass
