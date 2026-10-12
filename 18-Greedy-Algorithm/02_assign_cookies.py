"""
Problem title:
    Assign Cookies

Problem statement:
    Each child i has a greed factor g[i] (the minimum cookie size that makes
    the child happy). Each cookie j has size s[j]. A cookie can be given to at
    most one child, and a child gets at most one cookie. Return the maximum
    number of children that can be made happy.

What it teaches:
    * Sort both sides, then match greedily with two pointers.
    * Give each child the SMALLEST cookie that satisfies them, saving big
      cookies for greedier children.

Input example:
    greed   = [1, 2, 3]
    cookies = [1, 1]

Expected output:
    greed=[1, 2, 3] cookies=[1, 1] -> 1 happy children
    greed=[1, 2] cookies=[1, 2, 3] -> 2 happy children
    greed=[5, 10, 2, 9, 15, 9] cookies=[6, 1, 20, 3, 8] -> 3 happy children
    greed=[] cookies=[1, 2] -> 0 happy children
    greed=[3, 4] cookies=[] -> 0 happy children
    greed=[10, 11] cookies=[1, 2, 3] -> 0 happy children

Approach:
    Sort greed factors and cookie sizes ascending. Walk through cookies with a
    pointer; whenever the current cookie satisfies the least-greedy unfed
    child, feed that child and move to the next child.

Step-by-step logic:
    1. Sort children by greed (ascending) and cookies by size (ascending).
    2. child = 0. For every cookie in order:
       - if child is still in range and cookie >= greed[child],
         the child is happy: child += 1.
    3. The final value of `child` is the number of happy children.

Why it works:
    (Exchange argument) If an optimal answer feeds the least-greedy child a
    bigger cookie than necessary, swapping to the smallest valid cookie never
    hurts anyone, because the bigger cookie is then free for someone else.
    Small cookies that cannot satisfy even the least-greedy child are useless
    to everybody and are skipped.

Time complexity:
    O(n log n + m log m) for the two sorts, plus O(n + m) for the scan.

Space complexity:
    O(n + m) for the sorted copies (merge sort).

Edge cases:
    * No cookies or no children -> 0.
    * Cookies all too small -> 0.
    * More cookies than children -> leftover cookies are simply unused.

Alternative approach:
    Brute force over every assignment is exponential. A counting/bucket
    approach works if greed and size are small bounded integers.
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


def max_content_children(greed, cookies):
    """Return how many children can be satisfied."""
    ascending = lambda a, b: a < b
    greed_sorted = merge_sort(greed, ascending)
    cookies_sorted = merge_sort(cookies, ascending)

    child = 0
    for cookie in cookies_sorted:
        if child < len(greed_sorted) and cookie >= greed_sorted[child]:
            child += 1  # this child is happy; move to the next greedier child
    return child


def main():
    tests = [
        ([1, 2, 3], [1, 1]),
        ([1, 2], [1, 2, 3]),
        ([5, 10, 2, 9, 15, 9], [6, 1, 20, 3, 8]),
        ([], [1, 2]),
        ([3, 4], []),
        ([10, 11], [1, 2, 3]),
    ]
    for greed, cookies in tests:
        happy = max_content_children(greed, cookies)
        print(f"greed={greed} cookies={cookies} -> {happy} happy children")


if __name__ == "__main__":
    main()
