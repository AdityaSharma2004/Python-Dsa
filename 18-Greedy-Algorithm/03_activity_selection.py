"""
Problem title:
    Activity Selection (Maximum Non-Overlapping Meetings)

Problem statement:
    Given meetings as (start, finish) pairs and a single room, choose the
    maximum number of meetings that do not overlap. A meeting may start at the
    exact time another one finishes.

What it teaches:
    * Choosing the correct greedy criterion: earliest FINISH time.
    * Why "earliest start" and "shortest duration" are wrong (counterexamples).

Input example:
    [(1,4),(3,5),(0,6),(5,7),(3,9),(5,9),(6,10),(8,11),(8,12),(2,14),(12,16)]

Expected output:
    Chosen meetings: [(1, 4), (5, 7), (8, 11), (12, 16)]
    Count: 4

    Counterexample for 'earliest start' rule:
    Earliest start picks : [(0, 100)]
    Earliest finish picks: [(1, 2), (3, 4)]

    Edge cases:
    Empty list -> []
    Touching meetings -> [(1, 5), (5, 8)]

Approach:
    Sort meetings by finish time. Always take the first meeting, then take any
    later meeting whose start >= the finish time of the last chosen meeting.

Step-by-step logic:
    1. Sort by finish time (hand-written merge sort).
    2. Pick the first meeting; remember its finish as `last_finish`.
    3. For every other meeting: if start >= last_finish, pick it and update
       `last_finish`; otherwise skip it.

Why it works:
    The meeting that finishes first frees the room as early as possible, so it
    leaves the most time for everything else. Any optimal schedule can swap
    its first meeting for the earliest-finishing one without causing overlap.

Time complexity:
    O(n log n) for sorting + O(n) for the single scan.

Space complexity:
    O(n) for the sorted copy and the chosen list.

Edge cases:
    * Empty list -> no meetings.
    * Meetings that touch (end 5, start 5) are allowed: use >=, not >.
    * Identical meetings -> only one can be chosen.

Alternative approach:
    Dynamic programming over meetings sorted by finish also works but is
    O(n log n) with more code; greedy is simpler and just as fast.
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


def select_activities(activities):
    """Return the chosen (start, finish) pairs using earliest-finish-first."""
    if not activities:
        return []
    by_finish = merge_sort(activities, lambda a, b: a[1] < b[1])
    chosen = [by_finish[0]]
    last_finish = by_finish[0][1]
    for start, finish in by_finish[1:]:
        if start >= last_finish:  # touching meetings are fine
            chosen.append((start, finish))
            last_finish = finish
    return chosen


def select_by_earliest_start(activities):
    """Wrong greedy rule, kept to demonstrate a counterexample."""
    by_start = merge_sort(activities, lambda a, b: a[0] < b[0])
    chosen = []
    last_finish = None
    for start, finish in by_start:
        if last_finish is None or start >= last_finish:
            chosen.append((start, finish))
            last_finish = finish
    return chosen


def main():
    meetings = [(1, 4), (3, 5), (0, 6), (5, 7), (3, 9), (5, 9),
                (6, 10), (8, 11), (8, 12), (2, 14), (12, 16)]
    chosen = select_activities(meetings)
    print("Chosen meetings:", chosen)
    print("Count:", len(chosen))

    print("\nCounterexample for 'earliest start' rule:")
    trap = [(0, 100), (1, 2), (3, 4)]
    print("Earliest start picks :", select_by_earliest_start(trap))
    print("Earliest finish picks:", select_activities(trap))

    print("\nEdge cases:")
    print("Empty list ->", select_activities([]))
    print("Touching meetings ->", select_activities([(1, 5), (5, 8)]))


if __name__ == "__main__":
    main()
