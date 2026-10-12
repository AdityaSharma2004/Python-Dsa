r"""
Problem title:
    Level-Order (Breadth-First) Traversal

Problem statement:
    Return the values of a binary tree level by level, from top to bottom
    and left to right, both as one flat list and as a list of levels.
    Also return the zigzag order (alternate direction each level).

What it teaches:
    Breadth-first search with a queue (collections.deque) and the trick of
    processing exactly "size of the queue" nodes per level.

Input example:
            3
           / \
          9   20
             /  \
            15   7

Expected output:
    By levels: [[3], [9, 20], [15, 7]]
    Flat: [3, 9, 20, 15, 7]
    Zigzag: [[3], [20, 9], [15, 7]]
    Recursive gives same levels: True
    Empty tree: []
    Single node: [[1]]

Approach:
    Queue-based BFS.

Step-by-step logic:
    1. Put the root in the queue.
    2. While the queue is not empty, note its length k (the nodes of this
       level).
    3. Pop k nodes, record their values, push their non-None children.
    4. Append the level's values to the result.
    5. Zigzag: reverse every odd level by filling a list from the other end.

Why it works:
    A queue is first-in-first-out, so all nodes of a level are removed before
    any of their children (which sit behind them).

Time complexity:
    O(n) - every node enters and leaves the queue once.

Space complexity:
    O(w) where w is the maximum width of the tree (O(n) worst case).

Edge cases:
    Empty tree -> []; single node; skewed tree (levels of size 1).

Alternative approach:
    Recursive DFS passing the depth and appending into levels[depth].
"""

from collections import deque


class TreeNode:
    def __init__(self, value, left=None, right=None):
        self.value = value
        self.left = left
        self.right = right


def level_order(root):
    """Return a list of levels, each level a list of values."""
    levels = []
    if root is None:
        return levels
    queue = deque([root])
    while queue:
        level_size = len(queue)  # nodes on the current level
        level = []
        for _ in range(level_size):
            node = queue.popleft()
            level.append(node.value)
            if node.left:
                queue.append(node.left)
            if node.right:
                queue.append(node.right)
        levels.append(level)
    return levels


def flatten(levels):
    flat = []
    for level in levels:
        for value in level:
            flat.append(value)
    return flat


def zigzag(root):
    """Left-to-right on even levels, right-to-left on odd levels."""
    result = []
    if root is None:
        return result
    queue = deque([root])
    left_to_right = True
    while queue:
        size = len(queue)
        level = [None] * size
        for position in range(size):
            node = queue.popleft()
            slot = position if left_to_right else size - 1 - position
            level[slot] = node.value
            if node.left:
                queue.append(node.left)
            if node.right:
                queue.append(node.right)
        result.append(level)
        left_to_right = not left_to_right
    return result


def level_order_recursive(node, depth, levels):
    """Alternative: DFS that files each value under its depth."""
    if node is None:
        return
    if depth == len(levels):
        levels.append([])
    levels[depth].append(node.value)
    level_order_recursive(node.left, depth + 1, levels)
    level_order_recursive(node.right, depth + 1, levels)


def main():
    root = TreeNode(3, TreeNode(9), TreeNode(20, TreeNode(15), TreeNode(7)))
    levels = level_order(root)
    print("By levels:", levels)
    print("Flat:", flatten(levels))
    print("Zigzag:", zigzag(root))
    check = []
    level_order_recursive(root, 0, check)
    print("Recursive gives same levels:", check == levels)
    print("Empty tree:", level_order(None))
    print("Single node:", level_order(TreeNode(1)))


if __name__ == "__main__":
    main()
