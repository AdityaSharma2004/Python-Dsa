"""
Problem title:
    Josephus Problem Using a Circular Queue

Problem statement:
    n people stand in a circle numbered 1..n. Starting from person 1, every
    k-th person is eliminated, and counting continues from the next person.
    Return the elimination order and the number of the last survivor.

What it teaches:
    - Simulating a circle with a queue by "rotating" (dequeue then enqueue).
    - Modelling circular traversal with the modulo operator.
    - Checking a simulation against a closed-form recurrence.

Input example:
    n = 7, k = 3

Expected output:
    n=7 k=3 -> eliminated [3, 6, 2, 7, 5, 1] | survivor 4 | recurrence 4
    n=5 k=1 -> eliminated [1, 2, 3, 4] | survivor 5 | recurrence 5
    n=1 k=4 -> eliminated [] | survivor 1 | recurrence 1
    n=6 k=10 -> eliminated [4, 3, 6, 1, 5] | survivor 2 | recurrence 2

Approach:
    Store the people in a fixed-size circular queue. To skip a person, dequeue
    and enqueue them again at the rear. The k-th person is dequeued and not
    re-added. Repeat until one person remains.

Step-by-step logic:
    1. Enqueue 1..n.
    2. Repeat k - 1 times: dequeue a person and enqueue them at the rear.
    3. Dequeue the next person: eliminated, record them.
    4. Continue from step 2 until size == 1; the last person is the survivor.
    5. Cross-check with the recurrence J(1) = 0, J(m) = (J(m-1) + k) % m
       (0-based), adding 1 at the end.

Why it works:
    Moving the front person to the rear keeps the circular order intact, so
    the queue front always points at the person who is counted next.

Time complexity:
    O(n * k) for the simulation; the recurrence check is O(n).

Space complexity:
    O(n) for the circular queue and the elimination list.

Edge cases:
    - k = 1 (people are eliminated in order 1, 2, 3, ...).
    - n = 1 (the only person survives, nothing eliminated).
    - k larger than n (counting goes around the circle several times).

Alternative approach:
    Use the recurrence alone for O(n) time and O(1) space, but it does not
    give the elimination order.
"""


class CircularQueue:
    def __init__(self, capacity):
        self.capacity = capacity
        self.items = [None] * capacity
        self.front = 0
        self.size = 0

    def enqueue(self, value):
        self.items[(self.front + self.size) % self.capacity] = value
        self.size += 1

    def dequeue(self):
        value = self.items[self.front]
        self.items[self.front] = None
        self.front = (self.front + 1) % self.capacity
        self.size -= 1
        return value


def josephus_simulation(n, k):
    """Return (elimination_order, survivor) for n people and step k."""
    queue = CircularQueue(n)
    for person in range(1, n + 1):
        queue.enqueue(person)

    eliminated = []
    while queue.size > 1:
        for _ in range(k - 1):  # skip k - 1 people by sending them to the rear
            queue.enqueue(queue.dequeue())
        eliminated.append(queue.dequeue())  # the k-th person leaves
    return eliminated, queue.dequeue()


def josephus_recurrence(n, k):
    """Survivor (1-based) using J(m) = (J(m-1) + k) % m."""
    survivor = 0
    for people in range(2, n + 1):
        survivor = (survivor + k) % people
    return survivor + 1


def main():
    for n, k in ((7, 3), (5, 1), (1, 4), (6, 10)):
        order, survivor = josephus_simulation(n, k)
        check = josephus_recurrence(n, k)
        print("n={} k={} -> eliminated {} | survivor {} | recurrence {}".format(
            n, k, order, survivor, check))


if __name__ == "__main__":
    main()
