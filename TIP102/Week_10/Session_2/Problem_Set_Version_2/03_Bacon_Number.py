r"""
TIP102 | Week 10 | Session 2 | Problem Set Version 2 | Problem 3
Bacon Number

Source: statement reconstructed from the CodePath solution guide and written in our own words.
The original course page is behind a login, so wording and details may differ slightly.
Solution guide (only after you have tried!): https://github.com/codepath/compsci_guides/wiki/Bacon-Number

PROBLEM
-------
In `bacon_network`, each actor maps to the actors they have worked with. Kevin Bacon has Bacon number 0, his costars have 1, their costars have 2, and so on. Write `bacon_number(bacon_network, celeb)` that returns `celeb`'s Bacon number, or -1 if they are not connected.

EXAMPLES (test cases from the solution guide)
---------------------------------------------
HAPPY CASE
Input: 
```python
bacon_network = {
    "Kevin Bacon": ["Kyra Sedgewick", "Forest Whitaker", "Julia Roberts", "Tom Cruise"],
    "Kyra Sedgewick": ["Kevin Bacon"],
    "Tom Cruise": ["Kevin Bacon", "Kyra Sedgewick"],
    "Forest Whitaker": ["Kevin Bacon", "Denzel Washington"],
    "Denzel Washington": ["Forest Whitaker", "Julia Roberts"],
    "Julia Roberts": ["Denzel Washington", "Kevin Bacon", "George Clooney"],
    "George Clooney": ["Julia Roberts", "Vera Farmiga"],
    "Vera Farmiga": ["George Clooney", "Max Theriot"],
    "Max Theriot": ["Vera Farmiga", "Jennifer Lawrence"],
    "Jennifer Lawrence": ["Max Theriot"]
}
print(bacon_number(bacon_network, "Jennifer Lawrence"))
```
Output:
```markdown
5
Explanation: The path is Jennifer Lawrence -> Max Theriot -> Vera Farmiga -> George Clooney -> Julia Roberts -> Kevin Bacon. Jennifer Lawrence has a Bacon Number of 5.
```

EDGE CASE
Input: 
```python
bacon_network = {
    "Kevin Bacon": ["Kyra Sedgewick", "Tom Cruise"],
    "Kyra Sedgewick": ["Kevin Bacon"],
    "Tom Cruise": ["Kevin Bacon"]
}
print(bacon_number(bacon_network, "Tom Cruise"))
```
Output:
```markdown
1
Explanation: Tom Cruise has worked directly with Kevin Bacon, so his Bacon Number is 1.
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

from collections import deque


def bacon_number(bacon_network, celeb):
    pass
