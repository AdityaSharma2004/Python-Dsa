"""
Problem title:
    Basic Selection Sort (Ascending)

Problem statement:
    Sort a list of integers in ascending order using Selection Sort. Do not
    use sorted(), list.sort() or min() to do the work.

What it teaches:
    - Repeatedly selecting the minimum of the unsorted part.
    - Keeping a sorted prefix that grows by one element per pass.
    - Finding an index (not just a value) so the swap is possible.
    - Laravel analogy: scanning a list of orders for the cheapest one, moving
      it to the front, then repeating on the rest.

Input example:
    numbers = [64, 25, 12, 22, 11]

Expected output:
    Before: [64, 25, 12, 22, 11]
    After:  [11, 12, 22, 25, 64]
    Empty: []
    Single: [9]
    Already sorted: [1, 2, 3]
    Reversed: [1, 2, 3, 4, 5]
    Negatives: [-5, -1, 0, 3]
    Matches sorted()? True

Approach:
    For each position i from left to right, scan the rest of the list for the
    smallest value and swap it into position i.

Step-by-step logic:
    1. i = 0: the smallest of the whole list goes to index 0.
    2. i = 1: the smallest of indices 1.. goes to index 1.
    3. Continue until i = n - 2; the last element is then automatically in
       place.
    4. Remember the index of the minimum while scanning, swap once per pass.

Why it works:
    After pass i the first i + 1 positions hold the i + 1 smallest values in
    order, and the scan never touches them again.

Time complexity:
    O(n^2) in every case (always n(n-1)/2 comparisons).

Space complexity:
    O(1) extra - sorted in place (apart from the copy).

Edge cases:
    - Empty and single-element lists.
    - Already sorted lists still cost O(n^2) comparisons.
    - Duplicates and negative numbers work unchanged.

Alternative approach:
    Bubble Sort (see the Bubble Sort topic) or Insertion Sort.
"""


def find_min_index(items, start):
    """Index of the smallest value in items[start:]."""
    min_index = start
    for index in range(start + 1, len(items)):
        if items[index] < items[min_index]:
            min_index = index
    return min_index


def selection_sort(values):
    """Return a sorted copy of values (ascending)."""
    items = list(values)
    for position in range(len(items) - 1):
        min_index = find_min_index(items, position)
        if min_index != position:  # skip pointless self-swaps
            items[position], items[min_index] = items[min_index], items[position]
    return items


def main():
    numbers = [64, 25, 12, 22, 11]
    print("Before:", numbers)
    print("After: ", selection_sort(numbers))

    # Edge cases
    print("Empty:", selection_sort([]))
    print("Single:", selection_sort([9]))
    print("Already sorted:", selection_sort([1, 2, 3]))
    print("Reversed:", selection_sort([5, 4, 3, 2, 1]))
    print("Negatives:", selection_sort([0, -5, 3, -1]))

    # Verification against the built-in (used only to check, not to sort).
    sample = [8, 3, 9, 1, 7, 2]
    print("Matches sorted()?", selection_sort(sample) == sorted(sample))


if __name__ == "__main__":
    main()
