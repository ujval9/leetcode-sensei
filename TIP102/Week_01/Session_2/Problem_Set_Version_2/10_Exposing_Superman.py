r"""
TIP102 | Week 1 | Session 2 | Problem Set Version 2 | Problem 10
Exposing Superman

Source: CodePath TIP102 course page (statement copied word for word from the course PDF).
Note: a few long lines were cut off at the right edge in the PDF; check the solution guide examples if a line looks incomplete.
Solution guide (only after you have tried!): https://github.com/codepath/compsci_guides/wiki/Exposing-Superman

PROBLEM
-------
 Metropolis has a population n , with each citizen assigned an integer
 id from 1 to n . There's a rumor that Superman is an ordinary
 citizen among this group.

 If Superman is an ordinary citizen, then:

       Superman trusts nobody.

       Everybody (except for Superman) trusts Superman.

       There is exactly one citizen that satisfies properties 1 and 2.

 Write a function expose_superman() that accepts a 2D array
   trust where trust[i] = [ai, bi] representing that the person
 labeled ai trusts the person labeled bi . If a trust relationship
 does not exist in trust array, then such a trust relationship does not
 exist.

 Return the label of Superman if he is hiding amongst the population
 and can be identified, or return -1 otherwise.

  def expose_superman(trust, n):
      pass

 Example Usage

  n = 2
  trust = [[1, 2]]
  expose_superman(trust, n)

  n = 3
  trust = [[1, 3], [2, 3]]

 expose_superman(trust, n)

 n = 3
 trust = [[1, 3], [2, 3], [3, 1]]
 expose_superman(trust, n)

Example Output:

 2
 3
 -1
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

def expose_superman(trust, n):
    pass
