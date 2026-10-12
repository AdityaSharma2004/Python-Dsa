"""
Problem title:
    Bubble Sort in Descending Order

Problem statement:
    Sort a list of integers from largest to smallest using Bubble Sort. Make
    the order selectable so the same function can sort either way.

What it teaches:
    - Changing the comparison is all it takes to flip the sort order.
    - Passing the ordering rule as a parameter (a small comparison helper).
    - In descending order the SMALLEST value bubbles to the end each pass.

Input example:
    numbers = [5, 1, 4, 2, 8]

Expected output:
    Original:   [5, 1, 4, 2, 8]
    Descending: [8, 5, 4, 2, 1]
    Ascending:  [1, 2, 4, 5, 8]
    Empty: []
    Duplicates: [3, 3, 2, 1, 1]
    Already descending: [9, 7, 5]
    Negatives: [5, 0, -2, -9]

Approach:
    Same adjacent-swap passes as the basic version, but swap when the left
    element is SMALLER than the right one (for descending).

Step-by-step logic:
    1. Define out_of_order(left, right, descending).
    2. For each pass, compare neighbours with that helper.
    3. Swap when the pair is out of order for the chosen direction.
    4. After pass k the last k slots hold the k smallest values.

Why it works:
    "Out of order" simply means the pair violates the desired direction.
    Removing every violating adjacent pair, pass after pass, leaves the
    whole list ordered.

Time complexity:
    O(n^2) comparisons (n(n-1)/2).

Space complexity:
    O(1) extra besides the copy of the input.

Edge cases:
    - Empty and single-element lists.
    - Duplicates: equal neighbours are not swapped (strict comparison).
    - Already descending input stays unchanged.

Alternative approach:
    Sort ascending and then reverse the list by hand - works, but needs a
    second O(n) pass.
"""


def out_of_order(left, right, descending):
    """Return True if the pair must be swapped for the chosen direction."""
    if descending:
        return left < right
    return left > right


def bubble_sort(values, descending=False):
    """Return a sorted copy; descending=True gives largest first."""
    items = list(values)
    size = len(items)
    for pass_number in range(size - 1):
        for index in range(size - 1 - pass_number):
            if out_of_order(items[index], items[index + 1], descending):
                items[index], items[index + 1] = items[index + 1], items[index]
    return items


def main():
    numbers = [5, 1, 4, 2, 8]
    print("Original:  ", numbers)
    print("Descending:", bubble_sort(numbers, descending=True))
    print("Ascending: ", bubble_sort(numbers))

    # Edge cases
    print("Empty:", bubble_sort([], descending=True))
    print("Duplicates:", bubble_sort([3, 1, 3, 2, 1], descending=True))
    print("Already descending:", bubble_sort([9, 7, 5], descending=True))
    print("Negatives:", bubble_sort([-2, 5, -9, 0], descending=True))


if __name__ == "__main__":
    main()
