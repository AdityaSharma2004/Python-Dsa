r"""
Problem title:
    Binary Search Tree - Insertion

Problem statement:
    Implement a BST that inserts integers one by one. For every node, all
    values in the left subtree are smaller and all in the right subtree are
    larger. Duplicates are ignored. Show that an inorder walk prints the
    values in sorted order.

What it teaches:
    The BST ordering rule, recursive and iterative insertion, and how the
    insertion order decides the shape of the tree.

Input example:
    values = [50, 30, 70, 20, 40, 60, 80]

Expected output:
    Tree built from [50, 30, 70, 20, 40, 60, 80]
            80
        70
            60
    50
            40
        30
            20
    Inorder (sorted): [20, 30, 40, 50, 60, 70, 80]
    Iterative gives same order: True
    Duplicates ignored: [3, 5, 8]
    Height of balanced-looking tree: 3
    Height after inserting sorted values 1..5: 5

Approach:
    Walk down from the root: go left if smaller, right if larger, and attach
    the new node at the first empty spot.

Step-by-step logic:
    1. Empty tree: the new node becomes the root.
    2. Compare value with the current node.
    3. Smaller -> go left; larger -> go right; equal -> do nothing.
    4. When the chosen child is None, place the new node there.

Why it works:
    Search in a BST follows the same path, so the new node lands exactly
    where a future search for it will look.

Time complexity:
    O(h) per insertion: O(log n) for a balanced tree, O(n) when skewed
    (for example inserting already sorted values).

Space complexity:
    O(1) extra for the iterative version, O(h) stack for the recursive one.

Edge cases:
    Empty tree, duplicate values, sorted input (creates a chain).

Alternative approach:
    Build a balanced BST from sorted data by choosing middle elements.
"""


class TreeNode:
    def __init__(self, value):
        self.value = value
        self.left = None
        self.right = None


def insert_recursive(node, value):
    """Return the (possibly new) root of the subtree."""
    if node is None:
        return TreeNode(value)
    if value < node.value:
        node.left = insert_recursive(node.left, value)
    elif value > node.value:
        node.right = insert_recursive(node.right, value)
    return node  # equal values are ignored


def insert_iterative(root, value):
    """Same result using a loop and no recursion."""
    new_node = TreeNode(value)
    if root is None:
        return new_node
    current = root
    while True:
        if value < current.value:
            if current.left is None:
                current.left = new_node
                break
            current = current.left
        elif value > current.value:
            if current.right is None:
                current.right = new_node
                break
            current = current.right
        else:  # duplicate
            break
    return root


def inorder(node, result):
    if node is None:
        return
    inorder(node.left, result)
    result.append(node.value)
    inorder(node.right, result)


def height(node):
    if node is None:
        return 0
    left_height, right_height = height(node.left), height(node.right)
    return 1 + (left_height if left_height > right_height else right_height)


def print_sideways(node, depth=0):
    if node is None:
        return
    print_sideways(node.right, depth + 1)
    print("    " * depth + str(node.value))
    print_sideways(node.left, depth + 1)


def build(values, inserter):
    root = None
    for value in values:
        if inserter is insert_recursive:
            root = insert_recursive(root, value)
        else:
            root = insert_iterative(root, value)
    return root


def main():
    values = [50, 30, 70, 20, 40, 60, 80]
    root = build(values, insert_recursive)
    print("Tree built from", values)
    print_sideways(root)
    result = []
    inorder(root, result)
    print("Inorder (sorted):", result)
    again = []
    inorder(build(values, insert_iterative), again)
    print("Iterative gives same order:", again == result)
    dup = []
    inorder(build([5, 3, 5, 3, 8], insert_recursive), dup)
    print("Duplicates ignored:", dup)
    print("Height of balanced-looking tree:", height(root))
    chain = build([1, 2, 3, 4, 5], insert_recursive)
    print("Height after inserting sorted values 1..5:", height(chain))


if __name__ == "__main__":
    main()
