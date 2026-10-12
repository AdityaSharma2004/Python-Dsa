"""
Problem title:
    Bidirectional (Double) Selection Sort

Problem statement:
    Improve Selection Sort so that each pass selects BOTH the minimum and the
    maximum of the unsorted middle part, placing them at the left and right
    ends. This halves the number of passes.

What it teaches:
    - Growing the sorted region from both ends at the same time.
    - A classic trap: when the maximum sits at the left boundary, the first
      swap moves it, so its index must be corrected.
    - How to reason about invariants with two boundaries.

Input example:
    numbers = [29, 10, 14, 37, 13, 5, 21]

Expected output:
    Before: [29, 10, 14, 37, 13, 5, 21]
    After:  [5, 10, 13, 14, 21, 29, 37]
    Empty: []
    Single: [8]
    Max at left: [1, 2, 3, 9]
    All equal: [2, 2, 2, 2]
    Even length: [1, 2, 3, 4]
    Matches sorted()? True

Approach:
    Keep two boundaries, left and right. In each pass scan items[left..right]
    once for min_index and max_index, swap the minimum to left, then the
    maximum to right, and shrink the range from both sides.

Step-by-step logic:
    1. left = 0, right = n - 1.
    2. While left < right: find min_index and max_index in one scan.
    3. Swap items[left] with items[min_index].
    4. If max_index was equal to left, the maximum just moved to min_index, so
       set max_index = min_index.
    5. Swap items[right] with items[max_index]; left += 1; right -= 1.

Why it works:
    After every pass the smallest remaining value is at the left boundary and
    the largest remaining value is at the right boundary, so both outer
    regions only contain final values.

Time complexity:
    O(n^2) overall (about n/2 passes, each scanning the remaining range).

Space complexity:
    O(1) extra besides the copy.

Edge cases:
    - Empty and single-element lists.
    - Maximum located at the left boundary (the index correction above).
    - All values equal.
    - Odd and even lengths.

Alternative approach:
    Plain Selection Sort (file 01) does n - 1 passes with one selection each;
    comparisons are about the same, only the pass count halves.
"""


def bidirectional_selection_sort(values):
    """Return a sorted copy (ascending) selecting min and max in each pass."""
    items = list(values)
    left = 0
    right = len(items) - 1
    while left < right:
        min_index = left
        max_index = left
        for index in range(left + 1, right + 1):
            if items[index] < items[min_index]:
                min_index = index
            if items[index] > items[max_index]:
                max_index = index
        items[left], items[min_index] = items[min_index], items[left]
        # If the maximum was at 'left', the swap above moved it to min_index.
        if max_index == left:
            max_index = min_index
        items[right], items[max_index] = items[max_index], items[right]
        left += 1
        right -= 1
    return items


def main():
    numbers = [29, 10, 14, 37, 13, 5, 21]
    print("Before:", numbers)
    print("After: ", bidirectional_selection_sort(numbers))

    # Edge cases
    print("Empty:", bidirectional_selection_sort([]))
    print("Single:", bidirectional_selection_sort([8]))
    print("Max at left:", bidirectional_selection_sort([9, 1, 2, 3]))
    print("All equal:", bidirectional_selection_sort([2, 2, 2, 2]))
    print("Even length:", bidirectional_selection_sort([4, 3, 2, 1]))

    # Verification against the built-in (used only to check, not to sort).
    sample = [7, -3, 12, 0, 5, 5, -8, 2]
    print("Matches sorted()?", bidirectional_selection_sort(sample) == sorted(sample))


if __name__ == "__main__":
    main()
