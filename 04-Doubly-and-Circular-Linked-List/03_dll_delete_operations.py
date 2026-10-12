r"""
Problem: Delete from Head, Tail and by Value

Problem statement:
    Implement delete_head, delete_tail and delete_value(value) (first
    occurrence) for a doubly linked list and return whether a node was
    removed.

What it teaches:
    Unlinking a node using its own prev and next, and keeping head and tail
    correct when the last node disappears.

Input example:
    list = 10 <-> 20 <-> 30 <-> 40 <-> 50; delete_head(), delete_tail(),
    delete_value(30), delete_value(99)

Expected output:
    Start         : [10, 20, 30, 40, 50]
    delete_head   : 10 [20, 30, 40, 50]
    delete_tail   : 50 [20, 30, 40]
    delete 30     : True [20, 40]
    delete 99     : False [20, 40]
    Single node removed -> head: None tail: None
    Delete from empty: None

Approach:
    Find the node, then connect its prev neighbour to its next neighbour;
    special-case the ends.

Step-by-step logic:
    1. Locate the node to delete (head, tail, or first node holding the value).
    2. If node.prev exists set node.prev.next = node.next, else head =
    node.next.
    3. If node.next exists set node.next.prev = node.prev, else tail =
    node.prev.
    4. Decrease the size.

Why it works:
    Because each node has a prev link, no 'previous node' search is needed:
    deletion after finding the node is O(1).

Time complexity:
    delete_head and delete_tail O(1); delete_value O(n) to find the node.

Space complexity:
    O(1).

Edge cases:
    Deleting from an empty list, deleting the only node, value not present,
    value appearing several times.

Alternative approach:
    Store a dictionary from value to node for O(1) lookup (costs O(n) extra
    space and needs unique values).
"""


class Node:
    """A doubly linked list node."""

    def __init__(self, data):
        self.data = data
        self.prev = None
        self.next = None


class DoublyLinkedList:
    def __init__(self, values=()):
        self.head = None
        self.tail = None
        self.size = 0
        for value in values:
            self.append(value)

    def append(self, data):
        node = Node(data)
        if self.tail is None:
            self.head = self.tail = node
        else:
            node.prev = self.tail
            self.tail.next = node
            self.tail = node
        self.size += 1

    def _unlink(self, node):
        # Connect the neighbours around 'node'
        if node.prev:
            node.prev.next = node.next
        else:
            self.head = node.next
        if node.next:
            node.next.prev = node.prev
        else:
            self.tail = node.prev
        self.size -= 1
        return node.data

    def delete_head(self):
        return None if self.head is None else self._unlink(self.head)

    def delete_tail(self):
        return None if self.tail is None else self._unlink(self.tail)

    def delete_value(self, value):
        current = self.head
        while current:
            if current.data == value:
                self._unlink(current)
                return True
            current = current.next
        return False

    def to_list(self):
        items, current = [], self.head
        while current:
            items.append(current.data)
            current = current.next
        return items


def main():
    dll = DoublyLinkedList([10, 20, 30, 40, 50])
    print("Start         :", dll.to_list())
    print("delete_head   :", dll.delete_head(), dll.to_list())
    print("delete_tail   :", dll.delete_tail(), dll.to_list())
    print("delete 30     :", dll.delete_value(30), dll.to_list())
    print("delete 99     :", dll.delete_value(99), dll.to_list())
    single = DoublyLinkedList([5])
    single.delete_head()
    print("Single node removed -> head:", single.head, "tail:", single.tail)
    print("Delete from empty:", DoublyLinkedList().delete_tail())


if __name__ == "__main__":
    main()
