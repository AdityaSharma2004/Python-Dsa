"""
Problem Title: Maximum Subarray Sum (Divide and Conquer)

Problem Statement:
    Given a list of integers (positive and negative), find the largest sum of
    any non-empty contiguous subarray.

What It Teaches:
    - The "crossing" case: the best subarray lies in the left half, the right
      half, or crosses the midpoint.
    - A combine step that does linear work, giving O(n log n).

Input Example:
    [-2, 1, -3, 4, -1, 2, 1, -5, 4]

Expected Output:
    [-2, 1, -3, 4, -1, 2, 1, -5, 4] -> 6
    [5, 4, -1, 7, 8] -> 23
    [-8, -3, -6, -2, -5] -> -2
    [1] -> 1
    [0, 0, 0] -> 0

Approach:
    best(low, high) = largest of
      - best(low, mid)
      - best(mid + 1, high)
      - best crossing sum: (best suffix ending at mid) + (best prefix starting
        at mid + 1)

Step-by-Step Logic:
    1. Base case: one element -> itself.
    2. Recurse on both halves.
    3. From mid walk left keeping the largest running sum (left_best).
    4. From mid + 1 walk right keeping the largest running sum (right_best).
    5. crossing = left_best + right_best. Return the largest of the three.

Why It Works:
    Any contiguous subarray either lies completely in one half or contains
    both mid and mid + 1; those three cases cover everything.

Time Complexity:
    O(n log n): T(n) = 2T(n/2) + O(n).
Space Complexity:
    O(log n) recursion stack.

Edge Cases:
    All negative numbers (answer is the largest single element), single
    element, all positive (whole array), zeros, empty list (error).

Alternative Approach:
    Kadane's algorithm solves it in O(n) time, O(1) space (also shown below
    and used to verify the answer).
"""


def crossing_sum(data, low, mid, high):
    """Best sum of a subarray that includes both data[mid] and data[mid + 1]."""
    running = 0
    left_best = None
    for index in range(mid, low - 1, -1):
        running += data[index]
        if left_best is None or running > left_best:
            left_best = running
    running = 0
    right_best = None
    for index in range(mid + 1, high + 1):
        running += data[index]
        if right_best is None or running > right_best:
            right_best = running
    return left_best + right_best


def max_subarray(data, low, high):
    """Maximum subarray sum inside data[low..high]."""
    if low == high:
        return data[low]
    mid = (low + high) // 2
    left = max_subarray(data, low, mid)
    right = max_subarray(data, mid + 1, high)
    cross = crossing_sum(data, low, mid, high)
    best = left
    if right > best:
        best = right
    if cross > best:
        best = cross
    return best


def kadane(data):
    """O(n) reference solution used for verification."""
    best = current = data[0]
    for value in data[1:]:
        current = value if current < 0 else current + value
        if current > best:
            best = current
    return best


def main():
    samples = [
        [-2, 1, -3, 4, -1, 2, 1, -5, 4],
        [5, 4, -1, 7, 8],
        [-8, -3, -6, -2, -5],
        [1],
        [0, 0, 0],
    ]
    for data in samples:
        answer = max_subarray(data, 0, len(data) - 1)
        assert answer == kadane(data)
        print(f"{data} -> {answer}")


if __name__ == "__main__":
    main()
