"""
Problem title:
    Compare Selection, Bubble and Insertion Sort

Problem statement:
    Implement Selection Sort, Bubble Sort (with early exit) and Insertion Sort
    with counters, then compare their comparisons and writes on sorted,
    reversed and shuffled lists of the same size.

What it teaches:
    - Selection Sort always makes n(n-1)/2 comparisons but very few writes.
    - Bubble Sort (early exit) and Insertion Sort are fast on sorted data.
    - Choosing an algorithm by what is expensive: comparisons or writes.

Input example:
    n = 8 with three inputs: sorted, reversed, and a fixed shuffled list.

Expected output:
    Sorted  : [1, 2, 3, 4, 5, 6, 7, 8]
      Selection  comparisons=28 writes= 0
      Bubble     comparisons= 7 writes= 0
      Insertion  comparisons= 7 writes= 0
    Reversed: [8, 7, 6, 5, 4, 3, 2, 1]
      Selection  comparisons=28 writes= 8
      Bubble     comparisons=28 writes=56
      Insertion  comparisons=28 writes=35
    Shuffled: [5, 2, 8, 1, 9, 3, 7, 4]
      Selection  comparisons=28 writes=10
      Bubble     comparisons=25 writes=26
      Insertion  comparisons=18 writes=18
    Empty: (0, 0) (0, 0) (0, 0)
    All three match sorted()? True

Approach:
    Each sort returns (sorted_list, comparisons, writes), where a write is one
    swap (counted as 2 writes) or one element shift/placement. A small table is
    printed per input.

Step-by-step logic:
    1. Selection Sort: one comparison per scanned item, 2 writes per swap.
    2. Bubble Sort: compare neighbours; stop when a pass makes no swap.
    3. Insertion Sort: shift larger items right (1 write each), then place the
       key (1 write).
    4. Run all three on every input and print the counts.

Why it works:
    Counting the same two quantities in all three algorithms gives a fair
    comparison that matches the theory.

Time complexity:
    Selection O(n^2) always; Bubble O(n) best, O(n^2) worst; Insertion O(n)
    best, O(n^2) worst.

Space complexity:
    O(1) extra for each sort (apart from the copy).

Edge cases:
    - Empty and single-element lists (zero comparisons).
    - Reversed input is the worst case for Bubble and Insertion.
    - Sorted input is the best case for Bubble and Insertion, not Selection.

Alternative approach:
    Merge Sort or Quick Sort reduce comparisons to O(n log n) (see their
    topic folders).
"""


def selection_counted(values):
    """Selection Sort; return (list, comparisons, writes)."""
    items = list(values)
    comparisons = 0
    writes = 0
    for position in range(len(items) - 1):
        min_index = position
        for index in range(position + 1, len(items)):
            comparisons += 1
            if items[index] < items[min_index]:
                min_index = index
        if min_index != position:
            items[position], items[min_index] = items[min_index], items[position]
            writes += 2
    return items, comparisons, writes


def bubble_counted(values):
    """Bubble Sort with early exit; return (list, comparisons, writes)."""
    items = list(values)
    comparisons = 0
    writes = 0
    for end in range(len(items) - 1, 0, -1):
        swapped = False
        for index in range(end):
            comparisons += 1
            if items[index] > items[index + 1]:
                items[index], items[index + 1] = items[index + 1], items[index]
                writes += 2
                swapped = True
        if not swapped:  # already sorted, stop early
            break
    return items, comparisons, writes


def insertion_counted(values):
    """Insertion Sort; return (list, comparisons, writes)."""
    items = list(values)
    comparisons = 0
    writes = 0
    for index in range(1, len(items)):
        key = items[index]
        hole = index
        while hole > 0:
            comparisons += 1
            if items[hole - 1] > key:
                items[hole] = items[hole - 1]  # shift right
                writes += 1
                hole -= 1
            else:
                break
        if hole != index:
            items[hole] = key
            writes += 1
    return items, comparisons, writes


def report(title, data):
    """Print one comparison table for the given input."""
    print("%s: %s" % (title, data))
    for name, sort_function in (("Selection", selection_counted),
                                ("Bubble", bubble_counted),
                                ("Insertion", insertion_counted)):
        result, comparisons, writes = sort_function(data)
        print("  %-10s comparisons=%2d writes=%2d" % (name, comparisons, writes))


def main():
    report("Sorted  ", [1, 2, 3, 4, 5, 6, 7, 8])
    report("Reversed", [8, 7, 6, 5, 4, 3, 2, 1])
    report("Shuffled", [5, 2, 8, 1, 9, 3, 7, 4])

    # Edge cases
    print("Empty:", selection_counted([])[1:], bubble_counted([])[1:], insertion_counted([])[1:])

    # Verification against the built-in (used only to check, not to sort).
    sample = [5, 2, 8, 1, 9, 3, 7, 4]
    all_match = (selection_counted(sample)[0] == sorted(sample)
                 and bubble_counted(sample)[0] == sorted(sample)
                 and insertion_counted(sample)[0] == sorted(sample))
    print("All three match sorted()?", all_match)


if __name__ == "__main__":
    main()
