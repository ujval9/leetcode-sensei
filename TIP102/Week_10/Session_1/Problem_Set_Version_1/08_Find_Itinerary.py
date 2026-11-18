r"""
TIP102 | Week 10 | Session 1 | Problem Set Version 1 | Problem 8
Find Itinerary

Source: statement reconstructed from the CodePath solution guide and written in our own words.
The original course page is behind a login, so wording and details may differ slightly.
Solution guide (only after you have tried!): https://github.com/codepath/compsci_guides/wiki/Find-Itinerary

PROBLEM
-------
Each boarding pass is a (departure, arrival) tuple, and together they form one trip with no repeated cities. Write `find_itinerary(flights)` that returns the list of cities in travel order, starting from the city that is never an arrival.

EXAMPLES (test cases from the solution guide)
---------------------------------------------
HAPPY CASE
Input: boarding_passes = [
                    ("JFK", "ATL"),
                    ("SFO", "JFK"),
                    ("ATL", "ORD"),
                    ("LAX", "SFO")]
Output: ['LAX', 'SFO', 'JFK', 'ATL', 'ORD']
Explanation: The correct itinerary starts at LAX, then proceeds to SFO, JFK, ATL, and finally ORD.

EDGE CASE
Input: boarding_passes = [
                    ("LAX", "DXB"),
                    ("DFW", "JFK"),
                    ("LHR", "DFW"),
                    ("JFK", "LAX")]
Output: ['LHR', 'DFW', 'JFK', 'LAX', 'DXB']
Explanation: The correct itinerary starts at LHR, proceeds to DFW, JFK, LAX, and finally DXB.
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

def find_itinerary(flights):
    pass
