"""
Problem title:
    Verify Greedy Optimality by Brute Force

Problem statement:
    Check the greedy algorithm on many seeded random inputs against two
    independent references: (a) the best result over EVERY possible item
    order (brute force), and (b) the 0/1 knapsack dynamic programming answer,
    which must never exceed the fractional answer.

What it teaches:
    - Testing a greedy algorithm instead of just trusting it.
    - Generating all permutations by hand (recursive backtracking).
    - Floating-point comparison with a small tolerance.

Input example:
    300 random cases with 1-6 items, weights 1-10, values 1-50, capacity 1-25
    (random.seed(42))

Expected output:
    cases checked                  : 300
    greedy == best over all orders : True for every case
    fractional >= 0/1 knapsack     : True for every case
    cases where fractional > 0/1   : 177

Approach:
    For each random case compute the greedy value, the maximum fill value
    over all permutations of the items, and the 0/1 DP value. Compare them.

Step-by-step logic:
    1. greedy: order by ratio (insertion sort) and fill.
    2. brute force: generate every permutation recursively; fill the bag in
       that order; keep the largest total.
    3. 0/1 DP: classic one-dimensional table.
    4. Assert greedy == brute force (within 1e-9) and greedy >= 0/1 value.

Why it works:
    Some item order always reproduces an optimal solution (take items in that
    order until full), so the best over all orders is the true optimum. If
    the greedy order always matches it, the greedy rule is confirmed.

Time complexity:
    O(n! * n) per case for the brute force (n <= 6 keeps it small); greedy is
    O(n^2) with the insertion sort; the DP is O(n * capacity).

Space complexity:
    O(n) recursion depth for the permutations, O(capacity) for the DP table.

Edge cases:
    - Ties in ratio make several orders optimal (the totals still match).
    - Capacity bigger than total weight.
    - A single item.

Alternative approach:
    A formal proof by the exchange argument; testing only gives evidence, the
    proof gives certainty.
"""
import random


def fill_in_order(order, weights, values, capacity):
    total = 0.0
    remaining = capacity
    for index in order:
        if remaining <= 0:
            break
        if weights[index] <= remaining:
            total += values[index]
            remaining -= weights[index]
        else:
            total += values[index] * remaining / weights[index]
            remaining = 0
    return total


def greedy_value(weights, values, capacity):
    order = list(range(len(weights)))
    for i in range(1, len(order)):  # insertion sort by ratio, highest first
        current = order[i]
        j = i - 1
        while j >= 0 and (values[order[j]] / weights[order[j]]
                          < values[current] / weights[current]):
            order[j + 1] = order[j]
            j -= 1
        order[j + 1] = current
    return fill_in_order(order, weights, values, capacity)


def best_over_all_orders(weights, values, capacity):
    best = [0.0]

    def permute(order, used):
        if len(order) == len(weights):
            value = fill_in_order(order, weights, values, capacity)
            if value > best[0]:
                best[0] = value
            return
        for index in range(len(weights)):
            if not used[index]:
                used[index] = True
                order.append(index)
                permute(order, used)
                order.pop()  # backtrack
                used[index] = False

    permute([], [False] * len(weights))
    return best[0]


def knapsack_01(weights, values, capacity):
    table = [0] * (capacity + 1)
    for i in range(len(weights)):
        for w in range(capacity, weights[i] - 1, -1):
            if table[w - weights[i]] + values[i] > table[w]:
                table[w] = table[w - weights[i]] + values[i]
    return table[capacity]


def main():
    random.seed(42)
    cases = 300
    strictly_better = 0
    for _ in range(cases):
        n = random.randint(1, 6)
        weights = [random.randint(1, 10) for _ in range(n)]
        values = [random.randint(1, 50) for _ in range(n)]
        capacity = random.randint(1, 25)

        greedy = greedy_value(weights, values, capacity)
        brute = best_over_all_orders(weights, values, capacity)
        zero_one = knapsack_01(weights, values, capacity)

        assert abs(greedy - brute) < 1e-9, (weights, values, capacity)
        assert greedy + 1e-9 >= zero_one, (weights, values, capacity)
        if greedy > zero_one + 1e-9:
            strictly_better += 1

    print("cases checked                  :", cases)
    print("greedy == best over all orders : True for every case")
    print("fractional >= 0/1 knapsack     : True for every case")
    print("cases where fractional > 0/1   :", strictly_better)


if __name__ == "__main__":
    main()
