"""
Problem title:
    Trace the Greedy Fill Step by Step

Problem statement:
    Solve fractional knapsack and print a table showing, for every step, which
    item is considered, how much of it is taken, the capacity left, the value
    gained and the running total.

What it teaches:
    - Reading the greedy algorithm as a sequence of simple decisions.
    - The three cases: take whole, take a fraction, bag already full.
    - Debugging by tracing state after every step.

Input example:
    weights = [10, 20, 30], values = [60, 100, 120], capacity = 50

Expected output:
    capacity 50
    item   weight  ratio  taken      left    gain    total  note
    A          10   6.00     10        40   60.00    60.00  whole item
    B          20   5.00     20        20  100.00   160.00  whole item
    C          30   4.00     20         0   80.00   240.00  fraction 20/30
    final value: 240.0

    capacity 30 (bag fills exactly, no fraction)
    item   weight  ratio  taken      left    gain    total  note
    A          10   6.00     10        20   60.00    60.00  whole item
    B          20   5.00     20         0  100.00   160.00  whole item
    C          30   4.00      0         0       0   160.00  skipped
    final value: 160.0

Approach:
    Order the items by ratio (insertion sort, highest first), then run the
    greedy loop while recording a trace row per item.

Step-by-step logic:
    1. Rank items by value / weight, best first.
    2. For each item compute take = weight if it fits, else the remaining
       capacity (a part of the item).
    3. gained = ratio * take; remaining -= take; total += gained.
    4. Print one row per item.

Why it works:
    The trace is simply the greedy algorithm with its variables displayed;
    the last partly-taken item shows why a fraction appears at most once.

Time complexity:
    O(n^2) for the insertion sort plus O(n) for the loop.

Space complexity:
    O(n) for the ordered items.

Edge cases:
    - Bag exactly full after a whole item (no fraction at all).
    - Items after the bag is full are shown as "skipped".
    - Capacity 0 (every item skipped).

Alternative approach:
    Return only the final value (problem 01) when no trace is needed.
"""


def order_by_ratio(names, weights, values):
    """Return (name, weight, value, ratio) tuples, best ratio first."""
    items = []
    for index in range(len(names)):
        items.append((names[index], weights[index], values[index],
                      values[index] / weights[index]))
    for i in range(1, len(items)):
        current = items[i]
        j = i - 1
        while j >= 0 and items[j][3] < current[3]:
            items[j + 1] = items[j]
            j -= 1
        items[j + 1] = current
    return items


def traced_knapsack(names, weights, values, capacity):
    items = order_by_ratio(names, weights, values)
    remaining = capacity
    total = 0.0
    print("{:<6}{:>7}{:>7}{:>7}{:>10}{:>8}{:>9}  {}".format(
        "item", "weight", "ratio", "taken", "left", "gain", "total", "note"))
    for name, weight, value, ratio in items:
        if remaining <= 0:
            print("{:<6}{:>7}{:>7.2f}{:>7}{:>10}{:>8}{:>9.2f}  skipped".format(
                name, weight, ratio, 0, remaining, 0, total))
            continue
        if weight <= remaining:
            taken, note = weight, "whole item"
        else:
            taken, note = remaining, "fraction {}/{}".format(remaining, weight)
        gain = ratio * taken
        remaining -= taken
        total += gain
        print("{:<6}{:>7}{:>7.2f}{:>7}{:>10}{:>8.2f}{:>9.2f}  {}".format(
            name, weight, ratio, taken, remaining, gain, total, note))
    return total


def main():
    names = ["A", "B", "C"]
    weights = [10, 20, 30]
    values = [60, 100, 120]
    print("capacity 50")
    print("final value:", traced_knapsack(names, weights, values, 50))
    print()
    print("capacity 30 (bag fills exactly, no fraction)")
    print("final value:", traced_knapsack(names, weights, values, 30))


if __name__ == "__main__":
    main()
