class Node:
    def __init__(self,data):
        self.data=data
        self.next=None
class SinglyLinkedList:
    def __init__(self):
        self.head=None
        self.tail=None
        # Apending Nodes
    def appending(self,data):
        """Appened a new node at the end of the list."""
        node=Node(data)
        if self.head is None:
            self.head=node
            self.tail=node
        else:
            self.tail.next=node
            self.tail=node
    # Displaying Nodes
    def display(self):
        current=self.head
        while current:
            print(current.data, end=" -> ")
            current=current.next
        print("None")
    # size of the Nodes
    def Size(self):
        count=0
        current=self.head
        while current:
            count+=1
            current=current.next
        print("Size: ",count)
    # Searching Node
    def Searching(self,data):
        current=self.head
        while current:
            if current.data==data:
                print(data," is found.")
                return True
            current=current.next
        print(data," is not found.")
        return False 
    # deleting nodes
    def Deletion(self,data):  #let say we have 10,20,30
        current=self.head
        prev=None
        while current:
         if current.data==data: #if the value match then
            if prev:             #since prev is true
                prev.next=current.next #it updates the previous which points the next node 30 (delet the node 20)
            else:
                self.head=current.next
            return
         prev=current #if the value not found pre=10 and current=20
         current=current.next 
        print(f"{data} not found in the list.")
        
s=SinglyLinkedList()
s.appending(23)
s.appending(24)
s.appending(25)
s.Size()
s.display()
s.Searching(24)
s.Searching(26)
s.Deletion(24)
s.display()




# class SinglyLinkedList:
#     def delete(self, data):
#         """Delete a node by value."""
#         current = self.head
#         prev = None

#         while current:
#             if current.data == data:
#                 if prev:
#                     prev.next = current.next
#                 else:
#                     self.head = current.next
#                 return
#             prev = current
#             current = current.next

# # Example Usage
# sll.delete(20)  # Deletes 20 from the list
# sll.display()
