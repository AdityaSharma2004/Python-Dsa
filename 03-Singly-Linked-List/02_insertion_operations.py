"""
Problem title:
    Insertion at Head, Tail and Any Position

Problem statement:
    Implement a LinkedList class with three insertion operations:
    insert_at_head(value), insert_at_tail(value) and
    insert_at_position(index, value). Invalid positions must be rejected.

What it teaches:
    - Re-linking pointers in the correct order so no node is lost.
    - Why head insertion is O(1) but tail insertion needs a walk (or a tail
      pointer).
    - Handling position 0, position == length and out-of-range positions.

Input example:
    insert_at_tail(20), insert_at_tail(30), insert_at_head(10),
    insert_at_position(2, 25), insert_at_position(9, 99)

Expected output:
    After tail inserts 20, 30: [20, 30]
    After head insert 10:     [10, 20, 30]
    Insert 25 at index 2 (True): [10, 20, 25, 30]
    Insert 40 at index 4 (True): [10, 20, 25, 30, 40]
    Insert 99 at index 9 (False): [10, 20, 25, 30, 40]

Approach:
    Walk to the node just BEFORE the insertion point, then splice the new node
    in: new.next = prev.next first, then prev.next = new.

Step-by-step logic:
    1. Head insertion: new.next = head; head = new.
    2. Tail insertion: if empty, head = new; else walk to the last node and set
       last.next = new.
    3. Position insertion: if index == 0 use head insertion. Otherwise move
       (index - 1) steps; if we fall off the list the index is invalid.
       Then new.next = prev.next; prev.next = new.

Why it works:
    Setting new.next BEFORE changing prev.next keeps a reference to the rest of
    the list, so nothing is disconnected during the splice.

Time complexity:
    Head: O(1). Tail: O(n). Position: O(index), worst case O(n).

Space complexity:
    O(1) extra space per insertion.

Edge cases:
    - Inserting into an empty list.
    - index == 0 (new head) and index == length (new tail).
    - Negative or too-large index: returns False and changes nothing.

Alternative approach:
    Store a tail pointer so insert_at_tail becomes O(1).
"""


class Node:
    def __init__(self, data):
        self.data = data
        self.next = None


class LinkedList:
    def __init__(self):
        self.head = None

    def insert_at_head(self, value):
        node = Node(value)
        node.next = self.head  # new node points to the old first node
        self.head = node

    def insert_at_tail(self, value):
        node = Node(value)
        if self.head is None:
            self.head = node
            return
        current = self.head
        while current.next is not None:  # stop on the LAST node
            current = current.next
        current.next = node

    def insert_at_position(self, index, value):
        """Insert so the new node ends up at 'index'. Return True on success."""
        if index < 0:
            return False
        if index == 0:
            self.insert_at_head(value)
            return True
        previous = self.head
        for _ in range(index - 1):
            if previous is None:
                return False
            previous = previous.next
        if previous is None:  # index is beyond the end
            return False
        node = Node(value)
        node.next = previous.next  # keep the rest of the list first
        previous.next = node
        return True

    def to_list(self):
        values = []
        current = self.head
        while current is not None:
            values.append(current.data)
            current = current.next
        return values


def show(label, linked_list):
    print(label, linked_list.to_list())


def main():
    linked_list = LinkedList()
    linked_list.insert_at_tail(20)
    linked_list.insert_at_tail(30)
    show("After tail inserts 20, 30:", linked_list)

    linked_list.insert_at_head(10)
    show("After head insert 10:    ", linked_list)

    ok = linked_list.insert_at_position(2, 25)
    show("Insert 25 at index 2 (" + str(ok) + "):", linked_list)

    ok = linked_list.insert_at_position(4, 40)
    show("Insert 40 at index 4 (" + str(ok) + "):", linked_list)

    ok = linked_list.insert_at_position(9, 99)
    show("Insert 99 at index 9 (" + str(ok) + "):", linked_list)


if __name__ == "__main__":
    main()
