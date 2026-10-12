"""
Problem title:
    Basic Fractional Knapsack

Problem statement:
    You have n items, each with a weight and a value, and a bag that can carry
    at most "capacity" weight. Any fraction of an item may be taken (taking
    half of an item gives half of its value). Find the maximum total value.

What it teaches:
    - The greedy idea: always take the best value-per-weight item first.
    - Sorting items by ratio (hand-written insertion sort, no sort()).
    - Taking a fraction of the last item that does not fit whole.

Input example:
    weights = [10, 20, 30], values = [60, 100, 120], capacity = 50

Expected output:
    weights : [10, 20, 30]
    values  : [60, 100, 120]
    capacity: 50
    maximum value: 240.0
    capacity 0  -> 0.0
    capacity 100 -> 280.0

Approach:
    Compute ratio = value / weight for every item, order the items by ratio
    from highest to lowest, then fill the bag greedily.

Step-by-step logic:
    1. Build a list of (ratio, weight, value) for each item.
    2. Sort it by ratio, highest first.
    3. For each item: if it fits whole, take all of it and reduce the
       remaining capacity.
    4. Otherwise take the fraction remaining / weight of it and stop.

Why it works:
    Every kilogram of the bag should hold the most valuable material that is
    still available. Because items are divisible, swapping any lower-ratio
    weight for higher-ratio weight never makes the total worse (exchange
    argument), so the greedy fill is optimal.

Time complexity:
    O(n^2) here because of the simple insertion sort; O(n log n) when a
    merge sort, quick sort or the built-in sort is used. The greedy loop is
    O(n).

Space complexity:
    O(n) for the list of items.

Edge cases:
    - Capacity 0 (answer 0).
    - Capacity larger than the total weight (take everything).
    - Items with equal ratios (any order gives the same total).

Alternative approach:
    A max-heap of ratios avoids sorting everything (see problem 09).
"""


def build_items(weights, values):
    """Return a list of (ratio, weight, value) tuples."""
    items = []
    for index in range(len(weights)):
        items.append((values[index] / weights[index], weights[index], values[index]))
    return items


def insertion_sort_by_ratio_desc(items):
    """Sort tuples by their first element (the ratio), highest first."""
    for i in range(1, len(items)):
        current = items[i]
        j = i - 1
        while j >= 0 and items[j][0] < current[0]:
            items[j + 1] = items[j]  # shift smaller ratios to the right
            j -= 1
        items[j + 1] = current
    return items


def fractional_knapsack(weights, values, capacity):
    items = insertion_sort_by_ratio_desc(build_items(weights, values))
    total_value = 0.0
    remaining = capacity
    for ratio, weight, value in items:
        if remaining <= 0:
            break
        if weight <= remaining:  # the whole item fits
            total_value += value
            remaining -= weight
        else:  # take only the part that still fits, then the bag is full
            total_value += ratio * remaining
            remaining = 0
    return total_value


def main():
    weights = [10, 20, 30]
    values = [60, 100, 120]
    capacity = 50
    print("weights :", weights)
    print("values  :", values)
    print("capacity:", capacity)
    print("maximum value:", fractional_knapsack(weights, values, capacity))
    print("capacity 0  ->", fractional_knapsack(weights, values, 0))
    print("capacity 100 ->", fractional_knapsack(weights, values, 100))


if __name__ == "__main__":
    main()
