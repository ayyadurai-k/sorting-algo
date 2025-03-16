class Node:
    def __init__(self, data):
        self.data = data
        self.next = None
        self.prev = None


class Queue:
    def __init__(self):
        self.head = None
        self.tail = None
        self.count = 0  # Tracks size

    def enqueue(self, data):
        new_node = Node(data)
        if self.tail is None:  # If queue is empty
            self.head = self.tail = new_node
        else:
            self.tail.next = new_node
            new_node.prev = self.tail
            self.tail = new_node
        self.count += 1  # Increase size

    def dequeue(self):
        if self.isEmpty():
            print("Queue is empty!")
            return None
        data = self.head.data
        self.head = self.head.next
        if self.head:
            self.head.prev = None
        else:
            self.tail = None  # Queue is empty
        self.count -= 1  # Decrease size
        return data

    def first(self):
        return None if self.isEmpty() else self.head.data

    def size(self):
        return self.count

    def isEmpty(self):
        return self.head is None

    def printQueue(self):
        temp = self.head
        print("Queue elements:", end=" ")
        while temp:
            print(temp.data, end=" ")
            temp = temp.next
        print()


# Test the queue operations
if __name__ == '__main__':
    queue = Queue()

    print("Queue operations using Doubly Linked List\n")

    queue.enqueue(2)
    queue.enqueue(4)
    queue.enqueue(6)
    queue.enqueue(8)

    queue.printQueue()

    print("\nFirst element is:", queue.first())
    print("Size of queue:", queue.size())

    queue.dequeue()
    queue.dequeue()

    print("After dequeuing twice:")
    queue.printQueue()

    print("\nQueue is empty:", queue.isEmpty())
