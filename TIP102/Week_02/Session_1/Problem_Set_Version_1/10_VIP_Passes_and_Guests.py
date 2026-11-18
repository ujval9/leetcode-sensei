r"""
TIP102 | Week 2 | Session 1 | Problem Set Version 1 | Problem 10
VIP Passes and Guests

Source: CodePath TIP102 course page (statement copied word for word from the course PDF).
Note: a few long lines were cut off at the right edge in the PDF; check the solution guide examples if a line looks incomplete.
Solution guide (only after you have tried!): https://github.com/codepath/compsci_guides/wiki/VIP-Passes-and-Guests

PROBLEM
-------
You're given strings vip_passes representing the types of guests
that have VIP passes, and guests representing the guests you have
at the music festival. Each character in guests is a type of guest
you have. You want to know how many of the guests you have are
also VIP pass holders.

Letters are case sensitive, so "a" is considered a diﬀerent type of
guest from "A".

Here is the pseudocode for the problem. Implement this in Python and
explain your implementation step-by-step.

 1. Create an empty set called vip_set.
 2. For each character in vip_passes, add it to vip_set.
 3. Initialize a counter variable to 0.
 4. For each character in guests:
    * If the character is in vip_set, increment the count by 1.
 5. Return the count.

 def num_VIP_guests(vip_passes, guests):
     pass

Example Usage:

 vip_passes1 = "aA"
 guests1 = "aAAbbbb"

 vip_passes2 = "z"
 guests2 = "ZZ"

 print(num_VIP_guests(vip_passes1, guests1))
 print(num_VIP_guests(vip_passes2, guests2))

Example Output:

 3
 0
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

def num_VIP_guests(vip_passes, guests):
    pass
