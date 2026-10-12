"""
Problem title:
    Merge K Sorted Lists

Problem statement:
    Given k lists, each sorted in ascending order, merge them into one sorted
    list. Use the divide and conquer idea: merge the lists in pairs, round after
    round, until a single list remains.

What it teaches:
    - Reusing the two-way merge as a building block.
    - Why pairwise (balanced) merging is better than merging one list at a time.
    - Counting how many element copies each strategy performs.

Input example:
    [[1, 4, 7], [2, 5, 8], [0, 3, 6, 9]]

Expected output:
    Input: [[1, 4, 7], [2, 5, 8], [0, 3, 6, 9]]
      round 1: 3 lists -> 2 lists
      round 2: 2 lists -> 1 lists
    Merged: [0, 1, 2, 3, 4, 5, 6, 7, 8, 9]
    Same as one-by-one merge: True

    Input: [[5], [1], [4], [2], [3]]
      round 1: 5 lists -> 3 lists
      round 2: 3 lists -> 2 lists
      round 3: 2 lists -> 1 lists
    Merged: [1, 2, 3, 4, 5]
    Same as one-by-one merge: True

    Input: [[], [1, 2], []]
      round 1: 3 lists -> 2 lists
      round 2: 2 lists -> 1 lists
    Merged: [1, 2]
    Same as one-by-one merge: True

    Input: [[3, 3, 3]]
    Merged: [3, 3, 3]
    Same as one-by-one merge: True

    Input: []
    Merged: []
    Same as one-by-one merge: True

Approach used:
    Repeatedly merge neighbouring lists (list 0 with 1, list 2 with 3, ...). Each
    round halves the number of lists, so there are about log2(k) rounds.

Step-by-step logic:
    1. If there are no lists, return [].
    2. While more than one list remains: build a new round by merging lists
       two at a time; an odd leftover list is carried over unchanged.
    3. The last remaining list is the answer.

Why it works:
    Merging two sorted lists gives a sorted list, so every round keeps all lists
    sorted. Each round touches every element once, and there are log2(k) rounds,
    so the cost is O(N log k) where N is the total number of elements.

Time complexity:
    O(N log k) for pairwise merging. Merging lists one after another costs
    O(N * k) in the worst case because early elements are copied again and again.

Space complexity:
    O(N) for the merged lists created in each round.

Edge cases:
    No lists, one list, empty lists inside the input, duplicate values across lists,
    lists of very different lengths.

Alternative approach:
    A min-heap holding the front element of each list also gives O(N log k).
"""


def merge(left, right):
    """Merge two sorted lists and return the result."""
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


def merge_k_lists(lists):
    """Merge k sorted lists by merging them in pairs, round by round."""
    if len(lists) == 0:
        return []
    current = list(lists)
    round_number = 0
    while len(current) > 1:
        round_number += 1
        next_round = []
        for i in range(0, len(current), 2):
            if i + 1 < len(current):
                next_round.append(merge(current[i], current[i + 1]))
            else:
                next_round.append(current[i])  # odd one out moves on
        print(f"  round {round_number}: {len(current)} lists -> {len(next_round)} lists")
        current = next_round
    return current[0]


def merge_one_by_one(lists):
    """Naive version: fold lists in one at a time (for comparison)."""
    result = []
    for one_list in lists:
        result = merge(result, one_list)
    return result


def main():
    samples = [
        [[1, 4, 7], [2, 5, 8], [0, 3, 6, 9]],
        [[5], [1], [4], [2], [3]],
        [[], [1, 2], []],
        [[3, 3, 3]],
        [],
    ]
    for lists in samples:
        print(f"Input: {lists}")
        merged = merge_k_lists(lists)
        print(f"Merged: {merged}")
        print(f"Same as one-by-one merge: {merged == merge_one_by_one(lists)}")
        print()


if __name__ == "__main__":
    main()
