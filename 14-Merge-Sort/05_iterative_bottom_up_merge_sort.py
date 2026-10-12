"""
Problem title:
    Iterative (Bottom-Up) Merge Sort

Problem statement:
    Sort a list with merge sort without using recursion. Start with runs of size 1
    and repeatedly merge neighbouring runs, doubling the run size each pass.

What it teaches:
    - Converting a recursion into loops.
    - Bottom-up thinking: build sorted blocks of size 1, 2, 4, 8, ...
    - Merging inside one array using a temporary buffer and index ranges.

Input example:
    [5, 2, 9, 1, 5, 6, 3]

Expected output:
    [5, 2, 9, 1, 5, 6, 3] -> [1, 2, 3, 5, 5, 6, 9]
    [] -> []
    [1] -> [1]
    [4, 3, 2, 1] -> [1, 2, 3, 4]
    [1, 2, 3, 4, 5, 6] -> [1, 2, 3, 4, 5, 6]
    [10, -3, 7, 7, 0, -3, 2, 8, 1] -> [-3, -3, 0, 1, 2, 7, 7, 8, 10]

Approach used:
    width = 1. In each pass, merge every pair of adjacent blocks of length `width`
    from the source list into a second buffer. Swap the two lists and double the
    width until width >= n.

Step-by-step logic:
    1. source = copy of the input, buffer = list of the same length.
    2. For start in 0, 2*width, 4*width, ...: mid = min(start + width, n) and
       end = min(start + 2*width, n) (clamped by hand), merge source[start:mid]
       with source[mid:end] into buffer[start:end].
    3. Swap source and buffer; width = width * 2.
    4. Stop when width >= n; source holds the sorted data.

Why it works:
    After the pass with block size w, every block of w items is sorted. Merging two
    adjacent sorted blocks gives a sorted block of 2w items. When the block size
    reaches n, the whole list is one sorted block.

Time complexity:
    O(n log n): about log2(n) passes, each doing O(n) merge work.

Space complexity:
    O(n) for the buffer, but O(1) stack space (no recursion).

Edge cases:
    Empty list, single element, length that is not a power of two (the last block
    in a pass may be shorter or have no partner), duplicates.

Alternative approach:
    Recursive top-down merge sort (file 02) is shorter to write but uses O(log n)
    stack frames.
"""


def smaller_of(a, b):
    """Return the smaller of two integers (helper to avoid the min() built-in)."""
    if a < b:
        return a
    return b


def merge_ranges(source, buffer, start, mid, end):
    """Merge source[start:mid] and source[mid:end] into buffer[start:end]."""
    i = start
    j = mid
    k = start
    while i < mid and j < end:
        if source[i] <= source[j]:  # "<=" keeps the sort stable
            buffer[k] = source[i]
            i += 1
        else:
            buffer[k] = source[j]
            j += 1
        k += 1
    while i < mid:
        buffer[k] = source[i]
        i += 1
        k += 1
    while j < end:
        buffer[k] = source[j]
        j += 1
        k += 1


def bottom_up_merge_sort(items):
    """Return a new list sorted ascending, using loops only."""
    n = len(items)
    source = list(items)
    buffer = [0] * n
    width = 1
    while width < n:
        for start in range(0, n, 2 * width):
            mid = smaller_of(start + width, n)
            end = smaller_of(start + 2 * width, n)
            merge_ranges(source, buffer, start, mid, end)
        source, buffer = buffer, source  # the merged data is now in `source`
        width *= 2
    return source


def main():
    samples = [
        [5, 2, 9, 1, 5, 6, 3],
        [],
        [1],
        [4, 3, 2, 1],
        [1, 2, 3, 4, 5, 6],
        [10, -3, 7, 7, 0, -3, 2, 8, 1],
    ]
    for data in samples:
        print(f"{data} -> {bottom_up_merge_sort(data)}")


if __name__ == "__main__":
    main()
