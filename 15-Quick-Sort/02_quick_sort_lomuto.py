"""
Problem title:
    Quick Sort with Lomuto Partition

Problem statement:
    Sort a list of integers in ascending order, in place, using quick sort with
    the Lomuto partition scheme. Do not use sorted() or list.sort().

What it teaches:
    - Divide and conquer without a merge step: the partition does the work.
    - Recursing on index ranges (low, high) instead of copying sub-lists.
    - Why the recursion stops when the range has fewer than two elements.

Input example:
    [10, 7, 8, 9, 1, 5]

Expected output:
    [10, 7, 8, 9, 1, 5] -> [1, 5, 7, 8, 9, 10]
    [] -> []
    [3] -> [3]
    [1, 2, 3, 4, 5] -> [1, 2, 3, 4, 5]
    [5, 4, 3, 2, 1] -> [1, 2, 3, 4, 5]
    [4, -1, 4, 0, -1, 9, 2] -> [-1, -1, 0, 2, 4, 4, 9]
    [2, 2, 2, 2] -> [2, 2, 2, 2]

Approach used:
    Partition around the last element; the pivot lands in its final place. Then
    sort the part to the left of the pivot and the part to the right recursively.

Step-by-step logic:
    1. If low >= high the range has 0 or 1 element: return.
    2. p = lomuto_partition(arr, low, high).
    3. quick_sort(arr, low, p - 1) and quick_sort(arr, p + 1, high).

Why it works:
    After partitioning, the pivot is in its final sorted position, every element
    to its left is <= it and every element to its right is greater. Sorting the two
    sides independently therefore sorts the entire range.

Time complexity:
    Best/average O(n log n) (balanced splits); worst O(n^2) when every partition is
    lopsided, for example last-element pivot on an already sorted list.

Space complexity:
    O(1) extra data, but O(log n) average and O(n) worst-case recursion stack.

Edge cases:
    Empty list, single element, already sorted (worst case here), reverse sorted,
    all equal elements (also quadratic with Lomuto), negative numbers.

Alternative approach:
    Randomized or median-of-three pivots (files 05 and 06) avoid the sorted-input
    worst case; three-way partition (file 07) fixes the all-equal case.
"""


def lomuto_partition(arr, low, high):
    """Partition arr[low..high] around arr[high]; return the pivot's final index."""
    pivot = arr[high]
    boundary = low - 1
    for j in range(low, high):
        if arr[j] <= pivot:
            boundary += 1
            arr[boundary], arr[j] = arr[j], arr[boundary]
    arr[boundary + 1], arr[high] = arr[high], arr[boundary + 1]
    return boundary + 1


def quick_sort(arr, low, high):
    """Sort arr[low..high] in place."""
    if low >= high:  # base case: 0 or 1 element
        return
    pivot_index = lomuto_partition(arr, low, high)
    quick_sort(arr, low, pivot_index - 1)
    quick_sort(arr, pivot_index + 1, high)


def sort_list(arr):
    """Convenience wrapper: sort the whole list in place and return it."""
    quick_sort(arr, 0, len(arr) - 1)
    return arr


def main():
    samples = [
        [10, 7, 8, 9, 1, 5],
        [],
        [3],
        [1, 2, 3, 4, 5],
        [5, 4, 3, 2, 1],
        [4, -1, 4, 0, -1, 9, 2],
        [2, 2, 2, 2],
    ]
    for data in samples:
        original = list(data)
        print(f"{original} -> {sort_list(data)}")


if __name__ == "__main__":
    main()
