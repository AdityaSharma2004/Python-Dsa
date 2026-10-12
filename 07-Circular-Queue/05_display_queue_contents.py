"""
Problem title:
    Display a Circular Queue (Logical vs Physical View)

Problem statement:
    Add two display methods to a circular queue: logical_view() returning the
    items in queue order (front to rear), and physical_view() returning the
    raw array with "_" for empty slots plus markers for front and rear.

What it teaches:
    - Traversing a ring from front for exactly "size" steps.
    - Why logical order differs from array order after wrap-around.
    - Writing a safe display that works when empty, full or wrapped.

Input example:
    capacity = 5; enqueue 1..5; dequeue twice; enqueue 6, 7

Expected output:
    empty   logical: [] | physical: _ | _ | _ | _ | _
    full    logical: [1, 2, 3, 4, 5] | physical: 1F | 2 | 3 | 4 | 5R
    after 2 dequeues: [3, 4, 5] | physical: _ | _ | 3F | 4 | 5R
    wrapped logical: [3, 4, 5, 6, 7] | physical: 6 | 7R | 3F | 4 | 5

Approach:
    Logical view: start at front, visit (front + i) % capacity for i in
    0..size-1. Physical view: loop over the array and tag front/rear indexes.

Step-by-step logic:
    1. If size == 0, the logical view is the empty list.
    2. Otherwise collect items[(front + i) % capacity] for i in range(size).
    3. For the physical view, convert None to "_" and append "F" for the front
       index and "R" for the rear index (both letters if they coincide).

Why it works:
    Exactly "size" items follow front around the ring, so counting steps avoids
    reading stale or empty slots.

Time complexity:
    O(capacity) to build either view.

Space complexity:
    O(capacity) for the returned view.

Edge cases:
    - Empty queue (front/rear markers not shown).
    - Full queue (loop must stop after size steps, not when it returns to
      front, otherwise it would never begin).
    - Items wrapped across the array end.

Alternative approach:
    Loop until the index returns to rear; needs a special case for a full queue.
"""


class CircularQueue:
    def __init__(self, capacity):
        self.capacity = capacity
        self.items = [None] * capacity
        self.front = 0
        self.size = 0

    def enqueue(self, value):
        if self.size == self.capacity:
            return False
        self.items[(self.front + self.size) % self.capacity] = value
        self.size += 1
        return True

    def dequeue(self):
        if self.size == 0:
            return None
        value = self.items[self.front]
        self.items[self.front] = None
        self.front = (self.front + 1) % self.capacity
        self.size -= 1
        return value

    def logical_view(self):
        """Items in queue order, front first."""
        view = []
        for step in range(self.size):
            view.append(self.items[(self.front + step) % self.capacity])
        return view

    def physical_view(self):
        """Raw array as strings, '_' for empty, F/R markers for the ends."""
        rear_index = (self.front + self.size - 1) % self.capacity
        cells = []
        for index in range(self.capacity):
            text = "_" if self.items[index] is None else str(self.items[index])
            if self.size > 0 and index == self.front:
                text += "F"
            if self.size > 0 and index == rear_index:
                text += "R"
            cells.append(text)
        return " | ".join(cells)


def main():
    queue = CircularQueue(5)
    print("empty   logical:", queue.logical_view(), "| physical:", queue.physical_view())
    for value in (1, 2, 3, 4, 5):
        queue.enqueue(value)
    print("full    logical:", queue.logical_view(), "| physical:", queue.physical_view())
    queue.dequeue()
    queue.dequeue()
    print("after 2 dequeues:", queue.logical_view(), "| physical:", queue.physical_view())
    queue.enqueue(6)
    queue.enqueue(7)
    print("wrapped logical:", queue.logical_view(), "| physical:", queue.physical_view())


if __name__ == "__main__":
    main()
