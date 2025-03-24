class CircularQueue:
    def __init__(self,size):
        self.size=size
        self.queue=[]
        self.front=-1
        self.rear=-1
    def Enqueue(self,data):
      if self.rear == self.size-1:  # Check if the queue is full
        print("Queue is Full!")
        return

      if self.front == -1:  # First element insertion
        self.front = 0  
    
      self.rear += 1  # Move rear pointer forward
      self.queue[self.rear] = data  # Insert the element
      print(f"Enqueued: {data}")
    def Dequeue(self):
        if self.front==-1:
            print("Queue is Empty")
            return
        data=self.queue[self.front]
        self.front+=1
        print(f"Dequed:{data}")
    def display(self):
        print("Queue:",self.queue[self.front:self.rear+1])
cq = CircularQueue(5)
cq.Enqueue(20)  # Enqueue 20
cq.Enqueue(30)  # Enqueue 30
cq.Enqueue(40)  # Enqueue 40
cq.Enqueue(50)  # Enqueue 50 (Queue full now)

cq.display()  # Show all elements

cq.Dequeue()  # Remove 10
cq.Dequeue()  # Remove 20

cq.Dequeue(60)  # Add 60


cq.display()  # Show updated queue
    
