"""
Problem Title: Fibonacci with Memoization and Tabulation

Problem Statement:
    Compute the n-th Fibonacci number (F(0)=0, F(1)=1, F(n)=F(n-1)+F(n-2)).
    Show the slow plain recursion, then fix it with memoization (top-down DP),
    tabulation (bottom-up DP) and a space-optimised loop.

What It Teaches:
    - Overlapping subproblems: plain recursion solves the same F(k) again and again.
    - Memoization = recursion + a cache (like caching a DB query result in PHP).
    - Tabulation = fill a table from the smallest subproblem upward.
    - Reducing space when only the last two states matter.

Input Example:
    n = 10, then n = 30, then n = 90

Expected Output:
    n=10: naive=55 (177 calls), memo=55, table=55, optimised=55
    n=30: naive=832040 (2692537 calls), memo=832040, table=832040, optimised=832040
    n=90: memo=2880067194370816120, table=2880067194370816120, optimised=2880067194370816120
    Base cases: 0 1
    Error: n must be non-negative

Approach:
    Four versions of the same recurrence. Naive recursion counts its calls so
    you can SEE the waste. Memoization stores each answer in a dictionary.
    Tabulation fills table[0..n]. The optimised version keeps two variables.

Step-by-Step Logic:
    1. Base cases: F(0) = 0 and F(1) = 1.
    2. Naive: F(n) = F(n-1) + F(n-2), recomputing everything.
    3. Memo: before computing F(k) look in the cache; after computing, store it.
    4. Table: table[i] = table[i-1] + table[i-2] for i = 2..n.
    5. Optimised: keep only (previous, current) and slide them forward.

Why It Works:
    F(n) depends only on two smaller values, and each value F(k) is the same
    no matter who asks for it. Solving every k exactly once is enough.

Time Complexity:
    Naive O(2^n) (grows by about 1.6x per step); memoization, tabulation and
    optimised loop are all O(n).
Space Complexity:
    Naive O(n) call stack; memo O(n) cache + stack; table O(n); optimised O(1).

Edge Cases:
    n = 0 and n = 1 (base cases), negative n (rejected), large n (Python ints
    do not overflow, so F(90) is exact).

Alternative Approach:
    Matrix exponentiation or fast doubling computes F(n) in O(log n).
"""


def fib_naive(n, counter):
    """Plain recursion; counter[0] counts how many calls were made."""
    counter[0] += 1
    if n < 2:
        return n
    return fib_naive(n - 1, counter) + fib_naive(n - 2, counter)


def fib_memo(n, cache=None):
    """Top-down DP: recursion with a dictionary cache."""
    if n < 0:
        raise ValueError("n must be non-negative")
    if cache is None:
        cache = {}
    if n < 2:
        return n
    if n in cache:  # already solved -> reuse
        return cache[n]
    cache[n] = fib_memo(n - 1, cache) + fib_memo(n - 2, cache)
    return cache[n]


def fib_table(n):
    """Bottom-up DP: build a table from F(0) upward."""
    if n < 0:
        raise ValueError("n must be non-negative")
    if n < 2:
        return n
    table = [0] * (n + 1)
    table[1] = 1
    for i in range(2, n + 1):
        table[i] = table[i - 1] + table[i - 2]
    return table[n]


def fib_optimised(n):
    """Bottom-up DP keeping only the last two values."""
    if n < 0:
        raise ValueError("n must be non-negative")
    previous, current = 0, 1
    for _ in range(n):
        previous, current = current, previous + current
    return previous


def main():
    for n in (10, 30):
        counter = [0]
        naive = fib_naive(n, counter)
        print(f"n={n}: naive={naive} ({counter[0]} calls), memo={fib_memo(n)}, "
              f"table={fib_table(n)}, optimised={fib_optimised(n)}")
    n = 90
    print(f"n={n}: memo={fib_memo(n)}, table={fib_table(n)}, optimised={fib_optimised(n)}")
    print("Base cases:", fib_optimised(0), fib_optimised(1))
    try:
        fib_table(-1)
        fib_optimised(-1)
    except ValueError as error:
        print("Error:", error)


if __name__ == "__main__":
    main()
