"""
Problem title:
    Fractional Knapsack with a Max-Heap

Problem statement:
    Solve fractional knapsack without sorting all items. Build a max-heap
    keyed by value/weight ratio and repeatedly extract the best item until the
    bag is full. This is faster when only a few items fit in the bag.

What it teaches:
    - Using a heap as a "give me the current best item" structure.
    - The heap-based alternative to sorting.
    - heapq in Python is a MIN-heap, so store negative ratios.

Input example:
    weights = [10, 20, 30, 5, 15], values = [60, 100, 120, 50, 45],
    capacity = 40

Expected output:
    capacity  40: value 230.00 | items examined 4 of 5 | [1.0, 1.0, 0.16666666666666666, 1.0, 0.0]
    capacity   5: value  50.00 | items examined 1 of 5 | [0.0, 0.0, 0.0, 1.0, 0.0]
    capacity   0: value   0.00 | items examined 0 of 5 | [0.0, 0.0, 0.0, 0.0, 0.0]
    capacity 200: value 375.00 | items examined 5 of 5 | [1.0, 1.0, 1.0, 1.0, 1.0]

Approach:
    Push (-ratio, index) for each item with heapq.heapify (O(n)), then pop the
    best item, take it whole or as a fraction, and stop when the bag is full.

Step-by-step logic:
    1. heap = [(-value / weight, index) ...]; heapq.heapify(heap).
    2. While the heap is not empty and capacity remains: pop the smallest
       tuple, which is the highest ratio.
    3. Whole item fits: take it; else take remaining / weight and stop.
    4. Count the pops to show how many items were examined.

Why it works:
    A heap always exposes the maximum remaining ratio at its root, which is
    exactly the greedy choice, without ordering the items we never reach.

Time complexity:
    O(n + k log n), where k is the number of items examined (k <= n); the
    worst case is O(n log n), the same as sorting.

Space complexity:
    O(n) for the heap.

Edge cases:
    - Capacity 0 (nothing popped).
    - Heap empties before the bag is full (take everything).
    - Equal ratios (the smaller index pops first because tuples compare).

Alternative approach:
    Sort once and scan (problem 01); simpler and the same worst-case cost.
"""
import heapq


def heap_fractional_knapsack(weights, values, capacity):
    """Return (total_value, items_examined, fractions)."""
    heap = []
    for index in range(len(weights)):
        heap.append((-values[index] / weights[index], index))  # negative: max-heap
    heapq.heapify(heap)

    fractions = [0.0] * len(weights)
    total = 0.0
    remaining = capacity
    examined = 0
    while heap and remaining > 0:
        negative_ratio, index = heapq.heappop(heap)
        examined += 1
        if weights[index] <= remaining:
            fractions[index] = 1.0
            total += values[index]
            remaining -= weights[index]
        else:
            fractions[index] = remaining / weights[index]
            total += -negative_ratio * remaining
            remaining = 0
    return total, examined, fractions


def main():
    weights = [10, 20, 30, 5, 15]
    values = [60, 100, 120, 50, 45]
    for capacity in (40, 5, 0, 200):
        total, examined, fractions = heap_fractional_knapsack(weights, values, capacity)
        print("capacity {:>3}: value {:>6.2f} | items examined {} of {} | {}".format(
            capacity, total, examined, len(weights), fractions))


if __name__ == "__main__":
    main()
