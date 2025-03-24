import time
class RequestQueue:
    def __init__(self):
        self.queue=[]
    def Enqueue(self,request):
        self.queue.append(request)
    def Dequeue(self):
        if not self.queue:
            print("No Request")
            return
        request=self.queue.pop(0)
        print(f"Request is Processing: {request}")
        time.sleep(2)
        print(f"Request Completed: {request}")
        return request
    def display(self):
        print("Current queue",self.queue)
import time

class RequestQueue:
    def __init__(self):
        self.queue = []  # Initialize an empty list as a queue

    def enqueue(self, request):
        """Adds a request to the queue (enqueue)."""
        print(f"Request received: {request}")
        self.queue.append(request)  # Add request to the end of the list

    def dequeue(self):
        """Processes the first request in the queue (dequeue)."""
        if not self.queue:
            print("No requests to process!")
            return None
        request = self.queue.pop(0)  # Remove the first request (FIFO)
        print(f"Processing request: {request}")
        time.sleep(2)  # Simulate processing time
        print(f"Request {request} completed.")
        return request

    def display(self):
        """Displays the current queue state."""
        if not self.queue:
            print("Queue is empty.")
        else:
            print("Current queue:", self.queue)

# Example Usage
handler = RequestQueue()

# Enqueue (Adding requests)
handler.enqueue("User Login")
handler.enqueue("Data Retrieval")
handler.enqueue("Payment Processing")

# Display current queue
handler.display()

# Dequeue (Processing requests)
handler.dequeue()
handler.dequeue()

# Display queue after processing some requests
handler.display()

# Enqueue more requests
handler.enqueue("File Upload")
handler.enqueue("Email Notification")

# Process remaining requests
handler.dequeue()
handler.dequeue()
handler.dequeue()

# Final queue state
handler.display()

