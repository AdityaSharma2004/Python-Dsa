"""
Problem title:
    Merge Two Sorted Lists

Problem statement:
    Given two lists that are each already sorted in ascending order, produce one
    new sorted list that contains all elements of both. Do not use sorted() or
    list.sort(); write the merge step yourself.

What it teaches:
    - The merge operation, the heart of merge sort.
    - The two-pointer technique on sorted data.
    - Why taking "<=" from the left list keeps equal elements in order (stability).

Input example:
    left = [1, 4, 7], right = [2, 3, 9]

Expected output:
    merge([1, 4, 7], [2, 3, 9]) = [1, 2, 3, 4, 7, 9]
    merge([], [5, 6]) = [5, 6]
    merge([1, 2], []) = [1, 2]
    merge([], []) = []
    merge([1, 2, 3], [4, 5, 6]) = [1, 2, 3, 4, 5, 6]
    merge([2, 2, 5], [2, 3, 5]) = [2, 2, 2, 3, 5, 5]
    merge([-5, 0, 4], [-3, -3, 10]) = [-5, -3, -3, 0, 4, 10]

Approach used:
    Keep one pointer in each list. Repeatedly compare the two front elements, copy
    the smaller one into the result and move that pointer. When one list runs out,
    copy the rest of the other list.

Step-by-step logic:
    1. i = 0 (left pointer), j = 0 (right pointer), result = [].
    2. While both i < len(left) and j < len(right):
       if left[i] <= right[j] take left[i], else take right[j].
    3. Append whatever remains of left (from i) and of right (from j).
    4. Return result.

Why it works:
    Both inputs are sorted, so the smallest unused element overall is always one
    of the two front elements. Picking it each time builds the output in order.

Time complexity:
    O(n + m) where n and m are the two lengths: each element is copied once.

Space complexity:
    O(n + m) for the new result list.

Edge cases:
    One or both lists empty, all elements of one list smaller than the other,
    duplicates across lists, negative numbers.

Alternative approach:
    Concatenate and sort again: O((n + m) log(n + m)) and ignores the fact that
    the inputs are already sorted. The two-pointer merge is linear.
"""


def merge(left, right):
    """Return a new sorted list made from two sorted lists."""
    result = []
    i = 0
    j = 0
    while i < len(left) and j < len(right):
        # "<=" takes from the left on ties, which keeps the merge stable
        if left[i] <= right[j]:
            result.append(left[i])
            i += 1
        else:
            result.append(right[j])
            j += 1
    # At most one of these two loops runs: copy the leftovers
    while i < len(left):
        result.append(left[i])
        i += 1
    while j < len(right):
        result.append(right[j])
        j += 1
    return result


def main():
    samples = [
        ([1, 4, 7], [2, 3, 9]),
        ([], [5, 6]),
        ([1, 2], []),
        ([], []),
        ([1, 2, 3], [4, 5, 6]),
        ([2, 2, 5], [2, 3, 5]),
        ([-5, 0, 4], [-3, -3, 10]),
    ]
    for left, right in samples:
        print(f"merge({left}, {right}) = {merge(left, right)}")


if __name__ == "__main__":
    main()
