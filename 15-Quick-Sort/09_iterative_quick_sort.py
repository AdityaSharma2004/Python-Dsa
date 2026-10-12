"""
Problem title:
    Iterative Quick Sort with an Explicit Stack

Problem statement:
    Sort a list in place with quick sort WITHOUT recursion: keep the pending
    (low, high) ranges on a stack that you manage yourself. Process the
    smaller side first so the stack never holds more than O(log n) ranges.

What it teaches:
    - Every recursion can be turned into a loop plus a stack.
    - Pushing the larger range and handling the smaller one first bounds the
      stack depth to O(log n), even for sorted input.
    - Laravel analogy: a queue of pending jobs, each describing a slice of work.

Input example:
    [10, 7, 8, 9, 1, 5, 3, 6]

Expected output:
    [10, 7, 8, 9, 1, 5, 3, 6] -> [1, 3, 5, 6, 7, 8, 9, 10] (max stack size 3)
    ascending      sorted=True  max stack size=2
    descending     sorted=True  max stack size=2
    pseudo-random  sorted=True  max stack size=6
    duplicates     sorted=True  max stack size=3
    Empty: 0 []
    Single: 0 [5]

Approach used:
    Push (0, n - 1). While the stack is not empty: pop a range, partition it
    with Lomuto, then push the two sub-ranges (larger one first so the smaller
    one is popped and processed next).

Step-by-step logic:
    1. stack = [(0, n - 1)]; track the maximum stack size.
    2. Pop (low, high); skip if low >= high.
    3. p = partition(low, high); left = (low, p - 1); right = (p + 1, high).
    4. Push the larger of left/right first, then the smaller one.
    5. Repeat until the stack is empty.

Why it works:
    The stack replaces the call stack: every range still to be sorted is stored
    on it, and partitioning a range never touches elements outside it.
    Handling the smaller part next means each pending larger part is at least
    twice the size of the one being processed, so the stack depth is at most
    about log2(n).

Time complexity:
    Average O(n log n); worst O(n^2) (last-element pivot on sorted data).

Space complexity:
    O(log n) extra for the explicit stack (versus O(n) recursion in the worst
    case for the naive recursive version).

Edge cases:
    Empty list, single element, sorted and reverse-sorted data, duplicates,
    ranges of size 0 or 1 (skipped).

Alternative approach:
    Recursive quick sort (file 02); simpler to read but can use O(n) call
    stack in the worst case unless the smaller side is recursed first.
"""


def lomuto_partition(arr, low, high):
    """Partition arr[low..high] around arr[high]; return pivot's final index."""
    pivot = arr[high]
    boundary = low - 1
    for j in range(low, high):
        if arr[j] <= pivot:
            boundary += 1
            arr[boundary], arr[j] = arr[j], arr[boundary]
    arr[boundary + 1], arr[high] = arr[high], arr[boundary + 1]
    return boundary + 1


def iterative_quick_sort(arr):
    """Sort arr in place; return the largest stack size that was needed."""
    if len(arr) < 2:
        return 0
    stack = [(0, len(arr) - 1)]
    deepest = 1
    while stack:
        low, high = stack.pop()
        if low >= high:
            continue
        pivot_index = lomuto_partition(arr, low, high)
        left = (low, pivot_index - 1)
        right = (pivot_index + 1, high)
        left_size = left[1] - left[0]
        right_size = right[1] - right[0]
        # Push the larger range first so the smaller one is handled next.
        if left_size > right_size:
            stack.append(left)
            stack.append(right)
        else:
            stack.append(right)
            stack.append(left)
        if len(stack) > deepest:
            deepest = len(stack)
    return deepest


def main():
    data = [10, 7, 8, 9, 1, 5, 3, 6]
    before = list(data)
    depth = iterative_quick_sort(data)
    print(f"{before} -> {data} (max stack size {depth})")

    cases = [
        ("ascending", list(range(300))),
        ("descending", list(range(300, 0, -1))),
        ("pseudo-random", [(i * 7919) % 1009 for i in range(300)]),
        ("duplicates", [i % 5 for i in range(300)]),
    ]
    for name, values in cases:
        work = list(values)
        depth = iterative_quick_sort(work)
        ok = True
        for i in range(1, len(work)):
            if work[i - 1] > work[i]:
                ok = False
        print(f"{name:<14} sorted={ok}  max stack size={depth}")

    # Edge cases
    empty = []
    print("Empty:", iterative_quick_sort(empty), empty)
    single = [5]
    print("Single:", iterative_quick_sort(single), single)


if __name__ == "__main__":
    main()
