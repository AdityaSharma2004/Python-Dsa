"""
Problem Title: Binary Search as Divide and Conquer

Problem Statement:
    Given a sorted list of integers and a target value, return the index of
    the target, or -1 if it is absent. Solve it by repeatedly halving the
    search range (recursively), then compare with a loop-based version.

What It Teaches:
    - The divide / conquer / combine pattern in its simplest form.
    - Only ONE half is solved each time (so there is nothing to combine).
    - How to reason about base cases (empty range) in recursion.

Input Example:
    data = [2, 5, 8, 12, 16, 23, 38, 56, 72, 91]
    targets = 23, 2, 91, 7, 100

Expected Output:
    Data: [2, 5, 8, 12, 16, 23, 38, 56, 72, 91]
    search  23 -> index 5
    search   2 -> index 0
    search  91 -> index 9
    search   7 -> index -1
    search 100 -> index -1
    Empty list -> -1

Approach:
    Look at the middle element. If it equals the target we are done. If the
    target is smaller, the answer can only be in the left half; otherwise in
    the right half. Recurse on that half.

Step-by-Step Logic:
    1. Define the range [low, high]. If low > high the range is empty -> -1.
    2. mid = (low + high) // 2 (integer division, like intdiv() in PHP).
    3. data[mid] == target -> return mid.
    4. data[mid] > target -> search [low, mid - 1].
    5. data[mid] < target -> search [mid + 1, high].

Why It Works:
    The list is sorted, so every element on the "wrong" side of mid is
    guaranteed not to be the target. Each step throws away half of the
    candidates, so the range shrinks 1/2, 1/4, 1/8 ... until empty.

Time Complexity:
    O(log n): the range halves each call, so at most about log2(n) + 1 calls.
Space Complexity:
    Recursive version O(log n) call stack; iterative version O(1).

Edge Cases:
    Empty list, single element, target smaller than all, target larger than
    all, target equal to first / last element.

Alternative Approach:
    The iterative loop (also shown) has the same idea with O(1) space.
    Python's bisect module does this too, but we write it by hand to learn.
"""


def binary_search_recursive(data, target, low, high):
    """Search data[low..high] for target; return index or -1."""
    if low > high:  # base case: empty range
        return -1
    mid = (low + high) // 2
    if data[mid] == target:
        return mid
    if data[mid] > target:
        return binary_search_recursive(data, target, low, mid - 1)
    return binary_search_recursive(data, target, mid + 1, high)


def binary_search_iterative(data, target):
    """Same algorithm using a loop instead of recursion."""
    low, high = 0, len(data) - 1
    while low <= high:
        mid = (low + high) // 2
        if data[mid] == target:
            return mid
        if data[mid] > target:
            high = mid - 1
        else:
            low = mid + 1
    return -1


def main():
    data = [2, 5, 8, 12, 16, 23, 38, 56, 72, 91]
    print("Data:", data)
    for target in [23, 2, 91, 7, 100]:
        rec = binary_search_recursive(data, target, 0, len(data) - 1)
        itr = binary_search_iterative(data, target)
        assert rec == itr
        print(f"search {target:>3} -> index {rec}")
    print("Empty list ->", binary_search_recursive([], 5, 0, -1))


if __name__ == "__main__":
    main()
