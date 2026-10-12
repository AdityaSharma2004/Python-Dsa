r"""
Problem: Josephus Problem with a Circular Linked List

Problem statement:
    n people stand in a circle numbered 1..n. Starting from person 1, every
    k-th person is eliminated until one remains. Return the elimination
    order and the survivor.

What it teaches:
    Using a circular list to model a ring and deleting while walking.

Input example:
    n = 7, k = 3

Expected output:
    n=7 k=3 eliminated=[3, 6, 2, 7, 5, 1] survivor=4 (formula says 4)
    n=5 k=2 eliminated=[2, 4, 1, 5] survivor=3 (formula says 3)
    n=1 k=4 eliminated=[] survivor=1 (formula says 1)
    n=6 k=1 eliminated=[1, 2, 3, 4, 5] survivor=6 (formula says 6)
    n=4 k=10 eliminated=[2, 3, 1] survivor=4 (formula says 4)

Approach:
    Build a circular list, then repeatedly move k-1 steps, remove the next
    node and continue from the following node.

Step-by-step logic:
    1. Build a circle 1..n with a node pointing to the next.
    2. Keep 'previous' pointing at the node just before the current start.
    3. Move previous forward k-1 times.
    4. Remove previous.next, record it and link previous to the node after it.
    5. Stop when previous.next is previous (one person left).

Why it works:
    Walking k-1 steps from the node before the start lands on the node
    before the k-th person, so we can unlink the k-th person in O(1).

Time complexity:
    O(n * k): each of n-1 eliminations takes k-1 steps.

Space complexity:
    O(n) for the circle.

Edge cases:
    n = 1, k = 1 (eliminates in order), k larger than n (wraps naturally), n
    or k not positive.

Alternative approach:
    The mathematical recurrence J(n) = (J(n-1) + k) mod n solves the
    survivor in O(n) time and O(1) space (verified in the code).
"""


class Node:
    def __init__(self, data):
        self.data = data
        self.next = None


def build_circle(n):
    head = Node(1)
    current = head
    for number in range(2, n + 1):
        current.next = Node(number)
        current = current.next
    current.next = head  # close the circle
    return current  # the last node, i.e. the one before person 1


def josephus(n, k):
    if n <= 0 or k <= 0:
        raise ValueError("n and k must be positive")
    previous = build_circle(n)
    order = []
    while previous.next is not previous:
        for _ in range(k - 1):
            previous = previous.next
        victim = previous.next
        order.append(victim.data)
        previous.next = victim.next  # unlink the k-th person
    return order, previous.data


def josephus_formula(n, k):
    survivor = 0
    for people in range(2, n + 1):
        survivor = (survivor + k) % people
    return survivor + 1


def main():
    for n, k in ((7, 3), (5, 2), (1, 4), (6, 1), (4, 10)):
        order, survivor = josephus(n, k)
        print("n=%d k=%d eliminated=%s survivor=%d (formula says %d)"
              % (n, k, order, survivor, josephus_formula(n, k)))


if __name__ == "__main__":
    main()
