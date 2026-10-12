"""
Problem title:
    Recursive Array Operations (Sum, Maximum, Count, Reverse)

Problem statement:
    Without loops, write recursive functions that, for a list, compute the
    sum, find the largest element, count occurrences of a value, and
    reverse the list in place.

What it teaches:
    Using an index parameter to walk through a list recursively, and the
    pattern "combine current element with the answer for the rest".

Input example:
    data = [3, 8, 2, 8, 5]

Expected output:
    data: [3, 8, 2, 8, 5]
    sum: 26
    max: 8
    count of 8: 2
    reversed: [5, 8, 2, 8, 3]
    negatives max: -2
    empty sum: 0
    Error: cannot take the maximum of an empty list

Approach:
    Each function takes an index. Base case: index reached the end.

Step-by-step logic:
    1. sum: if index == len -> 0, else data[index] + sum(index + 1).
    2. maximum: last element is the base case; compare current with the
       maximum of the rest.
    3. count: add 1 when data[index] == target, then recurse.
    4. reverse: swap data[left], data[right] then recurse inward.

Why it works:
    Each call handles one element and trusts the recursive call to handle
    the rest correctly (the "recursive leap of faith").

Time complexity:
    O(n) for each function.

Space complexity:
    O(n) call stack.

Edge cases:
    Empty list (sum 0, max error, count 0), single element, all equal,
    negative numbers.

Alternative approach:
    Plain loops (O(1) space); or divide the array in halves (still O(n) time).
"""


def array_sum(data, index=0):
    if index == len(data):  # base case: nothing left
        return 0
    return data[index] + array_sum(data, index + 1)


def array_max(data, index=0):
    if not data:
        raise ValueError("cannot take the maximum of an empty list")
    if index == len(data) - 1:  # last element
        return data[index]
    rest_max = array_max(data, index + 1)
    return data[index] if data[index] > rest_max else rest_max


def count_occurrences(data, target, index=0):
    if index == len(data):
        return 0
    matched = 1 if data[index] == target else 0
    return matched + count_occurrences(data, target, index + 1)


def reverse_in_place(data, left=0, right=None):
    if right is None:
        right = len(data) - 1
    if left >= right:
        return
    data[left], data[right] = data[right], data[left]
    reverse_in_place(data, left + 1, right - 1)


def main():
    data = [3, 8, 2, 8, 5]
    print("data:", data)
    print("sum:", array_sum(data))
    print("max:", array_max(data))
    print("count of 8:", count_occurrences(data, 8))
    reverse_in_place(data)
    print("reversed:", data)
    print("negatives max:", array_max([-7, -2, -9]))
    print("empty sum:", array_sum([]))
    try:
        array_max([])
    except ValueError as error:
        print("Error:", error)


if __name__ == "__main__":
    main()
