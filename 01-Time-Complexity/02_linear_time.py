r"""
Problem title: Linear Time Operations - O(n)

Problem statement:
    Write functions that must look at every element once: sum of a list, count
    of even numbers, and the position of a target (linear search). Report how
    many loop iterations each one needed.

What it teaches:
    O(n): if the input doubles, the work doubles. One loop over the data is the
    typical sign of linear time.

Input example:
    numbers = [4, 7, 1, 9, 2, 8, 6]; target = 9
    and a doubled list of 14 numbers to show the work doubling.

Expected output:
    numbers: [4, 7, 1, 9, 2, 8, 6]
    sum_of_list: (37, 7)
    count_evens: (4, 7)
    linear_search for 9: (3, 4)
    linear_search for 100: (-1, 7)
    doubled list, sum steps: 14
    empty list sum: (0, 0)

Approach:
    Use a single for loop and a counter named steps.

Step-by-step logic:
    1. Start total = 0 and steps = 0.
    2. For every element, update the answer and increase steps by one.
    3. Return the answer and the steps.
    4. Call the function on a list and on a list twice as long, compare steps.

Why it works:
    The answer depends on every element, so no algorithm can skip any item
    without risking a wrong answer; one pass is both necessary and enough.

Time complexity:
    O(n) for sum_of_list and count_evens; linear_search is O(n) worst case.

Space complexity:
    O(1) - only counters are stored.

Edge cases:
    - Empty list: sum is 0, count is 0, search returns -1.
    - Target missing: search scans everything and returns -1.
    - Target at index 0: search stops after 1 step (best case).

Alternative approach:
    Python's built-in sum() is also O(n); it hides the loop but not the cost.
"""


def sum_of_list(numbers):
    total = 0
    steps = 0
    for value in numbers:
        total += value
        steps += 1
    return total, steps


def count_evens(numbers):
    count = 0
    steps = 0
    for value in numbers:
        steps += 1
        if value % 2 == 0:
            count += 1
    return count, steps


def linear_search(numbers, target):
    """Return (index or -1, steps)."""
    steps = 0
    for index in range(len(numbers)):
        steps += 1
        if numbers[index] == target:
            return index, steps  # stop early when found
    return -1, steps


def main():
    numbers = [4, 7, 1, 9, 2, 8, 6]
    doubled = numbers + numbers
    print("numbers:", numbers)
    print("sum_of_list:", sum_of_list(numbers))
    print("count_evens:", count_evens(numbers))
    print("linear_search for 9:", linear_search(numbers, 9))
    print("linear_search for 100:", linear_search(numbers, 100))
    print("doubled list, sum steps:", sum_of_list(doubled)[1])
    print("empty list sum:", sum_of_list([]))


if __name__ == "__main__":
    main()
