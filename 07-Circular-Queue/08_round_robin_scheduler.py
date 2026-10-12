"""
Problem title:
    Round-Robin CPU Scheduler with a Circular Queue

Problem statement:
    Each process has a name and a burst time (CPU time it needs). The CPU gives
    each process at most "quantum" time units per turn, in circular order.
    A process that is not finished goes to the back of the queue. Print the
    finish time of each process and its waiting time.

What it teaches:
    - A real use of a circular queue (OS scheduling, game turns, playlists).
    - Dequeue + enqueue as the "next turn" step.
    - Waiting time = finish time - burst time (all processes arrive at 0).

Input example:
    processes = P1:5, P2:3, P3:1, quantum = 2

Expected output:
    t= 2: P1 ran 2 unit(s), 3 left
    t= 4: P2 ran 2 unit(s), 1 left
    t= 5: P3 ran 1 unit(s), 0 left
    t= 7: P1 ran 2 unit(s), 1 left
    t= 8: P2 ran 1 unit(s), 0 left
    t= 9: P1 ran 1 unit(s), 0 left
    P1: burst=5 finish=9 waiting=4
    P2: burst=3 finish=8 waiting=5
    P3: burst=1 finish=5 waiting=4
    --- quantum 10 behaves like first come, first served ---
    t= 5: P1 ran 5 unit(s), 0 left
    t= 8: P2 ran 3 unit(s), 0 left
    t= 9: P3 ran 1 unit(s), 0 left
    P1: burst=5 finish=5 waiting=0
    P2: burst=3 finish=8 waiting=5
    P3: burst=1 finish=9 waiting=8

Approach:
    Put (name, remaining_time) pairs in a circular queue. Repeatedly dequeue
    the front, run it for min(quantum, remaining) units, advance the clock,
    and enqueue it again if time remains.

Step-by-step logic:
    1. Enqueue every process with its remaining time = burst time.
    2. While the queue is not empty: dequeue a process.
    3. run = quantum if remaining > quantum else remaining (no min() needed).
    4. clock += run, remaining -= run.
    5. If remaining > 0 enqueue it again, otherwise record finish = clock.
    6. waiting = finish - burst for each process.

Why it works:
    The queue keeps the processes in the order they should get the CPU, and
    re-enqueueing at the rear gives everyone a fair turn before anybody gets a
    second one.

Time complexity:
    O(T / quantum + n), where T is the total burst time (each turn is O(1)).

Space complexity:
    O(n) for the queue and result tables.

Edge cases:
    - Quantum larger than every burst (becomes first come, first served).
    - A burst of 0 (finishes at the moment its turn comes, using no time).
    - Single process.

Alternative approach:
    collections.deque gives the same behaviour; a fixed circular queue shows
    that n slots are enough because a process is never in the queue twice.
"""


class CircularQueue:
    def __init__(self, capacity):
        self.capacity = capacity
        self.items = [None] * capacity
        self.front = 0
        self.size = 0

    def is_empty(self):
        return self.size == 0

    def enqueue(self, value):
        self.items[(self.front + self.size) % self.capacity] = value
        self.size += 1

    def dequeue(self):
        value = self.items[self.front]
        self.items[self.front] = None
        self.front = (self.front + 1) % self.capacity
        self.size -= 1
        return value


def round_robin(processes, quantum):
    """processes: list of (name, burst). Return {name: (finish, waiting)}."""
    queue = CircularQueue(len(processes))
    for name, burst in processes:
        queue.enqueue((name, burst))
    bursts = dict(processes)

    clock = 0
    results = {}
    while not queue.is_empty():
        name, remaining = queue.dequeue()
        run = quantum if remaining > quantum else remaining
        clock += run
        remaining -= run
        print("t={:>2}: {} ran {} unit(s), {} left".format(clock, name, run, remaining))
        if remaining > 0:
            queue.enqueue((name, remaining))  # back of the line
        else:
            results[name] = (clock, clock - bursts[name])
    return results


def main():
    processes = [("P1", 5), ("P2", 3), ("P3", 1)]
    results = round_robin(processes, 2)
    for name, burst in processes:
        finish, waiting = results[name]
        print("{}: burst={} finish={} waiting={}".format(name, burst, finish, waiting))

    print("--- quantum 10 behaves like first come, first served ---")
    results = round_robin(processes, 10)
    for name, burst in processes:
        finish, waiting = results[name]
        print("{}: burst={} finish={} waiting={}".format(name, burst, finish, waiting))


if __name__ == "__main__":
    main()
