"""
Problem Title: House Robber (Maximum Sum of Non-Adjacent Elements)

Problem Statement:
    Houses on a street hold some amount of money. Adjacent houses have linked
    alarms, so you cannot take from two neighbouring houses. Return the maximum
    money you can take, and which houses give it.

What It Teaches:
    - A take / skip decision at every item (the seed of knapsack-style DP).
    - Defining dp[i] as "best answer using only the first i houses".
    - Reconstructing the chosen items by walking the table backwards.

Input Example:
    money = [2, 7, 9, 3, 1]

Expected Output:
    Money: [2, 7, 9, 3, 1]
    dp table: [0, 2, 7, 11, 11, 12]
    Maximum: 12 from houses [0, 2, 4]
    Two-variable check: 12
    [] -> 0 houses []
    [5] -> 5 houses [0]
    [4, 9] -> 9 houses [1]
    [0, 0, 0] -> 0 houses []
    [1, 2, 3, 1] -> 4 houses [0, 2]
    [6, 1, 1, 6] -> 12 houses [0, 3]

Approach:
    dp[i] = max(dp[i-1], dp[i-2] + money[i-1]): either skip house i, or take it
    and add the best result that stops two houses earlier.

Step-by-Step Logic:
    1. dp[0] = 0 (no houses), dp[1] = money[0].
    2. For each next house compute skip = dp[i-1] and take = dp[i-2] + money.
    3. dp[i] is the larger of the two (a plain if/else, no max()).
    4. Backtrack from i = n: if dp[i] != dp[i-1] the house was taken, jump to i-2.

Why It Works:
    The best plan for the first i houses either ignores house i (then it is the
    best plan for i-1 houses) or uses it (then house i-1 is forbidden and the
    rest is the best plan for i-2 houses). Those two cases cover everything.

Time Complexity:
    O(n).
Space Complexity:
    O(n) for the table (needed for backtracking); the value alone needs O(1).

Edge Cases:
    Empty street (0), one house, two houses (take the larger), all zeros,
    equal neighbours.

Alternative Approach:
    Keep just two variables (best_without, best_with) when you only need the value.
"""


def best_value(money):
    """Return the table dp where dp[i] = best total using the first i houses."""
    dp = [0] * (len(money) + 1)
    for i in range(1, len(money) + 1):
        skip = dp[i - 1]
        take = (dp[i - 2] if i >= 2 else 0) + money[i - 1]
        dp[i] = take if take > skip else skip
    return dp


def chosen_houses(money, dp):
    """Walk back through dp to recover the 0-based indices that were taken."""
    picked = []
    i = len(money)
    while i > 0:
        if dp[i] != dp[i - 1]:  # value changed -> house i-1 was taken
            picked.append(i - 1)
            i -= 2
        else:
            i -= 1
    picked.reverse()
    return picked


def rob_two_variables(money):
    """Space-optimised version returning only the value."""
    without_prev, with_prev = 0, 0
    for amount in money:
        new_with = without_prev + amount
        without_prev = with_prev if with_prev > without_prev else without_prev
        with_prev = new_with
    return with_prev if with_prev > without_prev else without_prev


def main():
    money = [2, 7, 9, 3, 1]
    dp = best_value(money)
    print("Money:", money)
    print("dp table:", dp)
    print("Maximum:", dp[-1], "from houses", chosen_houses(money, dp))
    print("Two-variable check:", rob_two_variables(money))
    for case in ([], [5], [4, 9], [0, 0, 0], [1, 2, 3, 1], [6, 1, 1, 6]):
        table = best_value(case)
        print(f"{case} -> {table[-1]} houses {chosen_houses(case, table)}")


if __name__ == "__main__":
    main()
