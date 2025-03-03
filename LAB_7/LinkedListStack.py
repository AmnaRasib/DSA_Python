class Node:
    def __init__(self,node):
        self.node=node
        self.next=None
class StackLinkedList:
    def __init__(self):
        self.head=None
        self.tail=None
    def PushStack(self,stack):
         node=Node(stack)
         if self.head is None:
             self.head=node
             self.tail=node
         else:
             self.tail.next=node
             self.tail=node
    def displayStack(self):
        current=self.head
        while current:
            print(current.node, end="->")
            current=current.next
        print("None")
    def popStack(self):
        current=self.head

        

l=StackLinkedList()
l.PushStack(12)
l.PushStack(9)
l.PushStack(8)
l.popStack(3)
l.displayStack()

