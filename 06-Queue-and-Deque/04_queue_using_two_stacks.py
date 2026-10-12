r"""
Problem: Implement a Queue Using Two Stacks

Problem statement:
    Build a FIFO queue using only two LIFO stacks (Python lists used with
    append and pop at the end). Support enqueue, dequeue and peek.

What it teaches:
    How reversing a stack twice restores order, and amortised analysis.

Input example:
    enqueue 1, 2, 3; dequeue; enqueue 4; dequeue x3

Expected output:
    enqueue(1) in=[1] out=[]
    enqueue(2) in=[1, 2] out=[]
    enqueue(3) in=[1, 2, 3] out=[]
    dequeue() -> 1 in=[] out=[3, 2]
    enqueue(4) in=[4] out=[3, 2]
    dequeue() -> 2 in=[4] out=[3]
    dequeue() -> 3 in=[4] out=[]
    dequeue() -> 4 in=[] out=[]
    dequeue() on empty -> Queue is empty

Approach:
    Push new items on an "in" stack. For dequeue, if the "out" stack is empty
    move everything from "in" to "out" (reversing the order) and pop "out".

Step-by-step logic:
    1. enqueue(x): in_stack.append(x).
    2. dequeue(): if out_stack is empty, pop every item of in_stack and push
    it onto out_stack.
    3. If out_stack is still empty the queue is empty: raise an error.
    4. Otherwise pop and return out_stack's top.
    5. peek() does the same transfer but only reads the top.

Why it works:
    Moving items from one stack to another reverses them, so the oldest item
    ends on top of out_stack. We transfer only when out_stack is empty, which
    keeps older items ahead of newer ones.

Time complexity:
    enqueue O(1); dequeue O(1) amortised (a single dequeue can cost O(n), but
    each item is moved at most once, so n operations cost O(n)).

Space complexity:
    O(n).

Edge cases:
    Dequeue on empty queue, interleaved enqueue and dequeue (do NOT transfer
    while out_stack still has items), single element.

Alternative approach:
    Do the transfer on every enqueue (O(n) enqueue, O(1) dequeue), or use one
    stack and recursion.
"""


class QueueWithTwoStacks:
    def __init__(self):
        self.in_stack = []
        self.out_stack = []

    def enqueue(self, value):
        self.in_stack.append(value)

    def _transfer(self):
        if not self.out_stack:  # only refill when it is completely empty
            while self.in_stack:
                self.out_stack.append(self.in_stack.pop())

    def dequeue(self):
        self._transfer()
        if not self.out_stack:
            raise IndexError("Queue is empty")
        return self.out_stack.pop()

    def peek(self):
        self._transfer()
        if not self.out_stack:
            raise IndexError("Queue is empty")
        return self.out_stack[-1]

    def is_empty(self):
        return not self.in_stack and not self.out_stack


def main():
    queue = QueueWithTwoStacks()

    def state():
        return "in=%s out=%s" % (queue.in_stack, queue.out_stack)

    for value in (1, 2, 3):
        queue.enqueue(value)
        print("enqueue(%d)" % value, state())
    print("dequeue() -> %d" % queue.dequeue(), state())
    queue.enqueue(4)
    print("enqueue(4)", state())
    for _ in range(3):
        print("dequeue() -> %d" % queue.dequeue(), state())
    try:
        queue.dequeue()
    except IndexError as error:
        print("dequeue() on empty ->", error)


if __name__ == "__main__":
    main()
