"""
Problem title:
    Basic Insertion Sort (ascending)

Problem statement:
    Given a list of integers, sort it in ascending order using insertion sort.
    Do not use sorted() or list.sort(); implement the algorithm yourself.

What it teaches:
    - How insertion sort grows a sorted "left part" one element at a time.
    - Shifting elements to the right instead of swapping every pair.
    - Writing an in-place algorithm that mutates the given list.

Input example:
    [5, 2, 4, 6, 1, 3]

Expected output:
    [5, 2, 4, 6, 1, 3] -> [1, 2, 3, 4, 5, 6]
    [] -> []
    [7] -> [7]
    [1, 2, 3, 4] -> [1, 2, 3, 4]
    [9, 7, 5, 3, 1] -> [1, 3, 5, 7, 9]
    [3, -1, 3, 0, -5, 2] -> [-5, -1, 0, 2, 3, 3]

Approach used:
    Treat index 0 as an already sorted part. Take each next element (the "key")
    and insert it into the correct place inside the sorted part.

Step-by-step logic:
    1. Loop i from 1 to n-1; key = arr[i].
    2. Set j = i - 1 (last index of the sorted part).
    3. While j >= 0 and arr[j] > key: copy arr[j] one slot right, j -= 1.
    4. Put key into arr[j + 1], the gap that was opened.

Why it works:
    Before each iteration arr[0..i-1] is sorted (loop invariant). Shifting every
    larger element right opens exactly the right gap for key, so arr[0..i] is
    sorted afterwards. When i reaches n, the whole list is sorted.

Time complexity:
    Worst/average O(n^2) (reverse order, many shifts); best O(n) (already sorted).

Space complexity:
    O(1) extra space (in place).

Edge cases:
    Empty list, single element, already sorted, reverse sorted, duplicates,
    negative numbers.

Alternative approach:
    Swap-based insertion (swap key leftwards pair by pair) is simpler to read but
    does about 3x more writes. Binary insertion sort (file 07) reduces comparisons.
"""


def insertion_sort(arr):
    """Sort arr in place in ascending order and return it."""
    for i in range(1, len(arr)):
        key = arr[i]
        j = i - 1
        # Shift elements of the sorted part that are bigger than key
        while j >= 0 and arr[j] > key:
            arr[j + 1] = arr[j]
            j -= 1
        arr[j + 1] = key  # drop key into the gap
    return arr


def main():
    samples = [
        [5, 2, 4, 6, 1, 3],
        [],
        [7],
        [1, 2, 3, 4],
        [9, 7, 5, 3, 1],
        [3, -1, 3, 0, -5, 2],
    ]
    for data in samples:
        original = list(data)
        result = insertion_sort(data)
        print(f"{original} -> {result}")


if __name__ == "__main__":
    main()
