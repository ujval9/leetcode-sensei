r"""
TIP102 | Week 5 | Session 1 | Problem Set Version 1 | Problem 1
New Horizons

Source: statement reconstructed from the CodePath solution guide and written in our own words.
The original course page is behind a login, so wording and details may differ slightly.
Solution guide (only after you have tried!): https://github.com/codepath/compsci_guides/wiki/New-Horizons

PROBLEM
-------
Write a `Villager` class whose constructor takes `name`, `species`, and `catchphrase` and stores them as attributes, plus a `furniture` attribute that starts as an empty list. Then create a villager named "Apollo", an "Eagle" whose catchphrase is "pah", and print its attributes.

EXAMPLES (test cases from the solution guide)
---------------------------------------------
HAPPY CASE
Input: 
apollo = Villager("Apollo", "Eagle", "pah")
print(apollo.name) 
print(apollo.species) 
print(apollo.catchphrase) 
print(apollo.furniture) 

Output: 
"Apollo"
"Eagle"
"pah"
[]

Explanation: 
The `Villager` object is instantiated correctly with the given attributes, and the default furniture list is empty.

EDGE CASE
Input: 
villager = Villager("", "", "")
print(villager.name) 
print(villager.species) 
print(villager.catchphrase) 
print(villager.furniture) 

Output: 
""
""
""
[]

Explanation: 
Even with empty string attributes, the `Villager` object should be instantiated correctly, and the default furniture list should still be empty.
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

    def __init__(self, name, species, catchphrase):
        pass
