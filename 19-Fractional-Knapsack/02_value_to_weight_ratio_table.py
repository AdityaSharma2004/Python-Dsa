"""
Problem title:
    Value-to-Weight Ratio Table and Ranking

Problem statement:
    For a list of named items with weight and value, compute each item's
    value density (value per unit weight) and print a table ranked from best
    to worst. The first item in the ranking is the one the greedy algorithm
    will take first.

What it teaches:
    - The ratio value / weight is the key quantity of the problem.
    - Ranking records without sorted() by using a selection-style pass.
    - Why a big value alone does not make an item the best choice.

Input example:
    spice shop: saffron (w=2, v=300), pepper (w=10, v=50), cardamom (w=5,
    v=100), salt (w=20, v=20), rice (w=50, v=400)

Expected output:
    rank item       weight  value   ratio
    1    saffron         2    300  150.00
    2    cardamom        5    100   20.00
    3    rice           50    400    8.00
    4    pepper         10     50    5.00
    5    salt           20     20    1.00
    highest value item: rice | best ratio item: saffron

Approach:
    Compute the ratio for each item, then repeatedly pick the unranked item
    with the largest ratio (selection ranking) and append it to the ranking.

Step-by-step logic:
    1. ratio = value / weight for every item.
    2. Keep a "used" flag per item.
    3. For rank 1..n: scan all unused items, remember the one with the
       largest ratio, mark it used and print its row.

Why it works:
    Each pass finds the best remaining item, so after n passes the items
    appear in non-increasing order of ratio.

Time complexity:
    O(n^2): n passes, each scanning up to n items.

Space complexity:
    O(n) for the ratios and the used flags.

Edge cases:
    - Ties in ratio (the earlier item keeps the better rank).
    - A heavy item with a huge value but a poor ratio ranks low.
    - A single item.

Alternative approach:
    Use a proper O(n log n) sort (merge sort / quick sort) once the sorting
    topics have been practised.
"""


def compute_ratios(items):
    """items: list of (name, weight, value). Return list of ratios."""
    ratios = []
    for name, weight, value in items:
        ratios.append(value / weight)
    return ratios


def rank_by_ratio(items):
    """Return item indexes ordered from highest to lowest ratio."""
    ratios = compute_ratios(items)
    used = [False] * len(items)
    ranking = []
    for _ in range(len(items)):
        best = -1
        for index in range(len(items)):
            if used[index]:
                continue
            if best == -1 or ratios[index] > ratios[best]:
                best = index
        used[best] = True
        ranking.append(best)
    return ranking, ratios


def main():
    items = [("saffron", 2, 300), ("pepper", 10, 50),
             ("cardamom", 5, 100), ("salt", 20, 20), ("rice", 50, 400)]
    ranking, ratios = rank_by_ratio(items)
    print("{:<5}{:<10}{:>7}{:>7}{:>8}".format("rank", "item", "weight", "value", "ratio"))
    for position, index in enumerate(ranking, start=1):
        name, weight, value = items[index]
        print("{:<5}{:<10}{:>7}{:>7}{:>8.2f}".format(
            position, name, weight, value, ratios[index]))
    biggest_value_item = items[0]
    for item in items:
        if item[2] > biggest_value_item[2]:
            biggest_value_item = item
    print("highest value item:", biggest_value_item[0],
          "| best ratio item:", items[ranking[0]][0])


if __name__ == "__main__":
    main()
