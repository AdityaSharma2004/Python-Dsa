r"""
Problem title: Linearithmic Time - O(n log n) with Merge Sort

Problem statement:
    Sort a list with merge sort and count the number of element comparisons.
    Compare the count with n * log2(n) for several sizes.

What it teaches:
    O(n log n): "split in halves (log n levels) and do linear work on each
    level". This is the speed limit of comparison-based sorting.

Input example:
    numbers = [38, 27, 43, 3, 9, 82, 10]

Expected output:
    input : [38, 27, 43, 3, 9, 82, 10]
    sorted: [3, 9, 10, 27, 38, 43, 82]
    comparisons: 13
    n = 8: comparisons = 17, n*log2(n) = 24
    n = 64: comparisons = 318, n*log2(n) = 384
    n = 512: comparisons = 3766, n*log2(n) = 4608

Approach:
    Divide the list into halves recursively, sort each half, merge the two
    sorted halves using a two-pointer merge.

Step-by-step logic:
    1. If the list has 0 or 1 items it is already sorted.
    2. Split at the middle and sort both halves recursively.
    3. Merge: compare the front items of both halves, take the smaller one.
    4. Count every comparison done during the merge.

Why it works:
    Merging two sorted lists is a single linear pass. The recursion has about
    log2(n) levels and every level merges n items in total.

Time complexity:
    O(n log n) in best, average and worst case.

Space complexity:
    O(n) for the temporary merged lists.

Edge cases:
    - Empty list and single element list.
    - Already sorted or reverse-sorted input (same complexity).
    - Duplicate values (taking from the left half first keeps it stable).

Alternative approach:
    Heap sort or quick sort (average case). A simple bubble sort is O(n^2).
"""

import math


def merge(left, right, counter):
    """Merge two sorted lists; counter[0] counts comparisons."""
    merged = []
    i = 0
    j = 0
    while i < len(left) and j < len(right):
        counter[0] += 1
        if left[i] <= right[j]:
            merged.append(left[i])
            i += 1
        else:
            merged.append(right[j])
            j += 1
    merged.extend(left[i:])
    merged.extend(right[j:])
    return merged


def merge_sort(numbers, counter):
    if len(numbers) <= 1:
        return numbers
    mid = len(numbers) // 2
    left = merge_sort(numbers[:mid], counter)
    right = merge_sort(numbers[mid:], counter)
    return merge(left, right, counter)


def main():
    numbers = [38, 27, 43, 3, 9, 82, 10]
    counter = [0]
    result = merge_sort(numbers, counter)
    print("input :", numbers)
    print("sorted:", result)
    print("comparisons:", counter[0])
    for n in [8, 64, 512]:
        data = [(i * 37) % n for i in range(n)]  # deterministic scrambled data
        counter = [0]
        merge_sort(data, counter)
        print(f"n = {n}: comparisons = {counter[0]}, n*log2(n) = {int(n * math.log2(n))}")


if __name__ == "__main__":
    main()
