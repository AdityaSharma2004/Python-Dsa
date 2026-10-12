"""
Problem title:
    Selection Sort Is Not Stable (and a Stable Fix)

Problem statement:
    Sort (name, marks) records by marks. Show that the usual swap-based
    Selection Sort can reorder students who have equal marks, then write a
    stable version that keeps their original order.

What it teaches:
    - What "stable" means: equal keys keep their original relative order.
    - Why a long-distance swap breaks stability.
    - Shifting elements instead of swapping makes Selection Sort stable.

Input example:
    records = [("Asha", 70), ("Ravi", 70), ("Meena", 40), ("Karan", 90)]

Expected output:
    Original: ['Asha', 'Ravi', 'Meena', 'Karan']
    Standard: ['Meena', 'Ravi', 'Asha', 'Karan'] stable? False
    Shifting: ['Meena', 'Asha', 'Ravi', 'Karan'] stable? True
    Empty: []
    All equal: ['A', 'B', 'C']

Approach:
    1. Standard version: find the minimum marks and swap it into place.
    2. Stable version: find the minimum, remove it by shifting the items
       between the two positions one step right, then put it in front.

Step-by-step logic:
    1. In the standard version, swapping Asha(70) with Meena(40) throws Asha
       behind Ravi(70) - their order has flipped.
    2. In the stable version, Meena is lifted out, Asha and Ravi slide one slot
       to the right (keeping their order) and Meena is placed at the front.
    3. Strict "<" while scanning keeps the earliest of equal minima.

Why it works:
    Shifting moves every skipped element by exactly one place, so no element
    jumps over an equal one.

Time complexity:
    O(n^2) comparisons; the stable version also does O(n^2) element moves in
    the worst case.

Space complexity:
    O(1) extra besides the copy.

Edge cases:
    - Empty list and single record.
    - All marks equal: a stable sort must leave the order unchanged.
    - Already sorted records.

Alternative approach:
    Sort (marks, original_index) pairs, or use Insertion Sort / Merge Sort,
    which are naturally stable.
"""


def unstable_selection_sort(records):
    """Classic swap-based Selection Sort on the marks (index 1)."""
    items = list(records)
    for position in range(len(items) - 1):
        min_index = position
        for index in range(position + 1, len(items)):
            if items[index][1] < items[min_index][1]:
                min_index = index
        items[position], items[min_index] = items[min_index], items[position]
    return items


def stable_selection_sort(records):
    """Selection Sort that shifts instead of swapping, so it is stable."""
    items = list(records)
    for position in range(len(items) - 1):
        min_index = position
        for index in range(position + 1, len(items)):
            if items[index][1] < items[min_index][1]:
                min_index = index
        chosen = items[min_index]
        # Slide everything between position and min_index one step right.
        for index in range(min_index, position, -1):
            items[index] = items[index - 1]
        items[position] = chosen
    return items


def names_of(records):
    """Return only the names, in order."""
    return [name for name, _ in records]


def is_stable(original, result):
    """True if records with equal marks keep their original relative order."""
    for first in range(len(result)):
        for second in range(first + 1, len(result)):
            if result[first][1] == result[second][1]:
                if original.index(result[first]) > original.index(result[second]):
                    return False
    return True


def main():
    records = [("Asha", 70), ("Ravi", 70), ("Meena", 40), ("Karan", 90)]
    unstable = unstable_selection_sort(records)
    stable = stable_selection_sort(records)
    print("Original:", names_of(records))
    print("Standard:", names_of(unstable), "stable?", is_stable(records, unstable))
    print("Shifting:", names_of(stable), "stable?", is_stable(records, stable))

    # Edge cases
    print("Empty:", stable_selection_sort([]))
    same = [("A", 1), ("B", 1), ("C", 1)]
    print("All equal:", names_of(stable_selection_sort(same)))


if __name__ == "__main__":
    main()
