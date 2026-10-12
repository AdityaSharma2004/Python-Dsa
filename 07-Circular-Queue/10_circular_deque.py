"""
Problem title:
    Circular Deque (Insert and Delete at Both Ends)

Problem statement:
    Implement a fixed-capacity double-ended queue on a ring. Support
    insert_front, insert_rear, delete_front, delete_rear, get_front,
    get_rear, is_empty and is_full, all in O(1).

What it teaches:
    - Moving backwards on a ring: (index - 1) % capacity.
    - Why Python's modulo makes the backward wrap-around safe.
    - Computing rear from front and size, as in the plain circular queue.

Input example:
    capacity = 4; insert_rear 1, 2; insert_front 3, 4; insert_rear 5;
    delete_rear; delete_front

Expected output:
    insert_rear 1, 2   raw=[1, 2, None, None] front_index=0 front=1 rear=2
    insert_front 3     raw=[1, 2, None, 3] front_index=3 front=3 rear=2
    insert_front 4     raw=[1, 2, 4, 3] front_index=2 front=4 rear=2
    insert_rear 5 on full -> False
    delete_rear -> 2
    delete_front -> 4
    after deletes      raw=[1, None, None, 3] front_index=3 front=3 rear=1
    delete_front on empty -> None
    insert_front on empty -> True
    front wrapped      raw=[None, 9] front_index=1 front=9 rear=9

Approach:
    Keep front (index of the first item) and size. The rear item lives at
    (front + size - 1) % capacity.

Step-by-step logic:
    1. insert_rear: slot = (front + size) % capacity; store; size += 1.
    2. insert_front: front = (front - 1) % capacity; store at front; size += 1.
    3. delete_front: clear items[front]; front = (front + 1) % capacity;
       size -= 1.
    4. delete_rear: clear items[(front + size - 1) % capacity]; size -= 1.
    5. Every operation first checks full / empty and returns False (or None)
       when it cannot proceed.

Why it works:
    The ring has no real beginning or end, so stepping front one slot
    backwards is as valid as stepping rear one slot forwards. Python's %
    returns a non-negative result, so (0 - 1) % 4 is 3.

Time complexity:
    O(1) for every operation.

Space complexity:
    O(capacity).

Edge cases:
    - insert_front on an empty deque (front moves back one slot, still fine).
    - Deleting from an empty deque / inserting into a full deque.
    - front moving below index 0 (wraps to capacity - 1).
    - Capacity 1.

Alternative approach:
    collections.deque(maxlen=...) or a doubly linked list; both hide the index
    arithmetic practised here.
"""


class CircularDeque:
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

    def insert_rear(self, value):
        if self.is_full():
            return False
        self.items[(self.front + self.size) % self.capacity] = value
        self.size += 1
        return True

    def insert_front(self, value):
        if self.is_full():
            return False
        self.front = (self.front - 1) % self.capacity  # step backwards
        self.items[self.front] = value
        self.size += 1
        return True

    def delete_front(self):
        if self.is_empty():
            return None
        value = self.items[self.front]
        self.items[self.front] = None
        self.front = (self.front + 1) % self.capacity
        self.size -= 1
        return value

    def delete_rear(self):
        if self.is_empty():
            return None
        rear_index = (self.front + self.size - 1) % self.capacity
        value = self.items[rear_index]
        self.items[rear_index] = None
        self.size -= 1
        return value

    def get_front(self):
        return None if self.is_empty() else self.items[self.front]

    def get_rear(self):
        if self.is_empty():
            return None
        return self.items[(self.front + self.size - 1) % self.capacity]


def show(label, deque):
    print("{:<18} raw={} front_index={} front={} rear={}".format(
        label, deque.items, deque.front, deque.get_front(), deque.get_rear()))


def main():
    deque = CircularDeque(4)
    deque.insert_rear(1)
    deque.insert_rear(2)
    show("insert_rear 1, 2", deque)
    deque.insert_front(3)
    show("insert_front 3", deque)
    deque.insert_front(4)
    show("insert_front 4", deque)
    print("insert_rear 5 on full ->", deque.insert_rear(5))
    print("delete_rear ->", deque.delete_rear())
    print("delete_front ->", deque.delete_front())
    show("after deletes", deque)

    empty = CircularDeque(2)
    print("delete_front on empty ->", empty.delete_front())
    print("insert_front on empty ->", empty.insert_front(9))
    show("front wrapped", empty)


if __name__ == "__main__":
    main()
