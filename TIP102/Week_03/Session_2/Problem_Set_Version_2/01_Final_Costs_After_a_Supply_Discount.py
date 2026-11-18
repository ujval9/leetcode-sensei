r"""
TIP102 | Week 3 | Session 2 | Problem Set Version 2 | Problem 1
Final Costs After a Supply Discount

Source: statement reconstructed from the CodePath solution guide and written in our own words.
The original course page is behind a login, so wording and details may differ slightly.
Solution guide (only after you have tried!): https://github.com/codepath/compsci_guides/wiki/Final-Costs-After-a-Supply-Discount

PROBLEM
-------
For each item i, the discount is the cost of the first later item j > i with costs[j] <= costs[i]; if there is none, there is no discount. Return the list of final costs after discounts.
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

def final_supply_costs(costs):
    pass


if __name__ == "__main__":
    # Example usage
    print(final_supply_costs([8, 4, 6, 2, 3]))  # Output: [4, 2, 4, 2, 3]
    print(final_supply_costs([1, 2, 3, 4, 5]))  # Output: [1, 2, 3, 4, 5]
    print(final_supply_costs([10, 1, 1, 6]))    # Output: [9, 0, 1, 6]
