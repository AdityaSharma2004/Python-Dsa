"""
Problem title:
    K Smallest Elements with Partial Selection Sort

Problem statement:
    Given a list and a number k, return the k smallest values in ascending
    order by running only the first k passes of Selection Sort. The rest of
    the list does not need to be sorted.

What it teaches:
    - Selection Sort builds the answer one finished element at a time, so you
      can stop early.
    - Partial sorting costs O(n * k) instead of O(n^2).
    - Typical use: "top 3 cheapest products" without sorting the whole table.

Input example:
    numbers = [64, 25, 12, 22, 11, 90, 3]
    k = 3

Expected output:
    Numbers: [64, 25, 12, 22, 11, 90, 3]
    3 smallest: [3, 11, 12]
    1 smallest: [3]
    k = 0: []
    k > length: [2, 5, 8]
    Duplicates: [1, 1, 4]
    Error: k must not be negative

Approach:
    Run the normal Selection Sort loop but only for position = 0 .. k - 1,
    then return the first k items.

Step-by-step logic:
    1. Copy the list and clamp k to the list length.
    2. For position in 0..k-1, find the smallest value in items[position:].
    3. Swap it into place.
    4. The first k slots now hold the k smallest values, in order.

Why it works:
    After pass i the first i + 1 slots are final (the i + 1 smallest values).
    Stopping after k passes leaves exactly the k smallest in front.

Time complexity:
    O(n * k): each of the k passes scans up to n items.

Space complexity:
    O(n) for the copy (O(1) extra apart from the copy).

Edge cases:
    - k = 0 returns an empty list.
    - k larger than the list length returns the fully sorted list.
    - Negative k is rejected with ValueError.
    - Duplicates are counted separately.

Alternative approach:
    A heap gives the k smallest in O(n log k); Quick Select finds the k-th
    smallest in O(n) on average.
"""


def k_smallest(values, k):
    """Return the k smallest values in ascending order."""
    if k < 0:
        raise ValueError("k must not be negative")
    items = list(values)
    k = min_of_two(k, len(items))
    for position in range(k):
        min_index = position
        for index in range(position + 1, len(items)):
            if items[index] < items[min_index]:
                min_index = index
        items[position], items[min_index] = items[min_index], items[position]
    return items[:k]


def min_of_two(first, second):
    """Smaller of two numbers (written by hand, no built-in min)."""
    if first < second:
        return first
    return second


def main():
    numbers = [64, 25, 12, 22, 11, 90, 3]
    print("Numbers:", numbers)
    print("3 smallest:", k_smallest(numbers, 3))
    print("1 smallest:", k_smallest(numbers, 1))

    # Edge cases
    print("k = 0:", k_smallest(numbers, 0))
    print("k > length:", k_smallest([5, 2, 8], 10))
    print("Duplicates:", k_smallest([4, 1, 4, 1, 4], 3))
    try:
        k_smallest(numbers, -1)
    except ValueError as error:
        print("Error:", error)


if __name__ == "__main__":
    main()
