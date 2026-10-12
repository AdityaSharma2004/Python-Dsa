r"""
Problem title: Searching an Array - Linear and Binary Search

Problem statement:
    Find the index of a target value in a list. Implement linear search (any
    list) and binary search (sorted list) and compare how many comparisons each
    needs. Return -1 when the target is absent.

What it teaches:
    Why sorted data is valuable: binary search discards half of the remaining
    elements each step, turning O(n) into O(log n).

Input example:
    numbers = [3, 8, 12, 19, 25, 31, 47, 52, 60, 74], targets 47, 3, 74, 50

Expected output:
    sorted list: [3, 8, 12, 19, 25, 31, 47, 52, 60, 74]
    target 47: linear (index, comparisons) = (6, 7), binary = (6, 4)
    target  3: linear (index, comparisons) = (0, 1), binary = (0, 3)
    target 74: linear (index, comparisons) = (9, 10), binary = (9, 4)
    target 50: linear (index, comparisons) = (-1, 10), binary = (-1, 4)
    empty list: (-1, 0) (-1, 0)

Approach:
    Linear search checks each element in turn. Binary search keeps a window
    [low, high], inspects the middle and moves low or high past it.

Step-by-step logic:
    Linear: for each index, if numbers[index] == target return index.
    Binary:
    1. low = 0, high = len - 1.
    2. mid = (low + high) // 2.
    3. If numbers[mid] == target -> found.
    4. If numbers[mid] < target -> low = mid + 1, else high = mid - 1.
    5. Stop when low > high -> not found.

Why it works:
    In a sorted list, if the middle is smaller than the target, every element to
    its left is smaller too, so the target can only be on the right.

Time complexity:
    Linear: O(n). Binary: O(log n).

Space complexity:
    O(1) for both (iterative versions).

Edge cases:
    - Empty list -> -1.
    - Target smaller than all / larger than all elements.
    - Duplicates: binary search returns any matching index, not necessarily the
      first one.
    - Binary search on an UNSORTED list gives wrong answers.

Alternative approach:
    A recursive binary search (O(log n) stack space) or the bisect module from
    the standard library.
"""


def linear_search(numbers, target):
    """Return (index or -1, comparisons)."""
    comparisons = 0
    for index in range(len(numbers)):
        comparisons += 1
        if numbers[index] == target:
            return index, comparisons
    return -1, comparisons


def binary_search(numbers, target):
    """Return (index or -1, comparisons). numbers must be sorted ascending."""
    low = 0
    high = len(numbers) - 1
    comparisons = 0
    while low <= high:
        mid = (low + high) // 2
        comparisons += 1
        if numbers[mid] == target:
            return mid, comparisons
        if numbers[mid] < target:
            low = mid + 1  # target can only be in the right half
        else:
            high = mid - 1  # target can only be in the left half
    return -1, comparisons


def main():
    numbers = [3, 8, 12, 19, 25, 31, 47, 52, 60, 74]
    print("sorted list:", numbers)
    for target in [47, 3, 74, 50]:
        linear_result = linear_search(numbers, target)
        binary_result = binary_search(numbers, target)
        print(f"target {target:>2}: linear (index, comparisons) = {linear_result}, "
              f"binary = {binary_result}")
    print("empty list:", linear_search([], 5), binary_search([], 5))


if __name__ == "__main__":
    main()
