r"""
TIP102 | Week 2 | Session 1 | Problem Set Version 2 | Problem 8
Find the Difference of Two Signal Arrays

Source: CodePath TIP102 course page (statement copied word for word from the course PDF).
Note: a few long lines were cut off at the right edge in the PDF; check the solution guide examples if a line looks incomplete.
Solution guide (only after you have tried!): https://github.com/codepath/compsci_guides/wiki/Find-the-Difference-of-Two-Signal-Arrays

PROBLEM
-------
You are given two 0-indexed integer arrays signals1 and
  signals2 , representing signal data from two diﬀerent probes.
 Return a list answer of size 2 where:

       answer[0] is a list of all distinct integers in signals1 which
      are not present in signals2 .

       answer[1] is a list of all distinct integers in signals2 which
      are not present in signals1 .

 Note that the integers in the lists may be returned in any order.

 Below is the pseudocode for the problem. Implement this in Python
 and explain your implementation step-by-step.

  1. Convert signals1 and signals2 to sets.
  2. Find the difference between set1 and set2 and store it in diff1.
  3. Find the difference between set2 and set1 and store it in diff2.
  4. Return the list [diff1, diff2].

  def find_difference(signals1, signals2):
      pass

 Example Usage:

  signals1_example1 = [1, 2, 3]
  signals2_example1 = [2, 4, 6]

  signals1_example2 = [1, 2, 3, 3]
  signals2_example2 = [1, 1, 2, 2]

  print(find_difference(signals1_example1, signals2_example1))
  print(find_difference(signals1_example2, signals2_example2))

 Example Output:

  [[1, 3], [4, 6]]
  [[3], []]
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

def find_difference(signals1, signals2):
    pass
