r"""
Problem title: Comparing Complexities - Growth Table and Duplicate Detection

Problem statement:
    (a) Print how many steps log n, n, n log n, n^2 and 2^n need for several
    input sizes. (b) Solve "does the list contain a duplicate?" in three ways -
    pairwise comparison, sort-then-scan, and a set - and compare step counts.

What it teaches:
    Why the choice of algorithm matters more than the speed of the computer, and
    how a different data structure (set) can drop O(n^2) to O(n).

Input example:
    sizes = 1, 8, 16, 32 for the table; list sizes 100, 200, 400 with no
    duplicates (worst case) for the comparison.

Expected output:
       n  log n    n  n log n    n^2          2^n
       1      0    1        0      1            2
       8      3    8       24     64          256
      16      4   16       64    256        65536
      32      5   32      160   1024   4294967296

        n  pairwise  sort+scan   set
      100      4950        615   100
      200     19900       1421   200
      400     79800       3213   400
    with duplicate: (True, 2) (True, 3)
    empty: (False, 0) (False, 0) (False, 0)

Approach:
    The table uses math formulas. The duplicate finders count operations.

Step-by-step logic:
    1. Pairwise: compare every pair -> n(n-1)/2 comparisons.
    2. Sort-scan: insertion-free merge sort (hand written) then compare
       neighbours -> about n log n + n steps.
    3. Set: for each value check membership then add -> n steps (average case
       for hashing).

Why it works:
    After sorting, equal values sit next to each other so one pass is enough.
    A set remembers what was seen in O(1) average time per lookup.

Time complexity:
    Pairwise O(n^2); sort-scan O(n log n); set O(n) average.

Space complexity:
    Pairwise O(1); sort-scan O(n) (merge sort buffers); set O(n).

Edge cases:
    - Empty list and one element: no duplicate.
    - Worst case is a list with no duplicates (all work must be done).
    - 2^n is only printed for n <= 32 to keep numbers readable.

Alternative approach:
    Compare len(numbers) with len(set(numbers)) - short but still O(n) space.
"""

import math


def print_growth_table():
    print(f"{'n':>4} {'log n':>6} {'n':>4} {'n log n':>8} {'n^2':>6} {'2^n':>12}")
    for n in [1, 8, 16, 32]:
        print(f"{n:>4} {int(math.log2(n)):>6} {n:>4} {int(n * math.log2(n)):>8} "
              f"{n * n:>6} {2 ** n:>12}")


def duplicate_pairwise(numbers):
    steps = 0
    for i in range(len(numbers)):
        for j in range(i + 1, len(numbers)):
            steps += 1
            if numbers[i] == numbers[j]:
                return True, steps
    return False, steps


def merge_sort(numbers, counter):
    if len(numbers) <= 1:
        return numbers
    mid = len(numbers) // 2
    left = merge_sort(numbers[:mid], counter)
    right = merge_sort(numbers[mid:], counter)
    merged = []
    i = j = 0
    while i < len(left) and j < len(right):
        counter[0] += 1
        if left[i] <= right[j]:
            merged.append(left[i])
            i += 1
        else:
            merged.append(right[j])
            j += 1
    merged.extend(left[i:])
    merged.extend(right[j:])
    return merged


def duplicate_sort_scan(numbers):
    counter = [0]
    ordered = merge_sort(numbers, counter)
    for index in range(1, len(ordered)):
        counter[0] += 1
        if ordered[index] == ordered[index - 1]:
            return True, counter[0]
    return False, counter[0]


def duplicate_set(numbers):
    seen = set()
    steps = 0
    for value in numbers:
        steps += 1
        if value in seen:
            return True, steps
        seen.add(value)
    return False, steps


def main():
    print_growth_table()
    print()
    print(f"{'n':>5} {'pairwise':>9} {'sort+scan':>10} {'set':>5}")
    for n in [100, 200, 400]:
        data = [(i * 7919) % 100003 for i in range(n)]  # distinct values
        print(f"{n:>5} {duplicate_pairwise(data)[1]:>9} "
              f"{duplicate_sort_scan(data)[1]:>10} {duplicate_set(data)[1]:>5}")
    print("with duplicate:", duplicate_pairwise([5, 1, 5]), duplicate_set([5, 1, 5]))
    print("empty:", duplicate_pairwise([]), duplicate_sort_scan([]), duplicate_set([]))


if __name__ == "__main__":
    main()
