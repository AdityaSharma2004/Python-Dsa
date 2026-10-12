"""
Problem title:
    Sort and Group Duplicate Values

Problem statement:
    Sort a list that contains many repeated values with Selection Sort, then
    walk through the sorted list once and report each distinct value together
    with how many times it occurs.

What it teaches:
    - Selection Sort handles duplicates without any special code.
    - After sorting, equal values sit next to each other, so counting them
      needs only one extra pass.
    - Laravel analogy: like orderBy('status') followed by a groupBy count.

Input example:
    numbers = [4, 2, 4, 1, 2, 4, 3, 1]

Expected output:
    Original: [4, 2, 4, 1, 2, 4, 3, 1]
    Sorted:   [1, 1, 2, 2, 3, 4, 4, 4]
    Value 1 appears 2 time(s)
    Value 2 appears 2 time(s)
    Value 3 appears 1 time(s)
    Value 4 appears 3 time(s)
    Empty: []
    All equal: [(7, 3)]
    All distinct: [(1, 1), (2, 1), (3, 1)]

Approach:
    1. Selection Sort the list (strict "<" keeps the first minimum).
    2. Scan the sorted list; while the value equals the previous one, grow the
       current count, otherwise start a new group.

Step-by-step logic:
    1. Sort: [4, 2, 4, 1, 2, 4, 3, 1] becomes [1, 1, 2, 2, 3, 4, 4, 4].
    2. Start with the first value and count = 1.
    3. For every next value: same as current -> count += 1; different -> save
       (value, count) and begin a new group.
    4. Save the final group after the loop ends.

Why it works:
    Sorting guarantees that equal values are contiguous, so a group can never
    be split into two separate runs.

Time complexity:
    O(n^2) for the sort plus O(n) for grouping, so O(n^2) overall.

Space complexity:
    O(n) for the sorted copy and the list of groups.

Edge cases:
    - Empty list gives no groups.
    - All values equal gives a single group.
    - All values distinct gives n groups of size 1.

Alternative approach:
    A dictionary counter does the grouping in O(n) without sorting; sorting is
    used here to practise Selection Sort on repeated values.
"""


def selection_sort(values):
    """Return a sorted copy (ascending) using Selection Sort."""
    items = list(values)
    for position in range(len(items) - 1):
        min_index = position
        for index in range(position + 1, len(items)):
            if items[index] < items[min_index]:
                min_index = index
        items[position], items[min_index] = items[min_index], items[position]
    return items


def group_sorted(sorted_items):
    """Return a list of (value, count) pairs from a sorted list."""
    groups = []
    if len(sorted_items) == 0:
        return groups
    current = sorted_items[0]
    count = 1
    for index in range(1, len(sorted_items)):
        if sorted_items[index] == current:
            count += 1
        else:
            groups.append((current, count))  # close the finished group
            current = sorted_items[index]
            count = 1
    groups.append((current, count))  # the last group is still open
    return groups


def main():
    numbers = [4, 2, 4, 1, 2, 4, 3, 1]
    ordered = selection_sort(numbers)
    print("Original:", numbers)
    print("Sorted:  ", ordered)
    for value, count in group_sorted(ordered):
        print("Value %d appears %d time(s)" % (value, count))

    # Edge cases
    print("Empty:", group_sorted(selection_sort([])))
    print("All equal:", group_sorted(selection_sort([7, 7, 7])))
    print("All distinct:", group_sorted(selection_sort([3, 1, 2])))


if __name__ == "__main__":
    main()
