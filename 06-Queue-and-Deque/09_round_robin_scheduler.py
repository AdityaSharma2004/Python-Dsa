r"""
Problem: Round-Robin CPU Scheduling with a Queue

Problem statement:
    Several processes need some CPU time (burst time). A scheduler gives each
    process at most a fixed time slice (quantum) in turn. Unfinished processes
    go to the back of the queue. Report finish times and waiting times.

What it teaches:
    A real use of a FIFO queue: fair rotation of work, and tracking time.

Input example:
    processes: P1=5, P2=3, P3=1 (all arrive at time 0), quantum = 2

Expected output:
    t=0-2 P1 (remaining 3)
    t=2-4 P2 (remaining 1)
    t=4-5 P3 finished
    t=5-7 P1 (remaining 1)
    t=7-8 P2 finished
    t=8-9 P1 finished
    Process  Burst  Finish  Turnaround  Waiting
    P1       5      9       9           4
    P2       3      8       8           5
    P3       1      5       5           4
    Average waiting time: 4.33

Approach:
    Keep a queue of (name, remaining time). Take the front, run it for
    min(quantum, remaining) units, then requeue it if work is left.

Step-by-step logic:
    1. Enqueue all processes in order.
    2. Dequeue the front process and run for run = quantum, or its remaining
    time if that is smaller (an if statement, no min()).
    3. Advance the clock by run and reduce the remaining time.
    4. If remaining > 0 enqueue it again; otherwise record the finish time.
    5. Turnaround = finish - arrival (0); waiting = turnaround - burst.

Why it works:
    The queue guarantees each unfinished process gets another turn only after
    all the others ahead of it, so nobody starves.

Time complexity:
    O(T / q + n), where T is the total burst time and q the quantum (number of
    time slices); each slice is O(1).

Space complexity:
    O(n).

Edge cases:
    Quantum larger than all bursts (becomes first-come-first-served), quantum
    of 1, a single process, burst times that are exact multiples of the
    quantum, an empty process list.

Alternative approach:
    First-come-first-served or shortest-job-first scheduling, which have
    different waiting-time trade-offs. Processes with different arrival
    times need an extra arrival queue.
"""

from collections import deque


def round_robin(bursts, quantum):
    """bursts: list of (name, burst_time). Returns (log, finish_times)."""
    queue = deque(bursts)
    clock = 0
    log = []
    finish = {}
    while queue:
        name, remaining = queue.popleft()
        run = quantum
        if remaining < quantum:
            run = remaining
        start = clock
        clock += run
        remaining -= run
        if remaining > 0:
            queue.append((name, remaining))
            log.append("t=%d-%d %s (remaining %d)" % (start, clock, name, remaining))
        else:
            finish[name] = clock
            log.append("t=%d-%d %s finished" % (start, clock, name))
    return log, finish


def main():
    bursts = [("P1", 5), ("P2", 3), ("P3", 1)]
    log, finish = round_robin(bursts, 2)
    for line in log:
        print(line)
    print("Process  Burst  Finish  Turnaround  Waiting")
    total_waiting = 0
    for name, burst in bursts:
        turnaround = finish[name]  # all arrive at time 0
        waiting = turnaround - burst
        total_waiting += waiting
        print("%-8s %-6d %-7d %-11d %d" % (name, burst, finish[name], turnaround, waiting))
    print("Average waiting time: %.2f" % (total_waiting / len(bursts)))


if __name__ == "__main__":
    main()
