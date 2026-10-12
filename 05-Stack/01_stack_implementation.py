r"""
Problem: Implement a Stack (push, pop, peek, is_empty, size)

Problem statement:
    Build a stack class that follows Last-In-First-Out (LIFO) order. It must
    support push, pop, peek, is_empty and size, and must report an error
    (not crash silently) when popping or peeking an empty stack.

What it teaches:
    The LIFO rule, the five core stack operations, and how a Python list can
    act as a stack when we only touch its right end.

Input example:
    push 10, push 20, push 30, peek, pop, pop, size, pop, pop on empty

Expected output:
    push(10) -> [10]
    push(20) -> [10, 20]
    push(30) -> [10, 20, 30]
    peek() -> 30
    pop() -> 30
    pop() -> 20
    size() -> 1
    pop() -> 10
    is_empty() -> True
    pop() on empty -> Stack is empty

Approach:
    Wrap a list. The end of the list is the top of the stack, so push is
    append and pop is list.pop().

Step-by-step logic:
    1. Keep a private list _items; the last element is the top.
    2. push(x): append x to the end.
    3. pop(): if empty raise an error, otherwise remove and return the end.
    4. peek(): same check, but only read the last element.
    5. is_empty() and size() look at the length of the list.

Why it works:
    Appending and removing at the right end of a Python list are amortised
    O(1), and the most recently added element is always at that end, which is
    exactly what LIFO requires.

Time complexity:
    push, pop, peek, is_empty, size are all O(1) (push amortised).

Space complexity:
    O(n) for n stored items.

Edge cases:
    Pop or peek on an empty stack, pushing None or duplicate values, popping
    until empty and then pushing again.

Alternative approach:
    Use a singly linked list and push/pop at the head; every operation is
    then strictly O(1) with no array resizing.
"""


class Stack:
    """A LIFO stack backed by a Python list."""

    def __init__(self):
        self._items = []

    def push(self, value):
        self._items.append(value)

    def pop(self):
        if self.is_empty():
            raise IndexError("Stack is empty")
        return self._items.pop()

    def peek(self):
        if self.is_empty():
            raise IndexError("Stack is empty")
        return self._items[-1]

    def is_empty(self):
        return len(self._items) == 0

    def size(self):
        return len(self._items)

    def to_list(self):
        """Bottom-to-top copy, handy for printing."""
        return list(self._items)


def main():
    stack = Stack()
    for value in (10, 20, 30):
        stack.push(value)
        print("push(%d) ->" % value, stack.to_list())
    print("peek() ->", stack.peek())
    print("pop() ->", stack.pop())
    print("pop() ->", stack.pop())
    print("size() ->", stack.size())
    print("pop() ->", stack.pop())
    print("is_empty() ->", stack.is_empty())
    try:
        stack.pop()
    except IndexError as error:
        print("pop() on empty ->", error)


if __name__ == "__main__":
    main()
