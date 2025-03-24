# Task 1: Implementing a Doubly Linked List (DLL)
class Node:
    def __init__(self,data):
        self.data=data
        self.next=None
        self.prev=None
class DoublyLinkedList:
    def __init__(self):
        self.head=None
        self.tail=None
    def insert(self,data):
        node=Node(data)
        if self.head is None:
            self.head=node
            self.tail=node
        else:
            self.tail.next=node
            node.prev=self.tail
            self.tail=node
    def display_forward(self):
        current=self.head
        while current:
            print(current.data,"<->",end=" ")
            current=current.next
        print("None")
    def display_Backward(self):
        current=self.tail
        while current:
            print(current.data,"<->",end=" ")
            current=current.prev
        print("None")

dll=DoublyLinkedList()
dll.insert(10)
dll.insert(20)
dll.insert(30)
dll.insert(40)
dll.display_forward()
dll.display_Backward()
