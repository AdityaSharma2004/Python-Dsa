"""
Problem Title: Longest Increasing Subsequence (LIS)

Problem Statement:
    Given a list of integers, find the length of the longest strictly increasing
    subsequence (elements keep their order but need not be adjacent) and one
    such subsequence.

What It Teaches:
    - A 1-D DP where dp[i] ends exactly at element i.
    - Storing parent pointers to rebuild the answer.
    - A faster O(n log n) idea using binary search on "tails".

Input Example:
    [10, 9, 2, 5, 3, 7, 101, 18]

Expected Output:
    Data: [10, 9, 2, 5, 3, 7, 101, 18]
    LIS length: 4 sequence: [2, 5, 7, 101]
    Fast O(n log n) length: 4
    [] -> 0 / 0
    [7] -> 1 / 1
    [5, 4, 3, 2, 1] -> 1 / 1
    [2, 2, 2] -> 1 / 1
    [1, 2, 3, 4] -> 4 / 4
    [0, 8, 4, 12, 2, 10, 6, 14] -> 4 / 4

Approach:
    dp[i] = length of the longest increasing subsequence that ENDS at index i.
    Look at every earlier index j with data[j] < data[i] and extend the best one.

Step-by-Step Logic:
    1. dp[i] = 1 for all i (each element alone), parent[i] = -1.
    2. For i in 1..n-1, for j in 0..i-1: if data[j] < data[i] and dp[j] + 1 > dp[i],
       set dp[i] = dp[j] + 1 and parent[i] = j.
    3. The answer ends at the index with the largest dp value (found by a loop).
    4. Follow parent pointers back to rebuild the sequence.
    5. Fast version: tails[k] = smallest possible last value of an increasing
       subsequence of length k+1; binary search where each number belongs.

Why It Works:
    Any increasing subsequence ending at i has a second-to-last element j with
    data[j] < data[i]; removing i leaves an increasing subsequence ending at j.

Time Complexity:
    O(n^2) for the DP version; O(n log n) for the tails version.
Space Complexity:
    O(n).

Edge Cases:
    Empty list (0), single element, strictly decreasing (answer 1), all equal
    (answer 1 because strictly increasing is required), already sorted.

Alternative Approach:
    The O(n log n) tails method is implemented below as a second function.
"""


def lis_dp(data):
    """Return (length, subsequence) with the O(n^2) DP."""
    n = len(data)
    if n == 0:
        return 0, []
    dp = [1] * n
    parent = [-1] * n
    for i in range(1, n):
        for j in range(i):
            if data[j] < data[i] and dp[j] + 1 > dp[i]:
                dp[i] = dp[j] + 1
                parent[i] = j
    best_index = 0
    for i in range(1, n):
        if dp[i] > dp[best_index]:
            best_index = i
    sequence = []
    while best_index != -1:
        sequence.append(data[best_index])
        best_index = parent[best_index]
    sequence.reverse()
    return len(sequence), sequence


def lis_length_fast(data):
    """O(n log n): keep the smallest tail value for each subsequence length."""
    tails = []
    for value in data:
        low, high = 0, len(tails)
        while low < high:  # binary search: first tail >= value
            mid = (low + high) // 2
            if tails[mid] < value:
                low = mid + 1
            else:
                high = mid
        if low == len(tails):
            tails.append(value)
        else:
            tails[low] = value
    return len(tails)


def main():
    data = [10, 9, 2, 5, 3, 7, 101, 18]
    length, sequence = lis_dp(data)
    print("Data:", data)
    print("LIS length:", length, "sequence:", sequence)
    print("Fast O(n log n) length:", lis_length_fast(data))
    for case in ([], [7], [5, 4, 3, 2, 1], [2, 2, 2], [1, 2, 3, 4], [0, 8, 4, 12, 2, 10, 6, 14]):
        print(f"{case} -> {lis_dp(case)[0]} / {lis_length_fast(case)}")


if __name__ == "__main__":
    main()
