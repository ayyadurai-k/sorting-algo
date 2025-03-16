class TreeNode:
    def __init__(self, key):
        self.val = key
        self.left = None
        self.right = None


class BST:
    def __init__(self):
        self.root = None

    def insert(self, key):
        """Insert key into BST (Iterative approach)."""
        if not self.root:
            self.root = TreeNode(key)
            return

        current = self.root
        while True:
            if key < current.val:
                if current.left:
                    current = current.left
                else:
                    current.left = TreeNode(key)
                    return
            else:
                if current.right:
                    current = current.right
                else:
                    current.right = TreeNode(key)
                    return

    def search(self, key):
        """Search for a key in the BST (Iterative approach)."""
        current = self.root
        while current:
            if key == current.val:
                return current
            elif key < current.val:
                current = current.left
            else:
                current = current.right
        return None

    def inorder_traversal(self):
        """Inorder traversal using an iterative approach."""
        result, stack = [], []
        current = self.root

        while stack or current:
            if current:
                stack.append(current)
                current = current.left
            else:
                current = stack.pop()
                result.append(current.val)
                current = current.right

        return result


def main():
    bst = BST()

    while True:
        print("\nBinary Search Tree Operations:")
        print("1. Insert")
        print("2. Search")
        print("3. Inorder Traversal")
        print("4. Exit")

        choice = input("Enter your choice: ").strip()

        if choice == '1':
            key = int(input("Enter the value to insert: ").strip())
            bst.insert(key)
            print(f"{key} inserted into the tree.")

        elif choice == '2':
            key = int(input("Enter the value to search: ").strip())
            result = bst.search(key)
            print(f"{key} {'found' if result else 'not found'} in the tree.")

        elif choice == '3':
            print("Inorder Traversal:", bst.inorder_traversal())

        elif choice == '4':
            print("Exiting...")
            break

        else:
            print("Invalid choice. Please enter a valid option.")


if __name__ == "__main__":
    main()
