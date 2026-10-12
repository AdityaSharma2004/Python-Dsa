"""
Problem title:
    Nth Node from the End (and Remove It)

Problem statement:
    Return the value of the nth node counting from the END of a singly linked
    list (n = 1 is the last node) using one pass. Then remove that node.

What it teaches:
    - The "gap" two-pointer technique.
    - Using a dummy node to simplify removal of the head.

Input example:
    1 -> 2 -> 3 -> 4 -> 5, n = 2   (value 4)

Expected output:
    n = 1 -> value: 5
    n = 2 -> value: 4
    n = 5 -> value: 1
    n = 6 -> value: None
    remove n = 2 -> [1, 2, 3, 5]
    remove n = 5 -> [2, 3, 4, 5]
    remove n = 1 -> [1, 2, 3, 4]
    remove n = 9 -> [1, 2, 3, 4, 5]

Approach:
    Advance a "lead" pointer n steps ahead, then move lead and "lag" together.
    When lead falls off the end, lag is exactly n nodes from the end.

Step-by-step logic:
    1. Move lead forward n times; if it runs out, n is larger than the list.
    2. lag = head.
    3. While lead is not None: advance both.
    4. lag is the nth node from the end.
    For removal, start lag at a dummy node pointing to head and stop one step
    early so lag is the node BEFORE the target, then lag.next = lag.next.next.

Why it works:
    The distance between lead and lag stays n. When lead is past the last node
    (None), lag sits n nodes before that None, i.e. the nth node from the end.

Time complexity:
    O(n), single pass.

Space complexity:
    O(1).

Edge cases:
    - n greater than length, or n <= 0: invalid.
    - n equals length: the head is the target (dummy node handles removal).
    - Single node list.

Alternative approach:
    Count the length L, then the target is at index L - n from the start.
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


def nth_from_end(head, n):
    """Return the value of the nth node from the end, or None if invalid."""
    if n <= 0:
        return None
    lead = head
    for _ in range(n):
        if lead is None:
            return None  # n is larger than the list
        lead = lead.next
    lag = head
    while lead is not None:
        lead = lead.next
        lag = lag.next
    return lag.data


def remove_nth_from_end(head, n):
    """Remove the nth node from the end and return the new head."""
    if n <= 0:
        return head
    dummy = Node(0)  # lets us treat head removal like any other removal
    dummy.next = head
    lead = dummy
    for _ in range(n):
        lead = lead.next
        if lead is None:
            return head  # n too large, nothing removed
    lag = dummy
    while lead.next is not None:  # stop one early so lag is BEFORE the target
        lead = lead.next
        lag = lag.next
    lag.next = lag.next.next
    return dummy.next


def main():
    values = [1, 2, 3, 4, 5]
    head = build_list(values)
    for n in (1, 2, 5, 6):
        print("n =", n, "-> value:", nth_from_end(head, n))

    for n in (2, 5, 1, 9):
        head = build_list(values)
        head = remove_nth_from_end(head, n)
        print("remove n =", n, "->", to_list(head))


if __name__ == "__main__":
    main()
