"""
Problem title:
    Why Only Value/Weight Works (Counterexamples)

Problem statement:
    Implement the greedy fill with three different ordering rules: highest
    ratio, lowest weight, and highest value. Run them on the same inputs and
    show that only the ratio rule is always optimal.

What it teaches:
    - A greedy algorithm needs the RIGHT greedy choice.
    - How to find a counterexample that disproves a wrong rule.
    - Reusing one fill routine with a different ordering key.

Input example:
    Case 1: weights = [1, 10], values = [1, 100], capacity = 10
    Case 2: weights = [10, 1, 1], values = [20, 15, 15], capacity = 10
    Case 3: classic [10, 20, 30] / [60, 100, 120], capacity = 50

Expected output:
    Case 1: capacity 10, weights [1, 10], values [1, 100]
       by ratio  ->  100.00  optimal
       by weight ->   91.00  WORSE
       by value  ->  100.00  optimal
    Case 2: capacity 10, weights [10, 1, 1], values [20, 15, 15]
       by ratio  ->   46.00  optimal
       by weight ->   46.00  optimal
       by value  ->   20.00  WORSE
    Case 3: capacity 50, weights [10, 20, 30], values [60, 100, 120]
       by ratio  ->  240.00  optimal
       by weight ->  240.00  optimal
       by value  ->  220.00  WORSE

Approach:
    Write fill(order, ...) that takes items in a given order. Build the order
    with a selection pass using a "score" for each rule, then compare totals.

Step-by-step logic:
    1. score for "ratio" = value / weight; for "weight" = -weight (smaller
       weight is better); for "value" = value.
    2. Order items by score, highest first (selection pass).
    3. Fill the bag in that order, taking a fraction of the last item.
    4. Print the three totals and mark the best one.

Why it works:
    The ratio rule maximises value per unit of capacity. The other rules
    optimise something else, so there are inputs where they waste capacity on
    items with poor value density.

Time complexity:
    O(n^2) per rule (selection pass), O(n) fill.

Space complexity:
    O(n).

Edge cases:
    - Inputs where a wrong rule agrees with the ratio rule prove nothing
      (case 3: lowest weight happens to match).
    - Ties between rules.

Alternative approach:
    Exhaustively try every ordering (problem 10) to confirm which rule wins.
"""


def order_by_score(scores):
    """Return indexes ordered by score, highest first (selection pass)."""
    used = [False] * len(scores)
    order = []
    for _ in range(len(scores)):
        best = -1
        for index in range(len(scores)):
            if not used[index] and (best == -1 or scores[index] > scores[best]):
                best = index
        used[best] = True
        order.append(best)
    return order


def fill(order, weights, values, capacity):
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


def scores_for(rule, weights, values):
    scores = []
    for index in range(len(weights)):
        if rule == "ratio":
            scores.append(values[index] / weights[index])
        elif rule == "weight":
            scores.append(-weights[index])
        else:
            scores.append(values[index])
    return scores


def compare_rules(weights, values, capacity):
    results = {}
    for rule in ("ratio", "weight", "value"):
        order = order_by_score(scores_for(rule, weights, values))
        results[rule] = fill(order, weights, values, capacity)
    return results


def main():
    cases = [
        ("Case 1", [1, 10], [1, 100], 10),
        ("Case 2", [10, 1, 1], [20, 15, 15], 10),
        ("Case 3", [10, 20, 30], [60, 100, 120], 50),
    ]
    for label, weights, values, capacity in cases:
        results = compare_rules(weights, values, capacity)
        print("{}: capacity {}, weights {}, values {}".format(
            label, capacity, weights, values))
        for rule in ("ratio", "weight", "value"):
            verdict = "optimal" if results[rule] == results["ratio"] else "WORSE"
            print("   by {:<7}-> {:>7.2f}  {}".format(rule, results[rule], verdict))


if __name__ == "__main__":
    main()
