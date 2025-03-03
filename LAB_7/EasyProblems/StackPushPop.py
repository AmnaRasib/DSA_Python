'''1.	Stack Push & Pop: Implement a stack where users can push and pop elements interactively.'''
class Stack:
    def __init__(self):
        self.items=[]
    def isEmpty(self):
        return self.items==[]
    def pushStack(self,data):
        self.items.append(data)
    def popStack(self):
        return self.items.pop()
s=Stack()
while True:
    print("push <Value>")
    print('pop')
    print('push')
    print('quit')
    do= input('What would you like to do? ').split()
    operation=do[0].strip().lower()
    if operation=='push':
        s.pushStack(int(do[1]))
    elif operation=='pop':
        if s.isEmpty():
            print('Stack is Empty.')
        else:
            print('Poped Values: ',s.popStack())
    elif operation=='quit':
      print(s.items)
      break
    

    
        
        
