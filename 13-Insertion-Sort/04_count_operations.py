"""
Problem title:
    Counting Comparisons and Shifts in Insertion Sort

Problem statement:
    Modify insertion sort so it returns how many comparisons and how many shifts
    (element moves) it performed. Compare best, average and worst case inputs.

What it teaches:
    - Measuring algorithm cost by counting basic operations.
    - Seeing O(n) best case versus O(n^2) worst case with real numbers.

Input example:
    sorted [1..6], a mixed list, and reversed [6..1]

Expected output:
    Best  (sorted)   [1, 2, 3, 4, 5, 6] -> [1, 2, 3, 4, 5, 6]  comparisons=5 shifts=0
    Mixed            [3, 1, 6, 2, 5, 4] -> [1, 2, 3, 4, 5, 6]  comparisons=10 shifts=6
    Worst (reversed) [6, 5, 4, 3, 2, 1] -> [1, 2, 3, 4, 5, 6]  comparisons=15 shifts=15

Approach used:
    Insertion sort with two counters. A comparison is counted each time
    arr[j] is compared with key; a shift each time an element moves right.

Step-by-step logic:
    1. Initialise comparisons = 0 and shifts = 0.
    2. In the inner loop, test j >= 0 first, then count one comparison for arr[j] > key.
    3. If the comparison is true, count a shift and move the element.
    4. Return the counters with the sorted list.

Why it works:
    Every operation of the algorithm is one of these two events, so the counters
    capture the true work. Sorted input: n-1 comparisons, 0 shifts. Reversed
    input: n(n-1)/2 comparisons and n(n-1)/2 shifts.

Time complexity:
    O(n^2) worst/average, O(n) best.

Space complexity:
    O(1).

Edge cases:
    Empty list (0 operations), single element, duplicates (equal elements are
    not shifted, so they cost one comparison and no shift).

Alternative approach:
    Count inversions with a separate brute-force double loop: the number of
    shifts of insertion sort always equals the number of inversions.
"""


def insertion_sort_counted(arr):
    """Sort arr in place; return (arr, comparisons, shifts)."""
    comparisons = 0
    shifts = 0
    for i in range(1, len(arr)):
        key = arr[i]
        j = i - 1
        while j >= 0:
            comparisons += 1
            if arr[j] > key:
                arr[j + 1] = arr[j]
                shifts += 1
                j -= 1
            else:
                break  # found the right place
        arr[j + 1] = key
    return arr, comparisons, shifts


def main():
    cases = [
        ("Best  (sorted)  ", [1, 2, 3, 4, 5, 6]),
        ("Mixed           ", [3, 1, 6, 2, 5, 4]),
        ("Worst (reversed)", [6, 5, 4, 3, 2, 1]),
    ]
    for label, data in cases:
        before = list(data)
        result, comparisons, shifts = insertion_sort_counted(data)
        print(f"{label} {before} -> {result}  comparisons={comparisons} shifts={shifts}")


if __name__ == "__main__":
    main()
