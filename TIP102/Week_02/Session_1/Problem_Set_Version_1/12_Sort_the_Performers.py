r"""
TIP102 | Week 2 | Session 1 | Problem Set Version 1 | Problem 12
Sort the Performers

Source: CodePath TIP102 course page (statement copied word for word from the course PDF).
Note: a few long lines were cut off at the right edge in the PDF; check the solution guide examples if a line looks incomplete.
Solution guide (only after you have tried!): https://github.com/codepath/compsci_guides/wiki/Sort-the-Performers

PROBLEM
-------
You are given an array of strings performer_names , and an array
  performance_times that consists of distinct positive integers
representing the performance durations in minutes. Both arrays are of
length n .

For each index i , performer_names[i] and
 performance_times[i] denote the name and performance duration
of the i th performer.

Return performer_names sorted in descending order by the
performance durations.

 def sort_performers(performer_names, performance_times):
     '''
     :type performer_names: List[str]
     :type performance_times: List[int]
     :rtype: List[str]
     '''

Example Usage:

 performer_names1 = ["Mary", "John", "Emma"]
 performance_times1 = [180, 165, 170]

 performer_names2 = ["Alice", "Bob", "Bob"]
 performance_times2 = [155, 185, 150]

 print(sort_performers(performer_names1, performance_times1))
 print(sort_performers(performer_names2, performance_times2))

Example Output:

 ["Mary", "Emma", "John"]
 ["Bob", "Alice", "Bob"]
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

from collections import defaultdict


def sort_performers(performer_names, performance_times):
    pass
