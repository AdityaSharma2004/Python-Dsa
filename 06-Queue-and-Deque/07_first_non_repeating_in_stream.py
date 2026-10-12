r"""
Problem: First Non-Repeating Character in a Stream

Problem statement:
    Characters arrive one at a time. After each arrival report the first
    character seen so far that has appeared exactly once, or '#' if none.

What it teaches:
    A queue of candidates combined with a frequency dictionary, with lazy
    removal of items that stopped being candidates.

Input example:
    "aabcbd"

Expected output:
    stream 'aabcbd' -> a # b b c c
    stream 'abc' -> a a a
    stream 'aabb' -> a # b #
    stream '' ->
    stream 'zzz' -> z # #

Approach:
    Count each character; keep a queue of characters in arrival order. Before
    answering, discard front characters whose count is greater than 1.

Step-by-step logic:
    1. On a new character increase its count; if the count is 1 enqueue it.
    2. While the queue front has a count above 1, dequeue it.
    3. Answer with the front, or '#' if the queue is empty.

Why it works:
    The queue holds characters in the order of first appearance, so after
    removing repeated ones the front is the earliest still-unique character.
    A character is removed only once, so total work is linear.

Time complexity:
    O(n) overall (O(1) amortised per character).

Space complexity:
    O(k) where k is the alphabet size (at most n).

Edge cases:
    Empty stream, all characters repeated, the unique character becoming
    repeated later, three or more repeats of one character.

Alternative approach:
    After every character scan the whole string again: O(n^2).
"""

from collections import deque


def first_unique_each_step(stream):
    counts = {}
    candidates = deque()
    answers = []
    for char in stream:
        counts[char] = counts.get(char, 0) + 1
        if counts[char] == 1:
            candidates.append(char)
        while candidates and counts[candidates[0]] > 1:
            candidates.popleft()  # no longer unique
        answers.append(candidates[0] if candidates else "#")
    return answers


def main():
    for stream in ("aabcbd", "abc", "aabb", "", "zzz"):
        print("stream %r ->" % stream, " ".join(first_unique_each_step(stream)))


if __name__ == "__main__":
    main()
