"""
Problem title:
    Exact Answers with fractions.Fraction

Problem statement:
    Solve fractional knapsack without floating-point rounding errors. Return
    the total value and the fraction taken of each item as exact rational
    numbers (for example 2/3, not 0.6666666666666666).

What it teaches:
    - Why floats can print values like 239.99999999999997.
    - Using fractions.Fraction (standard library) for exact arithmetic.
    - Comparing ratios exactly, so ties are detected correctly.

Input example:
    weights = [10, 20, 30], values = [60, 100, 120], capacity = 50
    plus a rounding demo: weights = [3, 7], values = [1, 1], capacity = 5

Expected output:
    exact total   : 240
    exact fractions: ['1', '1', '2/3']
    rounding demo : 9/7 ['1', '2/7']
    odd fractions : 19/3 = 6.333333333333333 ['1', '1/3']
    float 0.1 + 0.2 = 0.30000000000000004 | exact: 3/10

Approach:
    Same greedy algorithm as problem 01, but every ratio, fraction and total
    is a Fraction object.

Step-by-step logic:
    1. ratio = Fraction(value, weight) for each item.
    2. Order by ratio, highest first (insertion sort).
    3. Take whole items while they fit; for the last one take
       Fraction(remaining, weight).
    4. total += value * fraction.

Why it works:
    Fraction stores numerator and denominator as integers, so additions and
    multiplications are exact; the greedy argument itself is unchanged.

Time complexity:
    O(n^2) comparisons with the insertion sort. Each Fraction operation costs
    more than a float operation (it reduces by gcd), but the count of
    operations is still O(n^2).

Space complexity:
    O(n).

Edge cases:
    - Value exactly an integer (prints as e.g. 240, not 240.0).
    - Capacity 0.
    - Equal ratios compared exactly.

Alternative approach:
    Use floats and round the final answer, acceptable for quick estimates but
    not when exact comparison is needed.
"""
from fractions import Fraction


def fractional_knapsack_exact(weights, values, capacity):
    items = []
    for index in range(len(weights)):
        items.append((Fraction(values[index], weights[index]), index))

    for i in range(1, len(items)):  # insertion sort, highest ratio first
        current = items[i]
        j = i - 1
        while j >= 0 and items[j][0] < current[0]:
            items[j + 1] = items[j]
            j -= 1
        items[j + 1] = current

    total = Fraction(0)
    fractions = [Fraction(0)] * len(weights)
    remaining = Fraction(capacity)
    for ratio, index in items:
        if remaining <= 0:
            break
        if weights[index] <= remaining:
            fractions[index] = Fraction(1)
            total += values[index]
            remaining -= weights[index]
        else:
            fractions[index] = remaining / weights[index]
            total += values[index] * fractions[index]
            remaining = Fraction(0)
    return total, fractions


def main():
    total, fractions = fractional_knapsack_exact([10, 20, 30], [60, 100, 120], 50)
    print("exact total   :", total)
    print("exact fractions:", [str(f) for f in fractions])

    total, fractions = fractional_knapsack_exact([3, 7], [1, 1], 5)
    print("rounding demo :", total, [str(f) for f in fractions])

    total, fractions = fractional_knapsack_exact([7, 9], [5, 4], 10)
    print("odd fractions :", total, "=", float(total), [str(f) for f in fractions])

    float_sum = 0.1 + 0.2
    print("float 0.1 + 0.2 =", float_sum, "| exact:", Fraction(1, 10) + Fraction(2, 10))


if __name__ == "__main__":
    main()
