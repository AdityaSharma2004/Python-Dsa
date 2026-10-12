"""
Problem Title: Climbing Stairs

Problem Statement:
    You can climb 1 or 2 steps at a time. In how many distinct ways can you
    reach step n? Then generalise: you may take any step size from a given list.

What It Teaches:
    - Turning a counting question into a recurrence: ways(n) = ways(n-1) + ways(n-2).
    - Bottom-up DP with a 1-D table.
    - Generalising the recurrence by looping over allowed step sizes.

Input Example:
    n = 5 with steps {1, 2};  n = 6 with steps {1, 3, 4}

Expected Output:
    Classic (1 or 2 steps):
      n=0: 1 ways
      n=1: 1 ways
      n=2: 2 ways
      n=3: 3 ways
      n=5: 8 ways
      n=10: 89 ways
    Steps {1, 3, 4}, table for 0..6: [1, 1, 1, 2, 4, 6, 9]
    Ways to reach step 6: 9
    Check classic vs general for n=10: True
    No allowed steps, n=3: 0

Approach:
    Let ways[i] be the number of ways to stand on step i. The last move into
    step i came from i-1 (a 1-step) or i-2 (a 2-step), so we add those counts.

Step-by-Step Logic:
    1. ways[0] = 1 (one way to stay on the ground: do nothing).
    2. For i from 1 to n: ways[i] = sum of ways[i - s] for each allowed step s <= i.
    3. The answer is ways[n].
    4. For {1, 2} only the last two values matter, so O(1) space is possible.

Why It Works:
    Every path to step i ends with exactly one final move, so the groups
    "last move was s" are disjoint and together cover every path.

Time Complexity:
    O(n * k) for k allowed step sizes (O(n) for the classic 1-or-2 version).
Space Complexity:
    O(n) for the table; O(1) for the two-variable version.

Edge Cases:
    n = 0 (1 way), n = 1, step sizes larger than n, an empty step list
    (0 ways for n > 0).

Alternative Approach:
    Plain recursion is O(2^n); the classic version is also Fibonacci in disguise.
"""


def climb_classic(n):
    """Ways to climb n steps taking 1 or 2 at a time, O(1) extra space."""
    previous, current = 1, 1  # ways[0], ways[1]
    for _ in range(n - 1):
        previous, current = current, previous + current
    return current if n >= 1 else 1


def climb_with_steps(n, steps):
    """Ways to reach step n using any step size from the list `steps`."""
    ways = [0] * (n + 1)
    ways[0] = 1
    for i in range(1, n + 1):
        for step in steps:
            if step <= i:
                ways[i] += ways[i - step]
    return ways


def main():
    print("Classic (1 or 2 steps):")
    for n in (0, 1, 2, 3, 5, 10):
        print(f"  n={n}: {climb_classic(n)} ways")
    table = climb_with_steps(6, [1, 3, 4])
    print("Steps {1, 3, 4}, table for 0..6:", table)
    print("Ways to reach step 6:", table[6])
    print("Check classic vs general for n=10:",
          climb_classic(10) == climb_with_steps(10, [1, 2])[10])
    print("No allowed steps, n=3:", climb_with_steps(3, [])[3])


if __name__ == "__main__":
    main()
