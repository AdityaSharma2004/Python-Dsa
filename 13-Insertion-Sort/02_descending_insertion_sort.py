"""
Problem title:
    Insertion Sort in Descending Order

Problem statement:
    Sort a list of numbers from largest to smallest using insertion sort.
    Make the order selectable so one function handles both directions.

What it teaches:
    - Changing the comparison is all that is needed to flip the sort order.
    - Passing a boolean flag to make a function flexible.

Input example:
    [4, 10, 3, 8, 1]

Expected output:
    Original:    [4, 10, 3, 8, 1]
    Descending:  [10, 8, 4, 3, 1]
    Ascending:   [1, 3, 4, 8, 10]
    Equal items: [2, 2, 2]
    Empty list:  []

Approach used:
    Standard insertion sort, but an element is shifted right when it is SMALLER
    than the key (descending) instead of larger (ascending).

Step-by-step logic:
    1. For each i from 1, key = arr[i].
    2. Compare key with the elements on its left going backwards.
    3. For descending order, shift an element right while arr[j] < key.
    4. Place key into the opened gap.

Why it works:
    The invariant is now "arr[0..i-1] is sorted from large to small". Shifting
    smaller elements right leaves the gap exactly where key belongs.

Time complexity:
    O(n^2) worst/average, O(n) best (already in the requested order).

Space complexity:
    O(1).

Edge cases:
    Empty list, one element, all equal values (no shifts), already descending.

Alternative approach:
    Sort ascending and then reverse the list manually; this costs an extra pass.
"""


def should_shift(left, key, descending):
    """Return True when the left element must move right of key."""
    if descending:
        return left < key
    return left > key


def insertion_sort(arr, descending=False):
    """Sort arr in place; ascending by default, descending if requested."""
    for i in range(1, len(arr)):
        key = arr[i]
        j = i - 1
        while j >= 0 and should_shift(arr[j], key, descending):
            arr[j + 1] = arr[j]
            j -= 1
        arr[j + 1] = key
    return arr


def main():
    data = [4, 10, 3, 8, 1]
    print("Original:   ", data)
    print("Descending: ", insertion_sort(list(data), descending=True))
    print("Ascending:  ", insertion_sort(list(data)))
    print("Equal items:", insertion_sort([2, 2, 2], descending=True))
    print("Empty list: ", insertion_sort([], descending=True))


if __name__ == "__main__":
    main()
