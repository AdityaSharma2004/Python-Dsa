"""
Problem title:
    Search an Element and Count Occurrences

Problem statement:
    Given a linked list and a target value, return the zero-based index of the
    first occurrence (or -1 if absent), and also count how many times the
    target appears.

What it teaches:
    - Linear search on a structure with no random access.
    - Why a linked list cannot use index jumping like an array.
    - Returning early versus scanning the whole list.

Input example:
    list = 7 -> 3 -> 9 -> 3 -> 5, target = 3  (also target = 8)

Expected output:
    target 3 -> index 1 | count 2
    target 5 -> index 4 | count 1
    target 7 -> index 0 | count 1
    target 8 -> index -1 | count 0
    empty list, target 1 -> index -1 | count 0

Approach:
    Walk the list with a counter that tracks the current index.

Step-by-step logic:
    1. current = head, index = 0.
    2. If current.data == target, return index (first-occurrence search).
    3. Otherwise advance current and increment index.
    4. If current becomes None, return -1.
    5. For counting, do the same walk but never stop early; add 1 per match.

Why it works:
    Every node is visited in order, so the first match found has the smallest
    index, and a full pass sees every occurrence exactly once.

Time complexity:
    O(n) worst case for both functions (first-occurrence can stop earlier).

Space complexity:
    O(1).

Edge cases:
    - Empty list: -1 and count 0.
    - Target missing.
    - Target in the head or the tail.
    - Duplicates: index function reports only the first.

Alternative approach:
    Convert to a Python list and use .index(); that costs O(n) extra space and
    hides the pointer walk this problem is meant to teach.
"""


class Node:
    def __init__(self, data):
        self.data = data
        self.next = None


def build_list(values):
    head = None
    tail = None
    for value in values:
        node = Node(value)
        if head is None:
            head = node
        else:
            tail.next = node
        tail = node
    return head


def find_index(head, target):
    """Return index of first node equal to target, or -1."""
    current = head
    index = 0
    while current is not None:
        if current.data == target:
            return index
        current = current.next
        index += 1
    return -1


def count_occurrences(head, target):
    """Return how many nodes hold target."""
    count = 0
    current = head
    while current is not None:
        if current.data == target:
            count += 1
        current = current.next
    return count


def main():
    head = build_list([7, 3, 9, 3, 5])
    for target in (3, 5, 7, 8):
        print("target", target, "-> index", find_index(head, target),
              "| count", count_occurrences(head, target))

    empty = build_list([])
    print("empty list, target 1 -> index", find_index(empty, 1),
          "| count", count_occurrences(empty, 1))


if __name__ == "__main__":
    main()
