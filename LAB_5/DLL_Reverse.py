# Implement a method to print a DLL in reverse order
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
    def reverse_traverse(self):
        temp=self.head
        if not temp:
            print("List is Empty")
            return
        while temp.next:
            temp=temp.next
        while temp:
            print(temp.data, end="<->")
            temp=temp.prev
        print("None")

dll=DoublyLinkedList()
dll.append(10)
dll.append(20)
dll.append(30)
dll.Display()
dll.reverse_traverse()

