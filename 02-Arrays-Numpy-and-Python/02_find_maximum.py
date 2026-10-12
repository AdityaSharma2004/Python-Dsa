r"""
Problem title: Find Maximum, Minimum and Second Largest

Problem statement:
    Without using max() or min(), find the largest and smallest element of a
    list together with the index where each occurs, and also the second largest
    DISTINCT value.

What it teaches:
    The "running best" pattern: keep one variable with the best value seen so
    far and update it while scanning the array once.

Input example:
    numbers = [12, 45, 7, 45, 3, 29]

Expected output:
    numbers: [12, 45, 7, 45, 3, 29]
    maximum (value, index): (45, 1)
    minimum (value, index): (3, 4)
    second largest: 29
    negatives: (-3, 1) (-20, 2)
    single element: (5, 0) None
    all equal second largest: None
    empty: None None None

Approach:
    Start with the first element as both the maximum and minimum, then compare
    each remaining element with the stored values.

Step-by-step logic:
    1. If the list is empty there is nothing to find - return None.
    2. best = numbers[0]; remember its index.
    3. For every next element, if it is bigger (strictly), update best + index.
    4. Same idea for the minimum with a smaller-than check.
    5. Second largest: keep two variables, first and second; when a value is
       greater than first, the old first becomes second; if it is between them
       (and not equal to first), it becomes second.

Why it works:
    After processing i elements the variables always hold the answer for those
    i elements, so after the last element they hold the answer for the list.

Time complexity:
    O(n) - one pass.

Space complexity:
    O(1) - a few variables.

Edge cases:
    - Empty list -> None.
    - One element -> max = min, no second largest.
    - Duplicates: using ">" keeps the FIRST index of the maximum (12, 45, 45
      returns index 1).
    - All elements equal -> no second distinct largest.
    - Negative numbers work because we start from numbers[0], not from 0.

Alternative approach:
    Sort and take the ends: O(n log n), slower and unnecessary. Python's
    max()/min() do the same single pass internally.
"""


def find_maximum(numbers):
    """Return (max value, index of its first occurrence) or None."""
    if len(numbers) == 0:
        return None
    best_value = numbers[0]
    best_index = 0
    for index in range(1, len(numbers)):
        if numbers[index] > best_value:  # strict: keeps the first index
            best_value = numbers[index]
            best_index = index
    return best_value, best_index


def find_minimum(numbers):
    """Return (min value, index of its first occurrence) or None."""
    if len(numbers) == 0:
        return None
    best_value = numbers[0]
    best_index = 0
    for index in range(1, len(numbers)):
        if numbers[index] < best_value:
            best_value = numbers[index]
            best_index = index
    return best_value, best_index


def find_second_largest(numbers):
    """Return the second largest distinct value, or None if it does not exist."""
    first = None
    second = None
    for value in numbers:
        if first is None or value > first:
            second = first  # the old champion becomes runner-up
            first = value
        elif value != first and (second is None or value > second):
            second = value
    return second


def main():
    numbers = [12, 45, 7, 45, 3, 29]
    print("numbers:", numbers)
    print("maximum (value, index):", find_maximum(numbers))
    print("minimum (value, index):", find_minimum(numbers))
    print("second largest:", find_second_largest(numbers))
    print("negatives:", find_maximum([-8, -3, -20]), find_minimum([-8, -3, -20]))
    print("single element:", find_maximum([5]), find_second_largest([5]))
    print("all equal second largest:", find_second_largest([7, 7, 7]))
    print("empty:", find_maximum([]), find_minimum([]), find_second_largest([]))


if __name__ == "__main__":
    main()
