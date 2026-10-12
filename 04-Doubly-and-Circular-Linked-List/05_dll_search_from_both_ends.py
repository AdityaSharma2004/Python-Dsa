r"""
Problem: Search a Doubly Linked List from Both Ends

Problem statement:
    Return the index of a target value (any occurrence) by moving one
    pointer from the head and another from the tail at the same time. Return
    -1 if not found.

What it teaches:
    Using the tail pointer and prev links to halve the search distance when
    the target is near either end.

Input example:
    values = [4, 8, 15, 16, 23, 42], targets = 4, 42, 16, 99

Expected output:
    List: [4, 8, 15, 16, 23, 42]
    target  4 -> index  0 after 1 iteration(s)
    target 42 -> index  5 after 1 iteration(s)
    target 16 -> index  3 after 3 iteration(s)
    target 99 -> index -1 after 3 iteration(s)
    Empty list -> -1

Approach:
    Advance a front pointer and a back pointer together, checking both,
    until they meet or cross.

Step-by-step logic:
    1. front = head at index 0, back = tail at index n-1.
    2. While front_index <= back_index compare both nodes with the target.
    3. Return the matching index if either matches.
    4. Move front forward and back backward.
    5. If the loop ends return -1.

Why it works:
    Every node is checked by exactly one of the two pointers, and each
    iteration covers two nodes.

Time complexity:
    O(n) worst case, about n/2 iterations; O(1) when the target is at either
    end.

Space complexity:
    O(1).

Edge cases:
    Empty list, one node, target in the middle, duplicate targets (the
    nearer one wins), even and odd lengths.

Alternative approach:
    A single forward scan is simpler but takes n steps when the target sits
    at the tail.
"""


class Node:
    """A doubly linked list node."""

    def __init__(self, data):
        self.data = data
        self.prev = None
        self.next = None


def build(values):
    head = tail = None
    for value in values:
        node = Node(value)
        if head is None:
            head = tail = node
        else:
            tail.next = node
            node.prev = tail
            tail = node
    return head, tail


def search_both_ends(head, tail, size, target):
    front, back = head, tail
    front_index, back_index = 0, size - 1
    steps = 0
    while front is not None and front_index <= back_index:
        steps += 1
        if front.data == target:
            return front_index, steps
        if back.data == target:
            return back_index, steps
        front, front_index = front.next, front_index + 1
        back, back_index = back.prev, back_index - 1
    return -1, steps


def main():
    values = [4, 8, 15, 16, 23, 42]
    head, tail = build(values)
    print("List:", values)
    for target in (4, 42, 16, 99):
        index, steps = search_both_ends(head, tail, len(values), target)
        print("target %2d -> index %2d after %d iteration(s)" % (target, index, steps))
    empty_head, empty_tail = build([])
    print("Empty list ->", search_both_ends(empty_head, empty_tail, 0, 1)[0])


if __name__ == "__main__":
    main()
