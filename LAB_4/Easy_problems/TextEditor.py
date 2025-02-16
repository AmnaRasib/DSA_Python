class Node:
  def __init__(self,content):
    self.content=content
    self.next=None
class TextEditor:
  def __init__(self):
    self.head=None
    self.tail=None
  def Appending(self,text):
    node=Node(text)
    if self.head is None:
        self.head=node
        self.tail=node
    else:
       self.tail.next=node
       self.tail=node
  def display(self):
    current=self.head
    while current:
      print(current.content,end=" ")
      current=current.next
  def Undo(self):
    if self.head is None:
      print("Nothing to undo")
      return
    prev=self.head.next
    self.head=prev
    self.tail=prev
    
  def Delet(self,text):
    current=self.head
    prev=None
    while current:
      if current.content==text:
        if prev:
          prev.next=current.next
        else:
          self.head=current.next
        return
      prev=current
      current=current.next
   
t=TextEditor()
t.Appending("Hello")
t.Appending("World")
t.Undo()
t.display()



    
