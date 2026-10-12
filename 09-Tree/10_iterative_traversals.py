r"""
Problem title:
    Iterative Inorder, Preorder and Postorder Traversals

Problem statement:
    Perform the three depth-first traversals of a binary tree WITHOUT
    recursion, using an explicit stack (a Python list).

What it teaches:
    How the recursion call stack can be replaced by your own stack, which
    avoids recursion-limit errors on very deep trees.

Input example:
            1
           / \
          2   3
         / \
        4   5

Expected output:
    Inorder  : [4, 2, 5, 1, 3]
    Preorder : [1, 2, 4, 5, 3]
    Postorder: [4, 5, 2, 3, 1]
    Matches recursive inorder: True
    Empty tree: [] [] []
    Deep chain inorder length: 3000

Approach:
    Inorder: push the left spine, pop, visit, move right.
    Preorder: pop, visit, push right then left.
    Postorder: use two stacks (or reverse a root-right-left order).

Step-by-step logic:
    1. Inorder: current = root; while current or stack: push current and go
       left until None; pop, record value; current = popped.right.
    2. Preorder: push root; pop a node, record it, push right child first and
       then left so left is processed first.
    3. Postorder: the first stack yields root, left, right order; push each
       popped node on a second stack; popping the second stack gives
       left, right, root.

Why it works:
    The stack stores exactly the nodes whose work is still pending, just like
    the recursive call stack does.

Time complexity:
    O(n) for each traversal.

Space complexity:
    O(h) for inorder and preorder, O(n) for the two-stack postorder.

Edge cases:
    Empty tree, single node, skewed trees (stack grows to n).

Alternative approach:
    Morris traversal gives inorder in O(1) extra space by temporarily
    threading the tree.
"""


class TreeNode:
    def __init__(self, value, left=None, right=None):
        self.value = value
        self.left = left
        self.right = right


def inorder_iterative(root):
    result, stack = [], []
    current = root
    while current is not None or stack:
        while current is not None:  # go as far left as possible
            stack.append(current)
            current = current.left
        current = stack.pop()
        result.append(current.value)
        current = current.right
    return result


def preorder_iterative(root):
    result = []
    if root is None:
        return result
    stack = [root]
    while stack:
        node = stack.pop()
        result.append(node.value)
        if node.right:  # right first so that left comes out first
            stack.append(node.right)
        if node.left:
            stack.append(node.left)
    return result


def postorder_iterative(root):
    if root is None:
        return []
    first, second = [root], []
    while first:
        node = first.pop()
        second.append(node)
        if node.left:
            first.append(node.left)
        if node.right:
            first.append(node.right)
    result = []
    while second:  # popping reverses root-right-left into left-right-root
        result.append(second.pop().value)
    return result


def inorder_recursive(node, out):
    """Used only to verify the iterative answer."""
    if node:
        inorder_recursive(node.left, out)
        out.append(node.value)
        inorder_recursive(node.right, out)


def main():
    root = TreeNode(1, TreeNode(2, TreeNode(4), TreeNode(5)), TreeNode(3))
    print("Inorder  :", inorder_iterative(root))
    print("Preorder :", preorder_iterative(root))
    print("Postorder:", postorder_iterative(root))
    check = []
    inorder_recursive(root, check)
    print("Matches recursive inorder:", check == inorder_iterative(root))
    print("Empty tree:", inorder_iterative(None), preorder_iterative(None),
          postorder_iterative(None))
    deep = None
    for value in range(3000, 0, -1):  # 3000-deep chain: too deep for recursion
        deep = TreeNode(value, deep)
    print("Deep chain inorder length:", len(inorder_iterative(deep)))


if __name__ == "__main__":
    main()
