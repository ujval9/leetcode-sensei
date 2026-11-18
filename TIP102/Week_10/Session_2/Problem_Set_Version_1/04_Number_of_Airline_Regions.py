r"""
TIP102 | Week 10 | Session 2 | Problem Set Version 1 | Problem 4
Number of Airline Regions

Source: statement reconstructed from the CodePath solution guide and written in our own words.
The original course page is behind a login, so wording and details may differ slightly.
Solution guide (only after you have tried!): https://github.com/codepath/compsci_guides/wiki/Number-of-Airline-Regions

PROBLEM
-------
`is_connected` is an n x n matrix where `is_connected[i][j] == 1` means a direct flight between airports i and j. A region is a group of airports connected directly or indirectly. Write `num_airline_regions(is_connected)` that returns the number of regions.

EXAMPLES (test cases from the solution guide)
---------------------------------------------
HAPPY CASE
Input: is_connected = [
                      [1, 1, 0],  # Airport 0
                      [1, 1, 0],  # Airport 1
                      [0, 0, 1]   # Airport 2
                     ]
Output: 2
Explanation: Airports 0 and 1 are directly connected, forming one region, while airport 2 is isolated, forming another region.

EDGE CASE
Input: is_connected = [
                      [1, 0, 0, 1],  # Airport 0
                      [0, 1, 1, 0],  # Airport 1
                      [0, 1, 1, 0],  # Airport 2
                      [1, 0, 0, 1]   # Airport 3
                     ]
Output: 2
Explanation: Airports 0 and 3 are connected, forming one region, and airports 1 and 2 are connected, forming another region.
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

def num_airline_regions(is_connected):
    pass
