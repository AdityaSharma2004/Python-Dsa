"""
Problem title:
    Backtracking - Subsets and Permutations

Problem statement:
    Given a list of distinct items, generate (a) all subsets and (b) all
    permutations using recursive backtracking.

What it teaches:
    The choose -> explore -> un-choose pattern, building solutions in a
    shared path list and undoing the last choice after each recursive call.

Input example:
    items = [1, 2, 3]

Expected output:
    Subsets of [1, 2, 3] (8):
       []
       [3]
       [2]
       [2, 3]
       [1]
       [1, 3]
       [1, 2]
       [1, 2, 3]
    Permutations of [1, 2, 3] (6):
       [1, 2, 3]
       [1, 3, 2]
       [2, 1, 3]
       [2, 3, 1]
       [3, 1, 2]
       [3, 2, 1]
    Empty input: [[]] [[]]
    Count for 4 items: 16 subsets, 24 permutations

Approach:
    Subsets: at every index decide "skip" or "take".
    Permutations: at every position try each unused item.

Step-by-step logic:
    1. Keep a list `path` for the current partial answer.
    2. Subsets: when index == len(items) record a copy of path; otherwise
       explore without items[index], then append it, explore, and pop it.
    3. Permutations: when path has len(items) elements record a copy; else
       for each unused item append it, mark used, recurse, then undo both.
    4. Always store a COPY of path (path[:]) because path keeps changing.

Why it works:
    The recursion explores every decision sequence once. Undoing a choice
    (pop) restores the state so the next branch starts clean.

Time complexity:
    Subsets: O(n * 2^n). Permutations: O(n * n!).

Space complexity:
    O(n) recursion depth and path (excluding the output itself).

Edge cases:
    Empty input -> [[]] for both; single item; duplicates would produce
    repeated results (this program assumes distinct items).

Alternative approach:
    Subsets with bitmasks (counting from 0 to 2^n - 1); permutations with
    swapping in place.
"""


def subsets(items):
    results = []

    def explore(index, path):
        if index == len(items):  # decided about every item
            results.append(path[:])
            return
        explore(index + 1, path)  # choice 1: skip
        path.append(items[index])  # choice 2: take
        explore(index + 1, path)
        path.pop()  # backtrack

    explore(0, [])
    return results


def permutations(items):
    results = []
    used = [False] * len(items)

    def explore(path):
        if len(path) == len(items):
            results.append(path[:])
            return
        for position in range(len(items)):
            if used[position]:
                continue
            used[position] = True  # choose
            path.append(items[position])
            explore(path)  # explore
            path.pop()  # un-choose
            used[position] = False

    explore([])
    return results


def main():
    items = [1, 2, 3]
    all_subsets = subsets(items)
    print(f"Subsets of {items} ({len(all_subsets)}):")
    for subset in all_subsets:
        print("  ", subset)
    all_perms = permutations(items)
    print(f"Permutations of {items} ({len(all_perms)}):")
    for perm in all_perms:
        print("  ", perm)
    print("Empty input:", subsets([]), permutations([]))
    print("Count for 4 items:", len(subsets([1, 2, 3, 4])), "subsets,",
          len(permutations([1, 2, 3, 4])), "permutations")


if __name__ == "__main__":
    main()
