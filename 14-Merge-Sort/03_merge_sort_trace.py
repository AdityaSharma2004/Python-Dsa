"""
Problem title:
    Merge Sort Trace (split and merge steps)

Problem statement:
    Run merge sort on a small list and print every split and every merge, indented
    by recursion depth, so the divide-and-conquer tree becomes visible.

What it teaches:
    - How the recursion tree of merge sort looks.
    - The order in which splits (going down) and merges (coming back up) happen.
    - Using a depth parameter to indent trace output.

Input example:
    [6, 5, 3, 1, 8, 7, 2, 4]

Expected output:
    Input: [6, 5, 3, 1, 8, 7, 2, 4]
    split  [6, 5, 3, 1, 8, 7, 2, 4] -> [6, 5, 3, 1] | [8, 7, 2, 4]
      split  [6, 5, 3, 1] -> [6, 5] | [3, 1]
        split  [6, 5] -> [6] | [5]
        merge  [6] + [5] -> [5, 6]
        split  [3, 1] -> [3] | [1]
        merge  [3] + [1] -> [1, 3]
      merge  [5, 6] + [1, 3] -> [1, 3, 5, 6]
      split  [8, 7, 2, 4] -> [8, 7] | [2, 4]
        split  [8, 7] -> [8] | [7]
        merge  [8] + [7] -> [7, 8]
        split  [2, 4] -> [2] | [4]
        merge  [2] + [4] -> [2, 4]
      merge  [7, 8] + [2, 4] -> [2, 4, 7, 8]
    merge  [1, 3, 5, 6] + [2, 4, 7, 8] -> [1, 2, 3, 4, 5, 6, 7, 8]
    Sorted: [1, 2, 3, 4, 5, 6, 7, 8]

Approach used:
    Standard recursive merge sort, with a `depth` argument. Print a "split" line
    before recursing and a "merge" line after both halves are sorted.

Step-by-step logic:
    1. Print the current list as a split line (if it has more than one element).
    2. Recurse on the left half, then on the right half (depth + 1).
    3. Merge the two sorted halves and print the merge line.
    4. Return the merged list.

Why it works:
    The trace does not change the algorithm; it only reports what each call sees.
    Reading the output top to bottom shows depth-first order of the recursion.

Time complexity:
    O(n log n) for the sort itself (printing adds O(n) lines of output).

Space complexity:
    O(n) extra for merged lists plus O(log n) recursion stack.

Edge cases:
    Single element (no split/merge lines), empty list, odd length (halves differ
    in size by one), duplicates.

Alternative approach:
    Collect the trace lines in a list and print once at the end; this is easier to
    test because the output can be compared programmatically.
"""


def merge(left, right):
    """Merge two sorted lists into one new sorted list."""
    result = []
    i = 0
    j = 0
    while i < len(left) and j < len(right):
        if left[i] <= right[j]:
            result.append(left[i])
            i += 1
        else:
            result.append(right[j])
            j += 1
    while i < len(left):
        result.append(left[i])
        i += 1
    while j < len(right):
        result.append(right[j])
        j += 1
    return result


def merge_sort_trace(items, depth=0):
    """Sort `items`, printing each split and merge indented by depth."""
    indent = "  " * depth
    if len(items) <= 1:
        return list(items)
    mid = len(items) // 2
    print(f"{indent}split  {items} -> {items[:mid]} | {items[mid:]}")
    left_sorted = merge_sort_trace(items[:mid], depth + 1)
    right_sorted = merge_sort_trace(items[mid:], depth + 1)
    merged = merge(left_sorted, right_sorted)
    print(f"{indent}merge  {left_sorted} + {right_sorted} -> {merged}")
    return merged


def main():
    data = [6, 5, 3, 1, 8, 7, 2, 4]
    print(f"Input: {data}")
    result = merge_sort_trace(data)
    print(f"Sorted: {result}")


if __name__ == "__main__":
    main()
