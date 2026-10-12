"""
Problem title:
    Minimum Coins / Notes with Greedy Choice (Indian Denominations)

Problem statement:
    Given a list of denominations and an amount, return the fewest
    coins/notes that add up to the amount by always taking the largest
    denomination that still fits. Show that this greedy rule works for the
    Indian system but FAILS for an arbitrary system such as [1, 3, 4].

What it teaches:
    * The greedy template: choose the best-looking option, commit, repeat.
    * Greedy is only correct when the problem has the greedy-choice property.
    * Always try to break a greedy idea with a counterexample.

Input example:
    denominations = [500, 200, 100, 50, 20, 10, 5, 2, 1], amount = 289
    denominations = [1, 3, 4], amount = 6

Expected output:
    Amount 289: [200, 50, 20, 10, 5, 2, 2] -> 7 coins
    Amount 93: [50, 20, 20, 2, 1] -> 5 coins
    Amount 0: [] -> 0 coins
    Impossible amount (coins [5, 10], amount 3): None

    Counterexample: denominations [1, 3, 4], amount 6
    Greedy answer : [4, 1, 1] -> 3 coins
    True optimum  : 2 coins (3 + 3)
    Greedy is wrong here, so we need Dynamic Programming.

Approach:
    Sort denominations from largest to smallest. For each denomination use
    divmod to take as many as fit, then continue with the remainder.

Step-by-step logic:
    1. Sort denominations in descending order (hand-written merge sort).
    2. For each denomination, count, remainder = divmod(remaining, coin).
    3. Record the coin `count` times and carry on with the remainder.
    4. Stop when the remainder is 0. If we run out of coins first, there
       is no exact change.

Why it works:
    For the Indian system each larger note is a multiple-friendly step above
    the smaller ones (1,2,5,10,20,50,...), so swapping smaller coins for the
    bigger coin never increases the count. For [1, 3, 4] that argument fails:
    taking 4 first for amount 6 leaves 2, which costs two 1-coins (3 coins),
    while 3 + 3 uses only 2 coins.

Time complexity:
    O(d log d) to sort d denominations + O(d) for the loop. The loop does not
    depend on the amount because divmod handles repeats in one step.

Space complexity:
    O(d) for the sorted copy and the result list.

Edge cases:
    * amount = 0 -> no coins needed.
    * Amount that cannot be formed (e.g. coins [5, 10], amount 3) -> None.
    * Negative amount -> ValueError.

Alternative approach:
    Dynamic programming (try every coin for every sub-amount) is always
    correct for any denominations but costs O(amount * d). It is included
    below only as a checker for the counterexample.
"""


def merge_sort(items, comes_first):
    """Stable merge sort; `comes_first(a, b)` is True when a must precede b."""
    if len(items) <= 1:
        return list(items)
    middle = len(items) // 2
    left = merge_sort(items[:middle], comes_first)
    right = merge_sort(items[middle:], comes_first)
    merged = []
    i = j = 0
    while i < len(left) and j < len(right):
        # Take from the right only when it strictly belongs first (keeps stability)
        if comes_first(right[j], left[i]):
            merged.append(right[j])
            j += 1
        else:
            merged.append(left[i])
            i += 1
    merged.extend(left[i:])
    merged.extend(right[j:])
    return merged


def coin_change_greedy(denominations, amount):
    """Return a list of coins that sum to amount, or None if impossible."""
    if amount < 0:
        raise ValueError("amount must be non-negative")
    largest_first = merge_sort(denominations, lambda a, b: a > b)
    remaining = amount
    used = []
    for coin in largest_first:
        count, remaining = divmod(remaining, coin)
        used.extend([coin] * count)
        if remaining == 0:
            break
    return used if remaining == 0 else None


def coin_change_dp_count(denominations, amount):
    """Checker: true minimum number of coins using DP (or -1 if impossible)."""
    infinity = amount + 1
    best = [0] + [infinity] * amount
    for value in range(1, amount + 1):
        for coin in denominations:
            if coin <= value and best[value - coin] + 1 < best[value]:
                best[value] = best[value - coin] + 1
    return best[amount] if best[amount] != infinity else -1


def main():
    indian = [500, 200, 100, 50, 20, 10, 5, 2, 1]
    for amount in (289, 93, 0):
        coins = coin_change_greedy(indian, amount)
        print(f"Amount {amount}: {coins} -> {len(coins)} coins")

    print("Impossible amount (coins [5, 10], amount 3):",
          coin_change_greedy([5, 10], 3))

    print("\nCounterexample: denominations [1, 3, 4], amount 6")
    greedy = coin_change_greedy([1, 3, 4], 6)
    best = coin_change_dp_count([1, 3, 4], 6)
    print(f"Greedy answer : {greedy} -> {len(greedy)} coins")
    print(f"True optimum  : {best} coins (3 + 3)")
    print("Greedy is wrong here, so we need Dynamic Programming.")


if __name__ == "__main__":
    main()
