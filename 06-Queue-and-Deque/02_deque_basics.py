r"""
Problem: Use collections.deque as a Queue and a Double-Ended Queue

Problem statement:
    Demonstrate Python's collections.deque: use it as a FIFO queue, add and
    remove at both ends, rotate it, and compare the speed of removing from
    the front of a deque with removing from the front of a list.

What it teaches:
    The deque API (append, appendleft, pop, popleft, rotate, maxlen) and why
    deque is the right tool for queues.

Input example:
    deque of [1, 2, 3]; maxlen deque of size 3 fed with 1..5

Expected output:
    Queue use   : enqueue 1,2,3 -> deque([1, 2, 3])
    popleft()   : 1 -> deque([2, 3])
    appendleft(0): deque([0, 2, 3])
    pop()       : 3 -> deque([0, 2])
    extend [7, 8]: deque([0, 2, 7, 8])
    rotate(1)   : deque([8, 0, 2, 7])
    rotate(-2)  : deque([2, 7, 8, 0])
    maxlen=3 after 1..5: deque([3, 4, 5], maxlen=3)
    empty popleft -> pop from an empty deque
    removing front: deque and list give the same order: True

Approach:
    Call each deque method on small data and print the state after each one.

Step-by-step logic:
    1. append adds right, appendleft adds left; pop removes right, popleft
    removes left; all are O(1).
    2. rotate(k) shifts items right by k (left if k is negative).
    3. A deque with maxlen silently discards from the opposite end when full.
    4. A list's pop(0) shifts every other item, so it is O(n).

Why it works:
    CPython implements deque as a doubly linked list of fixed-size blocks, so
    both ends can be changed without moving the other elements.

Time complexity:
    append/pop/appendleft/popleft O(1); rotate(k) O(k); indexing in the
    middle O(n).

Space complexity:
    O(n).

Edge cases:
    popleft or pop on an empty deque raises IndexError; maxlen=0; rotating by
    more than the length (it wraps around).

Alternative approach:
    queue.Queue (thread-safe, slower) or a hand-written linked list queue.
"""

from collections import deque


def queue_demo():
    queue = deque()
    for value in (1, 2, 3):
        queue.append(value)
    print("Queue use   : enqueue 1,2,3 ->", queue)
    print("popleft()   :", queue.popleft(), "->", queue)
    return queue


def deque_ends_demo(dq):
    dq.appendleft(0)
    print("appendleft(0):", dq)
    print("pop()       :", dq.pop(), "->", dq)
    dq.extend([7, 8])
    print("extend [7, 8]:", dq)
    dq.rotate(1)
    print("rotate(1)   :", dq)
    dq.rotate(-2)
    print("rotate(-2)  :", dq)


def maxlen_demo():
    window = deque(maxlen=3)
    for value in range(1, 6):
        window.append(value)  # the oldest item falls out automatically
    print("maxlen=3 after 1..5:", window)


def empty_demo():
    try:
        deque().popleft()
    except IndexError as error:
        print("empty popleft ->", error)


def compare_with_list():
    """Remove from the front of both structures; the order must match."""
    items = list(range(5))
    dq = deque(items)
    from_list = [items.pop(0) for _ in range(5)]  # O(n) each
    from_deque = [dq.popleft() for _ in range(5)]  # O(1) each
    print("removing front: deque and list give the same order:",
          from_list == from_deque)


def main():
    dq = queue_demo()
    deque_ends_demo(dq)
    maxlen_demo()
    empty_demo()
    compare_with_list()


if __name__ == "__main__":
    main()
