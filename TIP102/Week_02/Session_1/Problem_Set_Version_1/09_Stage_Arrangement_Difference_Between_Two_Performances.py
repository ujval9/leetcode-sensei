r"""
TIP102 | Week 2 | Session 1 | Problem Set Version 1 | Problem 9
Stage Arrangement Difference Between Two Performances

Source: CodePath TIP102 course page (statement copied word for word from the course PDF).
Note: a few long lines were cut off at the right edge in the PDF; check the solution guide examples if a line looks incomplete.
Solution guide (only after you have tried!): https://github.com/codepath/compsci_guides/wiki/Stage-Arrangement-Difference-Between-Two-Performances

PROBLEM
-------
You are given two lists of strings s and t representing the stage
 arrangements of performers in two diﬀerent performances at a music
 festival, such that every performer occurs at most once in s and
  t , and t is a permutation of s .

 The stage arrangement diﬀerence between s and t is defined as
 the sum of the absolute diﬀerence between the index of the
 occurrence of each performer in s and the index of the occurrence
 of the same performer in t .

 Return the stage arrangement diﬀerence between s and t .

 A permutation is a rearrangement of a sequence. For example,
  [3, 1, 2] and [2, 1 , 3] are both permutations of the list
  [1, 2, 3] .

  def find_stage_arrangement_difference(s, t):
      '''
      :type s: List[str]
      :type t: List[str]
      :rtype: int
      '''

 Example Usage:

  s1 = ["Alice", "Bob", "Charlie"]
  t1 = ["Bob", "Alice", "Charlie"]
  s2 = ["Alice", "Bob", "Charlie", "David", "Eve"]
  t2 = ["Eve", "David", "Bob", "Alice", "Charlie"]

  print(find_stage_arrangement_difference(s1, t1))
  print(find_stage_arrangement_difference(s2, t2))

 Example Output:

  2
  12
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

def find_stage_arrangement_difference(s, t):
    pass
