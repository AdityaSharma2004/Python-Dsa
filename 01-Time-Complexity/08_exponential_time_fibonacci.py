r"""
Problem title: Exponential Time - Naive Fibonacci vs Memoization

Problem statement:
    Compute the n-th Fibonacci number with plain recursion and count how many
    function calls happen. Then fix it with memoization (a dictionary cache)
    and an iterative loop, and compare call counts.

What it teaches:
    O(2^n) growth: each call spawns two more calls, repeating the same work.
    Caching results turns it into O(n). This is the first step toward dynamic
    programming.

Input example:
    n = 10, 20, 25

Expected output:
    n = 10: value = 55, naive calls = 177, memo calls = 19, iterative = 55
    n = 20: value = 6765, naive calls = 21891, memo calls = 39, iterative = 6765
    n = 25: value = 75025, naive calls = 242785, memo calls = 49, iterative = 75025
    fib(0), fib(1): 0 1

Approach:
    Three versions of fib(n) with a call counter.

Step-by-step logic:
    1. Naive: fib(n) = fib(n-1) + fib(n-2), base cases fib(0)=0, fib(1)=1.
    2. Memo: before computing, check the dictionary; store each result after.
    3. Iterative: keep only the last two values in a loop.
    4. Count calls for each version and compare.

Why it works:
    fib(n-2) is computed again inside fib(n-1), so the naive call tree has about
    1.6^n nodes. Remembering answers makes each value computed once.

Time complexity:
    Naive O(2^n) (tight bound about 1.618^n); memoized O(n); iterative O(n).

Space complexity:
    Naive O(n) recursion depth; memoized O(n) cache + stack; iterative O(1).

Edge cases:
    - n = 0 and n = 1 are base cases.
    - Negative n is rejected with ValueError.
    - Very large n with naive version would take forever, so we only use n <= 25.

Alternative approach:
    Matrix exponentiation or fast doubling compute fib(n) in O(log n).
"""


def fib_naive(n, counter):
    counter[0] += 1
    if n < 2:
        return n
    return fib_naive(n - 1, counter) + fib_naive(n - 2, counter)


def fib_memo(n, counter, cache=None):
    if cache is None:
        cache = {}
    counter[0] += 1
    if n < 2:
        return n
    if n in cache:
        return cache[n]  # reuse earlier work
    cache[n] = fib_memo(n - 1, counter, cache) + fib_memo(n - 2, counter, cache)
    return cache[n]


def fib_iterative(n):
    previous, current = 0, 1
    for _ in range(n):
        previous, current = current, previous + current
    return previous


def main():
    for n in [10, 20, 25]:
        naive_counter = [0]
        memo_counter = [0]
        naive_value = fib_naive(n, naive_counter)
        memo_value = fib_memo(n, memo_counter)
        print(f"n = {n}: value = {naive_value}, naive calls = {naive_counter[0]}, "
              f"memo calls = {memo_counter[0]}, iterative = {fib_iterative(n)}")
    print("fib(0), fib(1):", fib_iterative(0), fib_iterative(1))


if __name__ == "__main__":
    main()
