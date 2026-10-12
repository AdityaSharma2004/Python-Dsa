"""
Problem title:
    Find the Middle Node (Slow and Fast Pointers)

Problem statement:
    Return the middle node of a singly linked list in ONE pass. If the list has
    an even number of nodes, return the second of the two middle nodes.

What it teaches:
    - The slow/fast (tortoise and hare) pointer pattern.
    - Solving a "position" problem without knowing the length first.

Input example:
    1 -> 2 -> 3 -> 4 -> 5        (middle = 3)
    1 -> 2 -> 3 -> 4 -> 5 -> 6   (middle = 4)

Expected output:
    [1, 2, 3, 4, 5] -> middle: 3 | two-pass check: 3
    [1, 2, 3, 4, 5, 6] -> middle: 4 | two-pass check: 4
    [9] -> middle: 9 | two-pass check: 9
    [4, 8] -> middle: 8 | two-pass check: 8
    [] -> middle: None | two-pass check: None

Approach:
    Move slow one step and fast two steps. When fast reaches the end, slow is
    in the middle. A two-pass length-based version is shown for comparison.

Step-by-step logic:
    1. slow = fast = head.
    2. While fast and fast.next exist: slow = slow.next; fast = fast.next.next.
    3. Return slow.

    Dry run on 1->2->3->4->5:
      start: slow=1 fast=1
      step1: slow=2 fast=3
      step2: slow=3 fast=5   (fast.next is None -> stop)  middle = 3

Why it works:
    fast covers twice the distance of slow, so when fast has travelled the full
    length n, slow has travelled n/2.

Time complexity:
    O(n) with a single pass (two-pass version is also O(n)).

Space complexity:
    O(1).

Edge cases:
    - Empty list: returns None.
    - One node: returns that node.
    - Two nodes: returns the second node (our even-length rule).

Alternative approach:
    Count the nodes (n), then walk n // 2 steps. Simple but needs two passes.
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


def find_middle(head):
    """One-pass middle using slow/fast pointers."""
    slow = head
    fast = head
    while fast is not None and fast.next is not None:
        slow = slow.next          # one step
        fast = fast.next.next     # two steps
    return slow


def find_middle_two_pass(head):
    """Alternative: count first, then walk half the length."""
    count = 0
    current = head
    while current is not None:
        count += 1
        current = current.next
    current = head
    for _ in range(count // 2):
        current = current.next
    return current


def describe(node):
    return "None" if node is None else str(node.data)


def main():
    samples = [[1, 2, 3, 4, 5], [1, 2, 3, 4, 5, 6], [9], [4, 8], []]
    for values in samples:
        head = build_list(values)
        one_pass = find_middle(head)
        two_pass = find_middle_two_pass(head)
        print(values, "-> middle:", describe(one_pass),
              "| two-pass check:", describe(two_pass))


if __name__ == "__main__":
    main()
