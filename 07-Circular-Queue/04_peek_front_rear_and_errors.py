"""
Problem title:
    Peek Front/Rear and Error Handling

Problem statement:
    Extend a circular queue with peek_front() and peek_rear() that return values
    WITHOUT removing them. Instead of returning None, raise clear exceptions:
    QueueFullError on enqueue to a full queue and QueueEmptyError when
    dequeuing or peeking an empty queue.

What it teaches:
    - Tracking front and rear precisely, including after wrap-around.
    - Distinguishing "no value" from a stored None via exceptions.
    - Writing defensive code for boundary conditions.

Input example:
    capacity = 3; peek on empty; enqueue 5, 6, 7; enqueue 8; dequeue; enqueue 8

Expected output:
    peek_front on empty -> ERROR: no front item: queue is empty
    dequeue on empty -> ERROR: cannot dequeue from an empty queue
    front: 5 | rear: 7
    enqueue 8 on full -> ERROR: queue is full (capacity 3)
    dequeue -> 5
    raw: [8, 6, 7] | front: 6 | rear: 8

Approach:
    Store front index and size. rear index = (front + size - 1) % capacity.

Step-by-step logic:
    1. peek_front: raise if empty, else return items[front].
    2. peek_rear: raise if empty, else return items[(front + size - 1) % cap].
    3. enqueue / dequeue as usual, but raise instead of returning flags.
    4. The demo catches each exception and prints its message.

Why it works:
    The rear is a pure function of front and size, so it is always correct,
    even when the stored items straddle the end of the array.

Time complexity:
    O(1) for every operation.

Space complexity:
    O(capacity).

Edge cases:
    - Peeking on an empty queue.
    - Peeking the rear when items wrap around the array end.
    - Capacity 1 where front and rear are the same item.

Alternative approach:
    Return a sentinel (None) instead of raising; simpler but ambiguous if None
    is a legitimate value.
"""


class QueueFullError(Exception):
    pass


class QueueEmptyError(Exception):
    pass


class CircularQueue:
    def __init__(self, capacity):
        self.capacity = capacity
        self.items = [None] * capacity
        self.front = 0
        self.size = 0

    def enqueue(self, value):
        if self.size == self.capacity:
            raise QueueFullError("queue is full (capacity " + str(self.capacity) + ")")
        self.items[(self.front + self.size) % self.capacity] = value
        self.size += 1

    def dequeue(self):
        if self.size == 0:
            raise QueueEmptyError("cannot dequeue from an empty queue")
        value = self.items[self.front]
        self.items[self.front] = None
        self.front = (self.front + 1) % self.capacity
        self.size -= 1
        return value

    def peek_front(self):
        if self.size == 0:
            raise QueueEmptyError("no front item: queue is empty")
        return self.items[self.front]

    def peek_rear(self):
        if self.size == 0:
            raise QueueEmptyError("no rear item: queue is empty")
        return self.items[(self.front + self.size - 1) % self.capacity]


def attempt(label, action):
    """Run action and print its result or the error message."""
    try:
        result = action()
        print(label, "->", result)
    except (QueueFullError, QueueEmptyError) as error:
        print(label, "-> ERROR:", error)


def main():
    queue = CircularQueue(3)
    attempt("peek_front on empty", queue.peek_front)
    attempt("dequeue on empty", queue.dequeue)
    for value in (5, 6, 7):
        queue.enqueue(value)
    print("front:", queue.peek_front(), "| rear:", queue.peek_rear())
    attempt("enqueue 8 on full", lambda: queue.enqueue(8))
    attempt("dequeue", queue.dequeue)
    queue.enqueue(8)  # this value is stored at index 0 (wrapped)
    print("raw:", queue.items, "| front:", queue.peek_front(),
          "| rear:", queue.peek_rear())


if __name__ == "__main__":
    main()
