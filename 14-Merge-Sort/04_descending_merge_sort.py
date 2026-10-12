"""
Problem title:
    Merge Sort in Descending Order

Problem statement:
    Sort a list from largest to smallest using merge sort. Make the order
    configurable so one function can sort both ascending and descending.

What it teaches:
    - Changing a single comparison in the merge step changes the sort order.
    - Passing the order as a parameter instead of copying the whole algorithm.
    - Keeping stability when the order is reversed (ties still take the left item).

Input example:
    [12, 11, 13, 5, 6, 7]

Expected output:
    Original:   [12, 11, 13, 5, 6, 7]
    Descending: [13, 12, 11, 7, 6, 5]
    Ascending:  [5, 6, 7, 11, 12, 13]
    With duplicates: [3, 3, 2, 1, 1]
    Negatives:       [4, 0, -1, -7]
    Empty:           []

Approach used:
    Same recursive merge sort as the ascending version. The merge step uses a
    helper `comes_first(a, b, descending)` that decides whether a should be
    placed before b.

Step-by-step logic:
    1. Split the list in two halves and sort each recursively.
    2. In merge, take left[i] if left[i] should come before-or-tie right[j]:
       ascending: left[i] <= right[j]; descending: left[i] >= right[j].
    3. Copy leftovers and return.

Why it works:
    The merge only needs a consistent "which one goes first" rule. Flipping the
    rule from <= to >= gives the mirror order, and using a non-strict comparison
    keeps equal elements in their original relative order.

Time complexity:
    O(n log n) for every input.

Space complexity:
    O(n) extra for merged lists (plus O(log n) recursion stack).

Edge cases:
    Empty list, single element, all equal elements, already descending,
    negative numbers.

Alternative approach:
    Sort ascending then reverse by hand: an extra O(n) pass, but ties would end up
    in reversed order, so the sort would no longer be stable.
"""


def comes_first(a, b, descending):
    """Return True if a may be placed before b in the chosen order."""
    if descending:
        return a >= b
    return a <= b


def merge(left, right, descending):
    """Merge two lists that are sorted in the chosen order."""
    result = []
    i = 0
    j = 0
    while i < len(left) and j < len(right):
        if comes_first(left[i], right[j], descending):
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


def merge_sort(items, descending=False):
    """Return a new sorted list (ascending by default)."""
    if len(items) <= 1:
        return list(items)
    mid = len(items) // 2
    left = merge_sort(items[:mid], descending)
    right = merge_sort(items[mid:], descending)
    return merge(left, right, descending)


def main():
    data = [12, 11, 13, 5, 6, 7]
    print(f"Original:   {data}")
    print(f"Descending: {merge_sort(data, descending=True)}")
    print(f"Ascending:  {merge_sort(data)}")
    print(f"With duplicates: {merge_sort([3, 1, 3, 2, 1], descending=True)}")
    print(f"Negatives:       {merge_sort([-1, -7, 4, 0], descending=True)}")
    print(f"Empty:           {merge_sort([], descending=True)}")


if __name__ == "__main__":
    main()
