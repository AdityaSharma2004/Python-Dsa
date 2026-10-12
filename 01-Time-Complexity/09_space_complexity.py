r"""
Problem title: Space Complexity - O(1) vs O(n) Extra Memory

Problem statement:
    Reverse a list in two ways: in place (swapping) and by building a new list.
    Also compute a running total (O(1) space) vs a prefix-sum list (O(n) space).
    Count how many extra list slots each version allocates.

What it teaches:
    Space complexity measures EXTRA memory, not counting the input itself.
    In place = O(1) extra; building a copy = O(n) extra. Recursion also uses
    stack space.

Input example:
    numbers = [1, 2, 3, 4, 5, 6]

Expected output:
    original: [1, 2, 3, 4, 5, 6]
    copy reversed: ([6, 5, 4, 3, 2, 1], 6)
    original after copy-reverse: [1, 2, 3, 4, 5, 6]
    prefix sums: ([1, 3, 6, 10, 15, 21], 6)
    running total: (21, 0)
    recursive sum: 21
    in-place reversed: ([6, 5, 4, 3, 2, 1], 0)
    original after in-place reverse: [6, 5, 4, 3, 2, 1]
    empty list: ([], 0) ([], 0)

Approach:
    Each function returns its result plus the number of extra slots it created.

Step-by-step logic:
    1. reverse_in_place swaps items from both ends moving inward (2 pointers).
    2. reverse_with_copy appends from the end to a new list (n slots).
    3. running_total keeps one number; prefix_sums keeps n numbers.
    4. recursive_sum uses one stack frame per element -> O(n) space.

Why it works:
    Swapping uses one temporary variable, regardless of list size. A copy needs a
    slot for every element. Recursion depth equals the list length.

Time complexity:
    All functions are O(n).

Space complexity:
    reverse_in_place O(1); reverse_with_copy O(n); running_total O(1);
    prefix_sums O(n); recursive_sum O(n) stack.

Edge cases:
    - Empty list and single element list need no swaps.
    - In-place reversal changes the original list (a side effect).
    - Deep recursion can hit Python's recursion limit (about 1000 frames).

Alternative approach:
    Python slicing numbers[::-1] is also O(n) extra space.
"""


def reverse_in_place(items):
    left = 0
    right = len(items) - 1
    while left < right:
        items[left], items[right] = items[right], items[left]
        left += 1
        right -= 1
    return items, 0  # no extra slots (just two index variables)


def reverse_with_copy(items):
    reversed_items = []
    for index in range(len(items) - 1, -1, -1):
        reversed_items.append(items[index])
    return reversed_items, len(reversed_items)


def running_total(items):
    total = 0
    for value in items:
        total += value
    return total, 0


def prefix_sums(items):
    sums = []
    total = 0
    for value in items:
        total += value
        sums.append(total)
    return sums, len(sums)


def recursive_sum(items, index=0):
    """Each pending call waits on the stack: depth = len(items)."""
    if index == len(items):
        return 0
    return items[index] + recursive_sum(items, index + 1)


def main():
    numbers = [1, 2, 3, 4, 5, 6]
    print("original:", numbers)
    print("copy reversed:", reverse_with_copy(numbers))
    print("original after copy-reverse:", numbers)
    print("prefix sums:", prefix_sums(numbers))
    print("running total:", running_total(numbers))
    print("recursive sum:", recursive_sum(numbers))
    print("in-place reversed:", reverse_in_place(numbers))
    print("original after in-place reverse:", numbers)
    print("empty list:", reverse_in_place([]), reverse_with_copy([]))


if __name__ == "__main__":
    main()
