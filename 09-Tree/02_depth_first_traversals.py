r"""
Problem title:
    Inorder, Preorder and Postorder Traversals

Problem statement:
    Visit every node of a binary tree in inorder (Left, Root, Right),
    preorder (Root, Left, Right) and postorder (Left, Right, Root) using
    recursion, returning the values as lists.

What it teaches:
    Depth-first traversal and how moving one line (the "visit" line) changes
    the output order.

Input example:
            1
           / \
          2   3
         / \
        4   5

Expected output:
    Preorder : [1, 2, 4, 5, 3]
    Inorder  : [4, 2, 5, 1, 3]
    Postorder: [4, 5, 2, 3, 1]
    Empty tree: []
    Right-skewed preorder: [1, 2, 3]
    Right-skewed postorder: [3, 2, 1]

Approach:
    Recursive function that handles the left subtree, right subtree and the
    current node in three different orders.

Step-by-step logic:
    1. If the node is None return (base case).
    2. Preorder: record node, go left, go right.
    3. Inorder: go left, record node, go right.
    4. Postorder: go left, go right, record node.

Why it works:
    Every subtree is itself a tree, so the same rule applies at each level;
    the position of "record" decides when a node is reported relative to its
    children.

Time complexity:
    O(n) - each node is visited once.

Space complexity:
    O(h) recursion stack where h is the height (O(n) for a skewed tree),
    plus the O(n) result list.

Edge cases:
    Empty tree, single node, only left or only right children.

Alternative approach:
    Iterative versions with an explicit stack (see 10_iterative_traversals.py).
"""


class TreeNode:
    def __init__(self, value, left=None, right=None):
        self.value = value
        self.left = left
        self.right = right


def preorder(node, result):
    if node is None:
        return
    result.append(node.value)  # root first
    preorder(node.left, result)
    preorder(node.right, result)


def inorder(node, result):
    if node is None:
        return
    inorder(node.left, result)
    result.append(node.value)  # root in the middle
    inorder(node.right, result)


def postorder(node, result):
    if node is None:
        return
    postorder(node.left, result)
    postorder(node.right, result)
    result.append(node.value)  # root last


def collect(traversal, root):
    """Run a traversal and return its list."""
    result = []
    traversal(root, result)
    return result


def main():
    root = TreeNode(1, TreeNode(2, TreeNode(4), TreeNode(5)), TreeNode(3))
    print("Preorder :", collect(preorder, root))
    print("Inorder  :", collect(inorder, root))
    print("Postorder:", collect(postorder, root))
    print("Empty tree:", collect(inorder, None))
    skewed = TreeNode(1, None, TreeNode(2, None, TreeNode(3)))
    print("Right-skewed preorder:", collect(preorder, skewed))
    print("Right-skewed postorder:", collect(postorder, skewed))


if __name__ == "__main__":
    main()
