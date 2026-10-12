r"""
Problem: Insert at Head, Tail and Any Position

Problem statement:
    Implement insert_at_head, insert_at_tail and insert_at_position(index,
    value) for a doubly linked list. Invalid positions must be rejected.

What it teaches:
    Rewiring prev and next pointers in the correct order, and handling the
    head, tail and middle cases separately.

Input example:
    Start empty. insert_at_tail(20), insert_at_head(10), insert_at_tail(40),
    insert_at_position(2, 30), insert_at_position(9, 99)

Expected output:
    After head/tail inserts : [10, 20, 40]
    Insert 30 at index 2    : True [10, 20, 30, 40]
    Insert 99 at index 9    : False [10, 20, 30, 40]
    Insert -1 at index -1   : False [10, 20, 30, 40]
    Backward check          : [40, 30, 20, 10]
    Size                    : 4

Approach:
    Delegate position 0 to head insertion and position size to tail
    insertion; for a middle index walk to the node currently at that index
    and splice the new node before it.

Step-by-step logic:
    1. Head insert: new.next = head; head.prev = new (if head exists); head
    = new.
    2. Tail insert: mirror image using tail.
    3. Middle insert: walk index steps to find the node 'after'.
    4. Set new.prev = after.prev, new.next = after.
    5. Set after.prev.next = new, then after.prev = new.

Why it works:
    A splice needs exactly four pointer changes; doing them in an order that
    never loses a reference keeps the list intact.

Time complexity:
    Head and tail insert O(1); positional insert O(n).

Space complexity:
    O(1) extra per insertion.

Edge cases:
    Empty list, index 0, index equal to size, negative index, index larger
    than size.

Alternative approach:
    Walk from the tail when the index is in the second half to halve the
    walking cost.
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

    def insert_at_head(self, data):
        node = Node(data)
        if self.head is None:
            self.head = self.tail = node
        else:
            node.next = self.head
            self.head.prev = node
            self.head = node
        self.size += 1

    def insert_at_tail(self, data):
        node = Node(data)
        if self.tail is None:
            self.head = self.tail = node
        else:
            node.prev = self.tail
            self.tail.next = node
            self.tail = node
        self.size += 1

    def insert_at_position(self, index, data):
        if index < 0 or index > self.size:
            return False
        if index == 0:
            self.insert_at_head(data)
        elif index == self.size:
            self.insert_at_tail(data)
        else:
            after = self.head
            for _ in range(index):  # node currently at 'index'
                after = after.next
            node = Node(data)
            node.prev = after.prev
            node.next = after
            after.prev.next = node
            after.prev = node
            self.size += 1
        return True

    def to_list(self):
        items, current = [], self.head
        while current:
            items.append(current.data)
            current = current.next
        return items

    def to_list_backward(self):
        items, current = [], self.tail
        while current:
            items.append(current.data)
            current = current.prev
        return items


def main():
    dll = DoublyLinkedList()
    dll.insert_at_tail(20)
    dll.insert_at_head(10)
    dll.insert_at_tail(40)
    print("After head/tail inserts :", dll.to_list())
    print("Insert 30 at index 2    :", dll.insert_at_position(2, 30), dll.to_list())
    print("Insert 99 at index 9    :", dll.insert_at_position(9, 99), dll.to_list())
    print("Insert -1 at index -1   :", dll.insert_at_position(-1, -1), dll.to_list())
    print("Backward check          :", dll.to_list_backward())
    print("Size                    :", dll.size)


if __name__ == "__main__":
    main()
