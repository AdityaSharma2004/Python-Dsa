"""
Problem title:
    Optimized Bubble Sort with a Swapped Flag

Problem statement:
    Improve Bubble Sort so that it stops as soon as a full pass makes no
    swaps. Show how many passes the plain and the optimized versions need.

What it teaches:
    - Early termination: a swap-free pass proves the list is sorted.
    - The best case drops from O(n^2) to O(n).
    - Measuring an improvement by counting passes.

Input example:
    nearly_sorted = [1, 2, 3, 5, 4, 6]
    reversed_list = [6, 5, 4, 3, 2, 1]

Expected output:
    nearly sorted  sorted=[1, 2, 3, 4, 5, 6] plain passes=5 optimized passes=2
    reversed       sorted=[1, 2, 3, 4, 5, 6] plain passes=5 optimized passes=5
    already sorted sorted=[1, 2, 3, 4, 5] plain passes=4 optimized passes=1
    empty          sorted=[] plain passes=0 optimized passes=0

Approach:
    Keep a boolean "swapped" that is reset at the start of every pass and set
    to True whenever a swap happens. If it is still False after the pass,
    break out of the outer loop.

Step-by-step logic:
    1. For each pass set swapped = False.
    2. Compare neighbours; on a swap set swapped = True.
    3. After the inner loop, if not swapped: the list is sorted - stop.
    4. Return the sorted list and the number of passes used.

Why it works:
    If no adjacent pair was out of order during a whole pass, every element
    is already <= its right neighbour, which means the list is sorted.

Time complexity:
    Best O(n) (one pass, already sorted). Average and worst O(n^2).

Space complexity:
    O(1) extra besides the copy.

Edge cases:
    - Already sorted list: exactly 1 pass.
    - Empty or one element: 0 passes.
    - Reversed list is the worst case and still needs n - 1 passes.

Alternative approach:
    Also remember the position of the last swap (see
    05_early_termination_last_swap.py) to shrink the range even faster.
"""


def plain_bubble_sort(values):
    """Plain version: always n - 1 passes. Returns (sorted_list, passes)."""
    items = list(values)
    size = len(items)
    passes = 0
    for pass_number in range(size - 1):
        passes += 1
        for index in range(size - 1 - pass_number):
            if items[index] > items[index + 1]:
                items[index], items[index + 1] = items[index + 1], items[index]
    return items, passes


def optimized_bubble_sort(values):
    """Stops early when a pass makes no swap. Returns (sorted_list, passes)."""
    items = list(values)
    size = len(items)
    passes = 0
    for pass_number in range(size - 1):
        swapped = False
        passes += 1
        for index in range(size - 1 - pass_number):
            if items[index] > items[index + 1]:
                items[index], items[index + 1] = items[index + 1], items[index]
                swapped = True
        if not swapped:  # nothing moved, so the list is already sorted
            break
    return items, passes


def main():
    samples = [
        ("nearly sorted", [1, 2, 3, 5, 4, 6]),
        ("reversed", [6, 5, 4, 3, 2, 1]),
        ("already sorted", [1, 2, 3, 4, 5]),
        ("empty", []),
    ]
    for name, data in samples:
        result, plain_passes = plain_bubble_sort(data)
        _, fast_passes = optimized_bubble_sort(data)
        print("%-14s sorted=%s plain passes=%d optimized passes=%d"
              % (name, result, plain_passes, fast_passes))


if __name__ == "__main__":
    main()
