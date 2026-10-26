"""
TREE & BINARY SEARCH TREE (BST) — BEGINNER'S COMPLETE PRACTICE FILE
===================================================================

This one file demonstrates:
1. TreeNode: value, left child, right child
2. Building a binary tree manually
3. Building a binary tree from a level-order list (None = missing child)
4. Printing a tree sideways
5. Preorder, inorder, postorder, and level-order traversal
6. BST insertion, searching, and deletion
7. Minimum, maximum, height, node count, leaf count
8. Inorder predecessor and successor
9. A simple interactive menu

BST rule used here:
- Smaller values go left.
- Larger values go right.
- Duplicate values are ignored.

Height is measured in EDGES:
- Empty tree: -1
- Single-node tree: 0
"""

from collections import deque


# ============================================================
# PART 1: NODE CLASS
# ============================================================

class TreeNode:
    """One node in a binary tree."""

    def __init__(self, value):
        self.value = value       # Data stored in this node
        self.left = None         # Reference to left child
        self.right = None        # Reference to right child


# ============================================================
# PART 2: BUILD A NORMAL BINARY TREE
# These functions do not enforce BST ordering.
# ============================================================

def build_manually():
    """
    Build this tree by connecting nodes manually:

            1
           / \
          2   3
         / \
        4   5
    """
    root = TreeNode(1)
    root.left = TreeNode(2)
    root.right = TreeNode(3)
    root.left.left = TreeNode(4)
    root.left.right = TreeNode(5)
    return root


def build_from_level_order(values):
    """
    Build a binary tree from level-order data.

    Example:
        [1, 2, 3, 4, 5, None, 6]

    None means that child position is empty.
    The list describes children of existing parents in queue order.
    """
    if not values or values[0] is None:
        return None

    root = TreeNode(values[0])
    waiting = deque([root])  # Parents waiting to receive children
    index = 1

    while waiting and index < len(values):
        parent = waiting.popleft()

        # Next value, if present, is this parent's left child.
        if index < len(values) and values[index] is not None:
            parent.left = TreeNode(values[index])
            waiting.append(parent.left)
        index += 1

        # Following value, if present, is this parent's right child.
        if index < len(values) and values[index] is not None:
            parent.right = TreeNode(values[index])
            waiting.append(parent.right)
        index += 1

    return root


# ============================================================
# PART 3: DISPLAY A TREE
# ============================================================

def print_sideways(node, depth=0):
    """
    Print the right subtree first, then the node, then the left.
    This makes the tree appear rotated sideways.
    """
    if node is None:
        return

    print_sideways(node.right, depth + 1)
    print("    " * depth + str(node.value))
    print_sideways(node.left, depth + 1)


def describe_node(node):
    """Describe a node's children and whether it is a leaf."""
    if node is None:
        return "Node does not exist (None)."

    left_value = node.left.value if node.left else None
    right_value = node.right.value if node.right else None

    if node.left is None and node.right is None:
        kind = "leaf"
    else:
        kind = "internal"

    return (
        f"Node {node.value}: left={left_value}, "
        f"right={right_value} ({kind})"
    )


# ============================================================
# PART 4: TREE TRAVERSALS
# Each traversal visits every existing node once.
# ============================================================

def preorder(node):
    """Root -> Left -> Right."""
    result = []

    def visit(current):
        if current is None:
            return
        result.append(current.value)  # Visit root first
        visit(current.left)
        visit(current.right)

    visit(node)
    return result


def inorder(node):
    """Left -> Root -> Right. In a BST, this gives sorted values."""
    result = []

    def visit(current):
        if current is None:
            return
        visit(current.left)
        result.append(current.value)  # Visit root in the middle
        visit(current.right)

    visit(node)
    return result


def postorder(node):
    """Left -> Right -> Root."""
    result = []

    def visit(current):
        if current is None:
            return
        visit(current.left)
        visit(current.right)
        result.append(current.value)  # Visit root last

    visit(node)
    return result


def level_order(node):
    """Visit the tree level by level using a queue."""
    if node is None:
        return []

    result = []
    queue = deque([node])

    while queue:
        current = queue.popleft()
        result.append(current.value)

        if current.left is not None:
            queue.append(current.left)
        if current.right is not None:
            queue.append(current.right)

    return result


# ============================================================
# PART 5: BINARY SEARCH TREE CLASS
# ============================================================

class BST:
    """Binary Search Tree: smaller left, larger right."""

    def __init__(self):
        self.root = None  # An empty BST has no root.

    # ---------------- INSERT ----------------

    def insert(self, value):
        """Insert a value; ignore duplicates."""
        self.root = self._insert(self.root, value)

    def _insert(self, node, value):
        # An empty position is where the new node belongs.
        if node is None:
            return TreeNode(value)

        if value < node.value:
            node.left = self._insert(node.left, value)
        elif value > node.value:
            node.right = self._insert(node.right, value)
        # If equal, do nothing: duplicates are ignored.

        return node

    # ---------------- SEARCH ----------------

    def search(self, value):
        """Return True if the value exists, otherwise False."""
        current = self.root

        while current is not None:
            if value == current.value:
                return True
            elif value < current.value:
                current = current.left
            else:
                current = current.right

        return False

    # ---------------- DELETE ----------------

    def delete(self, value):
        """Delete a value if present; preserve the BST rules."""
        self.root = self._delete(self.root, value)

    def _delete(self, node, value):
        if node is None:
            return None  # Value was not found in this branch.

        if value < node.value:
            node.left = self._delete(node.left, value)
        elif value > node.value:
            node.right = self._delete(node.right, value)
        else:
            # We found the node to delete.

            # Case 1: no children (leaf).
            if node.left is None and node.right is None:
                return None

            # Case 2a: only a right child.
            if node.left is None:
                return node.right

            # Case 2b: only a left child.
            if node.right is None:
                return node.left

            # Case 3: two children.
            # Find the inorder successor: smallest value in right subtree.
            successor = node.right
            while successor.left is not None:
                successor = successor.left

            # Copy successor's value into the node being deleted.
            node.value = successor.value

            # Remove the successor from its old position.
            node.right = self._delete(node.right, successor.value)

        return node

    # ---------------- MINIMUM / MAXIMUM ----------------

    def find_min(self):
        """Return the smallest value, or None if the tree is empty."""
        current = self.root
        if current is None:
            return None

        while current.left is not None:
            current = current.left
        return current.value

    def find_max(self):
        """Return the largest value, or None if the tree is empty."""
        current = self.root
        if current is None:
            return None

        while current.right is not None:
            current = current.right
        return current.value

    # ---------------- COUNT / HEIGHT ----------------

    def count_nodes(self):
        """Count all nodes."""
        def count(node):
            if node is None:
                return 0
            return 1 + count(node.left) + count(node.right)

        return count(self.root)

    def count_leaves(self):
        """Count nodes that have no children."""
        def count(node):
            if node is None:
                return 0
            if node.left is None and node.right is None:
                return 1
            return count(node.left) + count(node.right)

        return count(self.root)

    def height(self):
        """Height in edges: empty=-1, single node=0."""
        def get_height(node):
            if node is None:
                return -1
            return 1 + max(get_height(node.left), get_height(node.right))

        return get_height(self.root)

    # ---------------- TRAVERSALS ----------------

    def preorder(self):
        return preorder(self.root)

    def inorder(self):
        return inorder(self.root)

    def postorder(self):
        return postorder(self.root)

    def level_order(self):
        return level_order(self.root)

    # ---------------- PREDECESSOR / SUCCESSOR ----------------

    def predecessor(self, value):
        """
        Return the inorder predecessor (next smaller value), or None.
        Handles both a left subtree and ancestor-based cases.
        """
        current = self.root
        candidate = None

        while current is not None:
            if value < current.value:
                current = current.left
            elif value > current.value:
                candidate = current.value
                current = current.right
            else:
                # If left subtree exists, predecessor is its maximum.
                if current.left is not None:
                    current = current.left
                    while current.right is not None:
                        current = current.right
                    return current.value
                return candidate

        return None  # The requested value was not found.

    def successor(self, value):
        """
        Return the inorder successor (next larger value), or None.
        Handles both a right subtree and ancestor-based cases.
        """
        current = self.root
        candidate = None

        while current is not None:
            if value < current.value:
                candidate = current.value
                current = current.left
            elif value > current.value:
                current = current.right
            else:
                # If right subtree exists, successor is its minimum.
                if current.right is not None:
                    current = current.right
                    while current.left is not None:
                        current = current.left
                    return current.value
                return candidate

        return None  # The requested value was not found.


# ============================================================
# PART 6: DEMONSTRATION
# ============================================================

def demo():
    print("\n=== NORMAL BINARY TREE: BUILT MANUALLY ===")
    normal_root = build_manually()
    print_sideways(normal_root)
    print(describe_node(normal_root))
    print(describe_node(normal_root.left))
    print(describe_node(normal_root.left.left))

    print("\nTraversals of the manually built tree:")
    print("Preorder:   ", preorder(normal_root))
    print("Inorder:    ", inorder(normal_root))
    print("Postorder:  ", postorder(normal_root))
    print("Level-order:", level_order(normal_root))

    print("\n=== NORMAL BINARY TREE: BUILT FROM A LIST ===")
    values = [1, 2, 3, 4, 5, None, 6]
    normal_root = build_from_level_order(values)
    print("Input:", values)
    print_sideways(normal_root)
    print("Empty list produces:", build_from_level_order([]))

    print("\n=== BINARY SEARCH TREE ===")
    tree = BST()

    for value in [50, 30, 70, 20, 40, 60, 80]:
        tree.insert(value)

    print("BST shape:")
    print_sideways(tree.root)
    print("Inorder (sorted):", tree.inorder())
    print("Preorder:", tree.preorder())
    print("Postorder:", tree.postorder())
    print("Level-order:", tree.level_order())

    print("\nSearch 40:", tree.search(40))
    print("Search 99:", tree.search(99))
    print("Minimum:", tree.find_min())
    print("Maximum:", tree.find_max())
    print("Node count:", tree.count_nodes())
    print("Leaf count:", tree.count_leaves())
    print("Height in edges:", tree.height())
    print("Predecessor of 50:", tree.predecessor(50))
    print("Successor of 50:", tree.successor(50))

    print("\nDelete 20 (leaf):")
    tree.delete(20)
    print("Inorder:", tree.inorder())

    print("\nDelete 30 (now has one child, 40):")
    tree.delete(30)
    print("Inorder:", tree.inorder())

    print("\nDelete 70 (has two children, 60 and 80):")
    tree.delete(70)
    print("Inorder:", tree.inorder())


# ============================================================
# PART 7: OPTIONAL INTERACTIVE MENU
# ============================================================

def interactive_menu():
    """Let you experiment with BST operations while the program runs."""
    tree = BST()

    while True:
        print("\n========== BST MENU ==========")
        print("1. Insert a value")
        print("2. Search for a value")
        print("3. Delete a value")
        print("4. Display tree sideways")
        print("5. Show all traversals")
        print("6. Show minimum and maximum")
        print("7. Show node count, leaf count, and height")
        print("8. Find predecessor and successor")
        print("9. Insert the sample values")
        print("0. Exit")

        choice = input("Choose an option: ").strip()

        if choice == "1":
            try:
                value = int(input("Value to insert: "))
                already_exists = tree.search(value)
                tree.insert(value)
                if already_exists:
                    print("That value already exists; duplicates are ignored.")
                else:
                    print(f"Inserted {value}.")
            except ValueError:
                print("Please enter a valid integer.")

        elif choice == "2":
            try:
                value = int(input("Value to search: "))
                print("Found." if tree.search(value) else "Not found.")
            except ValueError:
                print("Please enter a valid integer.")

        elif choice == "3":
            try:
                value = int(input("Value to delete: "))
                existed = tree.search(value)
                tree.delete(value)
                print("Deleted." if existed else "Value was not in the tree.")
            except ValueError:
                print("Please enter a valid integer.")

        elif choice == "4":
            if tree.root is None:
                print("The tree is empty.")
            else:
                print_sideways(tree.root)

        elif choice == "5":
            print("Preorder:   ", tree.preorder())
            print("Inorder:    ", tree.inorder())
            print("Postorder:  ", tree.postorder())
            print("Level-order:", tree.level_order())

        elif choice == "6":
            print("Minimum:", tree.find_min())
            print("Maximum:", tree.find_max())

        elif choice == "7":
            print("Nodes:", tree.count_nodes())
            print("Leaves:", tree.count_leaves())
            print("Height in edges:", tree.height())

        elif choice == "8":
            try:
                value = int(input("Value: "))
                print("Predecessor:", tree.predecessor(value))
                print("Successor:", tree.successor(value))
            except ValueError:
                print("Please enter a valid integer.")

        elif choice == "9":
            for value in [50, 30, 70, 20, 40, 60, 80]:
                tree.insert(value)
            print("Sample values inserted; duplicates are ignored.")

        elif choice == "0":
            print("Goodbye!")
            break

        else:
            print("Invalid choice. Choose a number from 0 to 9.")


if __name__ == "__main__":
    # Run the demonstration first.
    demo()

    # Then ask whether to open the interactive menu.
    answer = input("\nOpen the interactive BST menu? (y/n): ").strip().lower()
    if answer == "y":
        interactive_menu()
