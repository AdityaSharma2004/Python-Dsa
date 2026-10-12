r"""
Problem: Sliding Window Maximum

Problem statement:
    Given an array and a window size k, report the maximum of every window of
    k consecutive elements as the window slides from left to right.

What it teaches:
    The monotonic deque: keep candidate indexes in decreasing order of value
    so the maximum is always at the front.

Input example:
    values = [1, 3, -1, -3, 5, 3, 6, 7], k = 3

Expected output:
    [1, 3, -1, -3, 5, 3, 6, 7] k=3 -> [3, 3, 5, 5, 6, 7]
    [4, 2, 12, 3] k=1 -> [4, 2, 12, 3]
    [9, 8, 7] k=3 -> [9]
    [1, 2, 3, 4] k=2 -> [2, 3, 4]
    [] k=3 -> []
    brute force agrees: True

Approach:
    The deque stores indexes whose values decrease from front to back. The
    front is the maximum of the current window.

Step-by-step logic:
    1. For each index i, drop the front index if it left the window
    (front <= i - k).
    2. Pop from the back while the back value is not larger than values[i];
    those can never be a maximum while i is in the window.
    3. Append i.
    4. Once i >= k - 1 a full window exists: record values[front].

Why it works:
    A smaller element that sits before a larger one expires earlier and is
    always smaller, so it can be discarded. The deque therefore holds exactly
    the useful candidates, in order.

Time complexity:
    O(n): each index enters and leaves the deque at most once.

Space complexity:
    O(k) for the deque (plus the output).

Edge cases:
    k = 1, k equal to the length, k larger than the length, empty array,
    duplicate values, decreasing or increasing arrays.

Alternative approach:
    Scan every window and find its maximum by hand: O(n * k) time (included
    below to verify the deque result).
"""

from collections import deque


def sliding_window_max(values, k):
    if k <= 0 or k > len(values):
        return []
    candidates = deque()  # indexes, values decreasing front -> back
    result = []
    for i, value in enumerate(values):
        if candidates and candidates[0] <= i - k:  # front left the window
            candidates.popleft()
        while candidates and values[candidates[-1]] <= value:
            candidates.pop()
        candidates.append(i)
        if i >= k - 1:
            result.append(values[candidates[0]])
    return result


def sliding_window_max_brute_force(values, k):
    result = []
    for start in range(len(values) - k + 1):
        best = values[start]
        for j in range(start + 1, start + k):
            if values[j] > best:
                best = values[j]
        result.append(best)
    return result


def main():
    samples = [([1, 3, -1, -3, 5, 3, 6, 7], 3), ([4, 2, 12, 3], 1),
               ([9, 8, 7], 3), ([1, 2, 3, 4], 2), ([], 3)]
    all_match = True
    for values, k in samples:
        answer = sliding_window_max(values, k)
        print(values, "k=%d ->" % k, answer)
        if values and answer != sliding_window_max_brute_force(values, k):
            all_match = False
    print("brute force agrees:", all_match)


if __name__ == "__main__":
    main()
