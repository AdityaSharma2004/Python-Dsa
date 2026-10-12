"""
Problem Title: k-th Smallest Element with Quickselect

Problem Statement:
    Find the k-th smallest element (1-based) of an unsorted list WITHOUT
    sorting the whole list.

What It Teaches:
    - Divide and conquer that discards one side after partitioning.
    - Partitioning (Lomuto) as a reusable building block.
    - Average O(n) vs worst case O(n^2) behaviour.

Input Example:
    data = [7, 10, 4, 3, 20, 15], k = 3 (and others)

Expected Output:
    Data: [7, 10, 4, 3, 20, 15]
    1-th smallest = 3
    3-th smallest = 7
    6-th smallest = 20
    Duplicates: [5, 2, 5, 2, 9, 5]
      k=1: 2
      k=2: 2
      k=3: 5
      k=4: 5
      k=5: 5
      k=6: 9
    k=7 -> k must be between 1 and len(data)

Approach:
    Partition the list around a pivot so smaller values are left of it and
    larger values right of it. The pivot ends at its final sorted position p.
    If p == k - 1 we are done; if p is larger, search the left part; otherwise
    search the right part.

Step-by-Step Logic:
    1. Copy the list (do not disturb the caller's data).
    2. Pick the last element of the range as pivot (Lomuto scheme).
    3. Move every element < pivot to the front of the range, then place the
       pivot right after them.
    4. Compare the pivot's index with the target index and recurse on one side.

Why It Works:
    After partitioning, the pivot sits where it would be in the sorted list, so
    we know exactly which side holds the k-th element. We only ever explore
    one side, so the expected work is n + n/2 + n/4 + ... = O(n).

Time Complexity:
    Average O(n); worst case O(n^2) with consistently bad pivots (sorted input
    and last-element pivot).
Space Complexity:
    O(n) for the copy plus O(log n) average recursion depth.

Edge Cases:
    k out of range (raise ValueError), duplicates, single element, already
    sorted input, k = 1 (minimum) and k = n (maximum).

Alternative Approach:
    Sort and index: O(n log n). A min-heap of size k: O(n log k). Median of
    medians gives guaranteed O(n) but is more complex.
"""


def partition(data, low, high):
    """Lomuto partition using data[high] as pivot; return pivot's final index."""
    pivot = data[high]
    boundary = low  # everything before boundary is < pivot
    for index in range(low, high):
        if data[index] < pivot:
            data[index], data[boundary] = data[boundary], data[index]
            boundary += 1
    data[boundary], data[high] = data[high], data[boundary]
    return boundary


def quickselect(data, low, high, target_index):
    """Return the element that belongs at target_index in sorted order."""
    if low == high:
        return data[low]
    pivot_index = partition(data, low, high)
    if pivot_index == target_index:
        return data[pivot_index]
    if pivot_index > target_index:
        return quickselect(data, low, pivot_index - 1, target_index)
    return quickselect(data, pivot_index + 1, high, target_index)


def kth_smallest(data, k):
    """k is 1-based."""
    if k < 1 or k > len(data):
        raise ValueError("k must be between 1 and len(data)")
    working_copy = list(data)
    return quickselect(working_copy, 0, len(working_copy) - 1, k - 1)


def main():
    data = [7, 10, 4, 3, 20, 15]
    print("Data:", data)
    for k in [1, 3, 6]:
        print(f"{k}-th smallest = {kth_smallest(data, k)}")
    duplicates = [5, 2, 5, 2, 9, 5]
    print("Duplicates:", duplicates)
    for k in range(1, len(duplicates) + 1):
        print(f"  k={k}: {kth_smallest(duplicates, k)}")
    reference = sorted(duplicates)  # verification only
    for k in range(1, len(duplicates) + 1):
        assert kth_smallest(duplicates, k) == reference[k - 1]
    try:
        kth_smallest(data, 7)
    except ValueError as error:
        print("k=7 ->", error)


if __name__ == "__main__":
    main()
