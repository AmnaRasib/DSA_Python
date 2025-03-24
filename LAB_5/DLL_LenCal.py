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
    def get_Length(self):
        count=0
        current=self.head
        while current:
            count+=1
            current=current.next
        return count
    
dll=DoublyLinkedList()
dll.append(10)
dll.append(20)
dll.append(30)
dll.Display()
print("Length of List: ",dll.get_Length())
