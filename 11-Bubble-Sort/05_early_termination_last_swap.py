"""
Problem title:
    Bubble Sort Shrinking the Range by the Last Swap

Problem statement:
    Implement a Bubble Sort that remembers the index of the last swap in each
    pass. Everything after that index is already sorted, so the next pass can
    stop there. Compare comparison counts with the basic version.

What it teaches:
    - A stronger optimization than the swapped flag.
    - Reasoning about which part of the list is provably sorted.
    - Counting comparisons to prove the improvement.

Input example:
    data = [3, 2, 1, 4, 5, 6, 7, 8]   (only the front is out of order)

Expected output:
    Basic     : [1, 2, 3, 4, 5, 6, 7, 8] comparisons = 28
    Last swap : [1, 2, 3, 4, 5, 6, 7, 8] comparisons = 8
    Sorted    : ([1, 2, 3, 4], 3)
    Empty     : ([], 0)
    Reversed  : ([1, 2, 3, 4], 6)

Approach:
    Track last_swap = index of the final swap in a pass. The next pass only
    needs to examine pairs up to last_swap. If no swap happened, stop.

Step-by-step logic:
    1. limit = n - 1 (number of pairs to compare in this pass).
    2. Walk index from 0 to limit - 1, swapping out-of-order pairs and
       setting new_limit = index whenever a swap happens.
    3. Set limit = new_limit. If it is 0, the list is sorted.
    4. Repeat while limit > 0.

Why it works:
    If the last swap in a pass was between positions i and i + 1, then no
    pair after i + 1 moved, so that suffix is already in final order.

Time complexity:
    Best O(n); worst and average O(n^2).

Space complexity:
    O(1) extra besides the copy.

Edge cases:
    - Already sorted: one pass, n - 1 comparisons.
    - Empty / single element: zero comparisons.
    - Sorted suffix (as in the example) saves many comparisons.

Alternative approach:
    Plain swapped flag (03_optimized_bubble_sort.py): simpler, saves less.
"""


def basic_comparisons(values):
    """Comparisons made by the simple n-1 pass bubble sort."""
    items = list(values)
    size = len(items)
    comparisons = 0
    for pass_number in range(size - 1):
        for index in range(size - 1 - pass_number):
            comparisons += 1
            if items[index] > items[index + 1]:
                items[index], items[index + 1] = items[index + 1], items[index]
    return items, comparisons


def last_swap_bubble_sort(values):
    """Return (sorted_list, comparisons) using the last-swap optimization."""
    items = list(values)
    comparisons = 0
    limit = len(items) - 1  # number of adjacent pairs still worth checking
    while limit > 0:
        new_limit = 0
        for index in range(limit):
            comparisons += 1
            if items[index] > items[index + 1]:
                items[index], items[index + 1] = items[index + 1], items[index]
                new_limit = index  # everything after index + 1 is settled
        limit = new_limit
    return items, comparisons


def main():
    data = [3, 2, 1, 4, 5, 6, 7, 8]
    result_a, count_a = basic_comparisons(data)
    result_b, count_b = last_swap_bubble_sort(data)
    print("Basic     :", result_a, "comparisons =", count_a)
    print("Last swap :", result_b, "comparisons =", count_b)

    # Edge cases
    print("Sorted    :", last_swap_bubble_sort([1, 2, 3, 4]))
    print("Empty     :", last_swap_bubble_sort([]))
    print("Reversed  :", last_swap_bubble_sort([4, 3, 2, 1]))


if __name__ == "__main__":
    main()
