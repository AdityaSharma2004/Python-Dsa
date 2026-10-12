"""
Problem title:
    Report Which Fraction of Each Item Was Taken

Problem statement:
    Besides the maximum value, return a list with the fraction (0 to 1) taken
    of every item in its ORIGINAL position, and print only the items that
    were actually taken.

What it teaches:
    - Keeping the original index while sorting (sorting shuffles positions).
    - Reporting the solution, not only the optimal value.
    - Verifying a solution: total weight <= capacity and value matches.

Input example:
    weights = [5, 10, 15], values = [10, 30, 20], capacity = 15

Expected output:
    fractions (original order): [1.0, 1.0, 0.0]
    items taken:
      item 0 (w=5, v=10) -> 100% of it
      item 1 (w=10, v=30) -> 100% of it
    total value : 40.0
    weight used : 15.0 of 15
    classic example: 240.0 [1.0, 1.0, 0.6666666666666666]

Approach:
    Sort the indexes (not the values) by ratio, fill greedily and write the
    fraction taken into result[original_index].

Step-by-step logic:
    1. indexes = [0, 1, ..., n-1], ordered by values[i] / weights[i] high to
       low (insertion sort on the indexes).
    2. fractions = [0.0] * n.
    3. For each index in that order: take 1.0 if the weight fits, else take
       remaining / weight and stop.
    4. Verify: sum of fraction * weight (by a loop) must not exceed capacity.

Why it works:
    The index list carries the identity of each item through the sort, so a
    fraction can be stored back where the caller expects it.

Time complexity:
    O(n^2) with the insertion sort; the fill and the verification are O(n).

Space complexity:
    O(n) for the index order and the fractions.

Edge cases:
    - Items never reached stay at 0.0.
    - Exactly one fractional item at most.
    - Capacity 0 (all fractions 0.0).

Alternative approach:
    Store (ratio, index) tuples and sort those, the same idea in another form.
"""


def order_indexes_by_ratio(weights, values):
    order = list(range(len(weights)))
    for i in range(1, len(order)):
        current = order[i]
        current_ratio = values[current] / weights[current]
        j = i - 1
        while j >= 0 and values[order[j]] / weights[order[j]] < current_ratio:
            order[j + 1] = order[j]
            j -= 1
        order[j + 1] = current
    return order


def knapsack_fractions(weights, values, capacity):
    """Return (total_value, fractions) with fractions in original order."""
    fractions = [0.0] * len(weights)
    remaining = capacity
    total = 0.0
    for index in order_indexes_by_ratio(weights, values):
        if remaining <= 0:
            break
        if weights[index] <= remaining:
            fractions[index] = 1.0
            total += values[index]
            remaining -= weights[index]
        else:
            fractions[index] = remaining / weights[index]
            total += values[index] * fractions[index]
            remaining = 0
    return total, fractions


def main():
    weights = [5, 10, 15]
    values = [10, 30, 20]
    capacity = 15
    total, fractions = knapsack_fractions(weights, values, capacity)
    print("fractions (original order):", fractions)
    print("items taken:")
    used_weight = 0.0
    for index in range(len(weights)):
        if fractions[index] > 0:
            print("  item {} (w={}, v={}) -> {:.0%} of it".format(
                index, weights[index], values[index], fractions[index]))
        used_weight += fractions[index] * weights[index]
    print("total value :", total)
    print("weight used : {} of {}".format(used_weight, capacity))

    total, fractions = knapsack_fractions([10, 20, 30], [60, 100, 120], 50)
    print("classic example:", total, fractions)


if __name__ == "__main__":
    main()
