"""
Problem title:
    Binary Insertion Sort

Problem statement:
    Improve insertion sort by using binary search to find the position where
    each key must be inserted, then shift elements to make room.

What it teaches:
    - Combining binary search with insertion sort.
    - That fewer comparisons do not change the O(n^2) shifting cost.

Input example:
    [37, 23, 0, 17, 12, 72, 31, 46, 100, 88, 54]

Expected output:
    Original: [37, 23, 0, 17, 12, 72, 31, 46, 100, 88, 54]
    Sorted:   [0, 12, 17, 23, 31, 37, 46, 54, 72, 88, 100]
    Duplicates: [1, 1, 3, 3, 5, 5]
    Empty: []

Approach used:
    For each key, binary search the sorted prefix arr[0..i-1] for the insertion
    index (after any equal values, to stay stable). Then shift the block right by one.

Step-by-step logic:
    1. key = arr[i]; low = 0, high = i.
    2. While low < high: mid = (low + high) // 2; if arr[mid] <= key, low = mid + 1,
       else high = mid.
    3. low is the insertion index.
    4. Shift arr[low..i-1] one step right and set arr[low] = key.

Why it works:
    The prefix is sorted so binary search is valid. Using <= moves past equal
    values, so the key lands after them (stability is kept).

Time complexity:
    Comparisons O(n log n), but shifts remain O(n^2) in the worst case, so the
    total is O(n^2).

Space complexity:
    O(1).

Edge cases:
    Empty list, one element, duplicates, key smaller or larger than everything.

Alternative approach:
    Plain insertion sort (file 01) compares while shifting; it has more
    comparisons but is faster in practice on nearly sorted data.
"""


def find_insert_position(arr, key, high):
    """Return the index in sorted arr[0..high-1] where key should go."""
    low = 0
    while low < high:
        mid = (low + high) // 2
        if arr[mid] <= key:
            low = mid + 1  # go right of equal values (stable)
        else:
            high = mid
    return low


def binary_insertion_sort(arr):
    """Sort arr in place using binary search to locate insert positions."""
    for i in range(1, len(arr)):
        key = arr[i]
        position = find_insert_position(arr, key, i)
        # Shift arr[position .. i-1] one step to the right
        j = i
        while j > position:
            arr[j] = arr[j - 1]
            j -= 1
        arr[position] = key
    return arr


def main():
    data = [37, 23, 0, 17, 12, 72, 31, 46, 100, 88, 54]
    print("Original:", data)
    print("Sorted:  ", binary_insertion_sort(list(data)))
    print("Duplicates:", binary_insertion_sort([5, 1, 5, 1, 3, 3]))
    print("Empty:", binary_insertion_sort([]))


if __name__ == "__main__":
    main()
