"""
Problem title:
    Basic Bubble Sort (Ascending)

Problem statement:
    Sort a list of integers in ascending order using Bubble Sort. Do not use
    sorted() or list.sort() to do the sorting.

What it teaches:
    - Comparing and swapping adjacent elements.
    - Why the largest value "bubbles up" to the end after every pass.
    - Writing nested loops whose inner range shrinks each pass.
    - Laravel analogy: like ordering a collection by hand, one neighbour
      comparison at a time, instead of calling ->sortBy().

Input example:
    numbers = [64, 34, 25, 12, 22, 11, 90]

Expected output:
    Before: [64, 34, 25, 12, 22, 11, 90]
    After:  [11, 12, 22, 25, 34, 64, 90]
    Empty: []
    Single: [5]
    Already sorted: [1, 2, 3, 4]
    Reversed: [1, 2, 3, 4]
    Negatives: [-7, -1, 0, 2, 3]
    Matches sorted()? True

Approach:
    Make n - 1 passes. In each pass compare every neighbouring pair and swap
    the pair if the left one is bigger.

Step-by-step logic:
    1. Pass 1 walks the whole list; the largest value ends at the last slot.
    2. Pass 2 walks all but the last slot; the second largest settles.
    3. Repeat until only one element is left unsorted.
    4. The inner loop stops at n - 1 - pass_number because the tail is
       already in its final place.

Why it works:
    After pass k the last k elements are the k largest values in sorted
    order, so the unsorted part shrinks by one every pass.

Time complexity:
    O(n^2) in best, average and worst case for this simple version
    (it always does n(n-1)/2 comparisons).

Space complexity:
    O(1) extra space - the list is sorted in place.

Edge cases:
    - Empty list and one-element list are already sorted.
    - Already sorted input still costs O(n^2) here (see 03 for the fix).
    - Negative numbers and duplicates work unchanged.

Alternative approach:
    Optimized Bubble Sort with a swapped flag (03_optimized_bubble_sort.py).
"""


def bubble_sort(values):
    """Sort a copy of values in ascending order and return it."""
    items = list(values)  # copy so the caller's list is not changed
    size = len(items)
    for pass_number in range(size - 1):
        for index in range(size - 1 - pass_number):
            if items[index] > items[index + 1]:
                # Swap the neighbours that are out of order.
                items[index], items[index + 1] = items[index + 1], items[index]
    return items


def main():
    numbers = [64, 34, 25, 12, 22, 11, 90]
    print("Before:", numbers)
    print("After: ", bubble_sort(numbers))

    # Edge cases
    print("Empty:", bubble_sort([]))
    print("Single:", bubble_sort([5]))
    print("Already sorted:", bubble_sort([1, 2, 3, 4]))
    print("Reversed:", bubble_sort([4, 3, 2, 1]))
    print("Negatives:", bubble_sort([3, -1, 0, -7, 2]))

    # Verification against the built-in (used only to check, not to sort).
    sample = [9, 4, 7, 1, 8, 2]
    print("Matches sorted()?", bubble_sort(sample) == sorted(sample))


if __name__ == "__main__":
    main()
