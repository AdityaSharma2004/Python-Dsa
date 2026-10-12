"""
Problem Title: Majority Element by Divide and Conquer

Problem Statement:
    Given a list, return the element that appears MORE than n/2 times, or
    None if no such element exists. Use divide and conquer.

What It Teaches:
    - A combine step that is not a simple merge: reconcile two candidates by
      counting them in the whole range.
    - Key idea: a majority of the whole must be a majority of at least one
      half.

Input Example:
    [2, 2, 1, 1, 1, 2, 2], [3, 3, 4, 2, 4, 4, 2, 4, 4], [1, 2, 3, 4]

Expected Output:
    [2, 2, 1, 1, 1, 2, 2] -> majority: 2
    [3, 3, 4, 2, 4, 4, 2, 4, 4] -> majority: 4
    [1, 2, 3, 4] -> majority: None
    [5] -> majority: 5
    [] -> majority: None
    [1, 1, 2, 2] -> majority: None

Approach:
    Find the majority candidate of the left half and of the right half. If they
    agree, that is the candidate. Otherwise count both candidates in the whole
    range and keep the one that occurs more often. Finally verify the
    candidate has more than n/2 occurrences.

Step-by-Step Logic:
    1. Base case: one element -> that element is the candidate.
    2. Split in halves, get left_candidate and right_candidate.
    3. If equal, return it. Otherwise count each inside [low, high].
    4. Return the one with the larger count.
    5. Top-level: count the final candidate; accept if count > n // 2.

Why It Works:
    If x occurs more than half the time overall, it cannot be a minority in
    both halves, so it is the candidate of at least one half. Counting the two
    candidates then picks the stronger one.

Time Complexity:
    O(n log n): T(n) = 2T(n/2) + O(n) for the counting step.
Space Complexity:
    O(log n) recursion stack.

Edge Cases:
    Empty list, single element, no majority (candidate fails verification),
    exactly n/2 occurrences (NOT a majority), all equal elements.

Alternative Approach:
    Boyer-Moore voting does it in O(n) time and O(1) space; a dictionary of
    counts is O(n) time and O(n) space.
"""


def count_in_range(data, value, low, high):
    """Count occurrences of value in data[low..high]."""
    total = 0
    for index in range(low, high + 1):
        if data[index] == value:
            total += 1
    return total


def candidate(data, low, high):
    """Return the majority candidate of data[low..high]."""
    if low == high:
        return data[low]
    mid = (low + high) // 2
    left = candidate(data, low, mid)
    right = candidate(data, mid + 1, high)
    if left == right:
        return left
    left_count = count_in_range(data, left, low, high)
    right_count = count_in_range(data, right, low, high)
    return left if left_count > right_count else right


def majority_element(data):
    """Return the majority element or None."""
    if not data:
        return None
    best = candidate(data, 0, len(data) - 1)
    if count_in_range(data, best, 0, len(data) - 1) > len(data) // 2:
        return best
    return None


def main():
    samples = [
        [2, 2, 1, 1, 1, 2, 2],
        [3, 3, 4, 2, 4, 4, 2, 4, 4],
        [1, 2, 3, 4],
        [5],
        [],
        [1, 1, 2, 2],
    ]
    for data in samples:
        print(f"{data} -> majority: {majority_element(data)}")


if __name__ == "__main__":
    main()
