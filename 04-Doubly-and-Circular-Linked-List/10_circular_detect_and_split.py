r"""
Problem: Detect a Circular List and Split It into Two Halves

Problem statement:
    Given the head of a linked list, decide whether it is circular (the last
    node links back to the head). If it is, split it into two circular lists
    of sizes ceil(n/2) and floor(n/2).

What it teaches:
    Floyd's slow and fast pointers on a possibly cyclic structure, and
    cutting a circle into two circles.

Input example:
    Circular list 1 -> 2 -> 3 -> 4 -> 5 -> back to 1; plain list 1 -> 2 ->
    3; a list with a cycle not at the head

Expected output:
    Circle   : has_cycle=True pure_circle=True
    Plain    : has_cycle=False pure_circle=False
    Loop to 2: has_cycle=True pure_circle=False
    Split odd : [1, 2, 3] [4, 5]
    Split even: [1, 2, 3] [4, 5, 6]

Approach:
    Use slow/fast pointers to detect any cycle; check whether the fast
    pointer returns to head to confirm it is a pure circle; for splitting,
    find the middle with slow/fast and rewire two next pointers.

Step-by-step logic:
    1. Fast moves two steps and slow one; if fast hits None the list is not
    circular.
    2. A pure circular list is detected when fast or fast.next equals head.
    3. To split: slow = fast = head and advance while fast.next is not head
    and fast.next.next is not head.
    4. slow is now the last node of the first half; head2 = slow.next.
    5. If the size is even move fast once more; then fast.next = head2 and
    slow.next = head.

Why it works:
    In a circle fast always laps slow, so they meet or reach the head again;
    and the node where fast finishes is the old tail that must be re-pointed
    to the second half.

Time complexity:
    O(n).

Space complexity:
    O(1).

Edge cases:
    Empty list, single node (circular to itself, cannot be split in two non-
    empty halves), two nodes, odd and even sizes, a list that loops back to
    a middle node instead of the head.

Alternative approach:
    Count the nodes first, then walk n/2 steps; or use a visited set (O(n)
    extra space) to detect cycles.
"""


class Node:
    def __init__(self, data):
        self.data = data
        self.next = None


def build(values, circular=False, loop_to=None):
    nodes = [Node(v) for v in values]
    for first, second in zip(nodes, nodes[1:]):
        first.next = second
    if nodes and circular:
        nodes[-1].next = nodes[0]
    if nodes and loop_to is not None:
        nodes[-1].next = nodes[loop_to]
    return nodes[0] if nodes else None


def has_cycle(head):
    slow = fast = head
    while fast is not None and fast.next is not None:
        slow = slow.next
        fast = fast.next.next
        if slow is fast:
            return True
    return False


def is_pure_circle(head):
    """True only when the last node links back to the head itself."""
    if head is None:
        return False
    current = head.next
    steps = 0
    while current is not None and current is not head:
        current = current.next
        steps += 1
        if steps > 10 ** 6:  # safety net for cycles that skip the head
            return False
    return current is head


def split_circle(head):
    slow = fast = head
    while fast.next is not head and fast.next.next is not head:
        slow = slow.next
        fast = fast.next.next
    if fast.next.next is head:  # even number of nodes: fast is one short
        fast = fast.next
    second = slow.next
    fast.next = second  # close the second half
    slow.next = head    # close the first half
    return head, second


def circle_to_list(head):
    items, current = [head.data], head.next
    while current is not head:
        items.append(current.data)
        current = current.next
    return items


def main():
    circle = build([1, 2, 3, 4, 5], circular=True)
    plain = build([1, 2, 3])
    tail_loop = build([1, 2, 3, 4], loop_to=1)
    print("Circle   : has_cycle=%s pure_circle=%s" % (has_cycle(circle), is_pure_circle(circle)))
    print("Plain    : has_cycle=%s pure_circle=%s" % (has_cycle(plain), is_pure_circle(plain)))
    print("Loop to 2: has_cycle=%s pure_circle=%s" % (has_cycle(tail_loop), is_pure_circle(tail_loop)))
    first, second = split_circle(circle)
    print("Split odd :", circle_to_list(first), circle_to_list(second))
    even = build([1, 2, 3, 4, 5, 6], circular=True)
    first, second = split_circle(even)
    print("Split even:", circle_to_list(first), circle_to_list(second))


if __name__ == "__main__":
    main()
