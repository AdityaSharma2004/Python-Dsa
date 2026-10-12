"""
Problem title:
    Optimal Merge Patterns (Minimum Cost to Merge Files)

Problem statement:
    You have files of given sizes. Merging two files of sizes a and b costs
    a + b and creates one file of size a + b. Merge all files into one with
    the minimum total cost.

What it teaches:
    * Using a min-heap (heapq) as the engine of a greedy algorithm.
    * The same idea that powers Huffman coding.

Input example:
    sizes = [20, 30, 10, 5, 30]

Expected output:
    Merge 5 + 10 -> 15
    Merge 15 + 20 -> 35
    Merge 30 + 30 -> 60
    Merge 35 + 60 -> 95
    Optimal total cost: 205
    Left-to-right cost (not greedy): 270

    Edge cases:
    No files        -> 0
    One file [42]   -> 0
    Two files [3,4] -> 7

Approach:
    Always merge the two smallest files. Push the merged file back into the
    heap and repeat until one file remains.

Step-by-step logic:
    1. Turn the sizes into a min-heap.
    2. While more than one file is left: pop the two smallest, add them to get
       the merge cost, add the cost to the total, push the merged size.
    3. The total is the answer.

Why it works:
    Every merge adds the sizes of the files involved to the cost, so a file
    that is merged early gets re-counted in every later merge above it.
    Putting the smallest files deepest in the merge tree (merging them first)
    minimises the repeated counting - the exchange argument used for Huffman.

Time complexity:
    O(n log n): n - 1 merges, each with two pops and one push at O(log n).

Space complexity:
    O(n) for the heap.

Edge cases:
    * Zero or one file -> cost 0.
    * Two files -> cost is their sum.
    * Equal sizes work fine; the heap only compares integers.

Alternative approach:
    Repeatedly sort the list and merge the first two (O(n^2 log n)). Merging
    in input order (not greedy) is simple but gives a higher cost.
"""

import heapq


def optimal_merge_cost(sizes):
    """Return (total_cost, list_of_merge_steps)."""
    heap = list(sizes)
    heapq.heapify(heap)  # O(n) build
    total_cost = 0
    steps = []
    while len(heap) > 1:
        first = heapq.heappop(heap)
        second = heapq.heappop(heap)
        merged = first + second
        total_cost += merged
        steps.append((first, second, merged))
        heapq.heappush(heap, merged)
    return total_cost, steps


def naive_left_to_right_cost(sizes):
    """Non-greedy baseline: merge files strictly in the given order."""
    if len(sizes) < 2:
        return 0
    running = sizes[0]
    total = 0
    for size in sizes[1:]:
        running += size
        total += running
    return total


def main():
    sizes = [20, 30, 10, 5, 30]
    cost, steps = optimal_merge_cost(sizes)
    for first, second, merged in steps:
        print(f"Merge {first} + {second} -> {merged}")
    print("Optimal total cost:", cost)
    print("Left-to-right cost (not greedy):", naive_left_to_right_cost(sizes))

    print("\nEdge cases:")
    print("No files        ->", optimal_merge_cost([])[0])
    print("One file [42]   ->", optimal_merge_cost([42])[0])
    print("Two files [3,4] ->", optimal_merge_cost([3, 4])[0])


if __name__ == "__main__":
    main()
