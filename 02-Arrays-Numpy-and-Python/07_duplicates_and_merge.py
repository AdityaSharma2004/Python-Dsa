r"""
Problem title: Remove Duplicates and Merge Sorted Arrays

Problem statement:
    (a) Remove duplicates from a SORTED list in place and return the new length.
    (b) Merge two sorted lists into one sorted list.
    (c) Find the duplicate values in any list.

What it teaches:
    The two-pointer technique on sorted data (a "slow" write pointer and a
    "fast" read pointer, and one pointer per list for merging) and using a set
    for fast duplicate detection.

Input example:
    sorted_numbers = [1, 1, 2, 2, 2, 3, 5, 5]
    left = [1, 4, 7], right = [2, 3, 9, 10]

Expected output:
    before: [1, 1, 2, 2, 2, 3, 5, 5]
    after remove_duplicates_sorted: [1, 2, 3, 5] length = 4
    all equal: 1
    empty: 0
    merge [1, 4, 7] [2, 3, 9, 10] -> [1, 2, 3, 4, 7, 9, 10]
    merge with empty: [5, 6] [1]
    merge with duplicates: [1, 3, 3, 3, 4]
    find_duplicates: [3, 1]
    no duplicates: []

Approach:
    (a) write = 1; for read in 1..n-1: if items[read] != items[write-1], copy it
        to items[write] and move write.
    (b) Compare the front of both lists, append the smaller, move that pointer;
        append what remains.
    (c) Walk once, remembering seen values in a set.

Step-by-step logic:
    Dry run (a) [1, 1, 2]: write=1; read=1: 1 == items[0] skip; read=2: 2 != 1
    -> items[1] = 2, write=2. Answer length 2 -> [1, 2].

Why it works:
    In sorted data equal values are neighbours, so comparing with the last kept
    value is enough. In merging, the smallest unused value is always at one of
    the two fronts.

Time complexity:
    (a) O(n). (b) O(n + m). (c) O(n) average (set lookups are O(1)).

Space complexity:
    (a) O(1). (b) O(n + m) for the result. (c) O(n) for the set.

Edge cases:
    - Empty lists for any function.
    - All elements equal -> length 1.
    - One list much longer than the other (leftover copy).
    - (a) and (b) REQUIRE sorted input.

Alternative approach:
    list(set(items)) removes duplicates but loses order; sorted(left + right)
    merges in O(n log n) instead of O(n + m).
"""


def remove_duplicates_sorted(items):
    """Keep one copy of each value in place. Returns the new length."""
    if len(items) == 0:
        return 0
    write = 1  # next slot to fill with a new unique value
    for read in range(1, len(items)):
        if items[read] != items[write - 1]:
            items[write] = items[read]
            write += 1
    # cut away the leftover tail so printing shows only the unique values
    while len(items) > write:
        items.pop()
    return write


def merge_sorted(left, right):
    """Return a new sorted list containing all values of both sorted lists."""
    merged = []
    i = 0
    j = 0
    while i < len(left) and j < len(right):
        if left[i] <= right[j]:
            merged.append(left[i])
            i += 1
        else:
            merged.append(right[j])
            j += 1
    while i < len(left):  # one of these two loops does nothing
        merged.append(left[i])
        i += 1
    while j < len(right):
        merged.append(right[j])
        j += 1
    return merged


def find_duplicates(items):
    """Return the values that appear more than once, in order of detection."""
    seen = set()
    reported = set()
    duplicates = []
    for value in items:
        if value in seen and value not in reported:
            duplicates.append(value)
            reported.add(value)
        seen.add(value)
    return duplicates


def main():
    sorted_numbers = [1, 1, 2, 2, 2, 3, 5, 5]
    print("before:", sorted_numbers)
    new_length = remove_duplicates_sorted(sorted_numbers)
    print("after remove_duplicates_sorted:", sorted_numbers, "length =", new_length)
    print("all equal:", remove_duplicates_sorted([4, 4, 4]))
    print("empty:", remove_duplicates_sorted([]))

    left = [1, 4, 7]
    right = [2, 3, 9, 10]
    print("merge", left, right, "->", merge_sorted(left, right))
    print("merge with empty:", merge_sorted([], [5, 6]), merge_sorted([1], []))
    print("merge with duplicates:", merge_sorted([1, 3, 3], [3, 4]))

    print("find_duplicates:", find_duplicates([3, 1, 3, 4, 1, 3, 9]))
    print("no duplicates:", find_duplicates([1, 2, 3]))


if __name__ == "__main__":
    main()
