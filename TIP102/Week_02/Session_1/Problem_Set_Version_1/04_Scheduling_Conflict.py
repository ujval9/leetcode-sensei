r"""
TIP102 | Week 2 | Session 1 | Problem Set Version 1 | Problem 4
Scheduling Conflict

Source: CodePath TIP102 course page (statement copied word for word from the course PDF).
Note: a few long lines were cut off at the right edge in the PDF; check the solution guide examples if a line looks incomplete.
Solution guide (only after you have tried!): https://github.com/codepath/compsci_guides/wiki/Scheduling-Conflict

PROBLEM
-------
Demand for your festival has exceeded expectations, so you're
expanding the festival to span two diﬀerent venues. Some artists will
perform both venues, while others will perform at just one. To ensure
that there are no scheduling conflicts, implement a function
 identify_conflicts() that accepts two dictionaries
 venue1_schedule and venue2_schedule each mapping the
artists playing at the venue to their set times. Return a dictionary
containing the key-value pairs that are the same in each schedule.

 def identify_conflicts(venue1_schedule, venue2_schedule):
     pass

Example Usage:

 venue1_schedule = {
     "Stromae": "9:00 PM",
     "Janelle Monáe": "8:00 PM",
     "HARDY": "7:00 PM",
     "Bruce Springsteen": "6:00 PM"
 }

 venue2_schedule = {
     "Stromae": "9:00 PM",
     "Janelle Monáe": "10:30 PM",
     "HARDY": "7:00 PM",
     "Wizkid": "6:00 PM"
 }

 print(identify_conflicts(venue1_schedule, venue2_schedule))

Example Output:

 {"Stromae": "9:00 PM", "HARDY": "7:00 PM"}
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

def identify_conflicts(venue1_schedule, venue2_schedule):
    pass
