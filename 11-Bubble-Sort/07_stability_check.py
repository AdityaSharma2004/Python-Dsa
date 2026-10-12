"""
Problem title:
    Is Bubble Sort Stable? (Sorting Records by Key)

Problem statement:
    Sort (name, score) records by score using Bubble Sort and verify that
    records with equal scores keep their original relative order.

What it teaches:
    - Definition of a stable sort.
    - Bubble Sort is stable because it only swaps strictly out-of-order pairs.
    - Sorting records by a key instead of plain numbers.
    - Laravel analogy: ->sortBy('score') on a collection that was already
      ordered by name; stability keeps names in order within equal scores.

Input example:
    records = [("Asha", 80), ("Ben", 90), ("Chitra", 80), ("Dev", 90),
               ("Esha", 70)]

Expected output:
    Strict (>)  : [('Esha', 70), ('Asha', 80), ('Chitra', 80), ('Ben', 90), ('Dev', 90)]
    Stable?       True
    Loose (>=)  : [('Esha', 70), ('Asha', 80), ('Chitra', 80), ('Dev', 90), ('Ben', 90)]
    Stable?       False
    All equal    : [('A', 1), ('B', 1), ('C', 1)]
    Empty        : []

Approach:
    Bubble sort comparing only the score field with a strict > test. A helper
    then checks stability by comparing the input order of tied records.

Step-by-step logic:
    1. Compare records[i][1] with records[i + 1][1].
    2. Swap only if the left score is strictly larger.
    3. Equal scores are never swapped, so they never cross each other.
    4. is_stable() scans neighbouring equal scores and checks that the
       original positions are still increasing.

Why it works:
    Elements only move past each other when one is strictly larger; two
    equal-key elements therefore can never change their relative order.

Time complexity:
    O(n^2) for sorting; O(n) for the stability check.

Space complexity:
    O(n) because original positions are stored for the check
    (the sort itself is O(1) extra).

Edge cases:
    - All scores equal: the list must come back unchanged.
    - Empty list and single record.
    - Using >= instead of > would make the sort unstable.

Alternative approach:
    Python's built-in sort is also stable; here we hand-write the sort so we
    can prove the property ourselves.
"""


def bubble_sort_by_score(records, strict=True):
    """Sort (name, score) records by score ascending. Returns a new list."""
    items = list(records)
    size = len(items)
    for pass_number in range(size - 1):
        for index in range(size - 1 - pass_number):
            left_score = items[index][1]
            right_score = items[index + 1][1]
            should_swap = left_score > right_score if strict else left_score >= right_score
            if should_swap:
                items[index], items[index + 1] = items[index + 1], items[index]
    return items


def is_stable(original, result):
    """True if records with equal scores keep their original order."""
    position = {}
    for index, record in enumerate(original):
        position[record[0]] = index  # names are unique in this demo
    for index in range(len(result) - 1):
        same_score = result[index][1] == result[index + 1][1]
        if same_score and position[result[index][0]] > position[result[index + 1][0]]:
            return False
    return True


def main():
    records = [("Asha", 80), ("Ben", 90), ("Chitra", 80), ("Dev", 90), ("Esha", 70)]
    stable = bubble_sort_by_score(records)
    print("Strict (>)  :", stable)
    print("Stable?      ", is_stable(records, stable))
    unstable = bubble_sort_by_score(records, strict=False)
    print("Loose (>=)  :", unstable)
    print("Stable?      ", is_stable(records, unstable))

    # Edge cases
    same = [("A", 1), ("B", 1), ("C", 1)]
    print("All equal    :", bubble_sort_by_score(same))
    print("Empty        :", bubble_sort_by_score([]))


if __name__ == "__main__":
    main()
