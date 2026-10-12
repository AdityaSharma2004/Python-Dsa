r"""
Problem title:
    Creating a Binary Tree and Displaying Its Shape

Problem statement:
    Build a binary tree out of node objects (each node has a value, a left
    child and a right child) and print it sideways so the structure is
    visible. Also build the same tree from a level-order list where None
    marks a missing child.

What it teaches:
    The Node class (like a linked-list node with two pointers), root,
    parent, child, leaf terminology, and how a tree is just linked objects.

Input example:
    level-order list = [1, 2, 3, 4, 5, None, 6]

Expected output:
    Manually built tree (sideways view, root at left):
        3
    1
            5
        2
            4
    node 1: left=2, right=3 (internal)
    node 2: left=4, right=5 (internal)
    node 4: left=None, right=None (leaf)

    Built from [1, 2, 3, 4, 5, None, 6]:
            6
        3
    1
            5
        2
            4

    Empty list -> None
    node 42: left=None, right=None (leaf)

Approach:
    Manual wiring with node.left / node.right, then a helper that creates
    nodes from a list using a queue of "parents waiting for children".

Step-by-step logic:
    1. Create the root from the first value.
    2. Keep a queue holding nodes that still need children.
    3. For each pair of next values: first is the left child, second the
       right child (None means no child). Non-None nodes join the queue.
    4. To print: show right subtree, node, left subtree with indentation by
       depth (a reversed in-order walk) so the tree appears rotated 90 deg.

Why it works:
    A level-order list lists parents before children in the same order the
    queue hands out parents, so each pair of values lands on the right parent.

Time complexity:
    Building: O(n). Printing: O(n).

Space complexity:
    O(n) for the nodes; queue and recursion O(n) worst case.

Edge cases:
    Empty list (no tree), only a root, None gaps, skewed (all left/right).

Alternative approach:
    Store the tree in an array (children of i at 2i+1 and 2i+2) as a heap does.
"""

from collections import deque


class TreeNode:
    """One node of a binary tree."""

    def __init__(self, value):
        self.value = value
        self.left = None
        self.right = None


def build_manually():
    """Wire nodes by hand to see the pointers explicitly."""
    root = TreeNode(1)
    root.left = TreeNode(2)
    root.right = TreeNode(3)
    root.left.left = TreeNode(4)
    root.left.right = TreeNode(5)
    return root


def build_from_level_order(values):
    """Create a tree from a list such as [1, 2, 3, None, 4]."""
    if not values or values[0] is None:
        return None
    root = TreeNode(values[0])
    waiting = deque([root])
    index = 1
    while waiting and index < len(values):
        parent = waiting.popleft()
        if index < len(values) and values[index] is not None:
            parent.left = TreeNode(values[index])
            waiting.append(parent.left)
        index += 1
        if index < len(values) and values[index] is not None:
            parent.right = TreeNode(values[index])
            waiting.append(parent.right)
        index += 1
    return root


def print_sideways(node, depth=0):
    """Right subtree first so the tree looks rotated left by 90 degrees."""
    if node is None:
        return
    print_sideways(node.right, depth + 1)
    print("    " * depth + str(node.value))
    print_sideways(node.left, depth + 1)


def describe(node):
    """Return a short text about a node's children."""
    left = node.left.value if node.left else None
    right = node.right.value if node.right else None
    kind = "leaf" if left is None and right is None else "internal"
    return f"node {node.value}: left={left}, right={right} ({kind})"


def main():
    print("Manually built tree (sideways view, root at left):")
    root = build_manually()
    print_sideways(root)
    print(describe(root))
    print(describe(root.left))
    print(describe(root.left.left))

    print("\nBuilt from [1, 2, 3, 4, 5, None, 6]:")
    tree = build_from_level_order([1, 2, 3, 4, 5, None, 6])
    print_sideways(tree)
    print("\nEmpty list ->", build_from_level_order([]))
    single = build_from_level_order([42])
    print(describe(single))


if __name__ == "__main__":
    main()
