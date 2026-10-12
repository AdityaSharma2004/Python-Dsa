"""
Problem Title: Fast Power (Exponentiation by Squaring)

Problem Statement:
    Compute base ** exp for a non-negative integer exponent using O(log exp)
    multiplications instead of exp multiplications. Also support a modulus
    (compute base ** exp % mod without huge numbers) and negative exponents
    for float results.

What It Teaches:
    - Divide and conquer where one half-result is reused (square it).
    - Why "compute half once" matters: calling power twice would be O(n).
    - Modular exponentiation, used in hashing and cryptography.

Input Example:
    2 ** 10, 3 ** 13, 2 ** -3, 7 ** 128 mod 13

Expected Output:
    2 ** 10      = 1024
    3 ** 13      = 1594323
    2 ** -3      = 0.125
    0 ** 0       = 1
    7 ** 128 % 13 = 3
    Recursive, iterative and naive results agree.

Approach:
    x^n = (x^(n/2))^2            when n is even
    x^n = x * (x^((n-1)/2))^2    when n is odd
    x^0 = 1

Step-by-Step Logic:
    1. Base case: exp == 0 -> 1.
    2. half = power(base, exp // 2) computed ONCE.
    3. result = half * half; if exp is odd multiply by base once more.
    4. For modulus, reduce after every multiplication.

Why It Works:
    Exponent laws: x^(2k) = (x^k)^2 and x^(2k+1) = x * (x^k)^2. The exponent
    halves each call, so only about log2(exp) levels exist.

Time Complexity:
    O(log exp) multiplications.
Space Complexity:
    O(log exp) recursion stack (iterative version O(1)).

Edge Cases:
    exp = 0 -> 1 (even for base 0), base = 0, base = 1, negative exponent
    (use 1 / power(base, -exp)), mod = 1 -> 0.

Alternative Approach:
    The naive loop multiplies base exp times: O(exp). The iterative binary
    exponentiation version (also shown) walks the bits of the exponent.
"""


def fast_power(base, exp, mod=None):
    """Recursive exponentiation by squaring (exp >= 0)."""
    if exp == 0:
        return 1 if mod is None else 1 % mod
    half = fast_power(base, exp // 2, mod)  # compute the half ONCE
    result = half * half
    if exp % 2 == 1:
        result *= base
    return result if mod is None else result % mod


def power_with_negative(base, exp):
    """Support negative exponents: x^-n = 1 / x^n."""
    if exp < 0:
        return 1 / fast_power(base, -exp)
    return fast_power(base, exp)


def fast_power_iterative(base, exp, mod=None):
    """Bit-by-bit version: square the base, multiply when the bit is 1."""
    result = 1
    while exp > 0:
        if exp & 1:
            result = result * base if mod is None else (result * base) % mod
        base = base * base if mod is None else (base * base) % mod
        exp >>= 1
    return result if mod is None else result % mod


def naive_power(base, exp):
    """O(exp) loop for comparison."""
    result = 1
    for _ in range(exp):
        result *= base
    return result


def main():
    print("2 ** 10      =", fast_power(2, 10))
    print("3 ** 13      =", fast_power(3, 13))
    print("2 ** -3      =", power_with_negative(2, -3))
    print("0 ** 0       =", fast_power(0, 0))
    print("7 ** 128 % 13 =", fast_power(7, 128, 13))
    for base, exp in [(2, 30), (5, 17), (9, 0), (1, 99)]:
        assert fast_power(base, exp) == naive_power(base, exp)
        assert fast_power_iterative(base, exp) == base ** exp
    assert fast_power(7, 128, 13) == pow(7, 128, 13)  # verification only
    print("Recursive, iterative and naive results agree.")


if __name__ == "__main__":
    main()
