r"""
Problem title:
    Validate a Binary Search Tree

Problem statement:
    Given the root of a binary tree, decide whether it is a valid BST: for
    every node all values in its left subtree are smaller and all values in
    its right subtree are larger (no duplicates allowed).

What it teaches:
    Why checking only parent and child is wrong, and how to pass down the
    allowed (low, high) range, or use the sorted property of inorder.

Input example:
            5
           / \
          1   6
             / \
            3   7        (3 is in the right subtree of 5 but is < 5)

Expected output:
    valid BST: bounds=True, inorder=True, parent-child-only=True
    tricky tree: bounds=False, inorder=False, parent-child-only=True
    duplicate value: bounds=False, inorder=False, parent-child-only=False
    single node: bounds=True, inorder=True, parent-child-only=True
    empty tree: bounds=True, inorder=True, parent-child-only=True

Approach:
    Recursively pass bounds: each node must satisfy low < value < high.

Step-by-step logic:
    1. Start with low = None and high = None (no limits).
    2. If node is None -> valid.
    3. If value <= low or value >= high -> invalid.
    4. Left child inherits (low, node.value); right child gets
       (node.value, high).
    Inorder method: collect inorder values and check they strictly increase.

Why it works:
    Each ancestor contributes a limit that every descendant must respect,
    which captures the "whole subtree" rule, not just the parent rule.

Time complexity:
    O(n) - every node is checked once.

Space complexity:
    O(h) recursion stack (inorder method: O(n) for the list).

Edge cases:
    Empty tree (valid), single node, duplicates (invalid here), nodes equal
    to a bound, a tree that looks valid locally but is not.

Alternative approach:
    Inorder traversal keeping only the previous value (O(1) extra beyond
    the stack).
"""


class TreeNode:
    def __init__(self, value, left=None, right=None):
        self.value = value
        self.left = left
        self.right = right


def is_valid_bst(node, low=None, high=None):
    if node is None:
        return True
    if low is not None and node.value <= low:
        return False
    if high is not None and node.value >= high:
        return False
    return (is_valid_bst(node.left, low, node.value)
            and is_valid_bst(node.right, node.value, high))


def inorder(node, result):
    if node is None:
        return
    inorder(node.left, result)
    result.append(node.value)
    inorder(node.right, result)


def is_valid_by_inorder(root):
    values = []
    inorder(root, values)
    for index in range(1, len(values)):
        if values[index] <= values[index - 1]:  # must strictly increase
            return False
    return True


def is_valid_parent_child_only(node):
    """WRONG idea shown on purpose: only compares a node with its children."""
    if node is None:
        return True
    if node.left and node.left.value >= node.value:
        return False
    if node.right and node.right.value <= node.value:
        return False
    return is_valid_parent_child_only(node.left) and \
        is_valid_parent_child_only(node.right)


def main():
    valid = TreeNode(8, TreeNode(3, TreeNode(1), TreeNode(6)),
                     TreeNode(10, None, TreeNode(14)))
    tricky = TreeNode(5, TreeNode(1), TreeNode(6, TreeNode(3), TreeNode(7)))
    duplicate = TreeNode(2, TreeNode(2), TreeNode(3))
    cases = [("valid BST", valid), ("tricky tree", tricky),
             ("duplicate value", duplicate), ("single node", TreeNode(1)),
             ("empty tree", None)]
    for name, tree in cases:
        print(f"{name}: bounds={is_valid_bst(tree)}, "
              f"inorder={is_valid_by_inorder(tree)}, "
              f"parent-child-only={is_valid_parent_child_only(tree)}")


if __name__ == "__main__":
    main()
