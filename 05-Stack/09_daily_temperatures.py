r"""
Problem: Daily Temperatures (Days Until a Warmer Day)

Problem statement:
    Given daily temperatures, return for each day how many days you must wait
    for a warmer temperature. Use 0 if there is no warmer day ahead.

What it teaches:
    A second use of the monotonic stack, this time storing indexes so we can
    compute distances.

Input example:
    [73, 74, 75, 71, 69, 72, 76, 73]

Expected output:
    [73, 74, 75, 71, 69, 72, 76, 73] -> [1, 1, 4, 2, 1, 1, 0, 0]
    [30, 40, 50, 60] -> [1, 1, 1, 0]
    [60, 50, 40] -> [0, 0, 0]
    [55] -> [0]
    [] -> []

Approach:
    Keep a stack of indexes of days still waiting for a warmer day. A warmer
    day resolves all colder days on top of the stack.

Step-by-step logic:
    1. answer = [0] * n; stack = [].
    2. For day i: while the stack top day is colder than day i, pop it and
    set answer[popped] = i - popped.
    3. Push i.
    4. Whatever remains in the stack keeps 0.

Why it works:
    Temperatures of waiting days on the stack never increase toward the top,
    so the first warmer day to arrive is the nearest one for each popped day.

Time complexity:
    O(n) - every index is pushed and popped at most once.

Space complexity:
    O(n).

Edge cases:
    Empty input, equal temperatures (not warmer), strictly decreasing list,
    single day.

Alternative approach:
    Scan backwards using the answers already computed to jump ahead, O(n)
    time with O(1) extra space besides the result.
"""


def days_until_warmer(temperatures):
    answer = [0] * len(temperatures)
    waiting = []  # indexes of days without a warmer day yet
    for day, temperature in enumerate(temperatures):
        while waiting and temperatures[waiting[-1]] < temperature:
            earlier = waiting.pop()
            answer[earlier] = day - earlier
        waiting.append(day)
    return answer


def main():
    samples = [[73, 74, 75, 71, 69, 72, 76, 73], [30, 40, 50, 60],
               [60, 50, 40], [55], []]
    for temperatures in samples:
        print(temperatures, "->", days_until_warmer(temperatures))


if __name__ == "__main__":
    main()
