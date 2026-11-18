r"""
TIP102 | Week 2 | Session 1 | Problem Set Version 2 | Problem 11
Sort Signal Data

Source: CodePath TIP102 course page (statement copied word for word from the course PDF).
Note: a few long lines were cut off at the right edge in the PDF; check the solution guide examples if a line looks incomplete.
Solution guide (only after you have tried!): https://github.com/codepath/compsci_guides/wiki/Sort-Signal-Data

PROBLEM
-------
Ground control needs to analyze the frequency of signal data received
from diﬀerent probes. Given an array of integers signals , sort the
array in increasing order based on the frequency of the values. If
multiple values have the same frequency, sort them in decreasing
order. Return the sorted array.

Below is a buggy or incomplete version of the solution. Identify and fix
the bugs in the code. Then, perform a code review and suggest
improvements.

 def frequency_sort(signals):
     freq = {}
     for signal in signals:
         if signal in freq:
             freq[signal] += 1
         else:
             freq[signal] = 0

      sorted_signals = sorted(signals, key=lambda x: (freq[x], x))

      return sorted_signals

Example Usage:

 signals1 = [1, 1, 2, 2, 2, 3]
 signals2 = [2, 3, 1, 3, 2]
 signals3 = [-1, 1, -6, 4, 5, -6, 1, 4, 1]

 print(frequency_sort(signals1))
 print(frequency_sort(signals2))
 print(frequency_sort(signals3))

Example Output:

 [3, 1, 1, 2, 2, 2]
 [1, 3, 3, 2, 2]
 [5, -1, 4, 4, -6, -6, 1, 1, 1]
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

def frequency_sort(signals):
    pass
