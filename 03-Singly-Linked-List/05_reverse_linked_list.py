"""
Problem title:
    Reverse a Singly Linked List

Problem statement:
    Reverse the direction of every link so that the last node becomes the head.
    Provide an iterative solution and a recursive solution.

What it teaches:
    - The classic three-pointer technique (previous, current, next).
    - Rewiring links in place instead of copying values.
    - How recursion can express the same idea using the call stack.

Input example:
    1 -> 2 -> 3 -> 4 -> 5

Expected output:
    Original:           [1, 2, 3, 4, 5]
    Reversed (iter):    [5, 4, 3, 2, 1]
    Reversed back (rec): [1, 2, 3, 4, 5]
    Empty: []
    Single: [42]

Approach:
    Iterative: for each node, save its next, point it backwards to previous,
    then step forward. Recursive: reverse the rest, then make the second node
    point back to the first.

Step-by-step logic:
    1. previous = None, current = head.
    2. Save following = current.next (otherwise we lose the rest of the list).
    3. current.next = previous (flip the arrow).
    4. previous = current; current = following.
    5. When current is None, previous is the new head.

    Dry run on 1 -> 2 -> 3:
      start     prev=None cur=1
      flip 1    None <- 1   prev=1 cur=2
      flip 2    None <- 1 <- 2   prev=2 cur=3
      flip 3    None <- 1 <- 2 <- 3   prev=3 cur=None -> new head = 3

Why it works:
    Each node is flipped exactly once, and we always hold a reference to the
    not-yet-processed part of the list in "following".

Time complexity:
    O(n) for both versions.

Space complexity:
    Iterative O(1). Recursive O(n) because of the call stack.

Edge cases:
    - Empty list (returns None).
    - Single node (returns itself).
    - Very long lists can overflow Python's recursion limit in the recursive
      version (about 1000 frames by default).

Alternative approach:
    Push all values on a stack and rebuild; simpler but uses O(n) extra space.
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


def reverse_iterative(head):
    previous = None
    current = head
    while current is not None:
        following = current.next  # remember the rest before breaking the link
        current.next = previous   # flip the arrow
        previous = current        # advance both pointers
        current = following
    return previous


def reverse_recursive(head):
    # Base case: empty list or last node
    if head is None or head.next is None:
        return head
    new_head = reverse_recursive(head.next)  # reverse everything after head
    head.next.next = head  # the next node now points back to head
    head.next = None       # head becomes the tail
    return new_head


def main():
    head = build_list([1, 2, 3, 4, 5])
    print("Original:          ", to_list(head))
    head = reverse_iterative(head)
    print("Reversed (iter):   ", to_list(head))
    head = reverse_recursive(head)
    print("Reversed back (rec):", to_list(head))

    print("Empty:", to_list(reverse_iterative(build_list([]))))
    print("Single:", to_list(reverse_recursive(build_list([42]))))


if __name__ == "__main__":
    main()
