"""
Problem Title: Coin Change - Number of Ways

Problem Statement:
    Given coin denominations (unlimited supply) and an amount, count how many
    different COMBINATIONS of coins sum to the amount (order does not matter:
    1+2 and 2+1 are the same). Also count ORDERED sequences to see the difference.

What It Teaches:
    - Counting DP versus optimising DP.
    - Loop order matters: coins outside / amounts inside counts combinations;
      amounts outside / coins inside counts ordered sequences (permutations).
    - 1-D table that is updated coin by coin.

Input Example:
    coins = [1, 2, 5], amount = 5

Expected Output:
    coins=[1, 2, 5], amount=5
    Combinations: 4
       [1, 1, 1, 1, 1]
       [1, 1, 1, 2]
       [1, 2, 2]
       [5]
    Ordered sequences: 9
    Amount 0: 1
    coins=[2], amount=3: 0
    coins=[1, 5, 10, 25], amount=100: 242
    No coins, amount 4: 0

Approach:
    ways[a] = number of ways to make amount a. Process one coin type at a time;
    for that coin, ways[a] += ways[a - coin].

Step-by-Step Logic:
    1. ways[0] = 1 (the empty combination), all others 0.
    2. For each coin: for a from coin to amount: ways[a] += ways[a - coin].
    3. Because each coin type is finished before the next starts, every
       combination is counted once in a fixed coin order.
    4. For ordered sequences swap the loops: for each amount, try every coin.

Why It Works:
    After processing the first k coin types, ways[a] counts combinations that
    use only those types. Adding type k+1 either does not use it (already
    counted) or uses at least one, which reduces to ways[a - coin].

Time Complexity:
    O(amount * number_of_coins).
Space Complexity:
    O(amount).

Edge Cases:
    Amount 0 (exactly 1 way), no coins, coin bigger than amount, duplicates in
    the coin list (avoid by passing distinct values).

Alternative Approach:
    A 2-D table ways[i][a] (first i coins) is easier to reason about but uses
    O(coins * amount) space.
"""


def count_combinations(coins, amount):
    """Number of unordered coin combinations that sum to amount."""
    ways = [0] * (amount + 1)
    ways[0] = 1
    for coin in coins:  # coin loop OUTSIDE -> combinations
        for current in range(coin, amount + 1):
            ways[current] += ways[current - coin]
    return ways[amount]


def count_sequences(coins, amount):
    """Number of ordered coin sequences that sum to amount."""
    ways = [0] * (amount + 1)
    ways[0] = 1
    for current in range(1, amount + 1):  # amount loop OUTSIDE -> sequences
        for coin in coins:
            if coin <= current:
                ways[current] += ways[current - coin]
    return ways[amount]


def list_combinations(coins, amount, start=0, partial=None):
    """Generate the actual combinations (small inputs only) for display."""
    if partial is None:
        partial = []
    if amount == 0:
        return [list(partial)]
    found = []
    for index in range(start, len(coins)):
        if coins[index] <= amount:
            partial.append(coins[index])
            found.extend(list_combinations(coins, amount - coins[index], index, partial))
            partial.pop()
    return found


def main():
    coins, amount = [1, 2, 5], 5
    print(f"coins={coins}, amount={amount}")
    print("Combinations:", count_combinations(coins, amount))
    for combo in list_combinations(coins, amount):
        print("  ", combo)
    print("Ordered sequences:", count_sequences(coins, amount))
    print("Amount 0:", count_combinations(coins, 0))
    print("coins=[2], amount=3:", count_combinations([2], 3))
    print("coins=[1, 5, 10, 25], amount=100:", count_combinations([1, 5, 10, 25], 100))
    print("No coins, amount 4:", count_combinations([], 4))


if __name__ == "__main__":
    main()
