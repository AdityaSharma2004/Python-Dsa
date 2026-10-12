"""
Problem title:
    Count Comparisons and Swaps in Bubble Sort

Problem statement:
    Instrument Bubble Sort so it returns how many comparisons and swaps it
    performed, then compare best, average and worst case inputs of size 8.

What it teaches:
    - Turning Big-O into real numbers.
    - Worst case (reversed) does n(n-1)/2 swaps and comparisons.
    - Best case (sorted) with the swapped flag does only n - 1 comparisons.
    - The number of swaps is independent of the optimization used.

Input example:
    best    = [1, 2, 3, 4, 5, 6, 7, 8]
    average = [3, 7, 1, 8, 2, 6, 4, 5]
    worst   = [8, 7, 6, 5, 4, 3, 2, 1]

Expected output:
    best     comparisons= 7 swaps= 0
    average  comparisons=22 swaps=13
    worst    comparisons=28 swaps=28
    n(n-1)/2 for n=8: 28
    Empty : (0, 0)
    Single: (0, 0)

Approach:
    Add two counters to the optimized bubble sort: one incremented on every
    comparison and one on every swap.

Step-by-step logic:
    1. comparisons += 1 before each "if left > right".
    2. swaps += 1 inside the swap branch.
    3. Return (sorted_list, comparisons, swaps).
    4. Print the formula n(n-1)/2 next to the worst case for comparison.

Why it works:
    Counters live in the same loops that define the running time, so they
    measure exactly the quantities used in the complexity analysis.

Time complexity:
    Best O(n), average O(n^2), worst O(n^2).

Space complexity:
    O(1) extra.

Edge cases:
    - Empty or single element: 0 comparisons, 0 swaps.
    - Reversed list with n elements: n(n-1)/2 of each.
    - Sorted list: swaps = 0.

Alternative approach:
    Time the code with time.perf_counter - noisy and hardware dependent,
    whereas operation counts are exact and repeatable.
"""


def bubble_sort_counted(values):
    """Return (sorted_list, comparisons, swaps) using the swapped flag."""
    items = list(values)
    size = len(items)
    comparisons = 0
    swaps = 0
    for pass_number in range(size - 1):
        swapped = False
        for index in range(size - 1 - pass_number):
            comparisons += 1
            if items[index] > items[index + 1]:
                items[index], items[index + 1] = items[index + 1], items[index]
                swaps += 1
                swapped = True
        if not swapped:
            break
    return items, comparisons, swaps


def main():
    cases = [
        ("best", [1, 2, 3, 4, 5, 6, 7, 8]),
        ("average", [3, 7, 1, 8, 2, 6, 4, 5]),
        ("worst", [8, 7, 6, 5, 4, 3, 2, 1]),
    ]
    for name, data in cases:
        _, comparisons, swaps = bubble_sort_counted(data)
        print("%-8s comparisons=%2d swaps=%2d" % (name, comparisons, swaps))
    size = 8
    print("n(n-1)/2 for n=8:", size * (size - 1) // 2)

    # Edge cases
    print("Empty :", bubble_sort_counted([])[1:])
    print("Single:", bubble_sort_counted([1])[1:])


if __name__ == "__main__":
    main()
