r"""
Problem title: Rotate an Array by K Positions

Problem statement:
    Rotate a list to the right by k positions, in place. Example: rotating
    [1, 2, 3, 4, 5, 6, 7] right by 3 gives [5, 6, 7, 1, 2, 3, 4]. Also show
    a left rotation.

What it teaches:
    The three-reversal trick - rotation without extra memory - and why k must
    be reduced with k % n.

Input example:
    numbers = [1, 2, 3, 4, 5, 6, 7], k = 3

Expected output:
    original: [1, 2, 3, 4, 5, 6, 7]
    extra-list version, k=3: [5, 6, 7, 1, 2, 3, 4]
    rotate right by 3: [5, 6, 7, 1, 2, 3, 4]
    rotate left by 3 (back): [1, 2, 3, 4, 5, 6, 7]
    rotate right by 10: [5, 6, 7, 1, 2, 3, 4]
    rotate by n (unchanged): [1, 2, 3]
    rotate right by -1: [2, 3, 4, 1]
    empty: []

Approach:
    Reverse the whole list, then reverse the first k elements, then reverse the
    remaining n - k elements. A simple extra-list version is also given.

Step-by-step logic:
    1. k = k % n (rotating by n gives the same list).
    2. Reverse everything:       [7, 6, 5, 4, 3, 2, 1]
    3. Reverse first k (3):      [5, 6, 7, 4, 3, 2, 1]
    4. Reverse the rest (n-k):   [5, 6, 7, 1, 2, 3, 4]

Why it works:
    Reversing the whole list moves the last k elements to the front (but
    backwards). Reversing each block restores their original order.

Time complexity:
    O(n) - every element is moved a constant number of times.

Space complexity:
    Three-reversal version: O(1). Extra-list version: O(n).

Edge cases:
    - Empty list (avoid k % 0 -> ZeroDivisionError).
    - k = 0 or k a multiple of n -> unchanged.
    - k larger than n (k = 10 on 7 elements acts like k = 3).
    - Negative k means rotating the other way (handled by Python's modulo).

Alternative approach:
    result[(i + k) % n] = numbers[i] with a new list; or slicing
    numbers[-k:] + numbers[:-k].
"""


def reverse_range(numbers, start, end):
    """Reverse numbers[start..end] (both inclusive) in place."""
    while start < end:
        numbers[start], numbers[end] = numbers[end], numbers[start]
        start += 1
        end -= 1


def rotate_right(numbers, k):
    """Rotate right by k using three reversals. Modifies the list in place."""
    n = len(numbers)
    if n == 0:
        return
    k = k % n  # k = 10 on 7 items is the same as k = 3
    if k == 0:
        return
    reverse_range(numbers, 0, n - 1)
    reverse_range(numbers, 0, k - 1)
    reverse_range(numbers, k, n - 1)


def rotate_left(numbers, k):
    """Rotate left by k - the same as rotating right by n - k."""
    n = len(numbers)
    if n == 0:
        return
    rotate_right(numbers, n - (k % n))


def rotate_right_extra_list(numbers, k):
    """Simple version using a new list: element i goes to (i + k) % n."""
    n = len(numbers)
    if n == 0:
        return []
    result = [0] * n
    for index in range(n):
        result[(index + k) % n] = numbers[index]
    return result


def main():
    numbers = [1, 2, 3, 4, 5, 6, 7]
    print("original:", numbers)
    print("extra-list version, k=3:", rotate_right_extra_list(numbers, 3))
    rotate_right(numbers, 3)
    print("rotate right by 3:", numbers)
    rotate_left(numbers, 3)
    print("rotate left by 3 (back):", numbers)

    big = [1, 2, 3, 4, 5, 6, 7]
    rotate_right(big, 10)
    print("rotate right by 10:", big)
    same = [1, 2, 3]
    rotate_right(same, 3)
    print("rotate by n (unchanged):", same)
    negative = [1, 2, 3, 4]
    rotate_right(negative, -1)
    print("rotate right by -1:", negative)
    empty = []
    rotate_right(empty, 5)
    print("empty:", empty)


if __name__ == "__main__":
    main()
