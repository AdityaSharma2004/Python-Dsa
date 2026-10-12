"""
Problem title:
    Three-Way Quick Sort (Duplicate-Heavy Arrays)

Problem statement:
    Sort a list that contains many repeated values in place using quick sort
    with three-way partitioning (smaller than / equal to / greater than the
    pivot). Compare its comparison count with the plain Lomuto version.

What it teaches:
    - Why two-way Lomuto partitioning is quadratic when all values are equal.
    - The Dutch National Flag idea with three zones: less, equal, greater.
    - Equal values are placed once and never touched again.

Input example:
    [4, 9, 4, 4, 1, 9, 4, 4, 1, 4]

Expected output:
    [4, 9, 4, 4, 1, 9, 4, 4, 1, 4] -> [1, 1, 4, 4, 4, 4, 4, 4, 9, 9]
    Comparisons (three-way vs Lomuto):
      few distinct  three-way=   297  lomuto=  3923  same result=True
      all equal     three-way=   149  lomuto= 11175  same result=True
      random-ish    three-way=  1247  lomuto=  1001  same result=True
    Empty: []

Approach used:
    Take arr[low] as the pivot. Keep pointers lt, i and gt:
    arr[low..lt-1] < pivot, arr[lt..i-1] == pivot, arr[gt+1..high] > pivot.
    Recurse only on the "less" and "greater" zones.

Step-by-step logic:
    1. pivot = arr[low]; lt = low; i = low + 1; gt = high.
    2. While i <= gt: if arr[i] < pivot swap arr[lt], arr[i] and lt, i += 1;
       if arr[i] > pivot swap arr[i], arr[gt] and gt -= 1 (do not move i);
       otherwise i += 1.
    3. Recurse on (low, lt - 1) and (gt + 1, high).

Why it works:
    After the loop, everything in [lt, gt] equals the pivot and is already in
    its final place. The two outer zones hold strictly smaller and strictly
    larger values, so sorting them recursively sorts the whole range.

Time complexity:
    O(n log n) average; O(n) when there are only a few distinct values; worst
    case O(n^2) for adversarial inputs with a fixed pivot.

Space complexity:
    O(1) extra data plus O(log n) average recursion stack.

Edge cases:
    Empty list, single element, all equal (one partition pass, no recursion),
    only two distinct values, already sorted data.

Alternative approach:
    Lomuto (file 02) or Hoare (file 04) partitioning: simpler, but they keep
    re-sorting equal elements.
"""


def three_way_quick_sort(arr, low, high, counter):
    """Sort arr[low..high] in place; counter[0] counts comparisons."""
    if low >= high:
        return
    pivot = arr[low]
    lt = low        # arr[low..lt-1]  < pivot
    i = low + 1     # arr[lt..i-1]   == pivot
    gt = high       # arr[gt+1..high] > pivot
    while i <= gt:
        counter[0] += 1
        if arr[i] < pivot:
            arr[lt], arr[i] = arr[i], arr[lt]
            lt += 1
            i += 1
        elif arr[i] > pivot:
            arr[i], arr[gt] = arr[gt], arr[i]
            gt -= 1  # the swapped-in value is unchecked, so keep i
        else:
            i += 1
    three_way_quick_sort(arr, low, lt - 1, counter)
    three_way_quick_sort(arr, gt + 1, high, counter)


def lomuto_quick_sort(arr, low, high, counter):
    """Plain Lomuto quick sort; counter[0] counts comparisons."""
    if low >= high:
        return
    pivot = arr[high]
    boundary = low - 1
    for j in range(low, high):
        counter[0] += 1
        if arr[j] <= pivot:
            boundary += 1
            arr[boundary], arr[j] = arr[j], arr[boundary]
    arr[boundary + 1], arr[high] = arr[high], arr[boundary + 1]
    lomuto_quick_sort(arr, low, boundary, counter)
    lomuto_quick_sort(arr, boundary + 2, high, counter)


def main():
    data = [4, 9, 4, 4, 1, 9, 4, 4, 1, 4]
    result = list(data)
    three_way_quick_sort(result, 0, len(result) - 1, [0])
    print(f"{data} -> {result}")

    print("Comparisons (three-way vs Lomuto):")
    cases = [
        ("few distinct", [i % 3 for i in range(150)]),
        ("all equal", [7] * 150),
        ("random-ish", [(i * 37) % 101 for i in range(150)]),
    ]
    for name, values in cases:
        a = list(values)
        b = list(values)
        count_a = [0]
        count_b = [0]
        three_way_quick_sort(a, 0, len(a) - 1, count_a)
        lomuto_quick_sort(b, 0, len(b) - 1, count_b)
        print(f"  {name:<13} three-way={count_a[0]:>6}  lomuto={count_b[0]:>6}  same result={a == b}")

    # Edge cases
    empty = []
    three_way_quick_sort(empty, 0, -1, [0])
    print("Empty:", empty)


if __name__ == "__main__":
    main()
