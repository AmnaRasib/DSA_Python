# : Implement a simple task manager where users can add/remove tasks.
class Node:
    def __init__(self,data):
        self.data=data
        self.next=None
class SinglyLinkedList:
    def __init__(self):
        self.head=None
        self.tail=None
    def append(self,task):
        node=Node(task)
        if self.head is None:
            self.head=node
            self.tail=node
        else:
            self.tail.next=node
            self.tail=node
    def display(self):
        current=self.head
        while current:
            print(current.data,end=" -> ")
            current=current.next
        print("None")
    def Size(self):
        count=0
        current=self.head
        while current:
            count+=1
            current=current.next
        print("The no of tasks in the list: ",count)
    def Search(self,task):
        current=self.head
        while current:
            if current.data==task:
                print(f"{task} is found.")
                return
            current=current.next
        print(f"{task} is not found.")
    def Delet(self,task):
        current=self.head
        prev=None
        while current:
            if current.data==task:
                if prev:
                    prev.next=current.next
                else:
                    self.head=current.next
                return
            prev=current
            current=current.next
        print(f"{task} is not found.")

t=SinglyLinkedList()
t.append("Buy Groceries.")
t.append("Home Task.")
t.append("Assignment.")
t.append("Donation.")
t.display()
t.Size()
t.Search("Donation.")
t.Search("Go to trip.")
t.Delet("Assignment.")
t.display()
        

