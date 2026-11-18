r"""
TIP102 | Week 3 | Session 2 | Problem Set Version 1 | Problem 1
Manage Performance Stage Changes

Source: statement reconstructed from the CodePath solution guide and written in our own words.
The original course page is behind a login, so wording and details may differ slightly.
Solution guide (only after you have tried!): https://github.com/codepath/compsci_guides/wiki/Manage-Performance-Stage-Changes

PROBLEM
-------
Process a list of commands: "Schedule X" adds performance X, "Cancel" removes the most recently scheduled performance, and "Reschedule" restores the most recently cancelled one. Return the list of performances still scheduled at the end.
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

def manage_stage_changes(changes):
    pass


if __name__ == "__main__":
    # Example usage
    print(manage_stage_changes(["Schedule A", "Schedule B", "Cancel", "Schedule C", "Reschedule", "Schedule D"]))  
    # Output: ["A", "C", "B", "D"]

    print(manage_stage_changes(["Schedule A", "Cancel", "Schedule B", "Cancel", "Reschedule", "Cancel"])) 
    # Output: []

    print(manage_stage_changes(["Schedule X", "Schedule Y", "Cancel", "Cancel", "Schedule Z"])) 
    # Output: ["Z"]
