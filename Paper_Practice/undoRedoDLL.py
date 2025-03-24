class Node:
    def __init__(self,data):
        self.data=data
        self.prev=None
        self.next=None
class UndoRedo:
    def __init__(self):
        self.head=None
        self.tail=None
        self.current=None
    def Write(self,data):
        node=Node(data)
        if self.head is None:
           self.head=node
           self.tail=node
           self.current=node
        else:
            self.current.next=node
            node.prev=self.current
            self.current=node
            self.tail=node
    def undo(self):
        if self.current and self.current.prev:
            self.current=self.current.prev
        elif self.current== self.head:
            self.current=None
    
    def redo(self):
        if self.current and self.current.next:
            self.current=self.current.next
    
    def Display(self):
        current=self.head
        while current:
            print(current.data , end=" <-> ")
        self.current=self.current.next
    
u=UndoRedo()
u.Write(15)
u.undo()
u.Display()

        