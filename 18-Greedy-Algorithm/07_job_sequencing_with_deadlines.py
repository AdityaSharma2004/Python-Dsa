"""
Problem title:
    Job Sequencing with Deadlines

Problem statement:
    Each job takes exactly one unit of time and has a deadline (the latest
    time slot it may occupy, slots start at 1) and a profit earned only if the
    job is finished by its deadline. Schedule jobs to maximise total profit.

What it teaches:
    * Greedy by profit with a "latest free slot" placement rule.
    * Combining a sort with a simple slot array.

Input example:
    jobs = [("a", 2, 100), ("b", 1, 19), ("c", 2, 27), ("d", 1, 25),
            ("e", 3, 15)]   # (name, deadline, profit)

Expected output:
    Slot 1: c
    Slot 2: a
    Slot 3: e
    Total profit: 142

    Second example:
    Slots: ['j3', None, None, 'j1'] Total profit: 60

    Empty list: ([], 0)

Approach:
    Sort jobs by profit (highest first). Put each job in the LATEST free slot
    on or before its deadline; if none is free, drop the job.

Step-by-step logic:
    1. Sort jobs by profit descending.
    2. Create `slots` with one entry per time unit up to the largest deadline.
    3. For each job, check slots from its deadline down to 1; place it in the
       first empty slot and add its profit. Otherwise skip it.
    4. Return the filled slots and total profit.

Why it works:
    The most profitable job is always worth keeping. Placing it as late as
    possible leaves earlier slots free for jobs with tighter deadlines, so we
    never block a job we could have fitted.

Time complexity:
    O(n log n) for the sort + O(n * D) for slot searching, where D is the
    largest deadline (O(n^2) worst case). A union-find structure would reduce
    placement to near O(n).

Space complexity:
    O(n + D).

Edge cases:
    * Deadline larger than the number of jobs: slots only go up to the
      maximum deadline, and extra empty slots are fine.
    * Empty job list -> profit 0.
    * Jobs with equal profit -> stable sort keeps input order.

Alternative approach:
    Sort by deadline and keep a min-heap of chosen profits, evicting the
    smallest when too many jobs compete for time (O(n log n)).
"""


def merge_sort(items, comes_first):
    """Stable merge sort; `comes_first(a, b)` is True when a must precede b."""
    if len(items) <= 1:
        return list(items)
    middle = len(items) // 2
    left = merge_sort(items[:middle], comes_first)
    right = merge_sort(items[middle:], comes_first)
    merged = []
    i = j = 0
    while i < len(left) and j < len(right):
        if comes_first(right[j], left[i]):
            merged.append(right[j])
            j += 1
        else:
            merged.append(left[i])
            i += 1
    merged.extend(left[i:])
    merged.extend(right[j:])
    return merged


def largest_deadline(jobs):
    """Return the biggest deadline in the job list (0 if empty)."""
    largest = 0
    for _, deadline, _ in jobs:
        if deadline > largest:
            largest = deadline
    return largest


def schedule_jobs(jobs):
    """Return (slots, total_profit); slots[t-1] is the job name in slot t."""
    by_profit = merge_sort(jobs, lambda a, b: a[2] > b[2])
    slots = [None] * largest_deadline(jobs)
    total_profit = 0
    for name, deadline, profit in by_profit:
        # Try the latest free slot not after the deadline
        slot = deadline
        while slot >= 1:
            if slots[slot - 1] is None:
                slots[slot - 1] = name
                total_profit += profit
                break
            slot -= 1
    return slots, total_profit


def main():
    jobs = [("a", 2, 100), ("b", 1, 19), ("c", 2, 27), ("d", 1, 25),
            ("e", 3, 15)]
    slots, profit = schedule_jobs(jobs)
    for index, name in enumerate(slots, start=1):
        print(f"Slot {index}: {name}")
    print("Total profit:", profit)

    print("\nSecond example:")
    jobs2 = [("j1", 4, 20), ("j2", 1, 10), ("j3", 1, 40), ("j4", 1, 30)]
    slots2, profit2 = schedule_jobs(jobs2)
    print("Slots:", slots2, "Total profit:", profit2)

    print("\nEmpty list:", schedule_jobs([]))


if __name__ == "__main__":
    main()
