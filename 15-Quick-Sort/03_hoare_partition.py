"""
Problem title:
    Hoare Partition

Problem statement:
    Implement Hoare's partition scheme: use the first element as the pivot and move
    two pointers towards each other, swapping out-of-place pairs, until they cross.
    Return the split index j such that arr[low..j] <= pivot <= arr[j+1..high].

What it teaches:
    - A second partition scheme and how it differs from Lomuto.
    - Two pointers moving from both ends.
    - That Hoare does not place the pivot at a final index; it returns a split point.

Input example:
    [5, 3, 8, 4, 2, 7, 1, 10]  (pivot = first element = 5)

Expected output:
    [5, 3, 8, 4, 2, 7, 1, 10] -> [1, 3, 2, 4, 8, 7, 5, 10], split after index 3, valid=True
    [1, 2, 3, 4, 5] -> [1, 2, 3, 4, 5], split after index 0, valid=True
    [5, 4, 3, 2, 1] -> [1, 4, 3, 2, 5], split after index 3, valid=True
    [3, 3, 3, 3] -> [3, 3, 3, 3], split after index 1, valid=True
    [2, 1] -> [1, 2], split after index 0, valid=True
    [10, 1, 2, 3] -> [3, 1, 2, 10], split after index 2, valid=True

Approach used:
    i starts just before low, j just after high. Move i right until arr[i] >= pivot,
    move j left until arr[j] <= pivot. If i >= j return j; otherwise swap and repeat.

Step-by-step logic:
    1. pivot = arr[low]; i = low - 1; j = high + 1.
    2. Loop: do i += 1 while arr[i] < pivot; do j -= 1 while arr[j] > pivot.
    3. If i >= j: return j.
    4. Swap arr[i] and arr[j] and continue.

Why it works:
    Everything left of i is <= pivot and everything right of j is >= pivot at all
    times. When the pointers meet or cross, the left side (up to j) holds only
    elements <= pivot and the right side only elements >= pivot. The first element
    as pivot guarantees j < high, so recursion on (low, j) and (j + 1, high) always
    shrinks.

Time complexity:
    O(n) for a single partition (each pointer moves across the range once).

Space complexity:
    O(1) extra.

Edge cases:
    Two elements, all equal elements (pointers stop at every item and meet in the
    middle), already sorted, pivot is the largest value.

Alternative approach:
    Lomuto partition (file 01) is easier to write but does more swaps on average
    and degrades badly when there are many equal elements.
"""


def hoare_partition(arr, low, high):
    """Partition arr[low..high] around arr[low]; return the split index j."""
    pivot = arr[low]
    i = low - 1
    j = high + 1
    while True:
        i += 1
        while arr[i] < pivot:
            i += 1
        j -= 1
        while arr[j] > pivot:
            j -= 1
        if i >= j:
            return j
        arr[i], arr[j] = arr[j], arr[i]


def check_split(arr, low, high, split):
    """Verify every item in arr[low..split] <= every item in arr[split+1..high]."""
    for a in range(low, split + 1):
        for b in range(split + 1, high + 1):
            if arr[a] > arr[b]:
                return False
    return True


def main():
    samples = [
        [5, 3, 8, 4, 2, 7, 1, 10],
        [1, 2, 3, 4, 5],
        [5, 4, 3, 2, 1],
        [3, 3, 3, 3],
        [2, 1],
        [10, 1, 2, 3],
    ]
    for data in samples:
        before = list(data)
        split = hoare_partition(data, 0, len(data) - 1)
        ok = check_split(data, 0, len(data) - 1, split)
        print(f"{before} -> {data}, split after index {split}, valid={ok}")


if __name__ == "__main__":
    main()
