"""
Problem Title: 0/1 Knapsack

Problem Statement:
    Given items with weights and values and a bag of capacity W, choose a subset
    of items (each taken whole or not at all) with total weight <= W and maximum
    total value. Report the value and the chosen items.

What It Teaches:
    - The classic 2-D DP table dp[i][w] and the take / skip decision.
    - Backtracking through the table to find which items were chosen.
    - Space optimisation to a 1-D table (iterating capacity downwards).
    - Why greedy-by-ratio is NOT safe here (see 19-Fractional-Knapsack).

Input Example:
    weights = [1, 3, 4, 5], values = [1, 4, 5, 7], capacity = 7

Expected Output:
    weights: [1, 3, 4, 5] values: [1, 4, 5, 7] capacity: 7
    Last row of table: [0, 1, 1, 4, 5, 7, 8, 9]
    Best value: 9
    Items taken (0-based): [1, 2] weights [3, 4] values [4, 5]
    1-D version: 9
    Brute force: 9
    Capacity 0: 0
    No items: 0
    Item too heavy: 0
    Ratio trap, optimal: 220 (greedy by ratio would give 160)

Approach:
    dp[i][w] = best value using the first i items with capacity w.
    Skip item i: dp[i-1][w]. Take it (if it fits): values[i-1] + dp[i-1][w - weight].

Step-by-Step Logic:
    1. Row 0 and column 0 are all 0 (no items or no capacity).
    2. For each item i and capacity w, compare skip and take, keep the larger.
    3. The answer is dp[n][W].
    4. Backtrack: start at (n, W); if dp[i][w] != dp[i-1][w] item i was taken,
       so subtract its weight; then move to row i-1.
    5. 1-D version: one array, and for each item loop w from W DOWN to its weight
       so an item cannot be used twice in the same round.

Why It Works:
    Each item is either in or out of the best subset. Both cases reduce to a
    smaller knapsack problem, and the table stores every smaller answer once.

Time Complexity:
    O(n * W) (pseudo-polynomial: depends on the numeric value of W).
Space Complexity:
    O(n * W) for the 2-D table; O(W) for the 1-D version (value only).

Edge Cases:
    Capacity 0, no items, an item heavier than the capacity, all items fit,
    equal ratios, zero-value items.

Alternative Approach:
    Brute force over all 2^n subsets (used below to verify), or branch and bound.
"""


def knapsack_table(weights, values, capacity):
    """Build the full (n+1) x (capacity+1) DP table."""
    n = len(weights)
    dp = [[0] * (capacity + 1) for _ in range(n + 1)]
    for i in range(1, n + 1):
        for w in range(capacity + 1):
            skip = dp[i - 1][w]
            take = 0
            if weights[i - 1] <= w:
                take = values[i - 1] + dp[i - 1][w - weights[i - 1]]
            dp[i][w] = take if take > skip else skip
    return dp


def chosen_items(weights, dp, capacity):
    """Backtrack through the table; return 0-based indices of taken items."""
    items = []
    w = capacity
    for i in range(len(weights), 0, -1):
        if dp[i][w] != dp[i - 1][w]:  # value changed -> item i-1 was taken
            items.append(i - 1)
            w -= weights[i - 1]
    items.reverse()
    return items


def knapsack_1d(weights, values, capacity):
    """Space-optimised: one row, capacity iterated downwards."""
    best = [0] * (capacity + 1)
    for weight, value in zip(weights, values):
        for w in range(capacity, weight - 1, -1):
            candidate = best[w - weight] + value
            if candidate > best[w]:
                best[w] = candidate
    return best[capacity]


def brute_force(weights, values, capacity):
    """Try every subset using bit masks (verification only; O(2^n))."""
    n = len(weights)
    best = 0
    for mask in range(1 << n):
        total_weight = total_value = 0
        for i in range(n):
            if mask >> i & 1:
                total_weight += weights[i]
                total_value += values[i]
        if total_weight <= capacity and total_value > best:
            best = total_value
    return best


def main():
    weights, values, capacity = [1, 3, 4, 5], [1, 4, 5, 7], 7
    dp = knapsack_table(weights, values, capacity)
    print("weights:", weights, "values:", values, "capacity:", capacity)
    print("Last row of table:", dp[-1])
    picked = chosen_items(weights, dp, capacity)
    print("Best value:", dp[-1][-1])
    print("Items taken (0-based):", picked,
          "weights", [weights[i] for i in picked], "values", [values[i] for i in picked])
    print("1-D version:", knapsack_1d(weights, values, capacity))
    print("Brute force:", brute_force(weights, values, capacity))
    print("Capacity 0:", knapsack_1d(weights, values, 0))
    print("No items:", knapsack_1d([], [], 10))
    print("Item too heavy:", knapsack_1d([10], [99], 5))
    # Greedy-by-ratio trap: ratios 6, 5, 4 -> greedy takes items 0 and 1 (value 160)
    print("Ratio trap, optimal:", knapsack_1d([10, 20, 30], [60, 100, 120], 50),
          "(greedy by ratio would give 160)")


if __name__ == "__main__":
    main()
