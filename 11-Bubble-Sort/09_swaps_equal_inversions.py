"""
Problem title:
    Swaps Made by Bubble Sort Equal the Number of Inversions

Problem statement:
    An inversion is a pair of positions i < j with values[i] > values[j].
    Show that the number of swaps Bubble Sort performs equals the number of
    inversions, by computing both independently.

What it teaches:
    - Inversions measure "how unsorted" a list is.
    - Each adjacent swap removes exactly one inversion.
    - A brute-force O(n^2) inversion counter to cross-check the sort.

Input example:
    numbers = [3, 1, 2, 5, 4]

Expected output:
    [3, 1, 2, 5, 4] inversions=3 swaps=3 equal=True
    [1, 2, 3, 4]   inversions=0 swaps=0 equal=True
    [4, 3, 2, 1]   inversions=6 swaps=6 equal=True
    [2, 2, 1, 1]   inversions=4 swaps=4 equal=True
    []             inversions=0 swaps=0 equal=True

Approach:
    Count inversions with two nested loops over all pairs. Count swaps by
    running Bubble Sort. Compare the two numbers.

Step-by-step logic:
    1. count_inversions: for every i, for every j > i, count values[i] >
       values[j].
    2. bubble_sort_swaps: normal bubble sort returning the swap count.
    3. Print both counts and whether they match.

Why it works:
    Swapping an adjacent out-of-order pair fixes exactly that one inversion
    and does not change the order of any other pair. A sorted list has zero
    inversions, so swaps needed = inversions.

Time complexity:
    O(n^2) for both functions.

Space complexity:
    O(1) extra (besides the copy used by the sort).

Edge cases:
    - Sorted list: 0 inversions, 0 swaps.
    - Reversed list: n(n-1)/2 inversions.
    - Equal values are not inversions (strict comparison).

Alternative approach:
    Merge Sort counts inversions in O(n log n) - see the Merge Sort topic.
"""


def count_inversions(values):
    """Brute-force count of pairs i < j with values[i] > values[j]."""
    inversions = 0
    for i in range(len(values)):
        for j in range(i + 1, len(values)):
            if values[i] > values[j]:
                inversions += 1
    return inversions


def bubble_sort_swaps(values):
    """Run bubble sort on a copy and return the number of swaps."""
    items = list(values)
    size = len(items)
    swaps = 0
    for pass_number in range(size - 1):
        swapped = False
        for index in range(size - 1 - pass_number):
            if items[index] > items[index + 1]:
                items[index], items[index + 1] = items[index + 1], items[index]
                swaps += 1
                swapped = True
        if not swapped:
            break
    return swaps


def main():
    samples = [
        [3, 1, 2, 5, 4],
        [1, 2, 3, 4],
        [4, 3, 2, 1],
        [2, 2, 1, 1],
        [],
    ]
    for numbers in samples:
        inversions = count_inversions(numbers)
        swaps = bubble_sort_swaps(numbers)
        print("%-14s inversions=%d swaps=%d equal=%s"
              % (numbers, inversions, swaps, inversions == swaps))


if __name__ == "__main__":
    main()
