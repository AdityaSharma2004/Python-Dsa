r"""
Problem: Next Greater Element

Problem statement:
    For every element of an array find the first element to its right that is
    strictly greater. If none exists, answer -1.

What it teaches:
    The monotonic stack technique: a stack kept in decreasing order that turns
    an O(n^2) search into O(n).

Input example:
    [4, 5, 2, 25], [13, 7, 6, 12], [3, 3, 3], [5, 4, 3, 2, 1], []

Expected output:
    [4, 5, 2, 25] -> [5, 25, 25, -1]
    [13, 7, 6, 12] -> [-1, 12, 12, -1]
    [3, 3, 3] -> [-1, -1, -1]
    [5, 4, 3, 2, 1] -> [-1, -1, -1, -1, -1]
    [] -> []
    brute force agrees: True

Approach:
    Walk left to right, keeping a stack of indexes whose answer is still
    unknown. When a bigger value arrives it answers every smaller index on
    top of the stack.

Step-by-step logic:
    1. result = [-1] * n; stack = [].
    2. For each index i: while the stack is not empty and the value at the
    stack top is smaller than values[i], pop it and set result[popped] to
    values[i].
    3. Push i.
    4. Indexes left in the stack never found a greater value and keep -1.

Why it works:
    The stack stays non-increasing from bottom to top, so the first larger
    value that arrives is the nearest greater element for every index it pops.
    Each index is pushed and popped once.

Time complexity:
    O(n).

Space complexity:
    O(n).

Edge cases:
    Empty array, equal values (strictly greater is required), strictly
    decreasing array (all -1), single element.

Alternative approach:
    Brute force: for each element scan to the right, O(n^2) time, O(1) extra
    space (included below to verify the stack answer).
"""


def next_greater_stack(values):
    result = [-1] * len(values)
    stack = []  # indexes with values in non-increasing order
    for index, value in enumerate(values):
        while stack and values[stack[-1]] < value:
            result[stack.pop()] = value
        stack.append(index)
    return result


def next_greater_brute_force(values):
    result = []
    for i in range(len(values)):
        answer = -1
        for j in range(i + 1, len(values)):
            if values[j] > values[i]:
                answer = values[j]
                break
        result.append(answer)
    return result


def main():
    samples = [[4, 5, 2, 25], [13, 7, 6, 12], [3, 3, 3], [5, 4, 3, 2, 1], []]
    all_match = True
    for values in samples:
        fast = next_greater_stack(values)
        print(values, "->", fast)
        if fast != next_greater_brute_force(values):
            all_match = False
    print("brute force agrees:", all_match)


if __name__ == "__main__":
    main()
