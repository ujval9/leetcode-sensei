r"""
TIP102 | Week 1 | Session 1 | Problem Set Version 1 | Problem 1
Hundred Acre Wood

Source: CodePath TIP102 course page (statement copied word for word from the course PDF).
Note: a few long lines were cut off at the right edge in the PDF; check the solution guide examples if a line looks incomplete.
Solution guide (only after you have tried!): https://github.com/codepath/compsci_guides/wiki/Hundred-Acre-Wood

PROBLEM
-------
Write a function welcome() that prints the string
 "Welcome to The Hundred Acre Wood!" .

 def welcome():
         pass

Example Usage:

 welcome()

Example Output:

 Welcome to The Hundred Acre Wood!
"""

# STATUS: solved    (not started | in progress | solved | solved with help)

"""
UNDERSTAND:
    * Input:
    * Output:

    * questions about the problem?

    * edge cases?


MATCH:    * similar problems?

PLAN
1.remove the pass in the function def welcome() , I dont know if you need to define the return type in python or it reads in your own. so i woud just write a print statement and string in that and it would display that.

IMPLEMENT:
def welcome():
    print("Welcome to The Hundred Acre Wood!")
REVIEW:

I will it would work out for all edged cases as you just call the function and dont pass anything. 
EVALUATE:
    * runtime and complexity?
The time complexity would O(1) as its just a print

"""

def welcome():
    print("Welcome to The Hundred Acre Wood!")

if __name__ == "__main__":
    welcome()
