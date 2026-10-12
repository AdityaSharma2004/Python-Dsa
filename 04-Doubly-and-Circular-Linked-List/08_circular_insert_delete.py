r"""
Problem: Insert and Delete in a Circular Linked List

Problem statement:
    Implement insert_at_front, insert_at_end and delete_value for a circular
    singly linked list that keeps only a tail pointer. The list must stay
    circular after every operation.

What it teaches:
    Updating the tail correctly and handling the single-node and delete-the-
    tail special cases.

Input example:
    insert_at_end(2), insert_at_end(3), insert_at_front(1), delete_value(3),
    delete_value(1), delete_value(2), delete_value(5)

Expected output:
    After inserts      : [1, 2, 3]
    delete 3 -> True  list: [1, 2]
    delete 1 -> True  list: [2]
    delete 2 -> True  list: []
    delete 5 -> False list: []
    Tail after empty   : None

Approach:
    Insert at front without moving tail; insert at end then move tail;
    delete by walking with a previous pointer starting at the tail.

Step-by-step logic:
    1. Front insert: new.next = tail.next; tail.next = new.
    2. End insert: same as front insert, then tail = new.
    3. Delete: prev = tail, current = tail.next; loop at most size times.
    4. When found: if it is the only node set tail = None; else prev.next =
    current.next.
    5. If the removed node was the tail set tail = prev.

Why it works:
    The circle is preserved because the node before the removed one is
    always linked to the node after it.

Time complexity:
    Inserts O(1); delete O(n).

Space complexity:
    O(1).

Edge cases:
    Empty list, single node, deleting the head, deleting the tail, value not
    found, duplicates (only first removed).

Alternative approach:
    Keep a head pointer too; then every insert and delete at the end needs a
    walk to find the last node.
"""


class Node:
    def __init__(self, data):
        self.data = data
        self.next = None


class CircularLinkedList:
    def __init__(self):
        self.tail = None

    def insert_at_front(self, data):
        node = Node(data)
        if self.tail is None:
            node.next = node
            self.tail = node
        else:
            node.next = self.tail.next
            self.tail.next = node

    def insert_at_end(self, data):
        self.insert_at_front(data)
        self.tail = self.tail.next  # the new node is now the tail

    def delete_value(self, value):
        if self.tail is None:
            return False
        previous, current = self.tail, self.tail.next
        while True:
            if current.data == value:
                if current is previous:  # only node
                    self.tail = None
                else:
                    previous.next = current.next
                    if current is self.tail:
                        self.tail = previous
                return True
            if current is self.tail:  # completed one lap
                return False
            previous, current = current, current.next

    def to_list(self):
        if self.tail is None:
            return []
        items, current = [], self.tail.next
        while True:
            items.append(current.data)
            if current is self.tail:
                break
            current = current.next
        return items


def main():
    clist = CircularLinkedList()
    clist.insert_at_end(2)
    clist.insert_at_end(3)
    clist.insert_at_front(1)
    print("After inserts      :", clist.to_list())
    for value in (3, 1, 2, 5):
        removed = clist.delete_value(value)
        print("delete %d -> %-5s list: %s" % (value, removed, clist.to_list()))
    print("Tail after empty   :", clist.tail)


if __name__ == "__main__":
    main()
