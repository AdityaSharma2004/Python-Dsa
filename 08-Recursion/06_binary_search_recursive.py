"""
Problem title:
    Recursive Binary Search

Problem statement:
    Given a sorted list and a target, return the index of the target or -1
    if it is absent. Use recursion.

What it teaches:
    Divide-and-conquer recursion where each call discards half of the data.

Input example:
    numbers = [2, 5, 8, 12, 16, 23, 38, 56, 72, 91], target = 23

Expected output:
    target=23: index=5, mids checked=[4, 7, 5], iterative=5
    target=2: index=0, mids checked=[4, 1, 0], iterative=0
    target=91: index=9, mids checked=[4, 7, 8, 9], iterative=9
    target=50: index=-1, mids checked=[4, 7, 5, 6], iterative=-1
    empty list: -1

Approach:
    Look at the middle element; recurse into the left or right half.

Step-by-step logic:
    1. If low > high the range is empty -> return -1.
    2. mid = (low + high) // 2.
    3. If numbers[mid] == target return mid.
    4. If target is smaller, search low..mid-1, else mid+1..high.

Why it works:
    The list is sorted, so the target can only be in one half. Discarding the
    other half is safe, and the range shrinks every call.

Time complexity:
    O(log n).

Space complexity:
    O(log n) for the recursion stack (iterative version: O(1)).

Edge cases:
    Empty list, one element, target smaller/larger than all, duplicates
    (returns any matching index).

Alternative approach:
    Iterative while-loop binary search; avoids stack use.
"""


def binary_search(numbers, target, low, high, steps):
    """Search numbers[low..high]; steps collects visited middle indices."""
    if low > high:  # base case: not found
        return -1
    mid = (low + high) // 2
    steps.append(mid)
    if numbers[mid] == target:
        return mid
    if target < numbers[mid]:
        return binary_search(numbers, target, low, mid - 1, steps)
    return binary_search(numbers, target, mid + 1, high, steps)


def binary_search_iterative(numbers, target):
    low, high = 0, len(numbers) - 1
    while low <= high:
        mid = (low + high) // 2
        if numbers[mid] == target:
            return mid
        if target < numbers[mid]:
            high = mid - 1
        else:
            low = mid + 1
    return -1


def main():
    numbers = [2, 5, 8, 12, 16, 23, 38, 56, 72, 91]
    for target in (23, 2, 91, 50):
        steps = []
        index = binary_search(numbers, target, 0, len(numbers) - 1, steps)
        print(f"target={target}: index={index}, mids checked={steps}, "
              f"iterative={binary_search_iterative(numbers, target)}")
    print("empty list:", binary_search([], 5, 0, -1, []))


if __name__ == "__main__":
    main()
