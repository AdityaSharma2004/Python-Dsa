r"""
Problem title: Logarithmic Time - O(log n) with Binary Search

Problem statement:
    Search a target in a SORTED list using binary search and count the steps.
    Also count how many times n can be halved before reaching 1.

What it teaches:
    O(log n): the problem size is cut in half every step, so even a million
    items need only about 20 steps. Requires sorted data.

Input example:
    sorted_numbers = [2, 5, 8, 12, 16, 23, 38, 56, 72, 91]; target = 23

Expected output:
    list: [2, 5, 8, 12, 16, 23, 38, 56, 72, 91]
    search 23: (5, 3)
    search 2: (0, 3)
    search 50: (-1, 4)
    search in empty list: (-1, 0)
    n = 8: halvings = 3, binary search steps = 4
    n = 1024: halvings = 10, binary search steps = 11
    n = 1000000: halvings = 19, binary search steps = 20

Approach:
    Keep low and high bounds, look at the middle, discard the half that cannot
    contain the target.

Step-by-step logic:
    1. low = 0, high = len - 1.
    2. mid = (low + high) // 2.
    3. If item at mid equals target -> done.
    4. If item is smaller than target -> low = mid + 1, else high = mid - 1.
    5. Repeat while low <= high.

Why it works:
    The list is sorted, so if the middle item is too small, everything left of
    it is also too small and can be ignored. Each step halves the range.

Time complexity:
    O(log n) - at most floor(log2(n)) + 1 comparisons.

Space complexity:
    O(1) - iterative version.

Edge cases:
    - Empty list returns -1 immediately.
    - Target smaller than first or larger than last item.
    - List must be sorted; otherwise the result is meaningless.

Alternative approach:
    Recursive binary search (same time, O(log n) stack space).
"""


def binary_search(sorted_numbers, target):
    """Return (index or -1, steps)."""
    low = 0
    high = len(sorted_numbers) - 1
    steps = 0
    while low <= high:
        steps += 1
        mid = (low + high) // 2
        if sorted_numbers[mid] == target:
            return mid, steps
        if sorted_numbers[mid] < target:
            low = mid + 1
        else:
            high = mid - 1
    return -1, steps


def count_halvings(n):
    """How many times can n be divided by 2 until it reaches 1? (floor of log2 n)"""
    count = 0
    while n > 1:
        n = n // 2
        count += 1
    return count


def main():
    sorted_numbers = [2, 5, 8, 12, 16, 23, 38, 56, 72, 91]
    print("list:", sorted_numbers)
    print("search 23:", binary_search(sorted_numbers, 23))
    print("search 2:", binary_search(sorted_numbers, 2))
    print("search 50:", binary_search(sorted_numbers, 50))
    print("search in empty list:", binary_search([], 5))
    for n in [8, 1024, 1000000]:
        big = list(range(n))
        _, steps = binary_search(big, n - 1)
        print(f"n = {n}: halvings = {count_halvings(n)}, binary search steps = {steps}")


if __name__ == "__main__":
    main()
