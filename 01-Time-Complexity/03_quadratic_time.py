r"""
Problem title: Quadratic Time Operations - O(n^2)

Problem statement:
    Given a list, (a) print/count every ordered pair (i, j), (b) count unordered
    pairs whose sum equals a target, and (c) detect a duplicate by comparing every
    pair. Report the number of comparisons made.

What it teaches:
    O(n^2): a loop inside a loop where both run about n times. Doubling the
    input makes the work about four times larger.

Input example:
    numbers = [3, 8, 2, 5, 7, 1]; target = 9

Expected output:
    numbers: [3, 8, 2, 5, 7, 1]
    ordered pairs steps: 36 (n*n = 36 )
    pairs with sum 9: (2, 15)
    n*(n-1)/2 = 15
    duplicates in numbers: (False, 15)
    duplicates in [4, 1, 4]: (True, 2)
    size 10: steps = 100
    size 20: steps = 400
    size 40: steps = 1600

Approach:
    Nested loops. For unordered pairs the inner loop starts at i + 1.

Step-by-step logic:
    1. Outer loop picks index i.
    2. Inner loop picks index j.
    3. Do the work and count one step per (i, j) combination.
    4. Compare counted steps with n * n and n * (n - 1) / 2.

Why it works:
    Every pair is visited exactly once, so no pair can be missed. Total visits:
    n * n for all ordered pairs, n * (n - 1) / 2 for unordered pairs.

Time complexity:
    O(n^2) for all three functions.

Space complexity:
    O(1) extra (only counters).

Edge cases:
    - Empty or one-element list: no pairs, 0 steps.
    - Duplicates: has_duplicate_pairwise stops as soon as one is found.
    - Pair must use two different positions (i != j).

Alternative approach:
    A set lets us find duplicates / pair sums in O(n) time (see file 10).
"""


def count_all_ordered_pairs(numbers):
    steps = 0
    for i in range(len(numbers)):
        for j in range(len(numbers)):
            steps += 1
    return steps


def count_pairs_with_sum(numbers, target):
    """Return (number of pairs with sum == target, comparisons)."""
    pairs = 0
    steps = 0
    for i in range(len(numbers)):
        for j in range(i + 1, len(numbers)):  # j > i avoids repeats
            steps += 1
            if numbers[i] + numbers[j] == target:
                pairs += 1
    return pairs, steps


def has_duplicate_pairwise(numbers):
    """Return (True/False, comparisons)."""
    steps = 0
    for i in range(len(numbers)):
        for j in range(i + 1, len(numbers)):
            steps += 1
            if numbers[i] == numbers[j]:
                return True, steps
    return False, steps


def main():
    numbers = [3, 8, 2, 5, 7, 1]
    n = len(numbers)
    print("numbers:", numbers)
    print("ordered pairs steps:", count_all_ordered_pairs(numbers), "(n*n =", n * n, ")")
    print("pairs with sum 9:", count_pairs_with_sum(numbers, 9))
    print("n*(n-1)/2 =", n * (n - 1) // 2)
    print("duplicates in numbers:", has_duplicate_pairwise(numbers))
    print("duplicates in [4, 1, 4]:", has_duplicate_pairwise([4, 1, 4]))
    for size in [10, 20, 40]:
        print(f"size {size}: steps = {count_all_ordered_pairs(list(range(size)))}")


if __name__ == "__main__":
    main()
