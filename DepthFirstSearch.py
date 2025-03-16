class TreeNode:
    def __init__(self, key):
        self.val = key
        self.left = None
        self.right = None


def dfs_recursive(node):
    """Recursive Depth-First Search (Preorder Traversal)."""
    if node:
        print(node.val, end=" ")
        dfs_recursive(node.left)
        dfs_recursive(node.right)


def dfs_iterative(root):
    """Iterative Depth-First Search (Preorder Traversal) using a stack."""
    if not root:
        return

    stack = [root]
    while stack:
        node = stack.pop()
        print(node.val, end=" ")

        if node.right:
            stack.append(node.right)
        if node.left:
            stack.append(node.left)


def build_tree():
    """Build a binary tree from user input (level-order) using a regular list instead of deque."""
    root_val = input("Enter root node value: ").strip()
    if root_val.lower() == "none":
        return None

    root = TreeNode(int(root_val))
    queue = [root]  # Using a list instead of deque

    while queue:
        current = queue.pop(0)  # This is O(n), unlike deque's O(1)

        left_val = input(f"Enter left child of {current.val} (or 'None'): ").strip()
        if left_val.lower() != "none":
            current.left = TreeNode(int(left_val))
            queue.append(current.left)

        right_val = input(f"Enter right child of {current.val} (or 'None'): ").strip()
        if right_val.lower() != "none":
            current.right = TreeNode(int(right_val))
            queue.append(current.right)

    return root


# Example Usage:
root = build_tree()
print("\nDFS Recursive:")
dfs_recursive(root)

print("\nDFS Iterative:")
dfs_iterative(root)
