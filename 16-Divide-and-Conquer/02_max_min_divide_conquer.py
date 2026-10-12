"""
Problem Title: Find Maximum and Minimum by Divide and Conquer

Problem Statement:
    Find both the largest and the smallest element of a list by splitting the
    list in two halves, solving each half recursively and combining the
    answers. Do not use the built-in max() or min().

What It Teaches:
    - A full divide / conquer / combine cycle with a real combine step.
    - Counting comparisons: the D&C method uses about 3n/2 - 2 comparisons,
      slightly fewer than the naive 2(n - 1).

Input Example:
    data = [34, 7, 23, 32, 5, 62, 32, 8, -4, 19]

Expected Output:
    Data: [34, 7, 23, 32, 5, 62, 32, 8, -4, 19]
    Divide & conquer: min=-4, max=62, comparisons=14
    Simple scan     : min=-4, max=62, comparisons=18
    Single element  : (42, 42)
    Empty list      : ValueError: list must not be empty

Approach:
    Base cases: one element is both min and max; two elements need exactly one
    comparison. Otherwise split at mid, solve both halves, and combine by
    comparing the two minimums and the two maximums.

Step-by-Step Logic:
    1. If low == high -> (data[low], data[low]).
    2. If high == low + 1 -> compare once and order the pair.
    3. Else mid = (low + high) // 2; get (min1, max1) and (min2, max2).
    4. Result = (smaller of min1/min2, larger of max1/max2).

Why It Works:
    The overall minimum must be the minimum of one of the halves, and the same
    holds for the maximum, so combining the half answers is always correct.

Time Complexity:
    O(n): T(n) = 2T(n/2) + 2 -> about 3n/2 comparisons.
Space Complexity:
    O(log n) recursion depth.

Edge Cases:
    Empty list (raise ValueError), one element, two elements, all equal
    elements, negative numbers, odd length.

Alternative Approach:
    A single left-to-right scan uses 2(n - 1) comparisons, also O(n) but with
    a slightly bigger constant and O(1) space.
"""


def min_max(data, low, high, counter):
    """Return (minimum, maximum) of data[low..high]; counter[0] counts compares."""
    if low == high:
        return data[low], data[low]
    if high == low + 1:
        counter[0] += 1
        if data[low] < data[high]:
            return data[low], data[high]
        return data[high], data[low]
    mid = (low + high) // 2
    min1, max1 = min_max(data, low, mid, counter)
    min2, max2 = min_max(data, mid + 1, high, counter)
    counter[0] += 2  # one compare for the minimums, one for the maximums
    smallest = min1 if min1 < min2 else min2
    largest = max1 if max1 > max2 else max2
    return smallest, largest


def find_min_max(data):
    """Public wrapper that validates input."""
    if not data:
        raise ValueError("list must not be empty")
    counter = [0]
    smallest, largest = min_max(data, 0, len(data) - 1, counter)
    return smallest, largest, counter[0]


def naive_min_max(data):
    """Single scan, 2 comparisons per element, for comparison."""
    smallest = largest = data[0]
    compares = 0
    for value in data[1:]:
        compares += 2
        if value < smallest:
            smallest = value
        if value > largest:
            largest = value
    return smallest, largest, compares


def main():
    data = [34, 7, 23, 32, 5, 62, 32, 8, -4, 19]
    print("Data:", data)
    smallest, largest, compares = find_min_max(data)
    print(f"Divide & conquer: min={smallest}, max={largest}, comparisons={compares}")
    smallest, largest, compares = naive_min_max(data)
    print(f"Simple scan     : min={smallest}, max={largest}, comparisons={compares}")
    print("Single element  :", find_min_max([42])[:2])
    try:
        find_min_max([])
    except ValueError as error:
        print("Empty list      : ValueError:", error)


if __name__ == "__main__":
    main()
