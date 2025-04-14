class StackQueue:
    def __init__(self):
        self.inbound_stack = []
        self.outbound_stack = []

    def enqueue(self, data):
        """Push data to inbound stack."""
        self.inbound_stack.append(data)

    def dequeue(self):
        """Move elements from inbound to outbound stack, then pop."""
        if not self.outbound_stack:
            while self.inbound_stack:
                self.outbound_stack.append(self.inbound_stack.pop())
        return self.outbound_stack.pop() if self.outbound_stack else None

# Example Usage
sq = StackQueue()
sq.enqueue(5)
sq.enqueue(10)
sq.enqueue(15)
print("Dequeued:", sq.dequeue())  # 5
print("Dequeued:", sq.dequeue())  # 10
