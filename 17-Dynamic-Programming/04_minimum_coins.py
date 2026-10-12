"""
Problem Title: Minimum Number of Coins (Coin Change, fewest coins)

Problem Statement:
    Given coin denominations (unlimited supply of each) and a target amount,
    return the fewest coins that add up to the amount, or -1 if impossible.
    Also report which coins are used.

What It Teaches:
    - Unbounded choice: each coin can be reused.
    - dp[a] = 1 + best of dp[a - coin] over all coins.
    - Using "infinity" as a marker for unreachable states.
    - Why greedy ("take the biggest coin") can fail where DP does not.

Input Example:
    coins = [1, 5, 6, 9], amount = 11

Expected Output:
    coins=[1, 5, 6, 9], amount=11 -> 2 coins [5, 6]
    Greedy on the same input: [9, 1, 1]
    coins=[2], amount=3 -> -1
    coins=[1, 2, 5], amount=0 -> (0, [])
    coins=[1, 2, 5], amount=27 -> (6, [2, 5, 5, 5, 5, 5])
    coins=[7], amount=3 -> -1

Approach:
    Build dp for amounts 0..target. dp[0] = 0. For each amount try every coin
    that fits and keep the smallest dp[a - coin] + 1. Remember the coin that
    achieved it so the coins can be rebuilt.

Step-by-Step Logic:
    1. dp = [INF] * (amount + 1); dp[0] = 0.
    2. For a in 1..amount: for each coin <= a, if dp[a-coin] + 1 < dp[a], update
       dp[a] and remember last_coin[a] = coin.
    3. If dp[amount] is still INF the amount cannot be formed -> -1.
    4. Otherwise follow last_coin from the amount down to 0.

Why It Works:
    The optimal solution for amount a ends with some coin c; removing it leaves
    an optimal solution for a - c. Trying every c finds the best one.

Time Complexity:
    O(amount * number_of_coins).
Space Complexity:
    O(amount).

Edge Cases:
    Amount 0 (0 coins), no way to form the amount, a coin larger than the
    amount, a single coin type, coin sets where greedy fails (e.g. [1,5,6,9]).

Alternative Approach:
    Greedy works only for "canonical" systems (e.g. 1,5,10,25); see
    18-Greedy-Algorithm for that discussion. BFS over amounts also works.
"""

INF = float("inf")


def min_coins(coins, amount):
    """Return (count, list_of_coins); count is -1 when impossible."""
    dp = [INF] * (amount + 1)
    last_coin = [0] * (amount + 1)
    dp[0] = 0
    for current in range(1, amount + 1):
        for coin in coins:
            if coin <= current and dp[current - coin] + 1 < dp[current]:
                dp[current] = dp[current - coin] + 1
                last_coin[current] = coin
    if dp[amount] == INF:
        return -1, []
    used = []
    remaining = amount
    while remaining > 0:
        used.append(last_coin[remaining])
        remaining -= last_coin[remaining]
    return dp[amount], used


def greedy_coins(coins, amount):
    """Largest-coin-first (assumes coins listed in descending order). May fail."""
    used = []
    for coin in coins:
        while amount >= coin:
            amount -= coin
            used.append(coin)
    return used if amount == 0 else None


def main():
    coins = [1, 5, 6, 9]
    count, used = min_coins(coins, 11)
    print(f"coins={coins}, amount=11 -> {count} coins {used}")
    print("Greedy on the same input:", greedy_coins([9, 6, 5, 1], 11))
    print("coins=[2], amount=3 ->", min_coins([2], 3)[0])
    print("coins=[1, 2, 5], amount=0 ->", min_coins([1, 2, 5], 0))
    print("coins=[1, 2, 5], amount=27 ->", min_coins([1, 2, 5], 27))
    print("coins=[7], amount=3 ->", min_coins([7], 3)[0])


if __name__ == "__main__":
    main()
