"""
Problem title:
    Recursive Merge Sort

Problem statement:
    Sort a list of integers in ascending order using merge sort. Implement both
    the recursive splitting and the merge step yourself (no sorted()/.sort()).

What it teaches:
    - Divide and conquer: split, solve each half recursively, combine.
    - The base case of a recursion (a list of 0 or 1 items is already sorted).
    - How the merge step does all the real sorting work.

Input example:
    [38, 27, 43, 3, 9, 82, 10]

Expected output:
    [38, 27, 43, 3, 9, 82, 10] -> [3, 9, 10, 27, 38, 43, 82]
    [] -> []
    [42] -> [42]
    [5, 1, 4, 2, 3] -> [1, 2, 3, 4, 5]
    [9, 8, 7, 6, 5, 4, 3, 2, 1] -> [1, 2, 3, 4, 5, 6, 7, 8, 9]
    [1, 2, 3, 4, 5] -> [1, 2, 3, 4, 5]
    [4, -2, 4, 0, -2, 7] -> [-2, -2, 0, 4, 4, 7]

Approach used:
    Split the list in the middle, sort each half with the same function, then merge
    the two sorted halves into one sorted list.

Step-by-step logic:
    1. If the list has 0 or 1 elements, return it (already sorted).
    2. mid = len(items) // 2; left = items[:mid]; right = items[mid:].
    3. left_sorted = merge_sort(left); right_sorted = merge_sort(right).
    4. Return merge(left_sorted, right_sorted).

Why it works:
    By induction: the base case is correct, and if both halves come back sorted
    then merging two sorted lists gives a sorted whole. Each level of recursion
    halves the size, so there are about log2(n) levels.

Time complexity:
    O(n log n) in best, average and worst cases: log n levels, O(n) merge work
    per level.

Space complexity:
    O(n) extra space for the merged lists (plus O(log n) recursion stack).

Edge cases:
    Empty list, single element, duplicates, already sorted, reverse sorted,
    odd and even lengths, negative numbers.

Alternative approach:
    Iterative bottom-up merge sort (file 05) avoids recursion. Quick sort sorts in
    place but is O(n^2) in the worst case.
"""


def merge(left, right):
    """Merge two sorted lists into one new sorted list."""
    result = []
    i = 0
    j = 0
    while i < len(left) and j < len(right):
        if left[i] <= right[j]:
            result.append(left[i])
            i += 1
        else:
            result.append(right[j])
            j += 1
    while i < len(left):
        result.append(left[i])
        i += 1
    while j < len(right):
        result.append(right[j])
        j += 1
    return result


def merge_sort(items):
    """Return a new list with the items of `items` sorted ascending."""
    if len(items) <= 1:  # base case
        return list(items)
    mid = len(items) // 2
    left_sorted = merge_sort(items[:mid])
    right_sorted = merge_sort(items[mid:])
    return merge(left_sorted, right_sorted)


def main():
    samples = [
        [38, 27, 43, 3, 9, 82, 10],
        [],
        [42],
        [5, 1, 4, 2, 3],
        [9, 8, 7, 6, 5, 4, 3, 2, 1],
        [1, 2, 3, 4, 5],
        [4, -2, 4, 0, -2, 7],
    ]
    for data in samples:
        print(f"{data} -> {merge_sort(data)}")


if __name__ == "__main__":
    main()
