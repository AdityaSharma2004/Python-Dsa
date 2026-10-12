r"""
Problem title: Best, Average and Worst Case of Linear Search

Problem statement:
    For a list of n distinct numbers, measure how many comparisons linear
    search needs when the target is first (best), in the middle (average-like),
    last or missing (worst). Then compute the true average over all positions.

What it teaches:
    The same algorithm can behave differently on different inputs:
      best case  Omega(1)   - target at index 0
      average    Theta(n/2) -> O(n)
      worst case O(n)       - target last or absent
    Interviewers usually ask for the WORST case.

Input example:
    numbers = [14, 3, 27, 8, 19, 42, 5, 31, 6, 11]  (n = 10)

Expected output:
    numbers: [14, 3, 27, 8, 19, 42, 5, 31, 6, 11]
    best case   (target 14 at front): 1
    middle case (target 19): 5
    worst case  (target 11 at end): 10
    worst case  (target 99 missing): 10
    average over all targets: 5.5
    formula (n + 1) / 2: 5.5
    empty list: 0

Approach:
    Write linear search returning the number of comparisons, then call it for
    each interesting target.

Step-by-step logic:
    1. Scan from index 0 and count each comparison.
    2. Stop immediately when the target is found.
    3. For the average, search every element once and divide total by n.

Why it works:
    If the target is at index k, exactly k + 1 comparisons happen. Averaging
    1, 2, ..., n gives (n + 1) / 2 which grows linearly with n.

Time complexity:
    Best O(1), average O(n), worst O(n).

Space complexity:
    O(1).

Edge cases:
    - Empty list: 0 comparisons.
    - Duplicate targets: search stops at the first one.
    - Target absent: exactly n comparisons.

Alternative approach:
    Binary search on sorted data has worst case O(log n).
"""


def linear_search_steps(numbers, target):
    """Return the number of comparisons used by linear search."""
    steps = 0
    for value in numbers:
        steps += 1
        if value == target:
            break
    return steps


def average_steps(numbers):
    """Average comparisons when the target is equally likely at any position."""
    total = 0
    for value in numbers:
        total += linear_search_steps(numbers, value)
    return total / len(numbers)


def main():
    numbers = [14, 3, 27, 8, 19, 42, 5, 31, 6, 11]
    n = len(numbers)
    print("numbers:", numbers)
    print("best case   (target 14 at front):", linear_search_steps(numbers, 14))
    print("middle case (target 19):", linear_search_steps(numbers, 19))
    print("worst case  (target 11 at end):", linear_search_steps(numbers, 11))
    print("worst case  (target 99 missing):", linear_search_steps(numbers, 99))
    print("average over all targets:", average_steps(numbers))
    print("formula (n + 1) / 2:", (n + 1) / 2)
    print("empty list:", linear_search_steps([], 5))


if __name__ == "__main__":
    main()
