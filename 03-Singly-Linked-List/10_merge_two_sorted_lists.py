"""
Problem title:
    Merge Two Sorted Linked Lists

Problem statement:
    Given the heads of two ascending sorted linked lists, splice their nodes
    together into one sorted list and return its head. Do not create new data
    nodes; reuse the existing ones.

What it teaches:
    - The dummy-head technique for building a result list.
    - The merge step used later in merge sort.
    - Preserving stability (when equal, take from the first list).

Input example:
    list1 = 1 -> 3 -> 5 -> 7
    list2 = 2 -> 3 -> 6

Expected output:
    Iterative merge: [1, 2, 3, 3, 5, 6, 7]
    Recursive merge: [1, 2, 3, 3, 5, 6, 7]
    One empty: [4, 5]
    Both empty: []
    Different lengths: [1, 2, 3, 4, 10]

Approach:
    Keep a "tail" of the merged list. Repeatedly attach the smaller front node
    from the two lists, then attach whatever remains.

Step-by-step logic:
    1. dummy = Node(0); tail = dummy.
    2. While both lists have nodes: if a.data <= b.data attach a and advance a,
       else attach b and advance b. Move tail forward.
    3. Attach the non-empty remainder: tail.next = a or b.
    4. Return dummy.next.

Why it works:
    Both lists are sorted, so the smallest unmerged value is always at one of
    the two fronts. Taking it keeps the output sorted.

Time complexity:
    O(m + n).

Space complexity:
    O(1) for the iterative version (only pointers); recursive uses O(m + n).

Edge cases:
    - One or both lists empty.
    - Lists of very different lengths.
    - Equal values across lists (we take list1 first for stability).

Alternative approach:
    Recursive merge: pick the smaller head and recurse on the rest.
"""


class Node:
    def __init__(self, data):
        self.data = data
        self.next = None


def build_list(values):
    head = None
    tail = None
    for value in values:
        node = Node(value)
        if head is None:
            head = node
        else:
            tail.next = node
        tail = node
    return head


def to_list(head):
    values = []
    while head is not None:
        values.append(head.data)
        head = head.next
    return values


def merge_sorted(list_a, list_b):
    dummy = Node(0)
    tail = dummy
    while list_a is not None and list_b is not None:
        if list_a.data <= list_b.data:  # <= keeps list_a first on ties
            tail.next = list_a
            list_a = list_a.next
        else:
            tail.next = list_b
            list_b = list_b.next
        tail = tail.next
    tail.next = list_a if list_a is not None else list_b  # leftover nodes
    return dummy.next


def merge_sorted_recursive(list_a, list_b):
    if list_a is None:
        return list_b
    if list_b is None:
        return list_a
    if list_a.data <= list_b.data:
        list_a.next = merge_sorted_recursive(list_a.next, list_b)
        return list_a
    list_b.next = merge_sorted_recursive(list_a, list_b.next)
    return list_b


def main():
    merged = merge_sorted(build_list([1, 3, 5, 7]), build_list([2, 3, 6]))
    print("Iterative merge:", to_list(merged))

    merged = merge_sorted_recursive(build_list([1, 3, 5, 7]), build_list([2, 3, 6]))
    print("Recursive merge:", to_list(merged))

    print("One empty:", to_list(merge_sorted(build_list([]), build_list([4, 5]))))
    print("Both empty:", to_list(merge_sorted(build_list([]), build_list([]))))
    print("Different lengths:",
          to_list(merge_sorted(build_list([10]), build_list([1, 2, 3, 4]))))


if __name__ == "__main__":
    main()
