"""
Problem title:
    Insertion Sort on a Singly Linked List

Problem statement:
    Sort a singly linked list in ascending order using insertion sort by
    relinking nodes (not by copying values into an array).

What it teaches:
    - Insertion sort with pointers: no shifting is needed, only relinking.
    - Using a dummy head node to avoid special cases when inserting at the front.

Input example:
    4 -> 2 -> 1 -> 3

Expected output:
    Before: 4 -> 2 -> 1 -> 3
    After : 1 -> 2 -> 3 -> 4

    Before: -1 -> 5 -> 3 -> 4 -> 0
    After : -1 -> 0 -> 3 -> 4 -> 5

    Before: 2 -> 2 -> 1
    After : 1 -> 2 -> 2

    Before: 7
    After : 7

    Before: empty
    After : empty

Approach used:
    Build a new sorted list. Take nodes one by one from the old list and insert
    each into the sorted list by walking from a dummy head until the next node
    is not smaller.

Step-by-step logic:
    1. dummy = a placeholder node whose next is the sorted list (initially empty).
    2. For each node in the original list, remember its next node.
    3. Find prev: start at dummy and advance while prev.next.value <= node.value.
    4. Link node between prev and prev.next. Continue with the remembered node.
    5. Return dummy.next.

Why it works:
    The sorted list is always sorted; each node is inserted at the first place
    where the following node is larger, which preserves order and stability.

Time complexity:
    O(n^2) worst case (for example an already sorted list: every insertion scans
    the whole sorted part from the head). Best case O(n) when the input is in
    reverse order, because every new node is smaller than the current head.

Space complexity:
    O(1) extra: nodes are relinked, only a few pointers are used.

Edge cases:
    Empty list, single node, duplicates, already sorted, reverse sorted.

Alternative approach:
    Merge sort for linked lists (file 14/07) is O(n log n).
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


def insertion_sort_list(head):
    """Sort a linked list with insertion sort and return the new head."""
    dummy = Node(0)  # placeholder before the sorted list
    current = head
    while current is not None:
        next_node = current.next  # save before we relink current
        prev = dummy
        # Stop at the first node larger than current (<= keeps stability)
        while prev.next is not None and prev.next.value <= current.value:
            prev = prev.next
        current.next = prev.next
        prev.next = current
        current = next_node
    return dummy.next


def main():
    for values in ([4, 2, 1, 3], [-1, 5, 3, 4, 0], [2, 2, 1], [7], []):
        head = build_list(values)
        print(f"Before: {to_text(head)}")
        head = insertion_sort_list(head)
        print(f"After : {to_text(head)}")
        print()


if __name__ == "__main__":
    main()
