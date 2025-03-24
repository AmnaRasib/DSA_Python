# Implement a class for Doubly Linked List that supports append, display, and delete from start
class Node:
    def __init__(self,data):
        self.data=data
        self.next=None
        self.prev=None
class DoublyLinkedList:
    def __init__(self):
        self.head=None
        self.tail=None
    def append(self,data):
        node=Node(data)
        if self.head is None:
            self.head=node
            self.tail=node
        else:
            self.tail.next=node
            node.prev=self.tail
            self.tail=node
    def Display(self):
        current=self.head
        while current:
            print(current.data, end="<->")
            current=current.next
        print("None")
    def delete_from_start(self):
        if not self.head:
            print("List is Empty")
            return
        self.head=self.head.next
        if self.head:
            self.head.prev=None
dll=DoublyLinkedList()
dll.append(10)
dll.append(20)
dll.append(30)
dll.Display()
dll.delete_from_start()
dll.Display()


    