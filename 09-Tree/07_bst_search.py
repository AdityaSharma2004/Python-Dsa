r"""
Problem title:
    Binary Search Tree - Search, Minimum, Maximum

Problem statement:
    Given a BST and a target, report whether the target exists (and the path
    taken). Also find the smallest and largest values, and the inorder
    successor of a value (the next larger value in the tree).

What it teaches:
    Using the ordering rule to discard half of the tree at each step, and
    that min / max are just "go left" / "go right" until you cannot.

Input example:
    BST built from [50, 30, 70, 20, 40, 60, 80], target = 60

Expected output:
    Search 60: found=True, path=[50, 70, 60], recursive=True
    Search 25: found=False, path=[50, 30, 20], recursive=False
    Search 50: found=True, path=[50], recursive=True
    Minimum: 20 Maximum: 80
    Successor of 20: 30
    Successor of 50: 60
    Successor of 80: None
    Empty tree: False None

Approach:
    Compare with the current node; go left if the target is smaller, right
    if larger.

Step-by-step logic:
    1. If node is None the target is absent.
    2. Equal -> found. Smaller -> left subtree. Larger -> right subtree.
    3. Minimum: keep going left. Maximum: keep going right.
    4. Successor: remember the last node where we turned left while
       searching; that is the smallest larger value on the path (or the
       minimum of the right subtree if one exists).

Why it works:
    All values on the left of a node are smaller and all on the right are
    larger, so one comparison eliminates an entire subtree.

Time complexity:
    O(h): O(log n) when balanced, O(n) when skewed.

Space complexity:
    Iterative: O(1). Recursive: O(h).

Edge cases:
    Empty tree, single node, target missing, target is the max (no successor).

Alternative approach:
    A full inorder traversal and linear scan works but costs O(n).
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


def search_recursive(node, target):
    if node is None:
        return False
    if target == node.value:
        return True
    if target < node.value:
        return search_recursive(node.left, target)
    return search_recursive(node.right, target)


def search_with_path(root, target):
    """Iterative search that also records the visited values."""
    path = []
    current = root
    while current is not None:
        path.append(current.value)
        if target == current.value:
            return True, path
        current = current.left if target < current.value else current.right
    return False, path


def find_min(node):
    if node is None:
        return None
    while node.left is not None:
        node = node.left
    return node.value


def find_max(node):
    if node is None:
        return None
    while node.right is not None:
        node = node.right
    return node.value


def inorder_successor(root, target):
    """Smallest value strictly greater than target, or None."""
    successor = None
    current = root
    while current is not None:
        if target < current.value:
            successor = current.value  # candidate; try to find a closer one
            current = current.left
        else:
            current = current.right
    return successor


def main():
    root = None
    for value in [50, 30, 70, 20, 40, 60, 80]:
        root = insert(root, value)
    for target in (60, 25, 50):
        found, path = search_with_path(root, target)
        print(f"Search {target}: found={found}, path={path}, "
              f"recursive={search_recursive(root, target)}")
    print("Minimum:", find_min(root), "Maximum:", find_max(root))
    for value in (20, 50, 80):
        print(f"Successor of {value}:", inorder_successor(root, value))
    print("Empty tree:", search_recursive(None, 1), find_min(None))


if __name__ == "__main__":
    main()
