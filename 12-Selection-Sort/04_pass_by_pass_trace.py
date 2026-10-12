"""
Problem title:
    Selection Sort with a Pass-by-Pass Trace

Problem statement:
    Run Selection Sort and print, for every pass, which index was chosen as
    the minimum, what was swapped and how the list looks afterwards. The
    sorted part is marked with a bar "|".

What it teaches:
    - How the sorted prefix grows by exactly one element per pass.
    - Reading the algorithm as snapshots.
    - Why Selection Sort picks first and swaps once.

Input example:
    numbers = [29, 10, 14, 37, 13]

Expected output:
    Start : | 29 10 14 37 13
    Pass 1: min=10 (swap index 0 <-> 1) -> 10 | 29 14 37 13
    Pass 2: min=13 (swap index 1 <-> 4) -> 10 13 | 14 37 29
    Pass 3: min=14 (no swap needed) -> 10 13 14 | 37 29
    Pass 4: min=29 (swap index 3 <-> 4) -> 10 13 14 29 | 37
    Result: [10, 13, 14, 29, 37]
    Sorted input trace: ['Pass 1: min=1 (no swap needed) -> 1 | 2 3', 'Pass 2: min=2 (no swap needed) -> 1 2 | 3']
    Empty trace: []

Approach:
    Standard Selection Sort that returns a list of trace lines instead of
    printing inside the sorting loops.

Step-by-step logic:
    1. For position i find min_index in items[i:].
    2. Swap if min_index differs from i.
    3. Build a text line: pass number, chosen value, swap info, and the list
       drawn as sorted | unsorted.
    4. After the last pass the whole list is sorted.

Why it works:
    The bar always sits right after the settled prefix; everything on its
    left is final because it is the smallest of what was left at that time.

Time complexity:
    O(n^2); building the text lines adds O(n) per pass, also O(n^2) total.

Space complexity:
    O(n^2) for the stored trace lines (O(1) extra for the sort itself).

Edge cases:
    - Sorted input: every pass reports "no swap needed".
    - Empty / single element: no passes.
    - Duplicates: the first smallest occurrence is chosen.

Alternative approach:
    Print directly inside the loop - simpler but harder to reuse or test.
"""


def format_state(items, sorted_count):
    """Draw the list as 'sorted | unsorted'."""
    left = " ".join(str(value) for value in items[:sorted_count])
    right = " ".join(str(value) for value in items[sorted_count:])
    return (left + " | " + right).strip()


def selection_sort_trace(values):
    """Return (sorted_list, trace_lines)."""
    items = list(values)
    trace = []
    for position in range(len(items) - 1):
        min_index = position
        for index in range(position + 1, len(items)):
            if items[index] < items[min_index]:
                min_index = index
        if min_index != position:
            note = "swap index %d <-> %d" % (position, min_index)
            items[position], items[min_index] = items[min_index], items[position]
        else:
            note = "no swap needed"
        trace.append("Pass %d: min=%d (%s) -> %s"
                     % (position + 1, items[position], note,
                        format_state(items, position + 1)))
    return items, trace


def main():
    numbers = [29, 10, 14, 37, 13]
    print("Start :", format_state(numbers, 0))
    result, trace = selection_sort_trace(numbers)
    for line in trace:
        print(line)
    print("Result:", result)

    # Edge cases
    print("Sorted input trace:", selection_sort_trace([1, 2, 3])[1])
    print("Empty trace:", selection_sort_trace([])[1])


if __name__ == "__main__":
    main()
