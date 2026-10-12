"""
Problem title:
    Randomized Quick Sort

Problem statement:
    Sort a list in place with quick sort that chooses its pivot at random. Show it
    handles already-sorted and reverse-sorted data without the O(n^2) slowdown
    that a fixed last-element pivot causes.

What it teaches:
    - Randomization as a defence against bad inputs: expected O(n log n) for all
      inputs.
    - Seeding a random generator so results are reproducible.
    - Measuring recursion depth to see that splits stay balanced.

Input example:
    sorted list 0..399, reverse list 400..1, and a list with duplicates

Expected output:
    Deepest recursion level (smaller means better balanced)
    input        fixed pivot  random pivot  sorted?
    ascending            399            17  True
    descending           399            17  True
    duplicates           n/a            63  True
    [9, 3, 7, 3, 1, 8, 2] -> [1, 2, 3, 3, 7, 8, 9]

Approach used:
    Pick a random index in [low, high], swap it into the last position and run the
    Lomuto partition. Track the deepest recursion level reached.

Step-by-step logic:
    1. random_index = random.randint(low, high); swap it with arr[high].
    2. Partition with Lomuto around arr[high].
    3. Recurse on both sides, passing depth + 1 and remembering the maximum depth.
    4. Compare the depth with the depth of a plain last-element pivot version.

Why it works:
    No fixed input can force bad splits because the pivot is chosen by chance. The
    expected number of comparisons is about 2 n ln n, and a bad split is very
    unlikely at every level.

Time complexity:
    Expected O(n log n) for any input; worst case O(n^2) is still possible but
    has a vanishingly small probability.

Space complexity:
    O(1) extra data plus expected O(log n) recursion stack.

Edge cases:
    Empty list, one element, all equal elements (still quadratic with Lomuto;
    see file 07), already sorted, reversed.

Alternative approach:
    Median of three (file 05) is deterministic and also avoids the sorted-input
    problem, but adversarial inputs can still defeat it.
"""

import random


def lomuto_partition(arr, low, high):
    """Partition around arr[high]; return the pivot's final index."""
    pivot = arr[high]
    boundary = low - 1
    for j in range(low, high):
        if arr[j] <= pivot:
            boundary += 1
            arr[boundary], arr[j] = arr[j], arr[boundary]
    arr[boundary + 1], arr[high] = arr[high], arr[boundary + 1]
    return boundary + 1


def randomized_quick_sort(arr, low, high, depth, deepest, randomize=True):
    """Sort arr[low..high] in place. deepest[0] records the maximum depth."""
    if depth > deepest[0]:
        deepest[0] = depth
    if low >= high:
        return
    if randomize:
        chosen = random.randint(low, high)  # a random pivot candidate
        arr[chosen], arr[high] = arr[high], arr[chosen]
    p = lomuto_partition(arr, low, high)
    randomized_quick_sort(arr, low, p - 1, depth + 1, deepest, randomize)
    randomized_quick_sort(arr, p + 1, high, depth + 1, deepest, randomize)


def run(data, randomize):
    """Sort a copy; return (sorted_list, deepest recursion depth)."""
    work = list(data)
    deepest = [0]
    randomized_quick_sort(work, 0, len(work) - 1, 0, deepest, randomize)
    return work, deepest[0]


def is_sorted_list(values):
    """True if values are in non-decreasing order."""
    for i in range(1, len(values)):
        if values[i - 1] > values[i]:
            return False
    return True


def main():
    random.seed(42)  # makes every run print the same numbers
    n = 400
    cases = [
        ("ascending", list(range(n))),
        ("descending", list(range(n, 0, -1))),
        ("duplicates", [i % 7 for i in range(n)]),
    ]
    print("Deepest recursion level (smaller means better balanced)")
    print(f"{'input':<11}{'fixed pivot':>13}{'random pivot':>14}  sorted?")
    for name, data in cases:
        if name == "duplicates":
            fixed_depth = "n/a"
        else:
            fixed_result, fixed_depth = run(data, randomize=False)
        random_result, random_depth = run(data, randomize=True)
        print(f"{name:<11}{fixed_depth:>13}{random_depth:>14}  {is_sorted_list(random_result)}")
    small = [9, 3, 7, 3, 1, 8, 2]
    result, _ = run(small, randomize=True)
    print(f"{small} -> {result}")


if __name__ == "__main__":
    main()
