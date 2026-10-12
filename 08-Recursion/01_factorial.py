"""
Problem title:
    Factorial Using Recursion

Problem statement:
    Given a non-negative integer n, compute n! = n * (n-1) * ... * 1 using
    recursion. By definition 0! = 1.

What it teaches:
    The two parts of every recursive function: the base case (when to stop)
    and the recursive case (how to shrink the problem). Also how the call
    stack grows and unwinds.

Input example:
    n = 5

Expected output:
    Tracing factorial(4):
    factorial(4) called
      factorial(3) called
        factorial(2) called
          factorial(1) called
          base case -> 1
        factorial(2) returns 2
      factorial(3) returns 6
    factorial(4) returns 24
    0! = 1 (iterative: 1)
    1! = 1 (iterative: 1)
    5! = 120 (iterative: 120)
    10! = 3628800 (iterative: 3628800)
    Error: factorial is not defined for negative numbers

Approach:
    factorial(n) = n * factorial(n - 1), with factorial(0) = 1.

Step-by-step logic:
    1. If n is 0 (or 1), return 1 -> base case.
    2. Otherwise ask factorial(n - 1) for the smaller answer.
    3. Multiply that answer by n and return it.
    4. Calls pile up on the call stack, then answers come back one by one.

Why it works:
    Each call solves a strictly smaller problem (n decreases by 1), so it must
    reach the base case, and multiplying on the way back gives n!.

Time complexity:
    O(n) - one call per value from n down to 0.

Space complexity:
    O(n) - the call stack holds n + 1 frames (the iterative version is O(1)).

Edge cases:
    n = 0 -> 1; n = 1 -> 1; negative n is invalid (raise ValueError);
    very large n hits Python's recursion limit (about 1000 frames).

Alternative approach:
    A simple loop multiplying 1..n uses O(1) extra space (shown below).
"""


def factorial(n):
    """Recursive factorial."""
    if n < 0:
        raise ValueError("factorial is not defined for negative numbers")
    if n <= 1:  # base case
        return 1
    return n * factorial(n - 1)  # recursive case


def factorial_trace(n, depth=0):
    """Same as factorial() but prints the call stack to visualise it."""
    indent = "  " * depth
    print(f"{indent}factorial({n}) called")
    if n <= 1:
        print(f"{indent}base case -> 1")
        return 1
    result = n * factorial_trace(n - 1, depth + 1)
    print(f"{indent}factorial({n}) returns {result}")
    return result


def factorial_iterative(n):
    """Loop version for comparison."""
    if n < 0:
        raise ValueError("factorial is not defined for negative numbers")
    result = 1
    for value in range(2, n + 1):
        result *= value
    return result


def main():
    print("Tracing factorial(4):")
    factorial_trace(4)
    for n in (0, 1, 5, 10):
        print(f"{n}! = {factorial(n)} (iterative: {factorial_iterative(n)})")
    try:
        factorial(-3)
    except ValueError as error:
        print("Error:", error)


if __name__ == "__main__":
    main()
