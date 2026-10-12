r"""
Problem: Generate Binary Numbers from 1 to N Using a Queue

Problem statement:
    Print the binary representation of every number from 1 to N using a queue
    and no number-to-binary conversion function.

What it teaches:
    Level-by-level generation with a queue (the idea behind BFS).

Input example:
    n = 10, n = 1, n = 0

Expected output:
    n=10: ['1', '10', '11', '100', '101', '110', '111', '1000', '1001', '1010']
    n=1: ['1']
    n=0: []
    matches bin(): True

Approach:
    Start with "1" in the queue. Dequeue a string s, record it, then enqueue
    s + "0" and s + "1".

Step-by-step logic:
    1. If n is 0 return an empty list; enqueue "1".
    2. Repeat n times: dequeue the front string, append it to the answer.
    3. Enqueue front + "0", then front + "1".

Why it works:
    The children of a binary number x are 2x (append 0) and 2x + 1 (append 1).
    The queue processes numbers level by level, i.e. in increasing order.

Time complexity:
    O(n * log n) because each of the n strings has length about log2(n).

Space complexity:
    O(n * log n) characters in the queue and the answer.

Edge cases:
    n = 0, n = 1, powers of two, large n (queue holds about n/2 entries).

Alternative approach:
    Repeated division by 2 for each number, O(log n) each; bin(i) is used only
    in the verification below.
"""

from collections import deque


def binary_numbers(n):
    result = []
    if n <= 0:
        return result
    queue = deque(["1"])
    for _ in range(n):
        current = queue.popleft()
        result.append(current)
        queue.append(current + "0")  # 2x
        queue.append(current + "1")  # 2x + 1
    return result


def main():
    for n in (10, 1, 0):
        print("n=%d:" % n, binary_numbers(n))
    expected = [bin(i)[2:] for i in range(1, 51)]  # verification only
    print("matches bin():", binary_numbers(50) == expected)


if __name__ == "__main__":
    main()
