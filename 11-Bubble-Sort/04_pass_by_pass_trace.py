"""
Problem title:
    Bubble Sort with a Pass-by-Pass Trace

Problem statement:
    Run Bubble Sort and record the state of the list after every pass, so you
    can see how the largest values settle at the end.

What it teaches:
    - Reading the algorithm as a series of snapshots.
    - How the sorted tail grows by one element per pass.
    - Using a "history" list to debug or explain an algorithm.

Input example:
    numbers = [5, 1, 4, 2, 8]

Expected output:
    Start   : [5, 1, 4, 2, 8]
    Pass 1  : [1, 4, 2, 5, 8]  (swaps: 3)
    Pass 2  : [1, 2, 4, 5, 8]  (swaps: 1)
    Pass 3  : [1, 2, 4, 5, 8]  (swaps: 0)
    Result  : [1, 2, 4, 5, 8]
    Sorted input passes: 1
    Empty input passes: 0

Approach:
    Use the optimized bubble sort and append a copy of the list to a history
    after each pass (copy, otherwise every entry would point to the same list).

Step-by-step logic:
    1. Save the starting list as snapshot 0.
    2. Run one pass of adjacent swaps.
    3. Save a copy of the list and the number of swaps in that pass.
    4. Stop when a pass makes no swaps.

Why it works:
    Each pass only changes positions inside the unsorted prefix, so the
    snapshots show the sorted suffix growing from the right.

Time complexity:
    O(n^2) for the sort; storing snapshots adds O(n) per pass.

Space complexity:
    O(n^2) in the worst case because of the stored snapshots
    (the sorting itself is O(1) extra).

Edge cases:
    - Sorted input produces just one (swap-free) pass.
    - Empty input produces only the initial snapshot.
    - Snapshots must be copies, not references.

Alternative approach:
    Print inside the loops instead of storing history - less reusable.
"""


def bubble_sort_with_trace(values):
    """Return (sorted_list, history) where history has one entry per pass."""
    items = list(values)
    history = []
    size = len(items)
    for pass_number in range(size - 1):
        swaps = 0
        for index in range(size - 1 - pass_number):
            if items[index] > items[index + 1]:
                items[index], items[index + 1] = items[index + 1], items[index]
                swaps += 1
        history.append((pass_number + 1, list(items), swaps))  # list() = copy
        if swaps == 0:
            break
    return items, history


def print_trace(original, history):
    """Print the starting list and each pass snapshot."""
    print("Start   :", original)
    for pass_number, snapshot, swaps in history:
        print("Pass %d  : %s  (swaps: %d)" % (pass_number, snapshot, swaps))


def main():
    numbers = [5, 1, 4, 2, 8]
    result, history = bubble_sort_with_trace(numbers)
    print_trace(numbers, history)
    print("Result  :", result)

    # Edge cases
    _, sorted_history = bubble_sort_with_trace([1, 2, 3])
    print("Sorted input passes:", len(sorted_history))
    _, empty_history = bubble_sort_with_trace([])
    print("Empty input passes:", len(empty_history))


if __name__ == "__main__":
    main()
