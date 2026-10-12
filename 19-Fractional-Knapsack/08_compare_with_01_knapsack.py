"""
Problem title:
    Fractional vs 0/1 vs Unbounded Knapsack

Problem statement:
    For the same items and capacity compute: (a) the fractional knapsack
    optimum, (b) the 0/1 knapsack optimum (dynamic programming), (c) what the
    ratio-greedy rule gives when items cannot be split, and (d) the unbounded
    knapsack optimum (unlimited copies). Explain the differences.

What it teaches:
    - Fractional >= 0/1 always, because splitting adds freedom.
    - Ratio-greedy is optimal only when items are divisible.
    - How a 1-D dynamic programming table solves 0/1 and unbounded versions.

Input example:
    weights = [10, 20, 30], values = [60, 100, 120], capacity = 50

Expected output:
    Fractional (greedy by ratio):     240.0
    0/1 knapsack (DP):                220
    Ratio-greedy, whole items only:   160
    Unbounded knapsack (DP):          300
    second example: 40.0 40 40 40

Approach:
    Fractional: greedy by ratio. 0/1: dp[w] = best value with capacity w,
    looping w downwards. Unbounded: same table but looping w upwards. Greedy
    on 0/1: take whole items by ratio and skip any that do not fit.

Step-by-step logic:
    1. Fractional: order by ratio, take whole items, then a fraction.
    2. 0/1 DP: for each item, for w from capacity down to weight:
       dp[w] = better of dp[w] and dp[w - weight] + value.
    3. Unbounded DP: for each item, for w from weight up to capacity, same
       update (going upwards allows reusing the item).
    4. Greedy-on-0/1: take an item only if it fits whole.

Why it works:
    The downward loop uses each item at most once because dp[w - weight] has
    not yet been updated for the current item; the upward loop deliberately
    uses updated values, which allows repeats.

Time complexity:
    Fractional O(n^2) with the insertion sort; DP versions O(n * capacity).

Space complexity:
    O(n) for the fractional version; O(capacity) for each DP table.

Edge cases:
    - Capacity 0 (all answers 0).
    - Item heavier than the capacity (skipped by 0/1 and unbounded).
    - Divisible items where splitting makes no difference (all agree).

Alternative approach:
    Recursion with memoisation for 0/1 knapsack (see the Dynamic Programming
    topic).
"""


def fractional(weights, values, capacity):
    items = []
    for i in range(len(weights)):
        items.append((values[i] / weights[i], weights[i], values[i]))
    for i in range(1, len(items)):  # insertion sort, highest ratio first
        current = items[i]
        j = i - 1
        while j >= 0 and items[j][0] < current[0]:
            items[j + 1] = items[j]
            j -= 1
        items[j + 1] = current
    total, remaining = 0.0, capacity
    for ratio, weight, value in items:
        if remaining <= 0:
            break
        if weight <= remaining:
            total += value
            remaining -= weight
        else:
            total += ratio * remaining
            remaining = 0
    return total


def greedy_whole_items_only(weights, values, capacity):
    """Ratio-greedy but items cannot be split (wrong for 0/1 in general)."""
    items = []
    for i in range(len(weights)):
        items.append((values[i] / weights[i], weights[i], values[i]))
    for i in range(1, len(items)):
        current = items[i]
        j = i - 1
        while j >= 0 and items[j][0] < current[0]:
            items[j + 1] = items[j]
            j -= 1
        items[j + 1] = current
    total, remaining = 0, capacity
    for ratio, weight, value in items:
        if weight <= remaining:
            total += value
            remaining -= weight
    return total


def knapsack_01(weights, values, capacity):
    table = [0] * (capacity + 1)
    for i in range(len(weights)):
        for w in range(capacity, weights[i] - 1, -1):  # downwards: use item once
            candidate = table[w - weights[i]] + values[i]
            if candidate > table[w]:
                table[w] = candidate
    return table[capacity]


def knapsack_unbounded(weights, values, capacity):
    table = [0] * (capacity + 1)
    for i in range(len(weights)):
        for w in range(weights[i], capacity + 1):  # upwards: item reusable
            candidate = table[w - weights[i]] + values[i]
            if candidate > table[w]:
                table[w] = candidate
    return table[capacity]


def main():
    weights = [10, 20, 30]
    values = [60, 100, 120]
    capacity = 50
    print("{:<34}{}".format("Fractional (greedy by ratio):",
                            fractional(weights, values, capacity)))
    print("{:<34}{}".format("0/1 knapsack (DP):",
                            knapsack_01(weights, values, capacity)))
    print("{:<34}{}".format("Ratio-greedy, whole items only:",
                            greedy_whole_items_only(weights, values, capacity)))
    print("{:<34}{}".format("Unbounded knapsack (DP):",
                            knapsack_unbounded(weights, values, capacity)))

    weights, values, capacity = [5, 10, 15], [10, 30, 20], 15
    print("second example:", fractional(weights, values, capacity),
          knapsack_01(weights, values, capacity),
          greedy_whole_items_only(weights, values, capacity),
          knapsack_unbounded(weights, values, capacity))


if __name__ == "__main__":
    main()
