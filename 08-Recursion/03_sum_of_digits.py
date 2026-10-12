"""
Problem title:
    Sum of Digits and Digital Root

Problem statement:
    Given a non-negative integer, return the sum of its digits using
    recursion. Then repeat until a single digit remains (digital root).

What it teaches:
    Shrinking a number with // 10 and % 10, and recursion that does a small
    piece of work and delegates the rest.

Input example:
    n = 9875

Expected output:
    n=0: sum=0, root=0, formula=0
    n=7: sum=7, root=7, formula=7
    n=1001: sum=2, root=2, formula=2
    n=9875: sum=29, root=2, formula=2
    n=123456789: sum=45, root=9, formula=9
    Error: n must be non-negative

Approach:
    sum_digits(n) = (n % 10) + sum_digits(n // 10), base case n < 10 -> n.

Step-by-step logic:
    1. If n is a single digit, return it.
    2. n % 10 is the last digit; n // 10 removes it.
    3. Add the last digit to the recursive result of the rest.
    4. Digital root: call sum_digits again until result < 10.

Why it works:
    Each call removes exactly one digit, so the number reaches a single
    digit (base case) after as many calls as it has digits.

Time complexity:
    O(d) where d = number of digits (d ~ log10 n).

Space complexity:
    O(d) recursion stack.

Edge cases:
    n = 0 -> 0; single digit; numbers with zeros (1001); negative (error).

Alternative approach:
    Convert to a string and add the characters, or loop with divmod; the
    digital root also equals 1 + (n - 1) % 9 for n > 0 (a math shortcut).
"""


def sum_digits(n):
    """Recursive sum of digits."""
    if n < 0:
        raise ValueError("n must be non-negative")
    if n < 10:  # base case: one digit
        return n
    return n % 10 + sum_digits(n // 10)


def digital_root(n):
    """Keep summing digits until one digit remains."""
    if n < 10:
        return n
    return digital_root(sum_digits(n))


def digital_root_formula(n):
    """Constant-time check of the digital root."""
    return 0 if n == 0 else 1 + (n - 1) % 9


def main():
    for n in (0, 7, 1001, 9875, 123456789):
        print(f"n={n}: sum={sum_digits(n)}, root={digital_root(n)}, "
              f"formula={digital_root_formula(n)}")
    try:
        sum_digits(-5)
    except ValueError as error:
        print("Error:", error)


if __name__ == "__main__":
    main()
