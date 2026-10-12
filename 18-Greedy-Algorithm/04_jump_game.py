"""
Problem title:
    Jump Game

Problem statement:
    nums[i] is the maximum jump length from index i. Starting at index 0,
    decide whether you can reach the last index.

What it teaches:
    * Greedy does not always need sorting.
    * Track one number ("farthest reachable index") instead of exploring paths.

Input example:
    [2, 3, 1, 1, 4]   and   [3, 2, 1, 0, 4]

Expected output:
    [2, 3, 1, 1, 4] -> True
    [3, 2, 1, 0, 4] -> False
    [0] -> True
    [0, 1] -> False
    [1, 1, 1, 1] -> True
    [4, 0, 0, 0, 0] -> True
    [] -> False

Approach:
    Scan left to right while maintaining `farthest`, the farthest index we
    could possibly reach so far. If the current index is beyond `farthest`,
    we are stuck.

Step-by-step logic:
    1. farthest = 0.
    2. For each index i with jump length nums[i]:
       - if i > farthest: index i is unreachable -> return False.
       - farthest = the larger of farthest and i + nums[i].
       - if farthest >= last index: return True.
    3. Finishing the loop means the last index was reachable.

Why it works:
    Every index from 0 to `farthest` is reachable (we can land on any index in
    between). So the only thing that matters is how far the best jump gets us.

Time complexity:
    O(n) - one pass.

Space complexity:
    O(1) - only a few variables.

Edge cases:
    * Single element -> already at the end (True).
    * Zeros: [0] is True, [0, 1] is False.
    * A zero in the middle is harmless if an earlier jump passes over it.

Alternative approach:
    Backtracking or DP from the end (O(n^2)) work but are slower. A backward
    greedy ("can index i reach the current goal?") is also O(n).
"""


def can_jump(nums):
    """Return True if the last index is reachable from index 0."""
    if not nums:
        return False
    farthest = 0
    last_index = len(nums) - 1
    for i, jump in enumerate(nums):
        if i > farthest:  # we never managed to land on index i
            return False
        reach = i + jump
        if reach > farthest:
            farthest = reach
        if farthest >= last_index:
            return True
    return True


def main():
    tests = [
        [2, 3, 1, 1, 4],
        [3, 2, 1, 0, 4],
        [0],
        [0, 1],
        [1, 1, 1, 1],
        [4, 0, 0, 0, 0],
        [],
    ]
    for nums in tests:
        print(f"{nums} -> {can_jump(nums)}")


if __name__ == "__main__":
    main()
