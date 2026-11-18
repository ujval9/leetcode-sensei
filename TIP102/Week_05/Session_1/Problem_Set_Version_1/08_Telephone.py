r"""
TIP102 | Week 5 | Session 1 | Problem Set Version 1 | Problem 8
Telephone

Source: statement reconstructed from the CodePath solution guide and written in our own words.
The original course page is behind a login, so wording and details may differ slightly.
Solution guide (only after you have tried!): https://github.com/codepath/compsci_guides/wiki/Telephone

PROBLEM
-------
Each `Villager` has a `neighbor` attribute pointing to another villager (or None). A message is passed from neighbor to neighbor. Write `message_received(start_villager, target_villager)` that returns True if a message starting at `start_villager` reaches `target_villager`, otherwise False.

EXAMPLES (test cases from the solution guide)
---------------------------------------------
HAPPY CASE
Input: 
isabelle = Villager("Isabelle", "Dog", "Normal", "what's up?")
tom_nook = Villager("Tom Nook", "Raccoon", "Cranky", "yes, yes")
kk_slider = Villager("K.K. Slider", "Dog", "Lazy", "dig it")
isabelle.neighbor = tom_nook
tom_nook.neighbor = kk_slider
result = message_received(isabelle, kk_slider)

Output: 
True

Explanation: 
The message can be passed from Isabelle to Tom Nook, and then from Tom Nook to KK Slider.

EDGE CASE
Input: 
isabelle = Villager("Isabelle", "Dog", "Normal", "what's up?")
kk_slider = Villager("K.K. Slider", "Dog", "Lazy", "dig it")
result = message_received(kk_slider, isabelle)

Output: 
False

Explanation: 
KK Slider has no neighbor, so the message cannot be passed to Isabelle.
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
    def __init__(self, name, species, personality, catchphrase, neighbor=None):
        self.name = name
        self.species = species
        self.personality = personality
        self.catchphrase = catchphrase
        self.furniture = []
        self.neighbor = neighbor


def message_received(start_villager, target_villager):
    pass
