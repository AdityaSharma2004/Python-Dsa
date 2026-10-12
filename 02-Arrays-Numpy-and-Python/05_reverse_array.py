r"""
Problem title: Reverse an Array

Problem statement:
    Reverse a list of numbers in place (without list.reverse(), reversed() or
    the [::-1] slice) and, as an alternative, build a new reversed list.

What it teaches:
    The two-pointer technique: one pointer at each end, swap and move inward.

Input example:
    numbers = [1, 2, 3, 4, 5, 6]

Expected output:
    original: [1, 2, 3, 4, 5, 6]
    reverse_copy: [6, 5, 4, 3, 2, 1] | original still [1, 2, 3, 4, 5, 6]
    reverse_in_place: [6, 5, 4, 3, 2, 1] swaps = 3
    odd length: [50, 40, 30, 20, 10]
    single: [7]
    empty: []
    palindrome: [1, 2, 1]

Approach:
    In place: swap numbers[left] with numbers[right] while left < right.
    Copy: walk from the last index to the first and append into a new list.

Step-by-step logic:
    1. left = 0, right = len - 1.
    2. Swap the two elements.
    3. left += 1, right -= 1.
    4. Repeat until the pointers meet or cross.
    Dry run [1, 2, 3, 4]: swap(0,3) -> [4, 2, 3, 1]; swap(1,2) -> [4, 3, 2, 1].

Why it works:
    The element at position i must end up at position n-1-i. Each swap puts two
    elements at their final positions, so n/2 swaps are enough.

Time complexity:
    O(n) - about n/2 swaps.

Space complexity:
    In place: O(1). Copy version: O(n).

Edge cases:
    - Empty list and single element: nothing to do.
    - Odd length: the middle element stays where it is.
    - Palindrome lists look unchanged after reversing.

Alternative approach:
    numbers[::-1] or reversed() - shorter, but they hide the algorithm. A
    recursive swap also works with O(n) call-stack space.
"""


def reverse_in_place(numbers):
    """Reverse the list using two pointers. Returns the swap count."""
    left = 0
    right = len(numbers) - 1
    swaps = 0
    while left < right:
        numbers[left], numbers[right] = numbers[right], numbers[left]
        left += 1
        right -= 1
        swaps += 1
    return swaps


def reverse_copy(numbers):
    """Return a NEW reversed list; the original is not changed."""
    result = []
    for index in range(len(numbers) - 1, -1, -1):
        result.append(numbers[index])
    return result


def main():
    numbers = [1, 2, 3, 4, 5, 6]
    print("original:", numbers)
    print("reverse_copy:", reverse_copy(numbers), "| original still", numbers)
    swaps = reverse_in_place(numbers)
    print("reverse_in_place:", numbers, "swaps =", swaps)

    odd = [10, 20, 30, 40, 50]
    reverse_in_place(odd)
    print("odd length:", odd)
    single = [7]
    reverse_in_place(single)
    print("single:", single)
    empty = []
    reverse_in_place(empty)
    print("empty:", empty)
    palindrome = [1, 2, 1]
    reverse_in_place(palindrome)
    print("palindrome:", palindrome)


if __name__ == "__main__":
    main()
