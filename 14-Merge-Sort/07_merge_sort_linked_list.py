"""
Problem title:
    Merge Sort on a Singly Linked List

Problem statement:
    Sort a singly linked list in ascending order using merge sort by relinking
    nodes. Do not copy the values into a Python list.

What it teaches:
    - Why merge sort suits linked lists (merging needs no random access).
    - Finding the middle with slow and fast pointers.
    - Splitting a list in two and merging with a dummy head node.

Input example:
    4 -> 2 -> 1 -> 3

Expected output:
    Before: 4 -> 2 -> 1 -> 3
    After : 1 -> 2 -> 3 -> 4

    Before: -1 -> 5 -> 3 -> 4 -> 0
    After : -1 -> 0 -> 3 -> 4 -> 5

    Before: 2 -> 2 -> 1
    After : 1 -> 2 -> 2

    Before: 9 -> 1
    After : 1 -> 9

    Before: 7
    After : 7

    Before: empty
    After : empty

Approach used:
    Find the middle with slow/fast pointers, cut the list there, recursively sort
    both halves and merge the two sorted lists by relinking nodes.

Step-by-step logic:
    1. If head is None or head.next is None, return head.
    2. slow = head, fast = head.next; move slow by 1 and fast by 2 until fast ends.
       slow is the last node of the first half.
    3. second = slow.next; slow.next = None (cut the list).
    4. Sort both halves recursively, then merge them with a dummy node, taking from
       the first list on ties (stable).

Why it works:
    Cutting at the middle halves the problem each time (log n levels) and the merge
    only changes next pointers, so each level costs O(n) without extra storage for
    the nodes themselves.

Time complexity:
    O(n log n) in all cases.

Space complexity:
    O(log n) recursion stack; no extra nodes are created (nodes are relinked).

Edge cases:
    Empty list, single node, two nodes, duplicates, already sorted, reversed.

Alternative approach:
    Insertion sort on a linked list (13-Insertion-Sort file 09) is O(n^2) in the
    worst case. Bottom-up merge sort on a list achieves O(1) stack space.
"""


class Node:
    """A node of a singly linked list."""

    def __init__(self, value):
        self.value = value
        self.next = None


def build_list(values):
    """Create a linked list from a Python list and return its head."""
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


def to_text(head):
    """Return the list as 'a -> b -> c' (or 'empty')."""
    parts = []
    current = head
    while current is not None:
        parts.append(str(current.value))
        current = current.next
    return " -> ".join(parts) if parts else "empty"


def split_middle(head):
    """Cut the list after its first half and return the head of the second half."""
    slow = head
    fast = head.next
    while fast is not None and fast.next is not None:
        slow = slow.next
        fast = fast.next.next
    second = slow.next
    slow.next = None  # end the first half
    return second


def merge_lists(a, b):
    """Merge two sorted linked lists by relinking nodes."""
    dummy = Node(0)
    tail = dummy
    while a is not None and b is not None:
        if a.value <= b.value:  # "<=" keeps equal values in original order
            tail.next = a
            a = a.next
        else:
            tail.next = b
            b = b.next
        tail = tail.next
    # One list is empty; attach the other one as it is
    tail.next = a if a is not None else b
    return dummy.next


def merge_sort_list(head):
    """Sort a linked list and return the new head."""
    if head is None or head.next is None:
        return head
    second = split_middle(head)
    left = merge_sort_list(head)
    right = merge_sort_list(second)
    return merge_lists(left, right)


def main():
    for values in ([4, 2, 1, 3], [-1, 5, 3, 4, 0], [2, 2, 1], [9, 1], [7], []):
        head = build_list(values)
        print(f"Before: {to_text(head)}")
        head = merge_sort_list(head)
        print(f"After : {to_text(head)}")
        print()


if __name__ == "__main__":
    main()
