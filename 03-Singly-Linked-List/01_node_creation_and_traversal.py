"""
Problem title:
    Node Creation and Traversal

Problem statement:
    Build a singly linked list from a Python list of values, then traverse it
    from head to tail, printing every value, and report its length.

What it teaches:
    - What a node is (a value plus a "next" reference).
    - How the head pointer is the only entry point to the list.
    - How to walk a list with a moving "current" pointer.

Input example:
    values = [10, 20, 30, 40]

Expected output:
    Linked list: 10 -> 20 -> 30 -> 40 -> None
    Values in order: [10, 20, 30, 40]
    Length: 4
    Empty list: None
    Empty length: 0

Approach:
    Create a Node class. Build the list by keeping a "tail" pointer so every
    append is O(1). Traverse with a "current" pointer until it becomes None.

Step-by-step logic:
    1. Start with head = None (empty list).
    2. For each value: create a node. If the list is empty it becomes the head;
       otherwise tail.next points to it. Move tail to the new node.
    3. To traverse: current = head; while current is not None, use
       current.data, then current = current.next.
    4. Count nodes during traversal to get the length.

Why it works:
    Each node knows only its successor, so following "next" visits every node
    exactly once and stops at None, which marks the end of the list.

Time complexity:
    Build: O(n). Traverse: O(n). Length: O(n).

Space complexity:
    O(n) for the n nodes created; traversal itself uses O(1) extra space.

Edge cases:
    - Empty input: head stays None, traversal prints nothing, length is 0.
    - Single value: head and tail are the same node.

Alternative approach:
    Keep a size counter inside a LinkedList class to get the length in O(1).
    (Laravel analogy: like a Collection that caches its count instead of
    recounting each time.)
"""


class Node:
    """One element of a singly linked list."""

    def __init__(self, data):
        self.data = data
        self.next = None


def build_list(values):
    """Build a linked list from a Python list and return the head node."""
    head = None
    tail = None
    for value in values:
        node = Node(value)
        if head is None:
            head = node  # first node is both head and tail
        else:
            tail.next = node  # link previous tail to the new node
        tail = node
    return head


def traverse(head):
    """Return the values of the list in order as a Python list."""
    result = []
    current = head
    while current is not None:
        result.append(current.data)
        current = current.next  # move one step forward
    return result


def length(head):
    """Count the nodes in the list."""
    count = 0
    current = head
    while current is not None:
        count += 1
        current = current.next
    return count


def format_list(head):
    """Return a string like 10 -> 20 -> None."""
    parts = [str(value) for value in traverse(head)]
    parts.append("None")
    return " -> ".join(parts)


def main():
    values = [10, 20, 30, 40]
    head = build_list(values)
    print("Linked list:", format_list(head))
    print("Values in order:", traverse(head))
    print("Length:", length(head))

    empty_head = build_list([])
    print("Empty list:", format_list(empty_head))
    print("Empty length:", length(empty_head))


if __name__ == "__main__":
    main()
