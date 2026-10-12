"""
Problem title:
    Count Swaps in Selection Sort (At Most n - 1)

Problem statement:
    Count the swaps and comparisons made by Selection Sort on different
    inputs and show that swaps never exceed n - 1 while comparisons are
    always n(n-1)/2.

What it teaches:
    - Selection Sort minimises the number of writes/swaps.
    - Comparisons are independent of the input order.
    - Why it is useful when writing to memory is expensive (e.g. flash).

Input example:
    sorted_list   = [1, 2, 3, 4, 5, 6]
    reversed_list = [6, 5, 4, 3, 2, 1]
    shuffled      = [4, 6, 1, 3, 5, 2]

Expected output:
    sorted    comparisons=15 swaps=0 -> [1, 2, 3, 4, 5, 6]
    reversed  comparisons=15 swaps=3 -> [1, 2, 3, 4, 5, 6]
    shuffled  comparisons=15 swaps=3 -> [1, 2, 3, 4, 5, 6]
    n(n-1)/2 for n=6: 15
    Empty : (0, 0)
    Single: (0, 0)

Approach:
    Selection Sort with two counters: comparisons (inside the scan) and swaps
    (only when the minimum is not already in place).

Step-by-step logic:
    1. For each pass scan the remaining items: comparisons += 1 per check.
    2. After the scan, swap once if needed: swaps += 1.
    3. At most one swap per pass and n - 1 passes give swaps <= n - 1.
    4. Compare with the formula n(n-1)/2 for comparisons.

Why it works:
    The scan only reads; a single swap is performed per pass after the
    minimum index is known.

Time complexity:
    O(n^2) comparisons, O(n) swaps.

Space complexity:
    O(1) extra.

Edge cases:
    - Sorted input: 0 swaps but still n(n-1)/2 comparisons.
    - Empty / single element: 0 and 0.
    - Reversed input: n // 2 swaps (each swap fixes two positions).

Alternative approach:
    Bubble Sort may need up to n(n-1)/2 swaps for the same input.
"""


def selection_sort_counted(values):
    """Return (sorted_list, comparisons, swaps)."""
    items = list(values)
    comparisons = 0
    swaps = 0
    for position in range(len(items) - 1):
        min_index = position
        for index in range(position + 1, len(items)):
            comparisons += 1
            if items[index] < items[min_index]:
                min_index = index
        if min_index != position:
            items[position], items[min_index] = items[min_index], items[position]
            swaps += 1
    return items, comparisons, swaps


def main():
    cases = [
        ("sorted", [1, 2, 3, 4, 5, 6]),
        ("reversed", [6, 5, 4, 3, 2, 1]),
        ("shuffled", [4, 6, 1, 3, 5, 2]),
    ]
    for name, data in cases:
        result, comparisons, swaps = selection_sort_counted(data)
        print("%-9s comparisons=%2d swaps=%d -> %s" % (name, comparisons, swaps, result))
    print("n(n-1)/2 for n=6:", 6 * 5 // 2)

    # Edge cases
    print("Empty :", selection_sort_counted([])[1:])
    print("Single:", selection_sort_counted([1])[1:])


if __name__ == "__main__":
    main()
