"""
Problem title:
    Find the Minimum and Maximum Positions in One Scan

Problem statement:
    Without using min() or max(), find the value and index of both the
    smallest and the largest element of a list in a single pass. This is the
    "selection" step that Selection Sort repeats.

What it teaches:
    - The core building block of Selection Sort.
    - Tracking an index instead of a value.
    - Which occurrence is returned when there are ties (the first one).
    - Doing two jobs in one loop.

Input example:
    numbers = [27, 8, 41, 8, 41, 3]

Expected output:
    List: [27, 8, 41, 8, 41, 3]
    Smallest: 3 at index 5
    Largest : 41 at index 2
    Single element: (0, 0)
    All equal: (0, 0)
    Negatives: (1, 2)
    Error: cannot find min/max of an empty list

Approach:
    Assume the first element is both min and max, then compare every other
    element to the current best indices and update them.

Step-by-step logic:
    1. min_index = max_index = 0.
    2. For each index from 1..n-1:
       - if items[index] < items[min_index]: min_index = index
       - if items[index] > items[max_index]: max_index = index
    3. Return both indices (values can be read from the list).

Why it works:
    The two variables always point to the smallest/largest element seen so
    far, so after the last element they point to the overall extremes.

Time complexity:
    O(n) - one pass, two comparisons per element.

Space complexity:
    O(1).

Edge cases:
    - Empty list raises ValueError (there is no minimum).
    - Single element: min and max are the same index 0.
    - Ties keep the first occurrence because only strict comparisons update.

Alternative approach:
    Compare elements in pairs to use about 3n/2 comparisons instead of 2n.
"""


def find_min_max(items):
    """Return (min_index, max_index) of a non-empty list."""
    if len(items) == 0:
        raise ValueError("cannot find min/max of an empty list")
    min_index = 0
    max_index = 0
    for index in range(1, len(items)):
        if items[index] < items[min_index]:
            min_index = index
        if items[index] > items[max_index]:
            max_index = index
    return min_index, max_index


def main():
    numbers = [27, 8, 41, 8, 41, 3]
    min_index, max_index = find_min_max(numbers)
    print("List:", numbers)
    print("Smallest: %d at index %d" % (numbers[min_index], min_index))
    print("Largest : %d at index %d" % (numbers[max_index], max_index))

    # Edge cases
    print("Single element:", find_min_max([5]))
    print("All equal:", find_min_max([4, 4, 4]))
    print("Negatives:", find_min_max([-3, -10, -1]))
    try:
        find_min_max([])
    except ValueError as error:
        print("Error:", error)


if __name__ == "__main__":
    main()
