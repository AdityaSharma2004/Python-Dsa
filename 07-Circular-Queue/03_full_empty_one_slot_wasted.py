"""
Problem title:
    Full vs Empty Without a Size Counter (One Wasted Slot)

Problem statement:
    Implement a circular queue that stores only front and rear indexes (no size
    counter). Decide "empty" and "full" using index comparisons alone. A queue
    created with capacity n can hold at most n - 1 items.

What it teaches:
    - The classic ambiguity: front == rear can mean empty OR full.
    - Sacrificing one slot to remove the ambiguity.
    - The full test (rear + 1) % n == front.

Input example:
    n = 4 slots (usable capacity 3); enqueue 1, 2, 3, 4; dequeue; enqueue 4

Expected output:
    start  : front=0 rear=0 slots=[None, None, None, None] empty=True full=False
    enq 1 -> ok      front=0 rear=1 slots=[1, None, None, None] empty=False full=False
    enq 2 -> ok      front=0 rear=2 slots=[1, 2, None, None] empty=False full=False
    enq 3 -> ok      front=0 rear=3 slots=[1, 2, 3, None] empty=False full=True
    enq 4 -> refused front=0 rear=3 slots=[1, 2, 3, None] empty=False full=True
    deq -> 1
    state  : front=1 rear=3 slots=[None, 2, 3, None] empty=False full=False
    enq 4 -> True
    state  : front=1 rear=0 slots=[None, 2, 3, 4] empty=False full=True
    drained: front=0 rear=0 slots=[None, None, None, None] empty=True full=False

Approach:
    front points at the oldest item. rear points at the NEXT free slot.
    Empty when front == rear. Full when (rear + 1) % n == front.

Step-by-step logic:
    1. Start with front = rear = 0 (empty).
    2. enqueue: if full -> refuse; else items[rear] = x; rear = (rear + 1) % n.
    3. dequeue: if empty -> refuse; else read items[front];
       front = (front + 1) % n.

Why it works:
    Because the queue never fills the last slot, rear can never catch up to
    front by adding an item, so front == rear can only mean empty.

Time complexity:
    O(1) for all operations.

Space complexity:
    O(n) array, one slot always unused.

Edge cases:
    - Slot count 1 can store nothing (always both empty and full); we reject
      slot counts below 2.
    - Wrap-around of both pointers independently.

Alternative approach:
    Keep a size counter or a boolean "is_full" flag and use every slot.
"""


class OneSlotWastedQueue:
    def __init__(self, slots):
        if slots < 2:
            raise ValueError("need at least 2 slots")
        self.slots = slots
        self.items = [None] * slots
        self.front = 0
        self.rear = 0  # next free position

    def is_empty(self):
        return self.front == self.rear

    def is_full(self):
        return (self.rear + 1) % self.slots == self.front

    def enqueue(self, value):
        if self.is_full():
            return False
        self.items[self.rear] = value
        self.rear = (self.rear + 1) % self.slots
        return True

    def dequeue(self):
        if self.is_empty():
            return None
        value = self.items[self.front]
        self.items[self.front] = None
        self.front = (self.front + 1) % self.slots
        return value

    def state(self):
        return "front={} rear={} slots={} empty={} full={}".format(
            self.front, self.rear, self.items, self.is_empty(), self.is_full())


def main():
    queue = OneSlotWastedQueue(4)
    print("start  :", queue.state())
    for value in (1, 2, 3, 4):
        accepted = queue.enqueue(value)
        print("enq", value, "->", "ok     " if accepted else "refused", queue.state())
    print("deq ->", queue.dequeue())
    print("state  :", queue.state())
    print("enq 4 ->", queue.enqueue(4))
    print("state  :", queue.state())
    while not queue.is_empty():
        queue.dequeue()
    print("drained:", queue.state())


if __name__ == "__main__":
    main()
