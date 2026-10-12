"""
Problem title:
    Ring Buffer That Overwrites the Oldest Item

Problem statement:
    Build a "last N events" log. It is a circular queue of fixed capacity, but
    when it is full a new item REPLACES the oldest one instead of being
    refused. Provide add(value) and contents() (oldest to newest).

What it teaches:
    - A circular queue used as a rolling window (logs, sensor data, undo
      history).
    - Moving the front pointer forward when the buffer is full.
    - Counting how many items were dropped.

Input example:
    capacity = 3; add 1, 2, 3, 4, 5

Expected output:
    add 1 -> contents: [1] | raw: [1, None, None] | dropped: 0
    add 2 -> contents: [1, 2] | raw: [1, 2, None] | dropped: 0
    add 3 -> contents: [1, 2, 3] | raw: [1, 2, 3] | dropped: 0
    add 4 -> contents: [2, 3, 4] | raw: [4, 2, 3] | dropped: 1
    add 5 -> contents: [3, 4, 5] | raw: [4, 5, 3] | dropped: 2
    capacity 1 keeps only the latest: ['c']

Approach:
    Keep items, front (oldest), size and a dropped counter. Writing position
    is (front + size) % capacity while there is room; when full, that same
    position equals front, so we overwrite front and advance it.

Step-by-step logic:
    1. If size < capacity: write at (front + size) % capacity, size += 1.
    2. Otherwise: write at front (the oldest slot), front = (front + 1) %
       capacity, dropped += 1. Size stays equal to capacity.
    3. contents() reads size items starting at front.

Why it works:
    When the ring is full the slot after the newest item is the oldest item,
    so overwriting it removes exactly the item that should leave the window.

Time complexity:
    O(1) per add; O(capacity) for contents().

Space complexity:
    O(capacity).

Edge cases:
    - Adding fewer items than capacity (nothing dropped).
    - Capacity 1 (always holds only the latest item).
    - Adding many more items than capacity (front wraps many times).

Alternative approach:
    collections.deque(maxlen=capacity) does the same job in one line, but it
    hides the pointer logic practised here.
"""


class RingBuffer:
    def __init__(self, capacity):
        if capacity < 1:
            raise ValueError("capacity must be at least 1")
        self.capacity = capacity
        self.items = [None] * capacity
        self.front = 0
        self.size = 0
        self.dropped = 0

    def add(self, value):
        """Store value; when full, overwrite the oldest item."""
        if self.size < self.capacity:
            self.items[(self.front + self.size) % self.capacity] = value
            self.size += 1
        else:
            self.items[self.front] = value  # the oldest slot is reused
            self.front = (self.front + 1) % self.capacity
            self.dropped += 1

    def contents(self):
        """Return stored values from oldest to newest."""
        result = []
        for step in range(self.size):
            result.append(self.items[(self.front + step) % self.capacity])
        return result


def main():
    buffer = RingBuffer(3)
    for value in (1, 2, 3, 4, 5):
        buffer.add(value)
        print("add", value, "-> contents:", buffer.contents(),
              "| raw:", buffer.items, "| dropped:", buffer.dropped)

    single = RingBuffer(1)
    for value in ("a", "b", "c"):
        single.add(value)
    print("capacity 1 keeps only the latest:", single.contents())


if __name__ == "__main__":
    main()
