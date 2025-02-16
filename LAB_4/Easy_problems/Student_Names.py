class Node:
    def __init__(self,data):
        self.data=data
        self.next=None
class SinglyLinkedList:
    def __init__(self):
        self.head=None
        self.tail=None
    def append(self,name):
        node=Node(name)
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
        print("The no. of Students present in list are: ",count)
    def Search(self,name):
        current=self.head
        while current:
            if current.data==name:
                print(f"{name} is found")
                return
            current=current.next
        print(f"{name} is not found.")
    def Delete(self,name):
        current=self.head
        prev=None
        while current:
            if current.data==name:
                if prev:
                    prev.next=current.next
                else:
                    self.head=current.next
                return
            prev=current
            current=current.next
        print("Udated List")
        print(f"{name} is not found.")
s=SinglyLinkedList()
s.append("Ali")
s.append("Aliyar")
s.append("Mehmed")
s.append("Ahmed")
s.append("Amna")
s.append("Ayesha")
s.display()
s.Size()
s.Search("Mehmed")
s.Search("Fatima")
s.Delete("Amna")
s.display()




            


       