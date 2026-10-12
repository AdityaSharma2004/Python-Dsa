r"""
Problem title:
    Count Nodes, Leaves and Internal Nodes (and Sum of Values)

Problem statement:
    For a binary tree compute: total number of nodes, number of leaf nodes
    (no children), number of internal nodes (at least one child) and the
    sum of all values.

What it teaches:
    Recursive aggregation: combining the answers of the left and right
    subtrees, and how the leaf test (both children None) works.

Input example:
            10
           /  \
          5    20
         / \     \
        3   7     30

Expected output:
    Sample tree: nodes=6, leaves=3, internal=3, sum=75
    Empty tree: nodes=0, leaves=0, internal=0, sum=0
    Single node: nodes=1, leaves=1, internal=0, sum=8
    Left chain: nodes=3, leaves=1, internal=2, sum=6

Approach:
    count(node) = 1 + count(left) + count(right); leaves return 1 only when
    both children are missing.

Step-by-step logic:
    1. None contributes 0.
    2. Nodes: 1 + nodes(left) + nodes(right).
    3. Leaves: if left and right are None return 1, else leaves(left) +
       leaves(right).
    4. Internal = nodes - leaves.
    5. Sum: value + sum(left) + sum(right).

Why it works:
    Every node belongs to exactly one subtree of its parent, so adding the
    subtree answers counts each node exactly once.

Time complexity:
    O(n) per function.

Space complexity:
    O(h) recursion stack.

Edge cases:
    Empty tree (all 0), single node (it is a leaf), node with one child
    (internal, not a leaf).

Alternative approach:
    Count with any traversal (BFS or DFS) and a running counter.
"""


class TreeNode:
    def __init__(self, value, left=None, right=None):
        self.value = value
        self.left = left
        self.right = right


def count_nodes(node):
    if node is None:
        return 0
    return 1 + count_nodes(node.left) + count_nodes(node.right)


def count_leaves(node):
    if node is None:
        return 0
    if node.left is None and node.right is None:  # leaf
        return 1
    return count_leaves(node.left) + count_leaves(node.right)


def count_internal(node):
    return count_nodes(node) - count_leaves(node)


def sum_values(node):
    if node is None:
        return 0
    return node.value + sum_values(node.left) + sum_values(node.right)


def report(title, root):
    print(f"{title}: nodes={count_nodes(root)}, leaves={count_leaves(root)}, "
          f"internal={count_internal(root)}, sum={sum_values(root)}")


def main():
    root = TreeNode(10,
                    TreeNode(5, TreeNode(3), TreeNode(7)),
                    TreeNode(20, None, TreeNode(30)))
    report("Sample tree", root)
    report("Empty tree", None)
    report("Single node", TreeNode(8))
    report("Left chain", TreeNode(1, TreeNode(2, TreeNode(3))))


if __name__ == "__main__":
    main()
