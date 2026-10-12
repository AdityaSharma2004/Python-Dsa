r"""
Problem: Implement a Stack Using Queues

Problem statement:
    Build a LIFO stack using only queue operations (enqueue at the back,
    dequeue from the front, size, is-empty). Support push, pop and top.

What it teaches:
    The mirror of "queue using stacks": making the newest item reachable first
    by rotating a queue.

Input example:
    push 1, 2, 3; top; pop; push 4; pop until empty

Expected output:
    push(1) -> top=1
    push(2) -> top=2
    push(3) -> top=3
    pop() -> 3
    push(4) -> top=4
    pop() -> 4
    pop() -> 2
    pop() -> 1
    pop() on empty -> Stack is empty

Approach:
    Use one queue. After enqueueing a new item, rotate the older items behind
    it so the new item sits at the front.

Step-by-step logic:
    1. push(x): note the current size n, enqueue x.
    2. Repeat n times: dequeue the front and enqueue it again.
    3. Now x is at the front, so pop() is a dequeue and top() reads the front.

Why it works:
    Rotating the n older items behind x reverses their relation to x, which
    places the most recent push at the front while keeping the older
    items in their previous (stack) order.

Time complexity:
    push O(n); pop, top, is_empty O(1).

Space complexity:
    O(n).

Edge cases:
    Pop or top on empty stack, a single element (no rotation needed), push
    after the stack became empty.

Alternative approach:
    Make push O(1) and pop O(n) by rotating n - 1 items at pop time, or use
    two queues.
"""

from collections import deque


class StackWithQueue:
    def __init__(self):
        self._queue = deque()

    def push(self, value):
        older_count = len(self._queue)
        self._queue.append(value)
        for _ in range(older_count):  # rotate older items behind the new one
            self._queue.append(self._queue.popleft())

    def pop(self):
        if not self._queue:
            raise IndexError("Stack is empty")
        return self._queue.popleft()

    def top(self):
        if not self._queue:
            raise IndexError("Stack is empty")
        return self._queue[0]

    def is_empty(self):
        return len(self._queue) == 0


def main():
    stack = StackWithQueue()
    for value in (1, 2, 3):
        stack.push(value)
        print("push(%d) -> top=%d" % (value, stack.top()))
    print("pop() ->", stack.pop())
    stack.push(4)
    print("push(4) -> top=%d" % stack.top())
    while not stack.is_empty():
        print("pop() ->", stack.pop())
    try:
        stack.pop()
    except IndexError as error:
        print("pop() on empty ->", error)


if __name__ == "__main__":
    main()
