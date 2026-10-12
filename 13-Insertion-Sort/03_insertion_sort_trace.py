"""
Problem title:
    Insertion Sort Pass-by-Pass Trace

Problem statement:
    Run insertion sort on a list and print the list after every pass, marking
    the sorted part and the key that was inserted.

What it teaches:
    - Visualising the loop invariant (sorted prefix grows by one each pass).
    - Using a trace to debug and to dry-run algorithms by hand.

Input example:
    [6, 3, 8, 2, 5]

Expected output:
    Start   : [6] 3 8 2 5
    Pass 1  : [3 6] 8 2 5   (inserted 3)
    Pass 2  : [3 6 8] 2 5   (inserted 8)
    Pass 3  : [2 3 6 8] 5   (inserted 2)
    Pass 4  : [2 3 5 6 8]   (inserted 5)
    Final   : [2, 3, 5, 6, 8]

Approach used:
    Standard insertion sort with a print statement after each insertion. The
    sorted prefix is shown in brackets.

Step-by-step logic:
    1. Print the starting list.
    2. For each i, extract key and shift larger sorted elements right.
    3. Insert key and print: the prefix arr[0..i] inside [ ], the rest outside.

Why it works:
    After pass i the first i+1 elements are sorted, which is what the brackets
    show; the printed state therefore proves the invariant at every step.

Time complexity:
    O(n^2) for the sort itself; printing adds O(n) per pass, still O(n^2) total.

Space complexity:
    O(1) for sorting (the printed text is temporary).

Edge cases:
    Empty or single element lists print no passes; already sorted lists show
    keys that do not move.

Alternative approach:
    Return a list of snapshots instead of printing, useful for unit tests.
"""


def format_state(arr, sorted_count):
    """Return a string with the sorted prefix wrapped in brackets."""
    left = " ".join(str(x) for x in arr[:sorted_count])
    right = " ".join(str(x) for x in arr[sorted_count:])
    return f"[{left}] {right}".rstrip()


def insertion_sort_with_trace(arr):
    """Sort arr in place, printing the state after every pass."""
    print(f"Start   : {format_state(arr, 1 if arr else 0)}")
    for i in range(1, len(arr)):
        key = arr[i]
        j = i - 1
        while j >= 0 and arr[j] > key:
            arr[j + 1] = arr[j]
            j -= 1
        arr[j + 1] = key
        print(f"Pass {i:<2} : {format_state(arr, i + 1)}   (inserted {key})")
    return arr


def main():
    data = [6, 3, 8, 2, 5]
    result = insertion_sort_with_trace(data)
    print("Final   :", result)


if __name__ == "__main__":
    main()
