r"""
Problem: Reverse a Doubly Linked List

Problem statement:
    Reverse a doubly linked list in place so that the old tail becomes the
    new head. Do not create new nodes.

What it teaches:
    That reversing a doubly linked list is just swapping the two pointers of
    every node.

Input example:
    1 <-> 2 <-> 3 <-> 4 <-> 5

Expected output:
    Original: [1, 2, 3, 4, 5]
      Forward after reverse : [5, 4, 3, 2, 1]
      Backward after reverse: [1, 2, 3, 4, 5]
    Original: [1, 2]
      Forward after reverse : [2, 1]
      Backward after reverse: [1, 2]
    Original: [9]
      Forward after reverse : [9]
      Backward after reverse: [9]
    Original: []
      Forward after reverse : []
      Backward after reverse: []

Approach:
    Walk the list once, swap prev and next in each node, then swap head and
    tail.

Step-by-step logic:
    1. Set current = head.
    2. Swap current.prev and current.next.
    3. Move to the original next, which is now current.prev.
    4. Repeat until current is None.
    5. Swap the head and tail references.

Why it works:
    After swapping, every arrow points the opposite way, which is exactly a
    reversed list.

Time complexity:
    O(n) one pass.

Space complexity:
    O(1) in place.

Edge cases:
    Empty list, single node, two nodes.

Alternative approach:
    Collect values into a list and rewrite them in reverse (simpler but O(n)
    extra space).
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


def reverse(head, tail):
    current = head
    while current:
        current.prev, current.next = current.next, current.prev
        current = current.prev  # old next, because pointers were swapped
    return tail, head  # new head, new tail


def forward(head):
    items = []
    while head:
        items.append(head.data)
        head = head.next
    return items


def backward(tail):
    items = []
    while tail:
        items.append(tail.data)
        tail = tail.prev
    return items


def main():
    for values in ([1, 2, 3, 4, 5], [1, 2], [9], []):
        head, tail = build(values)
        head, tail = reverse(head, tail)
        print("Original:", values)
        print("  Forward after reverse :", forward(head))
        print("  Backward after reverse:", backward(tail))


if __name__ == "__main__":
    main()
