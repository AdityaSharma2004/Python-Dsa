"""
Problem title:
    Remove Duplicates from a Linked List

Problem statement:
    Remove repeated values. Part A: the list is SORTED, so duplicates sit next
    to each other. Part B: the list is UNSORTED; keep the first occurrence of
    each value.

What it teaches:
    - Using adjacency in sorted data to remove duplicates in O(1) space.
    - Using a set to trade memory for speed on unsorted data.
    - Safe deletion while traversing.

Input example:
    sorted:   1 -> 1 -> 2 -> 3 -> 3 -> 3 -> 4
    unsorted: 4 -> 2 -> 4 -> 1 -> 2 -> 5

Expected output:
    Sorted before:   [1, 1, 2, 3, 3, 3, 4]
    Sorted after:    [1, 2, 3, 4]
    Unsorted before: [4, 2, 4, 1, 2, 5]
    Unsorted after:  [4, 2, 1, 5]
    All equal: [7]
    Empty: []

Approach:
    Sorted: compare each node with its next; if equal, bypass the next node.
    Unsorted: keep a set of seen values; bypass any node already in the set.

Step-by-step logic:
    Sorted:
      1. current = head.
      2. While current and current.next exist: if values are equal, set
         current.next = current.next.next (do not advance, the new next might
         also be equal); otherwise advance.
    Unsorted:
      1. seen = {head.data}; previous = head; current = head.next.
      2. If current.data in seen: previous.next = current.next.
         Otherwise add to seen and move previous forward.
      3. Always move current to the following node.

Why it works:
    In sorted data equal values are contiguous, so a local comparison is
    enough. In unsorted data the set remembers every value met so far.

Time complexity:
    Sorted: O(n). Unsorted with set: O(n) average.

Space complexity:
    Sorted: O(1). Unsorted: O(n) for the set.

Edge cases:
    - Empty list and single node.
    - All values equal (list collapses to one node).
    - Duplicates at the tail.
    - Without a set, an O(n^2) nested-loop approach gives O(1) space.

Alternative approach:
    For unsorted lists with no extra memory, for each node scan the rest of the
    list and delete matches (O(n^2) time).
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


def to_list(head):
    values = []
    while head is not None:
        values.append(head.data)
        head = head.next
    return values


def remove_duplicates_sorted(head):
    current = head
    while current is not None and current.next is not None:
        if current.data == current.next.data:
            current.next = current.next.next  # skip the duplicate
        else:
            current = current.next
    return head


def remove_duplicates_unsorted(head):
    if head is None:
        return head
    seen = {head.data}
    previous = head
    current = head.next
    while current is not None:
        if current.data in seen:
            previous.next = current.next  # bypass the repeated node
        else:
            seen.add(current.data)
            previous = current
        current = current.next
    return head


def main():
    sorted_head = build_list([1, 1, 2, 3, 3, 3, 4])
    print("Sorted before:  ", to_list(sorted_head))
    print("Sorted after:   ", to_list(remove_duplicates_sorted(sorted_head)))

    unsorted_head = build_list([4, 2, 4, 1, 2, 5])
    print("Unsorted before:", to_list(unsorted_head))
    print("Unsorted after: ", to_list(remove_duplicates_unsorted(unsorted_head)))

    print("All equal:", to_list(remove_duplicates_sorted(build_list([7, 7, 7]))))
    print("Empty:", to_list(remove_duplicates_unsorted(build_list([]))))


if __name__ == "__main__":
    main()
