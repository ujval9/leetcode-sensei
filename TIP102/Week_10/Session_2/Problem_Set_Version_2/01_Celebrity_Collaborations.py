r"""
TIP102 | Week 10 | Session 2 | Problem Set Version 2 | Problem 1
Celebrity Collaborations

Source: statement reconstructed from the CodePath solution guide and written in our own words.
The original course page is behind a login, so wording and details may differ slightly.
Solution guide (only after you have tried!): https://github.com/codepath/compsci_guides/wiki/Celebrity-Collaborations

PROBLEM
-------
Each actor in `collaborations` maps to a list of (costar, number_of_films) tuples (undirected, weighted). Represent this as a graph and answer the question in the problem: return the costar each actor has collaborated with the most.

EXAMPLES (test cases from the solution guide)
---------------------------------------------
HAPPY CASE
Input: 
```python
collaborations = {
    "Chadwick Boseman": [("Lupita Nyong'o", 2), ("Robert Downey Jr.", 3), ("Mark Ruffalo", 2)],
    "Lupita Nyong'o": [("Chadwick Boseman", 2), ("Robert Downey Jr.", 1)],
    "Robert Downey Jr.": [("Chadwick Boseman", 3), ("Lupita Nyong'o", 1), ("Mark Ruffalo", 3)],
    "Mark Ruffalo": [("Chadwick Boseman", 2), ("Robert Downey Jr.", 3)]
}
print(collaborations["Chadwick Boseman"])
```
Output:
```markdown
[("Lupita Nyong'o", 2), ("Robert Downey Jr.", 3), ("Mark Ruffalo", 2)]
```

EDGE CASE
Input: 
```python
collaborations = {}
```
Output:
```markdown
[]
Explanation: If no actors or collaborations are present, the output is an empty list.
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

# Write your code here
