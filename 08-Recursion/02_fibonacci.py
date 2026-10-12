"""
Problem title:
    Fibonacci Numbers (Naive vs Memoized Recursion)

Problem statement:
    Return the n-th Fibonacci number where F(0) = 0, F(1) = 1 and
    F(n) = F(n-1) + F(n-2).

What it teaches:
    Multiple recursive calls per level (a recursion tree), overlapping
    subproblems, and how caching (memoization) turns exponential into linear.

Input example:
    n = 10

Expected output:
    n=10: naive=55 (177 calls), memo=55 (19 calls), loop=55
    n=20: naive=6765 (21891 calls), memo=6765 (39 calls), loop=6765
    First 10 numbers: [0, 1, 1, 2, 3, 5, 8, 13, 21, 34]
    fib(50) with memo: 12586269025

Approach:
    Simple: fib(n) = fib(n-1) + fib(n-2).
    Improved: store each computed value in a dictionary and reuse it.

Step-by-step logic:
    1. Base cases: n = 0 -> 0, n = 1 -> 1.
    2. Naive: call fib(n-1) and fib(n-2) and add them.
    3. Memoized: before computing, look n up in the cache; after computing,
       save it. Each value is then computed only once.

Why it works:
    The naive tree recomputes the same values many times (fib(2) appears
    again and again). The cache removes this repeated work.

Time complexity:
    Naive: O(2^n). Memoized: O(n).

Space complexity:
    Naive: O(n) call stack depth. Memoized: O(n) for cache plus O(n) stack.

Edge cases:
    n = 0, n = 1, negative n (ValueError), large n with naive version is slow.

Alternative approach:
    Bottom-up loop keeping only the last two values: O(n) time, O(1) space.
"""


def fib_naive(n, counter):
    """Naive recursion; counter[0] counts how many calls were made."""
    counter[0] += 1
    if n < 0:
        raise ValueError("n must be non-negative")
    if n < 2:
        return n
    return fib_naive(n - 1, counter) + fib_naive(n - 2, counter)


def fib_memo(n, cache, counter):
    """Recursion with a dictionary cache."""
    counter[0] += 1
    if n < 0:
        raise ValueError("n must be non-negative")
    if n < 2:
        return n
    if n in cache:  # already solved -> reuse
        return cache[n]
    cache[n] = fib_memo(n - 1, cache, counter) + fib_memo(n - 2, cache, counter)
    return cache[n]


def fib_iterative(n):
    """Bottom-up version using two variables."""
    previous, current = 0, 1
    for _ in range(n):
        previous, current = current, previous + current
    return previous


def main():
    for n in (10, 20):
        naive_calls, memo_calls = [0], [0]
        a = fib_naive(n, naive_calls)
        b = fib_memo(n, {}, memo_calls)
        print(f"n={n}: naive={a} ({naive_calls[0]} calls), "
              f"memo={b} ({memo_calls[0]} calls), loop={fib_iterative(n)}")
    print("First 10 numbers:", [fib_iterative(i) for i in range(10)])
    print("fib(50) with memo:", fib_memo(50, {}, [0]))


if __name__ == "__main__":
    main()
