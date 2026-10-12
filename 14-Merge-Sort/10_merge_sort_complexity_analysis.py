"""
Problem title:
    Merge Sort Complexity Analysis (counting comparisons)

Problem statement:
    Count the element comparisons made by merge sort on inputs of growing size and
    on different input orders (sorted, reversed, shuffled). Compare the counts with
    the n * log2(n) estimate and with the n^2 growth of a quadratic sort.

What it teaches:
    - Measuring an algorithm by counting operations instead of using the clock.
    - That merge sort is O(n log n) for every input order.
    - How fast n^2 grows compared with n log n.

Input example:
    sizes 8, 16, 32, 64, 128, 256 with sorted, reversed and shuffled data

Expected output:
        n   sorted  reversed  shuffled  n*log2(n)     n*n
        8       12        12        17         24      64
       16       32        32        46         64     256
       32       80        80       122        160    1024
       64      192       192       299        384    4096
      128      448       448       730        896   16384
      256     1024      1024      1715       2048   65536
    Every column stays at or below n*log2(n); n*n grows much faster.

Approach used:
    A merge sort that keeps a comparison counter (a one-item list used as a mutable
    counter). Inputs are built by hand; "shuffled" data comes from a tiny seeded
    linear congruential generator so the output is the same on every run.

Step-by-step logic:
    1. Build the three kinds of input for each size n.
    2. Run merge sort and read the counter after each run.
    3. Compute ceil(log2 n) by repeated doubling and the estimate n * log2(n).
    4. Print the table next to n * n for contrast.

Why it works:
    Merging two lists of total length m needs at most m - 1 comparisons. There are
    log2(n) levels with total length n each, so comparisons are at most about
    n log2 n - n + 1 in every case; the actual count depends on the data but never
    exceeds this bound.

Time complexity:
    O(n log n) for each sort run; the whole demo adds a constant number of runs.

Space complexity:
    O(n) for merged lists (plus O(log n) recursion stack).

Edge cases:
    n = 1 (zero comparisons), sizes that are exact powers of two (used here so
    the n * log2(n) estimate is exact), data with duplicates.

Alternative approach:
    Time the sort with time.perf_counter(); that depends on the machine, which is
    why this file counts comparisons instead.
"""


def merge(left, right, counter):
    """Merge sorted lists, adding the number of comparisons to counter[0]."""
    result = []
    i = 0
    j = 0
    while i < len(left) and j < len(right):
        counter[0] += 1
        if left[i] <= right[j]:
            result.append(left[i])
            i += 1
        else:
            result.append(right[j])
            j += 1
    while i < len(left):
        result.append(left[i])
        i += 1
    while j < len(right):
        result.append(right[j])
        j += 1
    return result


def merge_sort(items, counter):
    """Recursive merge sort that counts comparisons."""
    if len(items) <= 1:
        return list(items)
    mid = len(items) // 2
    left = merge_sort(items[:mid], counter)
    right = merge_sort(items[mid:], counter)
    return merge(left, right, counter)


def pseudo_random_list(n, seed=12345):
    """Deterministic 'shuffled' data from a linear congruential generator."""
    values = []
    state = seed
    for _ in range(n):
        state = (state * 1103515245 + 12345) % 2147483648
        values.append(state % 1000)
    return values


def count_comparisons(items):
    """Sort a copy of items and return the comparison count."""
    counter = [0]
    merge_sort(items, counter)
    return counter[0]


def log2_of_power_of_two(n):
    """Return k where n == 2**k (n must be a power of two)."""
    k = 0
    while n > 1:
        n //= 2
        k += 1
    return k


def main():
    print(f"{'n':>5} {'sorted':>8} {'reversed':>9} {'shuffled':>9} {'n*log2(n)':>10} {'n*n':>7}")
    for n in (8, 16, 32, 64, 128, 256):
        ascending = list(range(n))
        descending = list(range(n, 0, -1))
        shuffled = pseudo_random_list(n)
        estimate = n * log2_of_power_of_two(n)
        print(
            f"{n:>5} {count_comparisons(ascending):>8} "
            f"{count_comparisons(descending):>9} {count_comparisons(shuffled):>9} "
            f"{estimate:>10} {n * n:>7}"
        )
    print("Every column stays at or below n*log2(n); n*n grows much faster.")


if __name__ == "__main__":
    main()
