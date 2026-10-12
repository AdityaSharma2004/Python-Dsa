"""
Problem title:
    Quick Select (k-th Smallest Element)

Problem statement:
    Find the k-th smallest element of an unsorted list (k = 1 is the minimum)
    without sorting the whole list, by reusing the quick sort partition and
    recursing into only ONE side.

What it teaches:
    - Partitioning can answer "what is at position k?" without full sorting.
    - Why discarding one side drops the average cost from O(n log n) to O(n).
    - Converting a recursive divide-and-conquer into a loop.

Input example:
    numbers = [7, 10, 4, 3, 20, 15], k = 3

Expected output:
    Numbers: [7, 10, 4, 3, 20, 15]
    k=1: 3
    k=3: 7
    k=6: 20
    Duplicates, k=3: 5
    Single element: 42
    Error: k must be between 1 and the list length
    Error: k must be between 1 and the list length
    Matches sorted() for every k? True

Approach used:
    Lomuto-partition the range; the pivot lands at its final sorted index p.
    If p equals the target index, we are done; otherwise continue in the left
    or right part only.

Step-by-step logic:
    1. target = k - 1 (zero-based position in sorted order).
    2. low = 0, high = n - 1. Loop: p = partition(low, high).
    3. If p == target return arr[p]; if target < p: high = p - 1;
       else: low = p + 1.
    4. A deterministic pseudo-random pivot swap protects against sorted input.

Why it works:
    After partition, exactly p elements are <= the pivot on its left, so the
    pivot is the (p + 1)-th smallest. The target lies on the side that
    contains its index; the other side can be ignored.

Time complexity:
    Average O(n) (n + n/2 + n/4 + ...); worst case O(n^2) with unlucky pivots.

Space complexity:
    O(1) extra: iterative, works on a copy of the list.

Edge cases:
    - k out of range (k < 1 or k > n) raises ValueError.
    - Empty list raises ValueError.
    - Duplicates: the k-th smallest counts repeated values separately.
    - Single element.

Alternative approach:
    Sort and index (O(n log n)), a heap of size k (O(n log k)), or the
    median-of-medians algorithm for guaranteed O(n).
"""


def lomuto_partition(arr, low, high):
    """Partition arr[low..high] around arr[high]; return pivot's final index."""
    pivot = arr[high]
    boundary = low - 1
    for j in range(low, high):
        if arr[j] <= pivot:
            boundary += 1
            arr[boundary], arr[j] = arr[j], arr[boundary]
    arr[boundary + 1], arr[high] = arr[high], arr[boundary + 1]
    return boundary + 1


def quick_select(values, k):
    """Return the k-th smallest element (1-based k) of values."""
    if k < 1 or k > len(values):
        raise ValueError("k must be between 1 and the list length")
    arr = list(values)  # do not disturb the caller's list
    target = k - 1
    low = 0
    high = len(arr) - 1
    state = 12345  # tiny deterministic generator for the pivot choice
    while True:
        state = (state * 1103515245 + 12345) % 2147483648
        chosen = low + state % (high - low + 1)
        arr[chosen], arr[high] = arr[high], arr[chosen]
        pivot_index = lomuto_partition(arr, low, high)
        if pivot_index == target:
            return arr[pivot_index]
        if target < pivot_index:
            high = pivot_index - 1
        else:
            low = pivot_index + 1


def main():
    numbers = [7, 10, 4, 3, 20, 15]
    print("Numbers:", numbers)
    for k in (1, 3, 6):
        print(f"k={k}: {quick_select(numbers, k)}")

    # Edge cases
    print("Duplicates, k=3:", quick_select([5, 1, 5, 1, 5], 3))
    print("Single element:", quick_select([42], 1))
    for bad in ([], 0), ([1, 2, 3], 4):
        try:
            quick_select(bad[0], bad[1])
        except ValueError as error:
            print("Error:", error)

    # Verification: k-th smallest equals sorted(...)[k-1] (check only).
    data = [(i * 53) % 97 for i in range(60)]
    ok = all(quick_select(data, k) == sorted(data)[k - 1] for k in range(1, 61))
    print("Matches sorted() for every k?", ok)


if __name__ == "__main__":
    main()
