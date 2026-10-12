r"""
Problem: Create a Doubly Linked List and Traverse It Both Ways

Problem statement:
    Build a doubly linked list from a Python list. Print it from head to
    tail and then from tail to head. Also return the length.

What it teaches:
    How a doubly linked list node stores two links, how head and tail are
    kept, and why backward traversal is cheap.

Input example:
    values = [10, 20, 30, 40]

Expected output:
    Input    : [10, 20, 30, 40]
    Forward  : 10 <-> 20 <-> 30 <-> 40
    Backward : 40 <-> 30 <-> 20 <-> 10
    Length   : 4

    Input    : [7]
    Forward  : 7
    Backward : 7
    Length   : 1

    Input    : []
    Forward  : (empty)
    Backward : (empty)
    Length   : 0

Approach:
    Append each value at the tail while keeping a tail pointer, then walk
    next pointers forward and prev pointers backward.

Step-by-step logic:
    1. Create an empty list with head = None and tail = None.
    2. For each value create a node; if the list is empty it is both head
    and tail.
    3. Otherwise link tail.next = node and node.prev = tail, then move tail.
    4. Forward: start at head and follow next until None.
    5. Backward: start at tail and follow prev until None.

Why it works:
    Every node knows both neighbours, so the tail pointer gives O(1) append
    and prev links give a direct way back.

Time complexity:
    Build O(n), each traversal O(n).

Space complexity:
    O(n) for the nodes, O(1) extra for traversal.

Edge cases:
    Empty list (both traversals print nothing), a single node (head is
    tail), duplicate values.

Alternative approach:
    Keep only a head pointer and find the tail by walking, which makes each
    append O(n).
"""


class Node:
    """A doubly linked list node."""

    def __init__(self, data):
        self.data = data
        self.prev = None
        self.next = None


class DoublyLinkedList:
    def __init__(self):
        self.head = None
        self.tail = None
        self.size = 0

    def append(self, data):
        node = Node(data)
        if self.head is None:  # empty list: node is both ends
            self.head = self.tail = node
        else:
            self.tail.next = node
            node.prev = self.tail
            self.tail = node
        self.size += 1

    def forward(self):
        items, current = [], self.head
        while current is not None:
            items.append(current.data)
            current = current.next
        return items

    def backward(self):
        items, current = [], self.tail
        while current is not None:
            items.append(current.data)
            current = current.prev
        return items


def from_list(values):
    dll = DoublyLinkedList()
    for value in values:
        dll.append(value)
    return dll


def show(items):
    return " <-> ".join(str(x) for x in items) if items else "(empty)"


def main():
    for values in ([10, 20, 30, 40], [7], []):
        dll = from_list(values)
        print("Input    :", values)
        print("Forward  :", show(dll.forward()))
        print("Backward :", show(dll.backward()))
        print("Length   :", dll.size)
        print()


if __name__ == "__main__":
    main()
