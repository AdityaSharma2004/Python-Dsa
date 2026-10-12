r"""
Problem: Largest Rectangle in a Histogram

Problem statement:
    Given bar heights of a histogram (each bar has width 1), find the area of
    the largest rectangle that fits entirely inside the bars.

What it teaches:
    An advanced monotonic stack: when a bar is shorter than the stack top, the
    popped bar defines a maximal rectangle whose width is found from the stack.

Input example:
    [2, 1, 5, 6, 2, 3]

Expected output:
    [2, 1, 5, 6, 2, 3] -> largest area 10
    [2, 4] -> largest area 4
    [1, 1, 1, 1] -> largest area 4
    [5] -> largest area 5
    [] -> largest area 0
    brute force agrees: True

Approach:
    Keep a stack of indexes with increasing heights. A shorter bar pops taller
    bars and each popped bar's rectangle is measured.

Step-by-step logic:
    1. Append a sentinel height 0 so every bar gets popped at the end.
    2. For each index i: while the stack top bar is taller than heights[i],
    pop it as height h.
    3. Width = i if the stack is now empty, else i - stack_top - 1.
    4. Area = h * width; keep the best area.
    5. Push i.

Why it works:
    When bar h is popped, the bar below it in the stack is the nearest
    shorter bar on the left and i is the nearest shorter bar on the right,
    so h can extend exactly across that gap.

Time complexity:
    O(n) - each index pushed and popped once.

Space complexity:
    O(n).

Edge cases:
    Empty list, single bar, all equal heights, strictly increasing or
    decreasing heights, zero-height bars.

Alternative approach:
    Brute force over every pair of bars (O(n^2)), included to verify; a
    divide and conquer on the minimum bar is O(n log n) on average.
"""


def largest_rectangle(heights):
    best = 0
    stack = []  # indexes of bars with increasing heights
    padded = list(heights) + [0]  # sentinel flushes the stack
    for i, current in enumerate(padded):
        while stack and padded[stack[-1]] > current:
            height = padded[stack.pop()]
            width = i if not stack else i - stack[-1] - 1
            area = height * width
            if area > best:
                best = area
        stack.append(i)
    return best


def largest_rectangle_brute_force(heights):
    best = 0
    for left in range(len(heights)):
        lowest = heights[left]
        for right in range(left, len(heights)):
            if heights[right] < lowest:
                lowest = heights[right]
            area = lowest * (right - left + 1)
            if area > best:
                best = area
    return best


def main():
    samples = [[2, 1, 5, 6, 2, 3], [2, 4], [1, 1, 1, 1], [5], []]
    all_match = True
    for heights in samples:
        area = largest_rectangle(heights)
        print(heights, "-> largest area", area)
        if area != largest_rectangle_brute_force(heights):
            all_match = False
    print("brute force agrees:", all_match)


if __name__ == "__main__":
    main()
