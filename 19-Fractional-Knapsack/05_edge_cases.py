"""
Problem title:
    Fractional Knapsack Edge Cases

Problem statement:
    Make the fractional knapsack function safe for unusual inputs: empty item
    list, capacity 0, capacity bigger than all items together, items with
    weight 0, negative capacity, and mismatched list lengths.

What it teaches:
    - Defensive programming around the "ratio = value / weight" division.
    - Why a zero-weight item with positive value is free value.
    - Input validation versus returning a sensible answer.

Input example:
    weights = [0, 4, 6], values = [7, 8, 9], capacity = 5

Expected output:
    empty lists                      -> 0.0
    capacity 0                       -> 0.0
    negative capacity                -> 0.0
    capacity larger than everything  -> 110.0
    zero-weight item                 -> 16.5
    single item, partly taken        -> 10.0
    ties in ratio                    -> 6.0
    mismatched lengths -> ValueError: weights and values must have the same length
    negative weight    -> ValueError: weights and values must be non-negative

Approach:
    Validate the input first. Treat zero-weight items as "take immediately"
    (their ratio is infinite), then run the normal greedy fill on the rest.

Step-by-step logic:
    1. Raise ValueError when lengths differ or any weight/value is negative.
    2. If capacity <= 0 return 0 (nothing can be carried).
    3. Add the value of every zero-weight item and drop it from the list.
    4. Sort the remaining items by ratio (insertion sort) and fill greedily.

Why it works:
    Zero-weight items cost no capacity, so taking all of them is always
    optimal; the remaining items all have positive weight, so no division by
    zero can occur.

Time complexity:
    O(n^2) with the insertion sort (O(n) validation and fill).

Space complexity:
    O(n) for the filtered list.

Edge cases:
    This whole file is about them; see the demo list in main().

Alternative approach:
    Give zero-weight items the ratio float("inf") and let the sort place them
    first; this works too but needs care when value is also 0.
"""


def validate(weights, values):
    if len(weights) != len(values):
        raise ValueError("weights and values must have the same length")
    for index in range(len(weights)):
        if weights[index] < 0 or values[index] < 0:
            raise ValueError("weights and values must be non-negative")


def fractional_knapsack(weights, values, capacity):
    validate(weights, values)
    if capacity <= 0:
        return 0.0

    free_value = 0.0
    items = []
    for index in range(len(weights)):
        if weights[index] == 0:
            free_value += values[index]  # costs nothing, always take it
        else:
            items.append((values[index] / weights[index], weights[index], values[index]))

    for i in range(1, len(items)):  # insertion sort, highest ratio first
        current = items[i]
        j = i - 1
        while j >= 0 and items[j][0] < current[0]:
            items[j + 1] = items[j]
            j -= 1
        items[j + 1] = current

    total = free_value
    remaining = capacity
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


def main():
    cases = [
        ("empty lists", [], [], 10),
        ("capacity 0", [5, 10], [50, 60], 0),
        ("negative capacity", [5, 10], [50, 60], -3),
        ("capacity larger than everything", [5, 10], [50, 60], 100),
        ("zero-weight item", [0, 4, 6], [7, 8, 9], 5),
        ("single item, partly taken", [8], [40], 2),
        ("ties in ratio", [2, 4], [4, 8], 3),
    ]
    for label, weights, values, capacity in cases:
        print("{:<32} -> {}".format(label, fractional_knapsack(weights, values, capacity)))

    try:
        fractional_knapsack([1, 2], [3], 5)
    except ValueError as error:
        print("mismatched lengths -> ValueError:", error)
    try:
        fractional_knapsack([1, -2], [3, 4], 5)
    except ValueError as error:
        print("negative weight    -> ValueError:", error)


if __name__ == "__main__":
    main()
