class Node:
    def __init__(self, data):
        self.data = data
        self.prev = None
        self.next = None


class DoublyLinkedList:
    def __init__(self):
        self.head = None
        self.tail = None  # Added tail pointer to optimize append()

    def append(self, data):
        new_node = Node(data)
        if not self.head:
            self.head = self.tail = new_node
        else:
            self.tail.next = new_node
            new_node.prev = self.tail
            self.tail = new_node  # Update tail pointer

    def prepend(self, data):
        new_node = Node(data)
        if not self.head:
            self.head = self.tail = new_node
        else:
            new_node.next = self.head
            self.head.prev = new_node
            self.head = new_node  # Update head pointer

    def delete(self, key):
        current = self.head
        while current:
            if current.data == key:
                if current.prev:
                    current.prev.next = current.next
                else:  # Deleting head node
                    self.head = current.next

                if current.next:
                    current.next.prev = current.prev
                else:  # Deleting tail node
                    self.tail = current.prev

                print(f"{key} deleted from the list.")
                return  # Stop after deleting

            current = current.next

        print(f"Element {key} not found in the list.")

    def print_list(self):
        if not self.head:
            print("The list is empty.")
            return
        current = self.head
        print("Doubly Linked List:", end=" ")
        while current:
            print(current.data, end=" ⇄ ")  # Improved representation
            current = current.next
        print("None")  # End marker


def main():
    dll = DoublyLinkedList()

    while True:
        print("\nDoubly Linked List Operations:")
        print("1. Append")
        print("2. Prepend")
        print("3. Delete")
        print("4. Print List")
        print("5. Exit")

        choice = input("Enter your choice: ").strip()

        if choice == '1':
            data = input("Enter the data to append: ")
            dll.append(data)
            print(f"{data} appended to the list.")

        elif choice == '2':
            data = input("Enter the data to prepend: ")
            dll.prepend(data)
            print(f"{data} prepended to the list.")

        elif choice == '3':
            data = input("Enter the data to delete: ")
            dll.delete(data)

        elif choice == '4':
            dll.print_list()

        elif choice == '5':
            print("Exiting...")
            break

        else:
            print("Invalid choice. Please enter a valid option.")


if __name__ == "__main__":
    main()
