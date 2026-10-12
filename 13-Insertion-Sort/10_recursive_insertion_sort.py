"""
Problem title:
    Recursive Insertion Sort

Problem statement:
    Implement insertion sort recursively: sort the first n-1 elements
    recursively, then insert the last element into its place.

What it teaches:
    - Seeing a loop-based algorithm as recursion (base case + smaller problem).
    - Call stack depth and how it limits recursion in Python.

Input example:
    [9, 4, 7, 1, 8, 2]

Expected output:
    [9, 4, 7, 1, 8, 2] -> [1, 2, 4, 7, 8, 9]
    [3, 3, 1] -> [1, 3, 3]
    [1] -> [1]
    [] -> []
    [5, 4, 3, 2, 1] -> [1, 2, 3, 4, 5]

Approach used:
    sort(arr, n): if n <= 1 return; sort(arr, n-1); then insert arr[n-1] into the
    sorted prefix arr[0..n-2] by shifting.

Step-by-step logic:
    1. Base case: 0 or 1 element is already sorted.
    2. Recursively sort the first n-1 elements.
    3. Save last = arr[n-1]; shift larger elements of the prefix right.
    4. Place last into the gap.

Why it works:
    By induction: if the recursive call sorts the prefix correctly, inserting the
    last element keeps the prefix of length n sorted.

Time complexity:
    O(n^2) worst/average, O(n) best.

Space complexity:
    O(n) because of the recursion stack (n nested calls), unlike the loop version.

Edge cases:
    Empty list, one element, duplicates. Very long lists (about 1000+) exceed
    Python's default recursion limit, which is why the loop version is preferred.

Alternative approach:
    The iterative version (file 01) uses O(1) space.
"""


def insert_last(arr, n):
    """Insert arr[n-1] into the sorted prefix arr[0..n-2]."""
    last = arr[n - 1]
    j = n - 2
    while j >= 0 and arr[j] > last:
        arr[j + 1] = arr[j]
        j -= 1
    arr[j + 1] = last


def recursive_insertion_sort(arr, n=None):
    """Sort the first n elements of arr in place (default: all)."""
    if n is None:
        n = len(arr)
    if n <= 1:  # base case
        return arr
    recursive_insertion_sort(arr, n - 1)  # sort the smaller problem
    insert_last(arr, n)
    return arr


def main():
    for data in ([9, 4, 7, 1, 8, 2], [3, 3, 1], [1], [], [5, 4, 3, 2, 1]):
        original = list(data)
        print(f"{original} -> {recursive_insertion_sort(data)}")


if __name__ == "__main__":
    main()
