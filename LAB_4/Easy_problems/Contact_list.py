# Create a contact list using linked lists where users can search by name.
class Node:
    def __init__(self,name,phone):
        self.name=name
        self.phone=phone
        self.next=None
class ContactList:
    def __init__(self):
        self.head=None
        self.tail=None
    def Appending(self,name,phone):
        node=Node(name,phone)
        if self.head is None:
            self.head=node
            self.tail=node
        else:
            self.tail.next=node
            self.tail=node
    def display(self):
        current=self.head
        while current:
            print("Name: ",current.name," Phone Number: ",current.phone,end=" --> ")
            current=current.next
        print("None")
    def Size(self):
        count=0
        current=self.head
        while current:
            count+=1
            current=current.next
        print("The no of contacts in this list is : ",count)
    def Search(self,name):
        current= self.head
        while current:
            if current.name==name:
                print(f"The Contact Number of {name} is {current.phone}")
                return
            else:
                print(f"{current.phone} not found.")
            current=current.next
c=ContactList()
c.Appending("Ali","0324615262")
c.Appending("Ahmed","012234566")
c.display()
c.Size()
c.Search("Ali")