"""
Problem Title: Karatsuba Fast Multiplication

Problem Statement:
    Multiply two non-negative integers using Karatsuba's divide and conquer
    method, which needs only THREE recursive multiplications of half-sized
    numbers instead of four.

What It Teaches:
    - A clever combine step that reduces the number of subproblems.
    - Recurrence T(n) = 3T(n/2) + O(n) -> O(n^1.585).
    - Working with digits using divmod and powers of 10.

Input Example:
    1234 * 5678, 12 * 34, 99999 * 99999

Expected Output:
    1234 * 5678 = 7006652
    12 * 34 = 408
    99999 * 99999 = 9999800001
    0 * 777 = 0
    5 * 123456789 = 617283945
    100000000000000000000 * 1000000000000007 = 100000000000000700000000000000000000

Approach:
    Split x = a*10^m + b and y = c*10^m + d. Then
    x*y = ac*10^(2m) + ((a+b)(c+d) - ac - bd)*10^m + bd.
    The middle term needs only one extra multiplication (a+b)(c+d).

Step-by-Step Logic:
    1. If either number has a single digit, multiply directly (base case).
    2. m = half of the digit count of the larger number.
    3. Split both numbers with divmod(x, 10**m).
    4. ac = karatsuba(a, c); bd = karatsuba(b, d);
       cross = karatsuba(a + b, c + d) - ac - bd.
    5. Combine: ac * 10^(2m) + cross * 10^m + bd.

Why It Works:
    (a+b)(c+d) = ac + ad + bc + bd, so subtracting ac and bd leaves ad + bc,
    exactly the middle coefficient, using one multiplication instead of two.

Time Complexity:
    O(n^log2(3)) ~ O(n^1.585) for n-digit numbers (schoolbook is O(n^2)).
Space Complexity:
    O(n) for digits plus O(log n) recursion depth.

Edge Cases:
    Zero operands, single-digit operands, different lengths, numbers that are
    powers of ten, very large numbers.

Alternative Approach:
    Schoolbook multiplication (4 half-size products) is O(n^2). For
    practical sizes Python's own * already uses Karatsuba internally.
"""


def digit_count(number):
    """Number of decimal digits (0 has one digit)."""
    count = 1
    while number >= 10:
        number //= 10
        count += 1
    return count


def karatsuba(x, y):
    """Multiply non-negative integers x and y."""
    if x < 10 or y < 10:
        return x * y  # base case: single digit
    half = max_of_two(digit_count(x), digit_count(y)) // 2
    base = 10 ** half
    a, b = divmod(x, base)
    c, d = divmod(y, base)
    high = karatsuba(a, c)
    low = karatsuba(b, d)
    middle = karatsuba(a + b, c + d) - high - low
    return high * base * base + middle * base + low


def max_of_two(first, second):
    """Tiny helper (we avoid max() as a matter of style in this topic)."""
    return first if first > second else second


def main():
    pairs = [(1234, 5678), (12, 34), (99999, 99999), (0, 777), (5, 123456789),
             (10 ** 20, 10 ** 15 + 7)]
    for x, y in pairs:
        result = karatsuba(x, y)
        assert result == x * y  # verification only
        print(f"{x} * {y} = {result}")


if __name__ == "__main__":
    main()
