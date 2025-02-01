from array import *
class MaxNumber:
    def __init__(self):
        self.list=[]
    def add_Elements(self):
      n=int(input("Enter the length of an array: "))
      for i in range(n):
           x=int(input(f"Enter the {i} index positive number: "))
           self.list.append(x)
      print(self.list)
    def max_Element(self):
         maxNum=self.list[0]
         for i in range (len(self.list)):
             if self.list[i] > maxNum:
                 maxNum=self.list[i]
         print("Max num: ",maxNum)
m=MaxNumber()
m.add_Elements()
m.max_Element()

             

