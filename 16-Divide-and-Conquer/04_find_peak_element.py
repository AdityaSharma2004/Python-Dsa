"""
Problem Title: Find a Peak Element

Problem Statement:
    A peak is an element strictly greater than its neighbours (outside the
    array counts as negative infinity). Given a list where adjacent elements
    are different, return the index of ANY peak in O(log n) time.

What It Teaches:
    - Divide and conquer works even on UNSORTED data when a local property
      tells you which half must contain the answer.
    - Reasoning about invariants ("a peak always exists on the rising side").

Input Example:
    [1, 3, 20, 4, 1, 0], [1, 2, 3, 4, 5], [9, 5, 2, 1], [1, 5, 2, 6, 3]

Expected Output:
    [1, 3, 20, 4, 1, 0] -> peak at index 2 (value 20)
    [1, 2, 3, 4, 5] -> peak at index 4 (value 5)
    [9, 5, 2, 1] -> peak at index 0 (value 9)
    [1, 5, 2, 6, 3] -> peak at index 3 (value 6)
    [7] -> peak at index 0 (value 7)

Approach:
    Compare the middle element with its right neighbour. If data[mid] <
    data[mid + 1] we are going uphill, so a peak must exist to the right.
    Otherwise a peak exists at mid or to the left.

Step-by-Step Logic:
    1. low = 0, high = n - 1.
    2. While low < high: mid = (low + high) // 2.
    3. If data[mid] < data[mid + 1]: low = mid + 1 else high = mid.
    4. When low == high that index is a peak.

Why It Works:
    Walking uphill you must eventually stop, either at a real peak or at the
    array end (which counts as a peak because the outside is -infinity). So
    the half we keep always contains a peak.

Time Complexity:
    O(log n).
Space Complexity:
    O(1) iterative (recursive version would use O(log n)).

Edge Cases:
    Single element, strictly increasing (peak at last), strictly decreasing
    (peak at first), several peaks (any one is accepted), empty list.

Alternative Approach:
    A linear scan finds a peak in O(n); the binary approach is faster.
"""


def find_peak(data):
    """Return the index of any peak element."""
    if not data:
        raise ValueError("list must not be empty")
    low, high = 0, len(data) - 1
    while low < high:
        mid = (low + high) // 2
        if data[mid] < data[mid + 1]:
            low = mid + 1  # uphill: a peak lies to the right
        else:
            high = mid  # downhill: mid itself or something left is a peak
    return low


def is_peak(data, index):
    """Verify that data[index] is greater than both neighbours."""
    left_ok = index == 0 or data[index - 1] < data[index]
    right_ok = index == len(data) - 1 or data[index + 1] < data[index]
    return left_ok and right_ok


def main():
    samples = [
        [1, 3, 20, 4, 1, 0],
        [1, 2, 3, 4, 5],
        [9, 5, 2, 1],
        [1, 5, 2, 6, 3],
        [7],
    ]
    for data in samples:
        index = find_peak(data)
        assert is_peak(data, index)
        print(f"{data} -> peak at index {index} (value {data[index]})")


if __name__ == "__main__":
    main()
