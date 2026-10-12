"""
Problem title:
    Quick Sort with Hoare Partition

Problem statement:
    Sort a list in place using quick sort built on Hoare's partition scheme.
    Compare the number of swaps with the Lomuto version on the same data.

What it teaches:
    - How the recursion differs for Hoare: (low, split) and (split + 1, high).
    - Why Hoare usually performs fewer swaps than Lomuto.
    - Counting swaps as a measure of work.

Input example:
    [29, 10, 14, 37, 13, 5, 21, 8]

Expected output:
    [29, 10, 14, 37, 13, 5, 21, 8] -> [5, 8, 10, 13, 14, 21, 29, 37]  hoare swaps=8, lomuto swaps=9
    [] -> []  hoare swaps=0, lomuto swaps=0
    [7] -> [7]  hoare swaps=0, lomuto swaps=0
    [2, 1] -> [1, 2]  hoare swaps=1, lomuto swaps=1
    [3, 3, 3, 3, 3] -> [3, 3, 3, 3, 3]  hoare swaps=5, lomuto swaps=14
    [9, 8, 7, 6, 5, 4, 3, 2, 1] -> [1, 2, 3, 4, 5, 6, 7, 8, 9]  hoare swaps=4, lomuto swaps=24
    [4, -2, 0, 4, -7, 11, 3] -> [-7, -2, 0, 3, 4, 4, 11]  hoare swaps=5, lomuto swaps=8

Approach used:
    Partition with the first element as pivot (Hoare), then recurse on the two
    ranges on either side of the returned split index.

Step-by-step logic:
    1. If low >= high return.
    2. split = hoare_partition(arr, low, high).
    3. quick_sort(arr, low, split) and quick_sort(arr, split + 1, high).
    4. Count each swap with a counter list so the two schemes can be compared.

Why it works:
    Each partition guarantees every element in the left range is <= every element
    in the right range, and both ranges are strictly smaller than the original, so
    sorting them recursively sorts the whole list.

Time complexity:
    Average O(n log n); worst O(n^2). With the first element as pivot, already
    sorted data splits off only one element per partition, so it is quadratic for
    Hoare too; a random or median-of-three pivot avoids this.

Space complexity:
    O(1) extra data plus O(log n) average recursion stack (O(n) worst case).

Edge cases:
    Empty list, single element, two elements, all equal elements, duplicates.

Alternative approach:
    Lomuto-based quick sort (file 02). The counts printed here show Hoare doing
    fewer swaps on typical data.
"""


def hoare_partition(arr, low, high, swaps):
    """Hoare partition; counts swaps in swaps[0]. Returns the split index."""
    pivot = arr[low]
    i = low - 1
    j = high + 1
    while True:
        i += 1
        while arr[i] < pivot:
            i += 1
        j -= 1
        while arr[j] > pivot:
            j -= 1
        if i >= j:
            return j
        arr[i], arr[j] = arr[j], arr[i]
        swaps[0] += 1


def quick_sort_hoare(arr, low, high, swaps):
    """Sort arr[low..high] in place using Hoare partitioning."""
    if low >= high:
        return
    split = hoare_partition(arr, low, high, swaps)
    quick_sort_hoare(arr, low, split, swaps)
    quick_sort_hoare(arr, split + 1, high, swaps)


def lomuto_partition(arr, low, high, swaps):
    """Lomuto partition; counts swaps in swaps[0]."""
    pivot = arr[high]
    boundary = low - 1
    for j in range(low, high):
        if arr[j] <= pivot:
            boundary += 1
            arr[boundary], arr[j] = arr[j], arr[boundary]
            swaps[0] += 1
    arr[boundary + 1], arr[high] = arr[high], arr[boundary + 1]
    swaps[0] += 1
    return boundary + 1


def quick_sort_lomuto(arr, low, high, swaps):
    """Sort arr[low..high] in place using Lomuto partitioning."""
    if low >= high:
        return
    p = lomuto_partition(arr, low, high, swaps)
    quick_sort_lomuto(arr, low, p - 1, swaps)
    quick_sort_lomuto(arr, p + 1, high, swaps)


def main():
    samples = [
        [29, 10, 14, 37, 13, 5, 21, 8],
        [],
        [7],
        [2, 1],
        [3, 3, 3, 3, 3],
        [9, 8, 7, 6, 5, 4, 3, 2, 1],
        [4, -2, 0, 4, -7, 11, 3],
    ]
    for data in samples:
        hoare_data = list(data)
        lomuto_data = list(data)
        hoare_swaps = [0]
        lomuto_swaps = [0]
        quick_sort_hoare(hoare_data, 0, len(hoare_data) - 1, hoare_swaps)
        quick_sort_lomuto(lomuto_data, 0, len(lomuto_data) - 1, lomuto_swaps)
        print(
            f"{data} -> {hoare_data}  hoare swaps={hoare_swaps[0]}, "
            f"lomuto swaps={lomuto_swaps[0]}"
        )


if __name__ == "__main__":
    main()
