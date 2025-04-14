class Node:
    def __init__(self, data):
        self.data = data
        self.next = None

class LinkedQueue:
    def __init__(self):
        self.head = None
        self.tail = None
        self.size = 0

    def enqueue(self, data):
        """Add an element to the tail of the queue."""
        new_node = Node(data)
        if self.tail:
            self.tail.next = new_node
        self.tail = new_node
        if self.head is None:
            self.head = new_node
        self.size += 1

    def dequeue(self):
        """Remove the front node."""
        if self.head is None:
            return None
        removed_data = self.head.data
        self.head = self.head.next
        if self.head is None:
            self.tail = None
        self.size -= 1
        return removed_data

# Example Usage
lq = LinkedQueue()
lq.enqueue(100)
lq.enqueue(200)
print("Dequeued:", lq.dequeue())  # 100
