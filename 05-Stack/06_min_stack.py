r"""
Problem: Min Stack (get minimum in O(1))

Problem statement:
    Design a stack that supports push, pop, top and get_min, where get_min
    returns the smallest element currently in the stack in constant time.

What it teaches:
    Augmenting a data structure with extra information (an auxiliary stack)
    to answer a query in O(1).

Input example:
    push 5, push 3, push 7, push 3, then pop four times

Expected output:
    push(5): top=5 min=5
    push(3): top=3 min=3
    push(7): top=7 min=3
    push(3): top=3 min=3
    pop() -> 3, min now 3
    pop() -> 7, min now 3
    pop() -> 3, min now 5
    pop() -> 5, stack is empty

Approach:
    Keep a second stack of minimums. Push onto it whenever the new value is
    less than or equal to the current minimum; pop it when the main stack
    pops the same value.

Step-by-step logic:
    1. push(x): push x on the main stack; if the min stack is empty or
    x <= its top, push x there too.
    2. pop(): pop the main stack; if the popped value equals the top of the
    min stack, pop the min stack as well.
    3. get_min(): read the top of the min stack.

Why it works:
    The min stack top is always the minimum of everything still on the main
    stack. Using <= keeps duplicates of the minimum so that popping one copy
    does not lose the minimum.

Time complexity:
    O(1) for every operation.

Space complexity:
    O(n) extra in the worst case (the min stack).

Edge cases:
    Duplicate minimums (the reason for <=), pop/top/get_min on empty stack,
    strictly decreasing and strictly increasing pushes.

Alternative approach:
    Store (value, current_min) pairs in a single stack, or encode the min in
    the stored value using arithmetic to save space.
"""


class MinStack:
    def __init__(self):
        self._stack = []
        self._mins = []

    def push(self, value):
        self._stack.append(value)
        if not self._mins or value <= self._mins[-1]:
            self._mins.append(value)

    def pop(self):
        if not self._stack:
            raise IndexError("Stack is empty")
        value = self._stack.pop()
        if value == self._mins[-1]:
            self._mins.pop()
        return value

    def top(self):
        if not self._stack:
            raise IndexError("Stack is empty")
        return self._stack[-1]

    def get_min(self):
        if not self._mins:
            raise IndexError("Stack is empty")
        return self._mins[-1]

    def is_empty(self):
        return not self._stack


def main():
    stack = MinStack()
    for value in (5, 3, 7, 3):
        stack.push(value)
        print("push(%d): top=%d min=%d" % (value, stack.top(), stack.get_min()))
    while not stack.is_empty():
        value = stack.pop()
        if stack.is_empty():
            print("pop() -> %d, stack is empty" % value)
        else:
            print("pop() -> %d, min now %d" % (value, stack.get_min()))


if __name__ == "__main__":
    main()
