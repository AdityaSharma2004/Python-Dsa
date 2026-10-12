"""
Problem title:
    Count Inversions Using Merge Sort

Problem statement:
    An inversion is a pair of positions (i, j) with i < j and arr[i] > arr[j].
    Count the inversions of a list in O(n log n) time. A brute-force O(n^2)
    version is included to verify the answer.

What it teaches:
    - Extending merge sort to compute extra information during the merge.
    - Why inversions measure "how unsorted" a list is.
    - Counting many pairs at once instead of one by one.

Input example:
    [2, 4, 1, 3, 5]

Expected output:
    [2, 4, 1, 3, 5]: inversions=3 (brute force=3) OK
    [1, 2, 3, 4, 5]: inversions=0 (brute force=0) OK
    [5, 4, 3, 2, 1]: inversions=10 (brute force=10) OK
    [1, 1, 1]: inversions=0 (brute force=0) OK
    []: inversions=0 (brute force=0) OK
    [8, 4, 2, 1]: inversions=6 (brute force=6) OK
    [3, 1, 2, 3, 1]: inversions=5 (brute force=5) OK

Approach used:
    Merge sort that returns (sorted_list, inversion_count). While merging, if an
    element from the right half is placed before the remaining left elements, it
    forms an inversion with every one of those remaining left elements.

Step-by-step logic:
    1. Base case: 0 or 1 element -> (list, 0).
    2. Recursively get (left_sorted, a) and (right_sorted, b).
    3. Merge. When right[j] < left[i] is chosen, add (len(left) - i) to the
       cross count, because left[i..] are all larger than right[j].
    4. Return (merged, a + b + cross).

Why it works:
    Every inversion is either inside the left half, inside the right half, or
    across the two halves. The recursive calls count the first two groups; the
    merge counts the cross pairs exactly once. Because both halves are sorted,
    one comparison accounts for a whole block of pairs.

Time complexity:
    O(n log n) for the merge-sort counter; O(n^2) for the brute-force check.

Space complexity:
    O(n) for merged lists (plus O(log n) recursion stack). Brute force uses O(1).

Edge cases:
    Empty list or one element (0 inversions), sorted list (0), reverse sorted
    list (n*(n-1)/2), duplicates (equal elements are NOT inversions).

Alternative approach:
    A Fenwick tree (BIT) over compressed values also counts inversions in
    O(n log n).
"""


def merge_and_count(left, right):
    """Merge sorted halves; return (merged_list, cross_inversions)."""
    result = []
    i = 0
    j = 0
    cross = 0
    while i < len(left) and j < len(right):
        if left[i] <= right[j]:  # "<=" so equal values are not counted
            result.append(left[i])
            i += 1
        else:
            result.append(right[j])
            # right[j] is smaller than all remaining left items
            cross += len(left) - i
            j += 1
    while i < len(left):
        result.append(left[i])
        i += 1
    while j < len(right):
        result.append(right[j])
        j += 1
    return result, cross


def sort_and_count(items):
    """Return (sorted_list, number_of_inversions)."""
    if len(items) <= 1:
        return list(items), 0
    mid = len(items) // 2
    left, left_count = sort_and_count(items[:mid])
    right, right_count = sort_and_count(items[mid:])
    merged, cross = merge_and_count(left, right)
    return merged, left_count + right_count + cross


def count_inversions_brute_force(items):
    """O(n^2) check: look at every pair."""
    count = 0
    for i in range(len(items)):
        for j in range(i + 1, len(items)):
            if items[i] > items[j]:
                count += 1
    return count


def main():
    samples = [
        [2, 4, 1, 3, 5],
        [1, 2, 3, 4, 5],
        [5, 4, 3, 2, 1],
        [1, 1, 1],
        [],
        [8, 4, 2, 1],
        [3, 1, 2, 3, 1],
    ]
    for data in samples:
        _, fast = sort_and_count(data)
        slow = count_inversions_brute_force(data)
        status = "OK" if fast == slow else "MISMATCH"
        print(f"{data}: inversions={fast} (brute force={slow}) {status}")


if __name__ == "__main__":
    main()
