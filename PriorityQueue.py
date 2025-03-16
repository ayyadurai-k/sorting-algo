import heapq

class PriorityQueue:
    def __init__(self):
        self.elements = []

    def is_empty(self):
        return not self.elements  # More Pythonic way

    def push(self, item, priority):
        """Push an item with a given priority into the queue."""
        heapq.heappush(self.elements, (priority, item))

    def pop(self):
        """Remove and return the item with the highest priority (lowest number)."""
        return heapq.heappop(self.elements)[1] if self.elements else None

    def peek(self):
        """Return the highest priority item without removing it."""
        return self.elements[0][1] if self.elements else None

    def __str__(self):
        """Return a string representation of the queue without modifying it."""
        return "Priority Queue: " + str(sorted(self.elements)) if self.elements else "Priority queue is empty."


def main():
    pq = PriorityQueue()

    while True:
        print("\nPriority Queue Operations:")
        print("1. Push")
        print("2. Pop")
        print("3. Print Queue")
        print("4. Exit")

        choice = input("Enter your choice: ").strip()

        if choice == '1':
            item = input("Enter the item to push: ").strip()
            priority = int(input("Enter the priority of the item: ").strip())
            pq.push(item, priority)
            print(f"{item} pushed to the queue with priority {priority}.")

        elif choice == '2':
            popped_item = pq.pop()
            print(f"Popped item: {popped_item}" if popped_item else "Priority queue is empty.")

        elif choice == '3':
            print(pq)  # Uses __str__() method instead of modifying the queue

        elif choice == '4':
            print("Exiting...")
            break

        else:
            print("Invalid choice. Please enter a valid option.")


if __name__ == "__main__":
    main()
