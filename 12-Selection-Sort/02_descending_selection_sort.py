"""
Problem title:
    Selection Sort in Descending Order

Problem statement:
    Sort a list from largest to smallest with Selection Sort by selecting the
    MAXIMUM of the unsorted part in each pass.

What it teaches:
    - Flipping the selection rule (maximum instead of minimum).
    - Writing find_max_index mirroring find_min_index.
    - The structure of the algorithm stays identical.

Input example:
    numbers = [29, 10, 14, 37, 13]

Expected output:
    Before: [29, 10, 14, 37, 13]
    After:  [37, 29, 14, 13, 10]
    Empty: []
    Duplicates: [5, 5, 2, 2, 1]
    Already descending: [9, 6, 3]
    Negatives: [2, 0, -4, -9]

Approach:
    For each position i, find the index of the largest value in items[i:] and
    swap it into position i.

Step-by-step logic:
    1. i = 0: largest overall goes to the front.
    2. i = 1: largest of the remainder goes to index 1.
    3. Continue until the list is exhausted.
    4. Use a strict ">" while scanning so the first maximum is kept.

Why it works:
    After pass i the first i + 1 slots hold the largest values in descending
    order; the remaining slots only contain smaller (or equal) values.

Time complexity:
    O(n^2) comparisons in all cases.

Space complexity:
    O(1) extra besides the copy.

Edge cases:
    - Empty and single-element lists.
    - Duplicates: equal values are all kept.
    - Already descending input needs zero swaps.

Alternative approach:
    Sort ascending, then reverse manually - needs an extra O(n) pass.
"""


def find_max_index(items, start):
    """Index of the largest value in items[start:]."""
    max_index = start
    for index in range(start + 1, len(items)):
        if items[index] > items[max_index]:
            max_index = index
    return max_index


def selection_sort_descending(values):
    """Return a copy of values sorted from largest to smallest."""
    items = list(values)
    for position in range(len(items) - 1):
        max_index = find_max_index(items, position)
        if max_index != position:
            items[position], items[max_index] = items[max_index], items[position]
    return items


def main():
    numbers = [29, 10, 14, 37, 13]
    print("Before:", numbers)
    print("After: ", selection_sort_descending(numbers))

    # Edge cases
    print("Empty:", selection_sort_descending([]))
    print("Duplicates:", selection_sort_descending([2, 5, 2, 5, 1]))
    print("Already descending:", selection_sort_descending([9, 6, 3]))
    print("Negatives:", selection_sort_descending([-4, 0, -9, 2]))


if __name__ == "__main__":
    main()
