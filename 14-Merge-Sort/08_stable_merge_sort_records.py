"""
Problem title:
    Stable Merge Sort on Records

Problem statement:
    Sort a list of (name, marks) records by marks, ascending, so that records with
    equal marks stay in their original order. Then sort by name using the same
    function to show that a key function makes the sort reusable.

What it teaches:
    - What "stable" means and why it matters for multi-level sorting.
    - Passing a key function to a sort routine.
    - That merge sort is stable when ties are taken from the left half.

Input example:
    [("Asha", 80), ("Bob", 70), ("Chen", 80), ("Dina", 70), ("Eli", 60)]

Expected output:
    Original : [('Asha', 80), ('Bob', 70), ('Chen', 80), ('Dina', 70), ('Eli', 60)]
    By marks : [('Eli', 60), ('Bob', 70), ('Dina', 70), ('Asha', 80), ('Chen', 80)]
    By name  : [('Asha', 80), ('Bob', 70), ('Chen', 80), ('Dina', 70), ('Eli', 60)]
    All equal: [('x', 1), ('y', 1), ('z', 1)]
    Empty    : []

Approach used:
    Recursive merge sort where the merge compares key(left) <= key(right). The
    "<=" means that on ties the left (earlier) record is taken first.

Step-by-step logic:
    1. Split the records, sort each half recursively.
    2. In the merge, compute the keys of the two front records.
    3. If key(left) <= key(right) take the left record, otherwise take the right.
    4. Copy leftovers. Equal keys therefore never swap order.

Why it works:
    Records with equal keys are always in the same half in the same order, or the
    left half contains the earlier ones. Taking from the left on ties keeps that
    order through every merge, so stability holds for the whole sort.

Time complexity:
    O(n log n) comparisons of keys.

Space complexity:
    O(n) extra for merged lists (plus O(log n) recursion stack).

Edge cases:
    Empty list, all keys equal (output must equal input), single record,
    keys that are strings.

Alternative approach:
    Sort by marks, then by name with two stable passes (secondary key first) to get
    a multi-key ordering. Quick sort is not stable by default.
"""


def merge(left, right, key):
    """Stable merge of two lists already sorted by key."""
    result = []
    i = 0
    j = 0
    while i < len(left) and j < len(right):
        if key(left[i]) <= key(right[j]):  # ties go to the left record
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


def merge_sort(records, key):
    """Return a new list sorted by key(record), stable."""
    if len(records) <= 1:
        return list(records)
    mid = len(records) // 2
    left = merge_sort(records[:mid], key)
    right = merge_sort(records[mid:], key)
    return merge(left, right, key)


def marks_of(record):
    """Key function: the marks (second field)."""
    return record[1]


def name_of(record):
    """Key function: the name (first field)."""
    return record[0]


def main():
    students = [("Asha", 80), ("Bob", 70), ("Chen", 80), ("Dina", 70), ("Eli", 60)]
    print("Original :", students)
    print("By marks :", merge_sort(students, marks_of))
    print("By name  :", merge_sort(students, name_of))
    same = [("x", 1), ("y", 1), ("z", 1)]
    print("All equal:", merge_sort(same, marks_of))
    print("Empty    :", merge_sort([], marks_of))


if __name__ == "__main__":
    main()
