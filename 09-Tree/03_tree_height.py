r"""
Problem title:
    Height (Maximum Depth) of a Binary Tree

Problem statement:
    Return the height of a binary tree, defined as the number of nodes on
    the longest path from the root down to a leaf. An empty tree has
    height 0. Also report the depth of a given value (root has depth 0)
    and whether the tree is height-balanced.

What it teaches:
    Post-order thinking: a node's answer depends on its children's answers.

Input example:
            1
           / \
          2   3
         /
        4
       /
      5

Expected output:
    Height: 4
    Height of left subtree: 3
    Height of right subtree: 1
    Depth of 1: 0
    Depth of 4: 2
    Depth of 5: 3
    Depth of 99: -1
    Balanced? False
    Balanced 3-node tree? True height 2
    Empty tree height: 0
    Single node height: 1

Approach:
    height(node) = 1 + larger of height(left), height(right); None -> 0.

Step-by-step logic:
    1. Base case: None has height 0.
    2. Ask both children for their heights.
    3. Take the bigger one (using an if, not max()) and add 1.
    4. Depth of a value: walk down, adding 1 for each edge, until found.
    5. Balanced: at every node the left/right heights differ by at most 1.

Why it works:
    The longest path through a node must go through its taller child, so the
    height is one more than the taller child's height.

Time complexity:
    O(n) for height and depth search; the simple balance check below is
    O(n^2) in the worst case because it recomputes heights at every node.

Space complexity:
    O(h) recursion stack.

Edge cases:
    Empty tree (0), single node (1), skewed tree (height = n).

Alternative approach:
    Level-order traversal counting levels (iterative, O(w) extra space).
"""


class TreeNode:
    def __init__(self, value, left=None, right=None):
        self.value = value
        self.left = left
        self.right = right


def height(node):
    if node is None:  # base case
        return 0
    left_height = height(node.left)
    right_height = height(node.right)
    if left_height > right_height:
        return left_height + 1
    return right_height + 1


def depth_of(node, target, depth=0):
    """Depth of target (root = 0) or -1 if it does not exist."""
    if node is None:
        return -1
    if node.value == target:
        return depth
    found = depth_of(node.left, target, depth + 1)
    if found != -1:
        return found
    return depth_of(node.right, target, depth + 1)


def is_balanced(node):
    """Simple version: compares heights at every node."""
    if node is None:
        return True
    difference = height(node.left) - height(node.right)
    if difference > 1 or difference < -1:
        return False
    return is_balanced(node.left) and is_balanced(node.right)


def main():
    root = TreeNode(1, TreeNode(2, TreeNode(4, TreeNode(5))), TreeNode(3))
    print("Height:", height(root))
    print("Height of left subtree:", height(root.left))
    print("Height of right subtree:", height(root.right))
    for value in (1, 4, 5, 99):
        print(f"Depth of {value}:", depth_of(root, value))
    print("Balanced?", is_balanced(root))
    balanced = TreeNode(1, TreeNode(2), TreeNode(3))
    print("Balanced 3-node tree?", is_balanced(balanced), "height",
          height(balanced))
    print("Empty tree height:", height(None))
    print("Single node height:", height(TreeNode(7)))


if __name__ == "__main__":
    main()
