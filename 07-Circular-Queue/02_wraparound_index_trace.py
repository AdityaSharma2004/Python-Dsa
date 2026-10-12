"""
Problem title:
    Trace Wrap-Around Indexes

Problem statement:
    Given a capacity and a list of operations ("E x" to enqueue x, "D" to
    dequeue), simulate a circular queue and print a trace showing the front
    index, the rear index and the raw array after every step. Highlight the
    moment the rear index wraps back to 0.

What it teaches:
    - The formula next = (index + 1) % capacity.
    - How front and rear chase each other around the ring.
    - Reading the raw array to see where values physically live.

Input example:
    capacity = 4
    ops = E 1, E 2, E 3, E 4, E 9 (rejected), D, D, E 5, E 6, D

Expected output:
    capacity = 4
    E 1  front=0 rear=0 [1, None, None, None]  ok
    E 2  front=0 rear=1 [1, 2, None, None]  ok
    E 3  front=0 rear=2 [1, 2, 3, None]  ok
    E 4  front=0 rear=3 [1, 2, 3, 4]  ok
    E 9  front=0 rear=3 [1, 2, 3, 4]  full
    D    front=1 rear=3 [None, 2, 3, 4]  removed 1
    D    front=2 rear=3 [None, None, 3, 4]  removed 2
    E 5  front=2 rear=0 [5, None, 3, 4]  ok, rear WRAPPED to 0
    E 6  front=2 rear=1 [5, 6, 3, 4]  ok
    D    front=3 rear=1 [5, 6, None, 4]  removed 3

Approach:
    Keep front, rear (index of the last stored item, -1 before the first
    enqueue) and a size counter. After each operation, print the state as a table row.

Step-by-step logic:
    1. enqueue: rear = (rear + 1) % capacity; items[rear] = x; size += 1.
       If rear is now 0 and the queue was not empty before, the rear wrapped.
    2. dequeue: items[front] = None; front = (front + 1) % capacity; size -= 1.
       When the queue becomes empty, set rear to just behind front so the
       next enqueue lands exactly on front.

Why it works:
    The remainder operator maps any index back into 0..capacity-1, which turns
    a straight array into a ring.

Time complexity:
    O(1) per operation, O(k) to trace k operations.

Space complexity:
    O(capacity).

Edge cases:
    - Full queue or empty queue operations are reported, not crashed.
    - Rear wrapping to 0 while front is still > 0.

Alternative approach:
    Store only front and size and compute rear on demand (see problem 01).
"""


class TracedQueue:
    def __init__(self, capacity):
        self.capacity = capacity
        self.items = [None] * capacity
        self.front = 0
        self.rear = -1  # -1 means "nothing stored yet"
        self.size = 0

    def enqueue(self, value):
        if self.size == self.capacity:
            return "full"
        was_empty = self.size == 0
        self.rear = (self.rear + 1) % self.capacity
        self.items[self.rear] = value
        self.size += 1
        if self.rear == 0 and not was_empty:
            return "ok, rear WRAPPED to 0"
        return "ok"

    def dequeue(self):
        if self.size == 0:
            return "empty"
        removed = self.items[self.front]
        self.items[self.front] = None
        self.front = (self.front + 1) % self.capacity
        self.size -= 1
        if self.size == 0:
            self.rear = (self.front - 1) % self.capacity  # keep rear just behind front
        return "removed " + str(removed)


def run_trace(capacity, operations):
    queue = TracedQueue(capacity)
    print("capacity =", capacity)
    for operation in operations:
        if operation[0] == "E":
            note = queue.enqueue(operation[1])
        else:
            note = queue.dequeue()
        label = "E " + str(operation[1]) if operation[0] == "E" else "D"
        print("{:<4} front={} rear={} {}  {}".format(
            label, queue.front, queue.rear, queue.items, note))


def main():
    operations = [("E", 1), ("E", 2), ("E", 3), ("E", 4), ("E", 9), ("D",), ("D",),
                  ("E", 5), ("E", 6), ("D",)]
    run_trace(4, operations)


if __name__ == "__main__":
    main()
