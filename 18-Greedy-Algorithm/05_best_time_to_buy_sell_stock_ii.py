"""
Problem title:
    Best Time to Buy and Sell Stock II (unlimited transactions)

Problem statement:
    prices[i] is the price of a stock on day i. You may buy and sell as many
    times as you like, but you can hold at most one share at a time. Return
    the maximum total profit.

What it teaches:
    * Greedy by local gains: collect every upward step.
    * A problem that looks like it needs planning but does not.

Input example:
    prices = [7, 1, 5, 3, 6, 4]

Expected output:
    prices=[7, 1, 5, 3, 6, 4] -> profit=7, trades(buy_day, sell_day)=[(1, 2), (3, 4)]
    prices=[1, 2, 3, 4, 5] -> profit=4, trades(buy_day, sell_day)=[(0, 4)]
    prices=[7, 6, 4, 3, 1] -> profit=0, trades(buy_day, sell_day)=[]
    prices=[3] -> profit=0, trades(buy_day, sell_day)=[]
    prices=[] -> profit=0, trades(buy_day, sell_day)=[]
    prices=[2, 2, 2] -> profit=0, trades(buy_day, sell_day)=[]

Approach:
    Add up every positive day-to-day difference prices[i] - prices[i-1].

Step-by-step logic:
    1. profit = 0.
    2. For each day i from 1 to n-1:
       - gain = prices[i] - prices[i-1]
       - if gain > 0: profit += gain (buy yesterday, sell today).
    3. Return profit.

Why it works:
    A rise from low to high equals the sum of the small daily rises in
    between, so collecting each rise separately gives the same profit as one
    big trade. Falling days are simply skipped (we do not hold then).

Time complexity:
    O(n) - single pass.

Space complexity:
    O(1).

Edge cases:
    * Empty list or one price -> 0.
    * Strictly decreasing prices -> 0.
    * Strictly increasing prices -> last minus first.

Alternative approach:
    Find each valley and the following peak explicitly (also O(n)), or use DP
    with states "holding" / "not holding".
"""


def max_profit(prices):
    """Return the maximum profit with unlimited buy/sell transactions."""
    profit = 0
    for day in range(1, len(prices)):
        gain = prices[day] - prices[day - 1]
        if gain > 0:  # only take upward moves
            profit += gain
    return profit


def trades(prices):
    """Return (buy_day, sell_day) pairs describing one optimal strategy."""
    result = []
    buy = None
    for day in range(len(prices)):
        next_higher = day + 1 < len(prices) and prices[day + 1] > prices[day]
        if buy is None and next_higher:
            buy = day  # start of a climb
        elif buy is not None and not next_higher:
            result.append((buy, day))  # climb ended, sell
            buy = None
    return result


def main():
    tests = [
        [7, 1, 5, 3, 6, 4],
        [1, 2, 3, 4, 5],
        [7, 6, 4, 3, 1],
        [3],
        [],
        [2, 2, 2],
    ]
    for prices in tests:
        print(f"prices={prices} -> profit={max_profit(prices)}, "
              f"trades(buy_day, sell_day)={trades(prices)}")


if __name__ == "__main__":
    main()
