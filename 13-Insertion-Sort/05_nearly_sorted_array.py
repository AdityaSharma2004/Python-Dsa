"""
Problem title:
    Insertion Sort on Nearly Sorted Arrays

Problem statement:
    Show that insertion sort is very fast when every element is at most k
    positions away from its sorted place. Build a nearly sorted list, sort it,
    and compare the number of shifts with a reversed list of the same size.

What it teaches:
    - Why insertion sort is "adaptive": its work depends on how disordered the input is.
    - Why it is used for small or almost sorted data (for example in hybrid sorts).

Input example:
    [1, 2, 4, 3, 5, 7, 6, 8, 10, 9] (each element is 1 step from its place)

Expected output:
    Nearly sorted input: [1, 2, 4, 3, 5, 7, 6, 8, 10, 9]
    Shifts for nearly sorted list (n=10): 3
    Shifts for reversed list      (n=10): 45
    Shifts for nearly sorted list (n=1000): 333
    Shifts for reversed list      (n=1000): 499500

Approach used:
    Count shifts with the normal algorithm on a nearly sorted list and on a
    reversed list of the same length, then compare the counts.

Step-by-step logic:
    1. Build a sorted list 1..n.
    2. Make it nearly sorted by swapping neighbouring pairs at fixed intervals.
    3. Sort a copy while counting shifts.
    4. Do the same for a reversed list and print both counts.

Why it works:
    The shifts needed equal the number of inversions. If each element is at most
    k places away from its final spot, every key shifts at most k times, so total
    shifts are at most n*k, i.e. O(n*k), which is O(n) for small constant k.

Time complexity:
    O(n*k) for a k-nearly sorted list; O(n^2) for the reversed list.

Space complexity:
    O(1) for sorting (plus the lists built for the demo).

Edge cases:
    k = 0 (already sorted), n smaller than the swap interval, empty list.

Alternative approach:
    A min-heap of size k+1 sorts k-nearly sorted data in O(n log k).
"""


def insertion_sort_count_shifts(arr):
    """Sort arr in place and return the number of shifts performed."""
    shifts = 0
    for i in range(1, len(arr)):
        key = arr[i]
        j = i - 1
        while j >= 0 and arr[j] > key:
            arr[j + 1] = arr[j]
            shifts += 1
            j -= 1
        arr[j + 1] = key
    return shifts


def make_nearly_sorted(n, step=3):
    """Return 1..n with the pair at (step-1, step) swapped repeatedly."""
    arr = []
    for value in range(1, n + 1):
        arr.append(value)
    # Swap neighbours at positions step-1 and step, 2*step-1 and 2*step, ...
    i = step - 1
    while i + 1 < n:
        arr[i], arr[i + 1] = arr[i + 1], arr[i]
        i += step
    return arr


def make_reversed(n):
    """Return [n, n-1, ..., 1]."""
    arr = []
    for value in range(n, 0, -1):
        arr.append(value)
    return arr


def main():
    n = 10
    nearly = make_nearly_sorted(n)
    reverse = make_reversed(n)
    print("Nearly sorted input:", nearly)
    nearly_shifts = insertion_sort_count_shifts(list(nearly))
    reverse_shifts = insertion_sort_count_shifts(list(reverse))
    print(f"Shifts for nearly sorted list (n={n}): {nearly_shifts}")
    print(f"Shifts for reversed list      (n={n}): {reverse_shifts}")

    n = 1000
    nearly_shifts = insertion_sort_count_shifts(make_nearly_sorted(n))
    reverse_shifts = insertion_sort_count_shifts(make_reversed(n))
    print(f"Shifts for nearly sorted list (n={n}): {nearly_shifts}")
    print(f"Shifts for reversed list      (n={n}): {reverse_shifts}")


if __name__ == "__main__":
    main()
