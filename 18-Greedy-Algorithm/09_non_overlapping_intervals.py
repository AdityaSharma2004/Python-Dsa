"""
Problem title:
    Non-overlapping Intervals (Minimum Removals)

Problem statement:
    Given intervals [start, end], return the minimum number of intervals to
    remove so that the remaining ones do not overlap. Intervals that only
    touch at an endpoint (e.g. [1,2] and [2,3]) do not overlap.

What it teaches:
    * Reusing the activity-selection idea: keep the most intervals, and the
      rest are the removals (removals = total - kept).
    * Sorting by END time, not start time.

Input example:
    [[1, 2], [2, 3], [3, 4], [1, 3]]

Expected output:
    [[1, 2], [2, 3], [3, 4], [1, 3]] -> remove 1
    [[1, 2], [1, 2], [1, 2]] -> remove 2
    [[1, 2], [2, 3]] -> remove 0
    [[1, 100], [11, 22], [1, 11], [2, 12]] -> remove 2
    [] -> remove 0

Approach:
    Sort by end time. Keep an interval if it starts at or after the end of the
    last kept interval; otherwise it overlaps and must be removed.

Step-by-step logic:
    1. Sort intervals by end time ascending.
    2. last_end = end of the first interval, removed = 0.
    3. For each following interval: if start >= last_end keep it and update
       last_end; else removed += 1.
    4. Return removed.

Why it works:
    Among overlapping intervals, the one that ends earliest blocks the least
    future space, so keeping it and removing the others can never be worse
    (same exchange argument as activity selection).

Time complexity:
    O(n log n) for sorting + O(n) scan.

Space complexity:
    O(n) for the sorted copy.

Edge cases:
    * Empty list -> 0.
    * Identical intervals: all but one are removed.
    * Touching intervals are not overlaps (use >=).

Alternative approach:
    Sort by start and, on overlap, remove the interval with the larger end
    (also O(n log n)). DP (longest chain) works in O(n^2).
"""


def merge_sort(items, comes_first):
    """Stable merge sort; `comes_first(a, b)` is True when a must precede b."""
    if len(items) <= 1:
        return list(items)
    middle = len(items) // 2
    left = merge_sort(items[:middle], comes_first)
    right = merge_sort(items[middle:], comes_first)
    merged = []
    i = j = 0
    while i < len(left) and j < len(right):
        if comes_first(right[j], left[i]):
            merged.append(right[j])
            j += 1
        else:
            merged.append(left[i])
            i += 1
    merged.extend(left[i:])
    merged.extend(right[j:])
    return merged


def erase_overlap_intervals(intervals):
    """Return the minimum number of intervals to remove."""
    if not intervals:
        return 0
    by_end = merge_sort(intervals, lambda a, b: a[1] < b[1])
    last_end = by_end[0][1]
    removed = 0
    for start, end in by_end[1:]:
        if start >= last_end:  # no overlap: keep it
            last_end = end
        else:  # overlap: drop this one (it ends later than the kept one)
            removed += 1
    return removed


def main():
    tests = [
        [[1, 2], [2, 3], [3, 4], [1, 3]],
        [[1, 2], [1, 2], [1, 2]],
        [[1, 2], [2, 3]],
        [[1, 100], [11, 22], [1, 11], [2, 12]],
        [],
    ]
    for intervals in tests:
        print(f"{intervals} -> remove {erase_overlap_intervals(intervals)}")


if __name__ == "__main__":
    main()
