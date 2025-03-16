class Queue:
    def __init__(self, max_size):
        self.queue = []
        self.max_size = max_size

    def is_empty(self):
        return len(self.queue) == 0

    def is_full(self):
        return len(self.queue) >= self.max_size

    def enqueue(self, item):
        if self.is_full():
            print("Queue is full")
        else:
            self.queue.append(item)
            print(f"Enqueued: {item}")

    def dequeue(self):
        if self.is_empty():
            return "Queue is empty"
        return self.queue.pop(0)

    def display(self):
        print("Queue:", self.queue)


# Taking user input for max queue size
max_size = int(input("Enter maximum size of queue: "))
queue = Queue(max_size)

while True:
    print("\n1. Enqueue")
    print("2. Dequeue")
    print("3. Display")
    print("4. Quit")
    
    choice = int(input("Enter your choice: "))

    if choice == 1:
        item = input("Enter element: ")
        queue.enqueue(item)
    elif choice == 2:
        print("Dequeued:", queue.dequeue())
    elif choice == 3:
        queue.display()
    elif choice == 4:
        print("Exit")
        break
    else:
        print("Invalid choice! Try again.")
