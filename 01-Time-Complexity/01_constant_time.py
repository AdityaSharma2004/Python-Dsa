r"""
Problem title: Constant Time Operations - O(1)

Problem statement:
    Show operations whose cost does NOT grow with the input size: reading an
    element by index, checking if a number is even, swapping two elements and
    computing 1 + 2 + ... + n with a formula. Count the "steps" used to prove it.

What it teaches:
    What O(1) means: the number of basic steps stays the same whether the list
    has 10 items or 1,000,000 items. (Think of Laravel's $array[0] - instant.)

Input example:
    sizes = [10, 1000, 100000]; for each size build [0, 1, ..., size-1]

Expected output:
    n = 10
      first element = 0, steps = 1
      swap ends: now 9 ... 0, steps = 3
      formula sum = 55, steps = 3
      loop sum    = 55, steps = 10
    n = 1000
      first element = 0, steps = 1
      swap ends: now 999 ... 0, steps = 3
      formula sum = 500500, steps = 3
      loop sum    = 500500, steps = 1000
    n = 100000
      first element = 0, steps = 1
      swap ends: now 99999 ... 0, steps = 3
      formula sum = 5000050000, steps = 3
      loop sum    = 5000050000, steps = 100000
    is_even(7): (False, 2)
    get_first_element([]): (None, 1)

Approach:
    Each function performs a fixed number of basic operations and returns the
    result together with the number of steps it used.

Step-by-step logic:
    1. get_first_element reads index 0 -> 1 step.
    2. is_even does one modulo and one comparison -> 2 steps.
    3. swap_first_and_last does 3 assignments -> 3 steps.
    4. sum_to_n_formula uses n * (n + 1) // 2 -> 3 steps (no loop).
    5. sum_to_n_loop is shown for contrast: it needs n steps -> O(n).

Why it works:
    Indexing a Python list is direct memory access, and arithmetic on a number
    takes the same time regardless of how many items surround it.

Time complexity:
    O(1) for the first four functions (the loop version is O(n)).

Space complexity:
    O(1) - only a few variables are used.

Edge cases:
    - Empty list: get_first_element must not crash (returns None).
    - Single element list: swap does nothing visible.
    - n = 0 for the sum formulas gives 0.

Alternative approach:
    sum_to_n_loop adds numbers one by one; it is correct but O(n).
"""


def get_first_element(items):
    """Return (first item or None, steps)."""
    if len(items) == 0:  # len() on a list is O(1) in Python
        return None, 1
    return items[0], 1


def is_even(number):
    """Return (True/False, steps)."""
    return number % 2 == 0, 2


def swap_first_and_last(items):
    """Swap first and last items in place. Return steps used."""
    if len(items) < 2:
        return 0
    temp = items[0]
    items[0] = items[-1]
    items[-1] = temp
    return 3


def sum_to_n_formula(n):
    """Gauss formula: no loop, so constant time."""
    return n * (n + 1) // 2, 3


def sum_to_n_loop(n):
    """Loop version for comparison: one step per number -> O(n)."""
    total = 0
    steps = 0
    for value in range(1, n + 1):
        total += value
        steps += 1
    return total, steps


def main():
    for size in [10, 1000, 100000]:
        data = list(range(size))
        first, first_steps = get_first_element(data)
        swap_steps = swap_first_and_last(data)
        formula_total, formula_steps = sum_to_n_formula(size)
        loop_total, loop_steps = sum_to_n_loop(size)
        print(f"n = {size}")
        print(f"  first element = {first}, steps = {first_steps}")
        print(f"  swap ends: now {data[0]} ... {data[-1]}, steps = {swap_steps}")
        print(f"  formula sum = {formula_total}, steps = {formula_steps}")
        print(f"  loop sum    = {loop_total}, steps = {loop_steps}")
    print("is_even(7):", is_even(7))
    print("get_first_element([]):", get_first_element([]))


if __name__ == "__main__":
    main()
