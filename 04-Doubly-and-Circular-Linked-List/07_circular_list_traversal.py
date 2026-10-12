r"""
Problem: Create and Traverse a Circular Linked List

Problem statement:
    Build a circular singly linked list from a Python list, traverse it
    exactly once, count its nodes, and show that following next pointers
    keeps cycling.

What it teaches:
    The do-while style loop needed because there is no None terminator, and
    how a tail pointer gives O(1) access to both ends.

Input example:
    values = [1, 2, 3, 4]

Expected output:
    One full traversal : [1, 2, 3, 4]
    Node count         : 4
    Walk 7 steps       : [1, 2, 3, 4, 1, 2, 3]
    Tail points to head: True
    Single node        : [9] self loop: True
    Empty list         : []

Approach:
    Keep only a tail pointer; tail.next is the head. Traverse by starting at
    head and stopping when we return to it.

Step-by-step logic:
    1. Create nodes; link each new node after the tail.
    2. Set new_node.next = tail.next (the head), then tail.next = new_node,
    then tail = new_node.
    3. Traverse: current = tail.next (head); print; move next.
    4. Stop when current is back at the head.
    5. Demonstrate wrap-around by taking n + 2 steps.

Why it works:
    In a circle the only reliable stopping point is the starting node, so we
    compare against it instead of None.

Time complexity:
    Build O(n); traversal and count O(n).

Space complexity:
    O(n) for nodes, O(1) extra.

Edge cases:
    Empty list (tail is None), single node pointing to itself, using while
    current is not None by mistake gives an infinite loop.

Alternative approach:
    Keep a head pointer and a size counter and loop size times.
"""


class Node:
    def __init__(self, data):
        self.data = data
        self.next = None


class CircularLinkedList:
    def __init__(self, values=()):
        self.tail = None
        for value in values:
            self.append(value)

    def append(self, data):
        node = Node(data)
        if self.tail is None:
            node.next = node  # a lone node points to itself
            self.tail = node
        else:
            node.next = self.tail.next  # new node points to head
            self.tail.next = node
            self.tail = node

    def to_list(self):
        if self.tail is None:
            return []
        items = []
        head = self.tail.next
        current = head
        while True:  # do-while: stop on returning to head
            items.append(current.data)
            current = current.next
            if current is head:
                break
        return items

    def walk(self, steps):
        """Return the data seen while taking 'steps' steps (shows wrap-around)."""
        if self.tail is None:
            return []
        seen, current = [], self.tail.next
        for _ in range(steps):
            seen.append(current.data)
            current = current.next
        return seen


def main():
    clist = CircularLinkedList([1, 2, 3, 4])
    items = clist.to_list()
    print("One full traversal :", items)
    print("Node count         :", len(items))
    print("Walk 7 steps       :", clist.walk(7))
    print("Tail points to head:", clist.tail.next.data == items[0])
    single = CircularLinkedList([9])
    print("Single node        :", single.to_list(), "self loop:", single.tail.next is single.tail)
    print("Empty list         :", CircularLinkedList().to_list())


if __name__ == "__main__":
    main()
