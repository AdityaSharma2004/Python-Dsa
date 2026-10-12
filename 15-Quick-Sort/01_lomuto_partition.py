"""
Problem title:
    Lomuto Partition

Problem statement:
    Write the Lomuto partition routine: choose the last element as the pivot and
    rearrange the list in place so that everything smaller than or equal to the
    pivot is on its left and everything larger is on its right. Return the final
    index of the pivot.

What it teaches:
    - The partition step, the heart of quick sort.
    - Maintaining a boundary index between "small" and "not yet processed/large".
    - Seeing that after partitioning the pivot is already in its final position.

Input example:
    [9, 4, 7, 3, 10, 5]  (pivot = last element = 5)

Expected output:
    [9, 4, 7, 3, 10, 5] -> [4, 3, 5, 9, 10, 7], pivot index=2, valid=True
    [1, 2, 3, 4, 5] -> [1, 2, 3, 4, 5], pivot index=4, valid=True
    [5, 4, 3, 2, 1] -> [1, 4, 3, 2, 5], pivot index=0, valid=True
    [4, 4, 4, 4] -> [4, 4, 4, 4], pivot index=3, valid=True
    [8] -> [8], pivot index=0, valid=True
    [2, 8, 7, 1, 3, 5, 6, 4] -> [2, 1, 3, 4, 7, 5, 6, 8], pivot index=3, valid=True

Approach used:
    Scan from left to right with index j. Keep i as the boundary of the "small"
    zone. Whenever arr[j] <= pivot, grow the small zone and swap arr[j] into it.
    At the end, swap the pivot into the slot right after the small zone.

Step-by-step logic:
    1. pivot = arr[high]; i = low - 1 (the small zone is empty).
    2. For j from low to high - 1: if arr[j] <= pivot then i += 1 and swap
       arr[i] with arr[j].
    3. Swap arr[i + 1] with arr[high] to put the pivot between the two zones.
    4. Return i + 1.

Why it works:
    Invariant: arr[low..i] <= pivot and arr[i+1..j-1] > pivot at every step. Each
    new element either extends the small zone (swap) or just extends the large zone
    (nothing to do). When j reaches high, placing the pivot at i + 1 splits the
    range correctly.

Time complexity:
    O(n) for one partition of n elements (one pass).

Space complexity:
    O(1): done in place with a few indices.

Edge cases:
    Single element, all elements smaller than the pivot (pivot stays last), all
    larger (pivot moves to the front), duplicates of the pivot, empty range.

Alternative approach:
    Hoare partition (file 03) uses two pointers moving towards each other and does
    fewer swaps on average.
"""


def lomuto_partition(arr, low, high):
    """Partition arr[low..high] around arr[high]; return the pivot's final index."""
    pivot = arr[high]
    boundary = low - 1  # last index of the "<= pivot" zone
    for j in range(low, high):
        if arr[j] <= pivot:
            boundary += 1
            arr[boundary], arr[j] = arr[j], arr[boundary]
    arr[boundary + 1], arr[high] = arr[high], arr[boundary + 1]
    return boundary + 1


def check_partition(arr, pivot_index):
    """Verify: left of pivot_index <= pivot <= ... right is greater."""
    pivot = arr[pivot_index]
    for k in range(pivot_index):
        if arr[k] > pivot:
            return False
    for k in range(pivot_index + 1, len(arr)):
        if arr[k] <= pivot:
            return False
    return True


def main():
    samples = [
        [9, 4, 7, 3, 10, 5],
        [1, 2, 3, 4, 5],
        [5, 4, 3, 2, 1],
        [4, 4, 4, 4],
        [8],
        [2, 8, 7, 1, 3, 5, 6, 4],
    ]
    for data in samples:
        before = list(data)
        index = lomuto_partition(data, 0, len(data) - 1)
        print(f"{before} -> {data}, pivot index={index}, valid={check_partition(data, index)}")


if __name__ == "__main__":
    main()
