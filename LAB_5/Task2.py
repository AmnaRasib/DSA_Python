# Task 2: Insertion Operations in DLL
class Node:
    def __init__(self,data):
        self.data=data
        self.next=None
        self.prev=None
class DoublyLinkedList:
    def __init__(self):
        self.head=None
    def insert_at_Beginning(self,data):
        node=Node(data)
        if self.head is None:
            self.head=node
        else:
            node.next=self.head
            self.head.prev=node
            self.head=node
    def insert_at_position(self,data,pos):
        node=Node(data)
        if pos==0:
            self.insert_at_Beginning(data)
            return
        current=self.head
        for _ in range(pos-1):
            if current is None:
                print("Position out of bounds")
                return
            current=current.next
        if current is None:
             print("Position out of bounds")
             return
        node.next=current.next
        if current.next:
            current.next.prev=node
        current.next=node
        node.prev=current
        

