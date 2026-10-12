"""
Problem title:
    Detect a Cycle (Floyd's Algorithm) and Find Where It Starts

Problem statement:
    Determine whether a singly linked list contains a cycle (some node's next
    points back to an earlier node). If it does, return the node where the
    cycle begins.

What it teaches:
    - Floyd's tortoise and hare cycle detection.
    - Why a cycle makes a naive traversal loop forever.
    - A hash-set alternative and its space trade-off.

Input example:
    1 -> 2 -> 3 -> 4 -> 5 -> (back to 3)

Expected output:
    1-2-3-4-5, tail -> 3 | cycle starts at: 3 | set check: True
    1-2-3-4, tail -> 1 (full loop) | cycle starts at: 1 | set check: True
    7, self-loop | cycle starts at: 7 | set check: True
    1-2-3, no cycle | cycle starts at: none | set check: False
    empty | cycle starts at: none | set check: False

Approach:
    Phase 1: slow moves 1 step, fast moves 2 steps. If they meet, there is a
    cycle. Phase 2: put one pointer at head, keep the other at the meeting
    point, move both one step at a time; they meet at the cycle start.

Step-by-step logic:
    1. slow = fast = head.
    2. While fast and fast.next: advance slow by 1, fast by 2; if slow is fast,
       a cycle exists.
    3. For the start: set finder = head; advance finder and slow together until
       finder is slow. That node is the cycle entrance.

Why it works:
    Inside a cycle fast gains one node on slow each step, so it must eventually
    land on slow. Let the distance from head to the cycle start be a. At the
    meeting point slow has walked a + b and fast 2(a + b), and the difference
    is a whole number of laps, so walking a more steps from the meeting point
    reaches the cycle start, exactly as a pointer from head does.

Time complexity:
    O(n).

Space complexity:
    O(1) for Floyd; O(n) for the visited-set alternative.

Edge cases:
    - Empty list or single node without a self-loop: no cycle.
    - Self-loop (node.next is node): cycle starts at that node.
    - Whole list is a cycle (tail points to head).

Alternative approach:
    Store visited nodes in a set; the first node seen twice is the cycle start.
"""


class Node:
    def __init__(self, data):
        self.data = data
        self.next = None


def build_list(values, cycle_to_index=None):
    """Build a list; if cycle_to_index is given, tail.next links to that node."""
    nodes = [Node(value) for value in values]
    for position in range(len(nodes) - 1):
        nodes[position].next = nodes[position + 1]
    if cycle_to_index is not None and nodes:
        nodes[-1].next = nodes[cycle_to_index]
    return nodes[0] if nodes else None


def find_cycle_start(head):
    """Return the node where the cycle begins, or None if there is no cycle."""
    slow = head
    fast = head
    while fast is not None and fast.next is not None:
        slow = slow.next
        fast = fast.next.next
        if slow is fast:  # compare identity, not value
            finder = head
            while finder is not slow:
                finder = finder.next
                slow = slow.next
            return finder
    return None


def has_cycle_with_set(head):
    """Alternative: remember visited nodes (uses O(n) memory)."""
    visited = set()
    current = head
    while current is not None:
        if current in visited:
            return True
        visited.add(current)
        current = current.next
    return False


def main():
    cases = [
        ("1-2-3-4-5, tail -> 3", [1, 2, 3, 4, 5], 2),
        ("1-2-3-4, tail -> 1 (full loop)", [1, 2, 3, 4], 0),
        ("7, self-loop", [7], 0),
        ("1-2-3, no cycle", [1, 2, 3], None),
        ("empty", [], None),
    ]
    for label, values, cycle_index in cases:
        head = build_list(values, cycle_index)
        start = find_cycle_start(head)
        start_text = "none" if start is None else str(start.data)
        print(label, "| cycle starts at:", start_text,
              "| set check:", has_cycle_with_set(head))


if __name__ == "__main__":
    main()
