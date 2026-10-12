"""
Problem title:
    Keep a Live List Sorted (Online Insertion)

Problem statement:
    Numbers arrive one at a time (a stream). After every arrival, the list of
    values seen so far must be sorted. Print the list after each insertion and
    report the median at each step.

What it teaches:
    - Insertion sort as an "online" algorithm: it can sort data as it arrives.
    - Inserting one element into an already sorted list in O(n).

Input example:
    stream = [5, 2, 9, 1, 7]

Expected output:
    after 5: [5]  median=5
    after 2: [2, 5]  median=3.5
    after 9: [2, 5, 9]  median=5
    after 1: [1, 2, 5, 9]  median=3.5
    after 7: [1, 2, 5, 7, 9]  median=5

Approach used:
    Keep a sorted list. For each new value, append it and run one insertion-sort
    step (shift larger values right) to put it in place.

Step-by-step logic:
    1. Start with an empty sorted list.
    2. Append the new value at the end.
    3. Walk left from the end, shifting larger values right.
    4. Place the value; then read the median from the middle index.

Why it works:
    The list was sorted before the arrival, so only the new element can be out
    of place. One insertion step repairs that, restoring the sorted invariant.

Time complexity:
    O(n) per insertion, O(n^2) for n arrivals in total.

Space complexity:
    O(n) to store the values seen so far.

Edge cases:
    First value (list of size 1), duplicate values, even count (median is the
    average of the two middle values), empty stream.

Alternative approach:
    Two heaps give the running median in O(log n) per value.
"""


def insert_sorted(sorted_list, value):
    """Insert value into sorted_list so it stays sorted."""
    sorted_list.append(value)
    j = len(sorted_list) - 2
    while j >= 0 and sorted_list[j] > value:
        sorted_list[j + 1] = sorted_list[j]
        j -= 1
    sorted_list[j + 1] = value


def median_of_sorted(sorted_list):
    """Return the median of a non-empty sorted list."""
    n = len(sorted_list)
    mid = n // 2
    if n % 2 == 1:
        return sorted_list[mid]
    return (sorted_list[mid - 1] + sorted_list[mid]) / 2


def main():
    stream = [5, 2, 9, 1, 7]
    live = []
    for value in stream:
        insert_sorted(live, value)
        print(f"after {value}: {live}  median={median_of_sorted(live)}")


if __name__ == "__main__":
    main()
