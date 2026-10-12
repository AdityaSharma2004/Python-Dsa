"""
Problem Title: Subset Sum (and Equal-Sum Partition)

Problem Statement:
    Given a list of non-negative integers and a target, decide whether some subset
    adds up exactly to the target and return one such subset. Then use it to test
    whether the list can be split into two parts with equal sums.

What It Teaches:
    - Boolean DP: dp[s] = "can we make sum s?".
    - A yes/no cousin of 0/1 knapsack (same take / skip structure).
    - Iterating sums downwards so each number is used at most once.
    - Reducing the partition problem to subset sum.

Input Example:
    numbers = [3, 34, 4, 12, 5, 2], target = 9

Expected Output:
    Numbers: [3, 34, 4, 12, 5, 2] target: 9
    Subset: [4, 5]
    1-D check: True
    Target 30: None
    Target 0: []
    Empty list, target 5: None
    Partition [1, 5, 11, 5]: True
    Partition [1, 2, 3, 5]: False

Approach:
    Keep a 2-D table reachable[i][s]: using the first i numbers can we make sum s?
    reachable[i][s] = reachable[i-1][s] or (s >= num and reachable[i-1][s - num]).

Step-by-Step Logic:
    1. reachable[i][0] = True for every i (empty subset).
    2. For each number and each sum s from 0 to target apply the rule above.
    3. reachable[n][target] is the answer.
    4. Backtrack: at row i, if reachable[i-1][s] is true skip number i; else take it
       and reduce s by the number.
    5. Partition: if the total is odd, answer False; else ask for total // 2.
    6. 1-D version: for each number loop s from target down to number.

Why It Works:
    A subset either leaves out the last number (use the smaller table) or includes
    it (then the rest must make target minus that number).

Time Complexity:
    O(n * target).
Space Complexity:
    O(n * target) for the 2-D table (O(target) for the 1-D yes/no version).

Edge Cases:
    Target 0 (always True via empty subset), empty list, target larger than the
    total, a zero in the list, odd total for partition.

Alternative Approach:
    Backtracking over all 2^n subsets, or a bit-mask trick using Python's big integers.
"""


def subset_sum_table(numbers, target):
    """reachable[i][s] is True if the first i numbers can form sum s."""
    n = len(numbers)
    reachable = [[False] * (target + 1) for _ in range(n + 1)]
    for i in range(n + 1):
        reachable[i][0] = True
    for i in range(1, n + 1):
        number = numbers[i - 1]
        for s in range(1, target + 1):
            reachable[i][s] = reachable[i - 1][s]
            if s >= number and reachable[i - 1][s - number]:
                reachable[i][s] = True
    return reachable


def find_subset(numbers, target):
    """Return a list of numbers summing to target, or None."""
    reachable = subset_sum_table(numbers, target)
    if not reachable[len(numbers)][target]:
        return None
    chosen = []
    s = target
    for i in range(len(numbers), 0, -1):
        if not reachable[i - 1][s]:  # cannot do without number i
            chosen.append(numbers[i - 1])
            s -= numbers[i - 1]
    chosen.reverse()
    return chosen


def subset_sum_1d(numbers, target):
    """Yes/no answer with a single boolean row."""
    can = [False] * (target + 1)
    can[0] = True
    for number in numbers:
        for s in range(target, number - 1, -1):
            if can[s - number]:
                can[s] = True
    return can[target]


def can_partition(numbers):
    """True if numbers split into two groups with equal sums."""
    total = 0
    for number in numbers:
        total += number
    if total % 2 == 1:
        return False
    return subset_sum_1d(numbers, total // 2)


def main():
    numbers, target = [3, 34, 4, 12, 5, 2], 9
    print("Numbers:", numbers, "target:", target)
    print("Subset:", find_subset(numbers, target))
    print("1-D check:", subset_sum_1d(numbers, target))
    print("Target 30:", find_subset(numbers, 30))
    print("Target 0:", find_subset(numbers, 0))
    print("Empty list, target 5:", find_subset([], 5))
    print("Partition [1, 5, 11, 5]:", can_partition([1, 5, 11, 5]))
    print("Partition [1, 2, 3, 5]:", can_partition([1, 2, 3, 5]))


if __name__ == "__main__":
    main()
