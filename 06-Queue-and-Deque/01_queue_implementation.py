r"""
Problem: Implement a Queue with a Linked List

Problem statement:
    Build a queue (First-In-First-Out) with enqueue, dequeue, front, rear,
    is_empty and size. Both enqueue and dequeue must be O(1).

What it teaches:
    FIFO order, and why a linked list with head and tail pointers beats a
    plain Python list (list.pop(0) is O(n)).

Input example:
    enqueue 10, 20, 30; dequeue twice; enqueue 40; dequeue until empty

Expected output:
    enqueue(10) -> [10]
    enqueue(20) -> [10, 20]
    enqueue(30) -> [10, 20, 30]
    front=10 rear=30 size=3
    dequeue() -> 10
    dequeue() -> 20
    enqueue(40) -> [30, 40]
    dequeue() -> 30
    dequeue() -> 40
    is_empty() -> True
    dequeue() on empty -> Queue is empty

Approach:
    Keep a head pointer (front) and a tail pointer (rear). Enqueue attaches a
    node after the tail; dequeue detaches the head.

Step-by-step logic:
    1. enqueue(x): make a node; if empty head = tail = node, otherwise
    tail.next = node and tail = node.
    2. dequeue(): if empty raise an error; take head.data, move head to
    head.next; if head became None also set tail to None.
    3. front() and rear() read head.data and tail.data.
    4. A size counter is updated on every change.

Why it works:
    New items are added at one end and removed from the other, so the oldest
    item is always at the head. Pointers make both ends reachable in O(1).

Time complexity:
    All operations O(1).

Space complexity:
    O(n) for n stored items.

Edge cases:
    Dequeue or front on empty queue, dequeuing the last item (tail must be
    reset), enqueue after the queue became empty.

Alternative approach:
    collections.deque (see the next file), or a list with a moving front
    index (wastes memory unless compacted).
"""


class Node:
    def __init__(self, data):
        self.data = data
        self.next = None


class Queue:
    def __init__(self):
        self._head = None
        self._tail = None
        self._size = 0

    def enqueue(self, value):
        node = Node(value)
        if self._tail is None:
            self._head = self._tail = node
        else:
            self._tail.next = node
            self._tail = node
        self._size += 1

    def dequeue(self):
        if self._head is None:
            raise IndexError("Queue is empty")
        value = self._head.data
        self._head = self._head.next
        if self._head is None:  # queue became empty: reset the tail too
            self._tail = None
        self._size -= 1
        return value

    def front(self):
        if self._head is None:
            raise IndexError("Queue is empty")
        return self._head.data

    def rear(self):
        if self._tail is None:
            raise IndexError("Queue is empty")
        return self._tail.data

    def is_empty(self):
        return self._size == 0

    def size(self):
        return self._size

    def to_list(self):
        items, current = [], self._head
        while current is not None:
            items.append(current.data)
            current = current.next
        return items


def main():
    queue = Queue()
    for value in (10, 20, 30):
        queue.enqueue(value)
        print("enqueue(%d) ->" % value, queue.to_list())
    print("front=%d rear=%d size=%d" % (queue.front(), queue.rear(), queue.size()))
    print("dequeue() ->", queue.dequeue())
    print("dequeue() ->", queue.dequeue())
    queue.enqueue(40)
    print("enqueue(40) ->", queue.to_list())
    print("dequeue() ->", queue.dequeue())
    print("dequeue() ->", queue.dequeue())
    print("is_empty() ->", queue.is_empty())
    try:
        queue.dequeue()
    except IndexError as error:
        print("dequeue() on empty ->", error)


if __name__ == "__main__":
    main()
