r"""
Problem: Check if a Doubly Linked List is a Palindrome

Problem statement:
    Given a doubly linked list of characters or numbers, return True if it
    reads the same forwards and backwards.

What it teaches:
    Why a tail pointer plus prev links makes the classic two-pointer
    palindrome check O(1) space.

Input example:
    ['r','a','c','e','c','a','r'], ['a','b','c'], [1,2,2,1]

Expected output:
    ['r', 'a', 'c', 'e', 'c', 'a', 'r'] palindrome? True
    ['a', 'b', 'b', 'a']   palindrome? True
    ['a', 'b', 'c']        palindrome? False
    [1, 2, 2, 1]           palindrome? True
    [1, 2, 3, 1]           palindrome? False
    [7]                    palindrome? True
    []                     palindrome? True

Approach:
    Compare the front and back nodes, move them toward each other, and stop
    when they meet or cross.

Step-by-step logic:
    1. Start left at head and right at tail.
    2. While left is not right and left.prev is not right compare data.
    3. Return False on the first mismatch.
    4. Move left = left.next and right = right.prev.
    5. Return True if all pairs matched.

Why it works:
    A palindrome means element i equals element n-1-i, which is exactly what
    the two moving pointers compare.

Time complexity:
    O(n) (n/2 comparisons).

Space complexity:
    O(1).

Edge cases:
    Empty list and one node are palindromes, even length, odd length, case
    sensitivity.

Alternative approach:
    For a singly linked list you would reverse the second half or use a
    stack, because there is no prev link.
"""


class Node:
    """A doubly linked list node."""

    def __init__(self, data):
        self.data = data
        self.prev = None
        self.next = None


def build(values):
    head = tail = None
    for value in values:
        node = Node(value)
        if head is None:
            head = tail = node
        else:
            tail.next = node
            node.prev = tail
            tail = node
    return head, tail


def is_palindrome(head, tail):
    left, right = head, tail
    while left is not None and left is not right and left.prev is not right:
        if left.data != right.data:
            return False
        left = left.next
        right = right.prev
    return True


def main():
    samples = [list("racecar"), list("abba"), list("abc"), [1, 2, 2, 1], [1, 2, 3, 1], [7], []]
    for values in samples:
        head, tail = build(values)
        print("%-22s palindrome? %s" % (values, is_palindrome(head, tail)))


if __name__ == "__main__":
    main()
