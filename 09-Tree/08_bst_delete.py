r"""
Problem title:
    Binary Search Tree - Deletion

Problem statement:
    Delete a value from a BST so that the result is still a valid BST.
    Handle all three cases: leaf, node with one child, node with two
    children.

What it teaches:
    The three deletion cases and the inorder-successor replacement trick.

Input example:
    BST from [50, 30, 70, 20, 40, 60, 80]; delete 20, then 30, then 50.

Expected output:
    Start             : inorder=[20, 30, 40, 50, 60, 70, 80] preorder=[50, 30, 20, 40, 70, 60, 80]
    Delete 20 (leaf)  : inorder=[30, 40, 50, 60, 70, 80] preorder=[50, 30, 40, 70, 60, 80]
    Delete 30 (1 child): inorder=[40, 50, 60, 70, 80] preorder=[50, 40, 70, 60, 80]
    Delete 50 (2 kids): inorder=[40, 60, 70, 80] preorder=[60, 40, 70, 80]
    Delete 999 (none) : inorder=[40, 60, 70, 80] preorder=[60, 40, 70, 80]
    Deleting the only node gives: None
    Delete from empty tree gives: None

Approach:
    Find the node recursively and rebuild the links on the way back.

Step-by-step logic:
    1. Search: go left if value < node, right if value > node.
    2. Case 1 (leaf): return None so the parent drops it.
    3. Case 2 (one child): return that child so it takes the node's place.
    4. Case 3 (two children): copy the smallest value of the right subtree
       (inorder successor) into this node, then delete that successor from
       the right subtree.
    5. Return the node so the parent link is restored.

Why it works:
    The inorder successor is larger than everything in the left subtree and
    not larger than anything else in the right subtree, so putting it in the
    deleted spot keeps the ordering rule intact.

Time complexity:
    O(h) - one walk down, plus one walk for the successor.

Space complexity:
    O(h) recursion stack.

Edge cases:
    Deleting the root, a missing value, an empty tree, a node with only one
    child, the last remaining node.

Alternative approach:
    Use the inorder predecessor (largest of the left subtree) instead.
"""


class TreeNode:
    def __init__(self, value):
        self.value = value
        self.left = None
        self.right = None


def insert(node, value):
    if node is None:
        return TreeNode(value)
    if value < node.value:
        node.left = insert(node.left, value)
    elif value > node.value:
        node.right = insert(node.right, value)
    return node


def find_min_node(node):
    while node.left is not None:
        node = node.left
    return node


def delete(node, value):
    """Delete value and return the new root of this subtree."""
    if node is None:  # value not present
        return None
    if value < node.value:
        node.left = delete(node.left, value)
    elif value > node.value:
        node.right = delete(node.right, value)
    else:
        if node.left is None:  # leaf or only a right child
            return node.right
        if node.right is None:  # only a left child
            return node.left
        successor = find_min_node(node.right)  # two children
        node.value = successor.value
        node.right = delete(node.right, successor.value)
    return node


def inorder(node, result):
    if node is None:
        return
    inorder(node.left, result)
    result.append(node.value)
    inorder(node.right, result)


def preorder(node, result):
    if node is None:
        return
    result.append(node.value)
    preorder(node.left, result)
    preorder(node.right, result)


def show(label, root):
    ordered, shape = [], []
    inorder(root, ordered)
    preorder(root, shape)
    print(f"{label}: inorder={ordered} preorder={shape}")


def main():
    root = None
    for value in [50, 30, 70, 20, 40, 60, 80]:
        root = insert(root, value)
    show("Start             ", root)
    root = delete(root, 20)
    show("Delete 20 (leaf)  ", root)
    root = delete(root, 30)
    show("Delete 30 (1 child)", root)
    root = delete(root, 50)
    show("Delete 50 (2 kids)", root)
    root = delete(root, 999)
    show("Delete 999 (none) ", root)
    single = delete(TreeNode(5), 5)
    print("Deleting the only node gives:", single)
    print("Delete from empty tree gives:", delete(None, 1))


if __name__ == "__main__":
    main()
