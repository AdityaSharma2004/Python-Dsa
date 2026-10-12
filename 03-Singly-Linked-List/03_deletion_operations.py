"""
Problem title:
    Delete a Node by Value and by Position

Problem statement:
    Implement delete_value(value), which removes the first node holding that
    value, and delete_at(index), which removes the node at a position. Both
    return True if something was deleted, otherwise False.

What it teaches:
    - Deleting the head versus deleting a middle/tail node.
    - Keeping a "previous" pointer so we can bypass the doomed node.
    - Why deleting from an empty list must be handled explicitly.

Input example:
    list = 5 -> 10 -> 15 -> 20 -> 25
    delete_value(5), delete_value(20), delete_at(1), delete_value(99)

Expected output:
    Start: [5, 10, 15, 20, 25]
    delete_value(5)  -> True [10, 15, 20, 25]
    delete_value(20) -> True [10, 15, 25]
    delete_at(1)     -> True [10, 25]
    delete_value(99) -> False [10, 25]
    delete_at(7)     -> False [10, 25]
    Empty delete_value(1) -> False

Approach:
    Track "previous" and "current" while scanning. To delete current, set
    previous.next = current.next. If current is the head, move head forward.

Step-by-step logic:
    1. If the list is empty, return False.
    2. If the head matches, head = head.next and return True.
    3. Otherwise walk with previous/current until current matches.
    4. Bypass it: previous.next = current.next.
    5. If we run out of nodes, the value or index was not found: return False.

Why it works:
    A singly linked list node has no back reference, so we need the node before
    the target to rewire the chain. Once nothing points to the target it is
    unreachable and Python's garbage collector frees it.

Time complexity:
    O(n) worst case for both operations (head deletion is O(1)).

Space complexity:
    O(1).

Edge cases:
    - Empty list.
    - Deleting the head, the tail, or the only node.
    - Value not present / index out of range / negative index.
    - Duplicates: only the FIRST match is removed.

Alternative approach:
    Use a dummy node before the head so the head needs no special case.
"""


class Node:
    def __init__(self, data):
        self.data = data
        self.next = None


class LinkedList:
    def __init__(self, values=()):
        self.head = None
        tail = None
        for value in values:
            node = Node(value)
            if self.head is None:
                self.head = node
            else:
                tail.next = node
            tail = node

    def delete_value(self, value):
        if self.head is None:
            return False
        if self.head.data == value:  # special case: removing the head
            self.head = self.head.next
            return True
        previous = self.head
        current = self.head.next
        while current is not None:
            if current.data == value:
                previous.next = current.next  # bypass the target node
                return True
            previous = current
            current = current.next
        return False

    def delete_at(self, index):
        if self.head is None or index < 0:
            return False
        if index == 0:
            self.head = self.head.next
            return True
        previous = self.head
        for _ in range(index - 1):
            previous = previous.next
            if previous is None:
                return False
        if previous.next is None:  # index == length or beyond
            return False
        previous.next = previous.next.next
        return True

    def to_list(self):
        values = []
        current = self.head
        while current is not None:
            values.append(current.data)
            current = current.next
        return values


def main():
    linked_list = LinkedList([5, 10, 15, 20, 25])
    print("Start:", linked_list.to_list())

    print("delete_value(5)  ->", linked_list.delete_value(5), linked_list.to_list())
    print("delete_value(20) ->", linked_list.delete_value(20), linked_list.to_list())
    print("delete_at(1)     ->", linked_list.delete_at(1), linked_list.to_list())
    print("delete_value(99) ->", linked_list.delete_value(99), linked_list.to_list())
    print("delete_at(7)     ->", linked_list.delete_at(7), linked_list.to_list())

    empty = LinkedList()
    print("Empty delete_value(1) ->", empty.delete_value(1))


if __name__ == "__main__":
    main()
