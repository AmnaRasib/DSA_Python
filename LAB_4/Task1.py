# Basic Singly Linked List Implementation
# Insertion at the Beginning, Middle, and End
class Node:
    def __init__(self,data):
        self.data=data
        self.next=None
class SinglyLinkedList:
    def __init__(self):
        self.head=None
    def append(self,data):
        """Appened a new node at the end of the list."""
        node=Node(data)
        if not self.head:
            self.head= node
        else:
            current=self.head
            while current.next:
                current=current.next
            current.next=node
    def display(self):
        """Print all the Elements of the list."""        
        current=self.head
        while current:
            print(current.data,end="->")
            current=current.next
        print("None")
    def insert_at_beginning(self, data):
        """Insert a node at the beginning of the linked list."""
        node=Node(data)
        node.next=self.head
        self.head=node
    def insert_at_position(self, data, pos):
        """Insert at a spaecific node."""
        node=Node(data)
        current=self.head
        for _ in range(pos - 1):
            if current.next is None:
                break
            current = current.next
        node.next = current.next
        current.next = node   
        # Deletion of Nodes
    def delete(self, data):
        """Delete a node by value."""
        current = self.head
        prev = None
        while current:
            if current.data == data:
                if prev:
                    prev.next = current.next
                else:
                    self.head = current.next
                return
            prev = current
            current = current.next   
    def search(self, data):
        """Search for an element in the linked list."""
        current = self.head
        while current:
            if current.data == data:
                return True
            current = current.next
        return False
    def reverse(self):
        """Reverse the linked list."""
        prev = None
        current = self.head
        while current:
            next_node = current.next
            current.next = prev
            prev = current
            current = next_node
        self.head = prev
sll=SinglyLinkedList()
sll.append(10)
sll.append(20)
sll.append(30)
sll.insert_at_beginning(5)
sll.insert_at_position(15, 2)
sll.delete(20) 
print(sll.search(15))  # True
print(sll.search(100))  # False
sll.reverse()
sll.display()
