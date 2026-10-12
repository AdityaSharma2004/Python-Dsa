r"""
Problem title: Analysing Nested Loops

Problem statement:
    Five loop patterns are given. For each one, count how many times the inner
    body runs for several values of n, and match the count to a formula / Big O.

What it teaches:
    How to read loop code and derive complexity:
      - two independent loops one after another  -> n + n      -> O(n)
      - loop inside loop                         -> n * n      -> O(n^2)
      - inner loop starts at i (triangle)        -> n(n+1)/2   -> O(n^2)
      - inner variable doubles                   -> n * log n  -> O(n log n)
      - three nested loops                       -> n^3        -> O(n^3)

Input example:
    n = 4, 8, 16

Expected output:
      n   seq  nested  triangle  doubling  triple
      4     8      16        10         8      64
      8    16      64        36        24     512
     16    32     256       136        64    4096
    formulas for n = 8:
      2n         = 16
      n*n        = 64
      n(n+1)/2   = 36
      n*log2(n)  = 24
      n^3        = 512
    n = 0 -> 0 0

Approach:
    Each pattern is a function returning how many times its innermost statement
    executed. We print the counts next to the predicted formula value.

Step-by-step logic:
    1. Write the loops exactly as in the pattern.
    2. Increase a counter in the innermost statement.
    3. Compare the counter with the formula.

Why it works:
    Big O counts how many times the innermost statement runs. Sequential loops
    ADD their costs; nested loops MULTIPLY their costs.

Time complexity:
    The analysis functions themselves cost as much as the loop they measure
    (up to O(n^3) for the cubic one, so keep n small).

Space complexity:
    O(1).

Edge cases:
    - n = 0 gives 0 for every pattern.
    - Inner loop that doubles needs start value >= 1 (starting at 0 never ends).
    - Drop constants: 2n and n + 5 are both O(n).

Alternative approach:
    Solve the counting with summation formulas (e.g. 1 + 2 + ... + n).
"""


def sequential_loops(n):
    count = 0
    for _ in range(n):
        count += 1
    for _ in range(n):
        count += 1
    return count  # 2n


def nested_loops(n):
    count = 0
    for _ in range(n):
        for _ in range(n):
            count += 1
    return count  # n * n


def triangle_loops(n):
    count = 0
    for i in range(n):
        for _ in range(i, n):  # inner length shrinks: n, n-1, ..., 1
            count += 1
    return count  # n(n+1)/2


def doubling_inner_loop(n):
    count = 0
    for _ in range(n):
        step = 1
        while step < n:
            count += 1
            step *= 2  # doubles each time -> about log2(n) iterations
    return count  # n * ceil(log2 n)


def triple_loops(n):
    count = 0
    for _ in range(n):
        for _ in range(n):
            for _ in range(n):
                count += 1
    return count  # n^3


def main():
    print(f"{'n':>3} {'seq':>5} {'nested':>7} {'triangle':>9} {'doubling':>9} {'triple':>7}")
    for n in [4, 8, 16]:
        print(f"{n:>3} {sequential_loops(n):>5} {nested_loops(n):>7} "
              f"{triangle_loops(n):>9} {doubling_inner_loop(n):>9} {triple_loops(n):>7}")
    n = 8
    print("formulas for n = 8:")
    print("  2n         =", 2 * n)
    print("  n*n        =", n * n)
    print("  n(n+1)/2   =", n * (n + 1) // 2)
    print("  n*log2(n)  =", n * 3)
    print("  n^3        =", n ** 3)
    print("n = 0 ->", nested_loops(0), triangle_loops(0))


if __name__ == "__main__":
    main()
