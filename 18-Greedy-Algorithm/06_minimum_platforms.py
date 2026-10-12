"""
Problem title:
    Minimum Number of Railway Platforms

Problem statement:
    Given arrival and departure times (24-hour style, e.g. 930 = 9:30) of
    trains, find the minimum number of platforms needed so that no train has
    to wait. A train arriving exactly when another departs needs its own
    platform (the departing train is still there at that moment).

What it teaches:
    * Sorting two lists independently and sweeping with two pointers.
    * Turning "overlap" questions into "how many are active at once".

Input example:
    arrivals   = [900, 940, 950, 1100, 1500, 1800]
    departures = [910, 1200, 1120, 1130, 1900, 2000]

Expected output:
    Platforms needed: 3
    Back-to-back trains (arrive 900, leave 1000 / arrive 1000, leave 1100): 2
    Four trains all overlapping: 4
    No trains: 0

Approach:
    Sort arrivals and departures separately. Sweep through time: an arrival
    takes a platform, a departure frees one. The answer is the highest number
    of platforms in use at any moment.

Step-by-step logic:
    1. Sort both lists ascending (hand-written merge sort).
    2. i = j = 0, in_use = 0, best = 0.
    3. While i < n: if arrivals[i] <= departures[j], a train arrives:
       in_use += 1, i += 1. Else a train leaves: in_use -= 1, j += 1.
    4. After every arrival update best if in_use is larger.

Why it works:
    The trains present at any time are exactly arrivals so far minus
    departures so far, and the identity of a train does not matter, only the
    counts. So sorting arrival and departure times independently is safe.

Time complexity:
    O(n log n) for the sorts + O(n) for the sweep.

Space complexity:
    O(n) for the sorted copies.

Edge cases:
    * Empty input -> 0.
    * Arrival equals a departure time -> use <= so both count.
    * All trains overlapping -> answer is n.

Alternative approach:
    Sort trains by arrival and keep a min-heap of departure times (also
    O(n log n)). Or a brute force count at each arrival in O(n^2).
"""


def merge_sort(items, comes_first):
    """Stable merge sort; `comes_first(a, b)` is True when a must precede b."""
    if len(items) <= 1:
        return list(items)
    middle = len(items) // 2
    left = merge_sort(items[:middle], comes_first)
    right = merge_sort(items[middle:], comes_first)
    merged = []
    i = j = 0
    while i < len(left) and j < len(right):
        if comes_first(right[j], left[i]):
            merged.append(right[j])
            j += 1
        else:
            merged.append(left[i])
            i += 1
    merged.extend(left[i:])
    merged.extend(right[j:])
    return merged


def min_platforms(arrivals, departures):
    """Return the minimum number of platforms required."""
    if len(arrivals) != len(departures):
        raise ValueError("arrivals and departures must have the same length")
    ascending = lambda a, b: a < b
    arr = merge_sort(arrivals, ascending)
    dep = merge_sort(departures, ascending)

    in_use = 0
    best = 0
    i = j = 0
    n = len(arr)
    while i < n:
        if arr[i] <= dep[j]:  # next event is an arrival
            in_use += 1
            i += 1
            if in_use > best:
                best = in_use
        else:  # next event is a departure
            in_use -= 1
            j += 1
    return best


def main():
    arrivals = [900, 940, 950, 1100, 1500, 1800]
    departures = [910, 1200, 1120, 1130, 1900, 2000]
    print("Platforms needed:", min_platforms(arrivals, departures))

    print("Back-to-back trains (arrive 900, leave 1000 / arrive 1000, "
          "leave 1100):",
          min_platforms([900, 1000], [1000, 1100]))
    print("Four trains all overlapping:",
          min_platforms([100, 110, 120, 130], [500, 510, 520, 530]))
    print("No trains:", min_platforms([], []))


if __name__ == "__main__":
    main()
