"""
Problem title:
    Pivot Selection Strategies

Problem statement:
    Implement quick sort with three pivot rules (first element, last element,
    median of three) and compare how many comparisons each makes on random, sorted
    and reverse-sorted data of the same size.

What it teaches:
    - Why pivot choice decides whether quick sort is O(n log n) or O(n^2).
    - The median-of-three trick (first, middle, last).
    - Counting comparisons to compare strategies fairly.

Input example:
    n = 200 elements: pseudo-random, ascending, descending

Expected output:
    Comparisons for n = 200
    input         first    last  median3  all sorted?
    random         1661    1518     1380  True
    ascending     19900   19900     1153  True
    descending    19900   19900     1786  True

Approach used:
    A Lomuto-based quick sort that first swaps the chosen pivot into the last
    position, then partitions as usual. The comparison counter is a one-item list.

Step-by-step logic:
    1. choose_pivot_index(arr, low, high, strategy) returns an index.
    2. Swap that element with arr[high] so Lomuto can use it.
    3. Partition and recurse, counting every arr[j] <= pivot comparison.
    4. Print one row per input type with the counts for all three strategies.

Why it works:
    A last-element pivot on sorted data is always the maximum, so every partition
    peels off one element: n + (n-1) + ... = about n^2 / 2 comparisons. Median of
    three picks a middle value on such data, producing balanced splits.

Time complexity:
    O(n log n) average; O(n^2) worst case. First/last pivots are quadratic on
    sorted input; median of three is not (though adversarial inputs still exist).

Space complexity:
    O(1) extra data plus recursion stack: O(log n) balanced, O(n) lopsided.
    Input size is kept small so the lopsided case stays within Python's default
    recursion limit.

Edge cases:
    Ranges with 1 or 2 elements, all equal elements, pivot already at the end.

Alternative approach:
    A random pivot (file 06) gives O(n log n) expected time on every input.
"""


def pseudo_random_list(n, seed=2024):
    """Deterministic pseudo-random data from a tiny linear congruential generator."""
    values = []
    state = seed
    for _ in range(n):
        state = (state * 1103515245 + 12345) % 2147483648
        values.append(state % 10000)
    return values


def median_of_three_index(arr, low, high):
    """Return the index (low, mid or high) holding the median value of the three."""
    mid = (low + high) // 2
    a, b, c = arr[low], arr[mid], arr[high]
    if (a <= b <= c) or (c <= b <= a):
        return mid
    if (b <= a <= c) or (c <= a <= b):
        return low
    return high


def choose_pivot_index(arr, low, high, strategy):
    """Pick a pivot index by strategy name: 'first', 'last' or 'median3'."""
    if strategy == "first":
        return low
    if strategy == "last":
        return high
    return median_of_three_index(arr, low, high)


def partition(arr, low, high, strategy, counter):
    """Lomuto partition after moving the chosen pivot to arr[high]."""
    pivot_index = choose_pivot_index(arr, low, high, strategy)
    arr[pivot_index], arr[high] = arr[high], arr[pivot_index]
    pivot = arr[high]
    boundary = low - 1
    for j in range(low, high):
        counter[0] += 1
        if arr[j] <= pivot:
            boundary += 1
            arr[boundary], arr[j] = arr[j], arr[boundary]
    arr[boundary + 1], arr[high] = arr[high], arr[boundary + 1]
    return boundary + 1


def quick_sort(arr, low, high, strategy, counter):
    """Sort arr[low..high] in place with the given pivot strategy."""
    if low >= high:
        return
    p = partition(arr, low, high, strategy, counter)
    quick_sort(arr, low, p - 1, strategy, counter)
    quick_sort(arr, p + 1, high, strategy, counter)


def count_comparisons(data, strategy):
    """Sort a copy of data; return (comparisons, sorted_correctly)."""
    work = list(data)
    counter = [0]
    quick_sort(work, 0, len(work) - 1, strategy, counter)
    in_order = True
    for i in range(1, len(work)):
        if work[i - 1] > work[i]:
            in_order = False
    return counter[0], in_order


def main():
    n = 200
    inputs = [
        ("random", pseudo_random_list(n)),
        ("ascending", list(range(n))),
        ("descending", list(range(n, 0, -1))),
    ]
    print(f"Comparisons for n = {n}")
    print(f"{'input':<11}{'first':>8}{'last':>8}{'median3':>9}  all sorted?")
    for name, data in inputs:
        row = []
        all_ok = True
        for strategy in ("first", "last", "median3"):
            comparisons, ok = count_comparisons(data, strategy)
            row.append(comparisons)
            all_ok = all_ok and ok
        print(f"{name:<11}{row[0]:>8}{row[1]:>8}{row[2]:>9}  {all_ok}")


if __name__ == "__main__":
    main()
