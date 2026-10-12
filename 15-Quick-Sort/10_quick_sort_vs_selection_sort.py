"""
Problem title:
    Quick Sort vs Selection Sort: Growth of Comparisons

Problem statement:
    Count the comparisons made by Selection Sort (always n(n-1)/2) and by quick
    sort with a median-of-three pivot for growing input sizes, and show how the
    gap widens as n doubles. Use a hand-written deterministic data generator.

What it teaches:
    - O(n^2) versus O(n log n) in concrete numbers, not just formulas.
    - What "doubling n" does to each algorithm (about x4 versus a bit over x2).
    - How to benchmark by counting operations instead of measuring seconds.

Input example:
    n = 50, 100, 200, 400 pseudo-random integers

Expected output:
        n  selection   quick   ratio  sorted?
       50       1225     212     5.8  True
      100       4950     550     9.0  True
          growth vs previous n: selection x4.04, quick x2.59
      200      19900    1329    15.0  True
          growth vs previous n: selection x4.02, quick x2.42
      400      79800    3004    26.6  True
          growth vs previous n: selection x4.01, quick x2.26
    Empty: 0
    Single element comparisons: 0

Approach used:
    Both sorts carry a comparison counter. The data comes from a tiny linear
    congruential generator so each run prints the same table. The quick sort
    uses a median-of-three pivot and Lomuto partitioning.

Step-by-step logic:
    1. Generate n values for each size.
    2. Run Selection Sort and quick sort on separate copies, counting every
       element comparison.
    3. Print both counts and their ratio, and the growth versus the previous n.
    4. Verify both results are sorted.

Why it works:
    Selection Sort compares every pair exactly once: n(n-1)/2. Quick sort with
    balanced splits has about log2(n) levels of roughly n comparisons each, so
    the gap grows with n.

Time complexity:
    Selection Sort O(n^2); quick sort O(n log n) average.

Space complexity:
    O(1) extra for Selection Sort; O(log n) average recursion stack for quick
    sort. Sizes are small enough to stay inside Python's recursion limit.

Edge cases:
    Empty list (zero comparisons), single element, all equal values (quick
    sort with Lomuto degrades towards O(n^2) here, see file 07).

Alternative approach:
    Compare against Merge Sort (always O(n log n)) or time the sorts with
    time.perf_counter(); counting comparisons is more repeatable.
"""


def make_data(n, seed):
    """Deterministic pseudo-random list of n integers."""
    values = []
    state = seed
    for _ in range(n):
        state = (state * 1103515245 + 12345) % 2147483648
        values.append(state % 100000)
    return values


def selection_sort_comparisons(values):
    """Selection Sort a copy; return (sorted_list, comparisons)."""
    items = list(values)
    comparisons = 0
    for position in range(len(items) - 1):
        min_index = position
        for index in range(position + 1, len(items)):
            comparisons += 1
            if items[index] < items[min_index]:
                min_index = index
        items[position], items[min_index] = items[min_index], items[position]
    return items, comparisons


def median_of_three_index(arr, low, high):
    """Index of the median of arr[low], arr[mid], arr[high]."""
    mid = (low + high) // 2
    a, b, c = arr[low], arr[mid], arr[high]
    if (a <= b <= c) or (c <= b <= a):
        return mid
    if (b <= a <= c) or (c <= a <= b):
        return low
    return high


def quick_sort_counted(arr, low, high, counter):
    """In-place quick sort; counter[0] counts comparisons."""
    if low >= high:
        return
    pivot_index = median_of_three_index(arr, low, high)
    arr[pivot_index], arr[high] = arr[high], arr[pivot_index]
    pivot = arr[high]
    boundary = low - 1
    for j in range(low, high):
        counter[0] += 1
        if arr[j] <= pivot:
            boundary += 1
            arr[boundary], arr[j] = arr[j], arr[boundary]
    arr[boundary + 1], arr[high] = arr[high], arr[boundary + 1]
    quick_sort_counted(arr, low, boundary, counter)
    quick_sort_counted(arr, boundary + 2, high, counter)


def is_sorted_list(values):
    """True if values are in non-decreasing order."""
    for i in range(1, len(values)):
        if values[i - 1] > values[i]:
            return False
    return True


def main():
    print(f"{'n':>5}{'selection':>11}{'quick':>8}{'ratio':>8}  sorted?")
    previous = None
    for n in (50, 100, 200, 400):
        data = make_data(n, seed=7)
        selection_result, selection_count = selection_sort_comparisons(data)
        quick_data = list(data)
        counter = [0]
        quick_sort_counted(quick_data, 0, n - 1, counter)
        ratio = selection_count / counter[0]
        ok = is_sorted_list(selection_result) and is_sorted_list(quick_data)
        print(f"{n:>5}{selection_count:>11}{counter[0]:>8}{ratio:>8.1f}  {ok}")
        if previous is not None:
            print(f"      growth vs previous n: selection x{selection_count / previous[0]:.2f}, "
                  f"quick x{counter[0] / previous[1]:.2f}")
        previous = (selection_count, counter[0])

    # Edge cases
    print("Empty:", selection_sort_comparisons([])[1])
    one = [3]
    count = [0]
    quick_sort_counted(one, 0, 0, count)
    print("Single element comparisons:", count[0])


if __name__ == "__main__":
    main()
