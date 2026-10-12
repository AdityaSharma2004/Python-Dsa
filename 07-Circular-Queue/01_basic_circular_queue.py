"""
Problem title:
    Basic Fixed-Size Circular Queue

Problem statement:
    Implement a queue with a fixed capacity using a Python list as a ring.
    Support enqueue(value), dequeue(), is_empty() and is_full(). Enqueue on a
    full queue and dequeue on an empty queue must be refused safely.

What it teaches:
    - Why a plain array queue wastes space after dequeues.
    - Reusing freed slots by wrapping the index with the modulo operator.
    - Using a size counter to tell "full" from "empty".

Input example:
    capacity = 3; enqueue 10, 20, 30, 40; dequeue; enqueue 40; dequeue all

Expected output:
    enqueue 10 -> ok
    enqueue 20 -> ok
    enqueue 30 -> ok
    enqueue 40 -> REFUSED (full)
    dequeue -> 10
    enqueue 40 -> ok
    raw slots: [40, 20, 30] front = 1
    dequeue -> 20
    dequeue -> 30
    dequeue -> 40
    dequeue on empty -> None
    is_empty: True | is_full: False

Approach:
    Keep "front" (index of the oldest item) and "size" (how many items are
    stored). The rear slot is always (front + size) % capacity.

Step-by-step logic:
    1. enqueue: if size == capacity -> full, refuse. Otherwise write at
       (front + size) % capacity and size += 1.
    2. dequeue: if size == 0 -> empty, refuse. Otherwise read items[front],
       clear that slot, front = (front + 1) % capacity, size -= 1.

Why it works:
    The modulo makes index capacity-1 + 1 wrap to 0, so the array behaves like
    a circle. The size counter gives an unambiguous full/empty test, because
    front alone looks identical in both states.

Time complexity:
    O(1) for every operation.

Space complexity:
    O(capacity) for the fixed array.

Edge cases:
    - Enqueue when full / dequeue when empty.
    - Capacity 1.
    - Using a slot again after wrap-around.

Alternative approach:
    A dynamic list with pop(0) works but each dequeue is O(n); collections.deque
    is O(1) but hides the ring mechanics this problem teaches.
"""


class CircularQueue:
    def __init__(self, capacity):
        if capacity < 1:
            raise ValueError("capacity must be at least 1")
        self.capacity = capacity
        self.items = [None] * capacity
        self.front = 0
        self.size = 0

    def is_empty(self):
        return self.size == 0

    def is_full(self):
        return self.size == self.capacity

    def enqueue(self, value):
        """Add value at the rear. Return False if the queue is full."""
        if self.is_full():
            return False
        rear_index = (self.front + self.size) % self.capacity  # wrap around
        self.items[rear_index] = value
        self.size += 1
        return True

    def dequeue(self):
        """Remove and return the front value, or None if empty."""
        if self.is_empty():
            return None
        value = self.items[self.front]
        self.items[self.front] = None  # free the slot
        self.front = (self.front + 1) % self.capacity
        self.size -= 1
        return value


def main():
    queue = CircularQueue(3)
    for value in (10, 20, 30, 40):
        accepted = queue.enqueue(value)
        print("enqueue", value, "->", "ok" if accepted else "REFUSED (full)")

    print("dequeue ->", queue.dequeue())
    print("enqueue 40 ->", "ok" if queue.enqueue(40) else "REFUSED (full)")
    print("raw slots:", queue.items, "front =", queue.front)

    while not queue.is_empty():
        print("dequeue ->", queue.dequeue())
    print("dequeue on empty ->", queue.dequeue())
    print("is_empty:", queue.is_empty(), "| is_full:", queue.is_full())


if __name__ == "__main__":
    main()
