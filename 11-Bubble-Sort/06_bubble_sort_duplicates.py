"""
Problem title:
    Bubble Sort with Duplicate Values

Problem statement:
    Sort lists that contain repeated values using Bubble Sort, and count how
    many swaps are really needed. Show why equal neighbours must NOT be
    swapped.

What it teaches:
    - Strict (>) versus non-strict (>=) comparison.
    - Swapping equal values wastes work and breaks stability.
    - Handling lists where every value is the same.

Input example:
    numbers = [4, 2, 4, 1, 2, 4]

Expected output:
    Strict  (>) : [1, 2, 2, 4, 4, 4] swaps = 6
    Loose  (>=) : [1, 2, 2, 4, 4, 4] swaps = 11
    All equal   : ([7, 7, 7, 7], 0)
    Negatives   : ([-3, -3, -1, -1], 3)
    Empty       : ([], 0)

Approach:
    Standard optimized bubble sort that swaps only when left > right
    (strictly). A second function uses >= to show the wasted swaps.

Step-by-step logic:
    1. Compare each neighbouring pair.
    2. Swap only when the left value is strictly greater.
    3. Count swaps to measure the work.
    4. With >=, equal pairs swap back and forth and the optimized version
       would never see a swap-free pass (it loops until the pass limit).

Why it works:
    Equal values are already in a valid relative order, so leaving them
    alone is correct and cheaper.

Time complexity:
    O(n^2) worst case; O(n) best case with the swapped flag.

Space complexity:
    O(1) extra besides the copy.

Edge cases:
    - All elements equal: zero swaps, finishes after one pass.
    - Duplicates at both ends.
    - Negative duplicates.

Alternative approach:
    Counting sort handles heavy duplicates in O(n + k) but is a different
    algorithm and only suits small integer ranges.
"""


def bubble_sort_counting_swaps(values, strict=True):
    """Return (sorted_list, swaps). strict=False uses >= (wasteful)."""
    items = list(values)
    size = len(items)
    swaps = 0
    for pass_number in range(size - 1):
        swapped = False
        for index in range(size - 1 - pass_number):
            left, right = items[index], items[index + 1]
            should_swap = left > right if strict else left >= right
            if should_swap:
                items[index], items[index + 1] = right, left
                swaps += 1
                swapped = True
        if strict and not swapped:
            break  # with >= the flag is not trusted, so run all passes
    return items, swaps


def main():
    numbers = [4, 2, 4, 1, 2, 4]
    result, swaps = bubble_sort_counting_swaps(numbers)
    print("Strict  (>) :", result, "swaps =", swaps)
    result, swaps = bubble_sort_counting_swaps(numbers, strict=False)
    print("Loose  (>=) :", result, "swaps =", swaps)

    # Edge cases
    print("All equal   :", bubble_sort_counting_swaps([7, 7, 7, 7]))
    print("Negatives   :", bubble_sort_counting_swaps([-1, -3, -1, -3]))
    print("Empty       :", bubble_sort_counting_swaps([]))


if __name__ == "__main__":
    main()
