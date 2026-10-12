r"""
Problem title: Array Traversal

Problem statement:
    Given a list of integers, visit every element and show the common ways to
    traverse an array: forward, backward, with the index, every k-th element,
    and from both ends at the same time.

What it teaches:
    Python lists are arrays: elements sit side by side and are reached by index.
    Traversal means touching each element once. (Like looping over a PHP array
    with a for loop or foreach.)

Input example:
    numbers = [4, 8, 15, 16, 23, 42]

Expected output:
    numbers: [4, 8, 15, 16, 23, 42]
    forward: [4, 8, 15, 16, 23, 42]
    backward: [42, 23, 16, 15, 8, 4]
    with index: ['0 -> 4', '1 -> 8', '2 -> 15', '3 -> 16', '4 -> 23', '5 -> 42']
    every 2nd: [4, 15, 23]
    every 4th: [4, 23]
    both ends: [4, 42, 8, 23, 15, 16]
    both ends (odd length): [1, 5, 2, 4, 3]
    empty forward: []
    single both ends: [9]

Approach:
    Use simple for/while loops with range(); count the elements visited so the
    cost is visible.

Step-by-step logic:
    1. Forward: index 0, 1, 2, ... len-1.
    2. Backward: index len-1 down to 0 (range with step -1).
    3. With index: print "index -> value" pairs.
    4. Every k-th element: range(0, len, k).
    5. Two ends: keep a left and a right index and move them towards each other.

Why it works:
    Every element has a fixed position, so a loop over the positions visits each
    element exactly once.

Time complexity:
    O(n) for each traversal - every element is visited once (or n/k times for
    the k-th element version, still O(n) in terms of n).

Space complexity:
    O(1) extra - only loop variables (the result lists in this file are only
    built to make the output easy to print).

Edge cases:
    - Empty list: loops do nothing and no error is raised.
    - Single element: forward, backward and both-ends give that element once.
    - Odd length for the two-ends version: the middle element is visited once.

Alternative approach:
    Python's "for value in numbers" hides the index; use enumerate() when you
    need both. Recursion can also traverse, but it uses O(n) stack space.
"""


def traverse_forward(numbers):
    """Return the elements in order, first to last."""
    visited = []
    for index in range(len(numbers)):
        visited.append(numbers[index])
    return visited


def traverse_backward(numbers):
    """Return the elements from last to first."""
    visited = []
    for index in range(len(numbers) - 1, -1, -1):  # stop at -1 so 0 is included
        visited.append(numbers[index])
    return visited


def traverse_with_index(numbers):
    """Return 'index -> value' strings."""
    lines = []
    for index in range(len(numbers)):
        lines.append(f"{index} -> {numbers[index]}")
    return lines


def traverse_every_kth(numbers, k):
    """Return every k-th element starting from index 0."""
    if k <= 0:
        raise ValueError("k must be a positive integer")
    visited = []
    for index in range(0, len(numbers), k):
        visited.append(numbers[index])
    return visited


def traverse_from_both_ends(numbers):
    """Visit left and right ends together, moving towards the middle."""
    visited = []
    left = 0
    right = len(numbers) - 1
    while left <= right:
        visited.append(numbers[left])
        if left != right:  # avoid visiting the middle element twice
            visited.append(numbers[right])
        left += 1
        right -= 1
    return visited


def main():
    numbers = [4, 8, 15, 16, 23, 42]
    print("numbers:", numbers)
    print("forward:", traverse_forward(numbers))
    print("backward:", traverse_backward(numbers))
    print("with index:", traverse_with_index(numbers))
    print("every 2nd:", traverse_every_kth(numbers, 2))
    print("every 4th:", traverse_every_kth(numbers, 4))
    print("both ends:", traverse_from_both_ends(numbers))
    print("both ends (odd length):", traverse_from_both_ends([1, 2, 3, 4, 5]))
    print("empty forward:", traverse_forward([]))
    print("single both ends:", traverse_from_both_ends([9]))


if __name__ == "__main__":
    main()
