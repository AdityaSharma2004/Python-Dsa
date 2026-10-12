"""
Problem title:
    Stable Insertion Sort on Records

Problem statement:
    Sort a list of (name, marks) records by marks in ascending order using
    insertion sort. Students with equal marks must keep their original relative
    order (a stable sort). Also show what an unstable variant would do.

What it teaches:
    - The meaning of stability and why it matters for multi-level sorting.
    - That using ">" (not ">=") in the shift condition keeps insertion sort stable.

Input example:
    [("Asha", 80), ("Bob", 70), ("Chen", 80), ("Dina", 70), ("Eli", 60)]

Expected output:
    Original : [('Asha', 80), ('Bob', 70), ('Chen', 80), ('Dina', 70), ('Eli', 60)]
    Stable   : [('Eli', 60), ('Bob', 70), ('Dina', 70), ('Asha', 80), ('Chen', 80)]
    Unstable : [('Eli', 60), ('Dina', 70), ('Bob', 70), ('Chen', 80), ('Asha', 80)]

Approach used:
    Insertion sort comparing only the marks. Shift while left.marks > key.marks,
    strictly greater, so equal keys stop the shifting and stay behind earlier ones.

Step-by-step logic:
    1. Take record = arr[i] as the key.
    2. Shift records whose marks are strictly greater than key's marks.
    3. Insert the key; it lands after any earlier record with equal marks.
    4. For comparison, an unstable version uses ">=" which jumps over equals.

Why it works:
    An equal element is never moved past another equal element, so the original
    left-to-right order of equals is preserved.

Time complexity:
    O(n^2) worst/average, O(n) best.

Space complexity:
    O(1).

Edge cases:
    All marks equal (output equals input), empty list, single record.

Alternative approach:
    Decorate each record with its original index and compare (marks, index);
    this makes any sort effectively stable.
"""


def insertion_sort_by_marks(records, stable=True):
    """Sort (name, marks) tuples in place by marks."""
    for i in range(1, len(records)):
        key = records[i]
        j = i - 1
        while j >= 0:
            left_marks = records[j][1]
            key_marks = key[1]
            # stable: strictly greater; unstable demo: greater or equal
            move = left_marks > key_marks if stable else left_marks >= key_marks
            if not move:
                break
            records[j + 1] = records[j]
            j -= 1
        records[j + 1] = key
    return records


def main():
    students = [("Asha", 80), ("Bob", 70), ("Chen", 80), ("Dina", 70), ("Eli", 60)]
    print("Original :", students)
    print("Stable   :", insertion_sort_by_marks(list(students), stable=True))
    print("Unstable :", insertion_sort_by_marks(list(students), stable=False))


if __name__ == "__main__":
    main()
