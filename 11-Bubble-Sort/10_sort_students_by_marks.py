"""
Problem title:
    Sort Students by Marks with a Custom Key (Generic Bubble Sort)

Problem statement:
    Given student dictionaries with "name" and "marks", sort them by marks
    from highest to lowest, using a generic Bubble Sort that accepts a key
    function and a reverse flag. Ties must stay in their original order.

What it teaches:
    - Making an algorithm reusable with a key function (like sortBy in
      Laravel collections or usort callbacks in PHP).
    - Sorting dictionaries/records, not only numbers.
    - Combining descending order with stability.

Input example:
    students = [{"name": "Riya", "marks": 82}, {"name": "Aman", "marks": 91},
                {"name": "Zoya", "marks": 82}, {"name": "Karan", "marks": 67}]

Expected output:
    1. Aman   91
    2. Riya   82
    3. Zoya   82
    4. Karan  67
    By name: ['Aman', 'Karan', 'Riya', 'Zoya']
    Empty: []

Approach:
    Bubble sort where the comparison is done on key(item) instead of item.
    Swap only when the pair is strictly out of order, which keeps it stable.

Step-by-step logic:
    1. key = a function such as lambda student: student["marks"].
    2. For each neighbour pair compute both keys.
    3. Ascending: swap if key_left > key_right.
       Descending: swap if key_left < key_right.
    4. Print a ranked list.

Why it works:
    The algorithm only needs a way to say which of two items comes first;
    the key function supplies that for any record type.

Time complexity:
    O(n^2) comparisons; each key call is assumed O(1).

Space complexity:
    O(1) extra besides the copy.

Edge cases:
    - Empty list of students.
    - Ties (Riya and Zoya both 82) keep original order.
    - Sorting by name (strings) works with the same function.

Alternative approach:
    sorted(students, key=...) - shortest in real code, but it hides the
    algorithm that this exercise is about.
"""


def bubble_sort_by_key(items, key, reverse=False):
    """Return a new list sorted by key(item). Stable. reverse=True: high first."""
    result = list(items)
    size = len(result)
    for pass_number in range(size - 1):
        swapped = False
        for index in range(size - 1 - pass_number):
            left_key = key(result[index])
            right_key = key(result[index + 1])
            if reverse:
                out_of_order = left_key < right_key
            else:
                out_of_order = left_key > right_key
            if out_of_order:  # strict test keeps equal keys in place
                result[index], result[index + 1] = result[index + 1], result[index]
                swapped = True
        if not swapped:
            break
    return result


def main():
    students = [
        {"name": "Riya", "marks": 82},
        {"name": "Aman", "marks": 91},
        {"name": "Zoya", "marks": 82},
        {"name": "Karan", "marks": 67},
    ]
    ranked = bubble_sort_by_key(students, key=lambda s: s["marks"], reverse=True)
    for rank, student in enumerate(ranked, start=1):
        print("%d. %-6s %d" % (rank, student["name"], student["marks"]))

    by_name = bubble_sort_by_key(students, key=lambda s: s["name"])
    print("By name:", [s["name"] for s in by_name])

    # Edge cases
    print("Empty:", bubble_sort_by_key([], key=lambda s: s["marks"]))


if __name__ == "__main__":
    main()
