"""
Problem title:
    Power Calculation x^n (Linear vs Fast Exponentiation)

Problem statement:
    Compute x raised to the integer power n using recursion, without
    using ** or pow(). Support negative n.

What it teaches:
    How halving the problem (x^n = (x^(n/2))^2) reduces the number of calls
    from n to log n.

Input example:
    x = 2, n = 10

Expected output:
    2^10 simple: 1024 calls: 11
    2^10 fast: 1024 calls: 5
    3^0 = 1
    2^-3 = 0.125
    (-2)^5 = -32
    2^30 = 1073741824
    Error: 0 cannot be raised to a negative power

Approach:
    Simple: power(x, n) = x * power(x, n - 1).
    Fast: compute half = power(x, n // 2); square it; multiply by x if n is odd.

Step-by-step logic:
    1. n == 0 -> 1 (base case).
    2. Negative n: compute 1 / power(x, -n).
    3. Fast version: half = power_fast(x, n // 2).
    4. If n is even result = half * half, else half * half * x.

Why it works:
    x^n = x^(n/2) * x^(n/2) for even n, and an extra factor x for odd n.
    Each call halves n, so only about log2(n) calls are needed.

Time complexity:
    Simple: O(n). Fast: O(log n).

Space complexity:
    Simple: O(n) stack. Fast: O(log n) stack.

Edge cases:
    n = 0 -> 1, n = 1, negative n, x = 0 with negative n (error), x negative.

Alternative approach:
    Iterative binary exponentiation using the bits of n (O(1) space).
"""


def power_simple(x, n, counter):
    """n multiplications; counter[0] counts calls."""
    counter[0] += 1
    if n == 0:
        return 1
    return x * power_simple(x, n - 1, counter)


def power_fast(x, n, counter):
    """Exponentiation by squaring (n >= 0)."""
    counter[0] += 1
    if n == 0:
        return 1
    half = power_fast(x, n // 2, counter)  # computed once and reused
    if n % 2 == 0:
        return half * half
    return half * half * x


def power(x, n):
    """Public wrapper that supports negative exponents."""
    if n < 0:
        if x == 0:
            raise ZeroDivisionError("0 cannot be raised to a negative power")
        return 1 / power_fast(x, -n, [0])
    return power_fast(x, n, [0])


def main():
    simple_calls, fast_calls = [0], [0]
    print("2^10 simple:", power_simple(2, 10, simple_calls),
          "calls:", simple_calls[0])
    print("2^10 fast:", power_fast(2, 10, fast_calls), "calls:", fast_calls[0])
    print("3^0 =", power(3, 0))
    print("2^-3 =", power(2, -3))
    print("(-2)^5 =", power(-2, 5))
    print("2^30 =", power(2, 30))
    try:
        power(0, -1)
    except ZeroDivisionError as error:
        print("Error:", error)


if __name__ == "__main__":
    main()
