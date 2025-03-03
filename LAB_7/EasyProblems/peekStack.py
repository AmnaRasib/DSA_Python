class Stack:
    def __init__(self):
        self.items=[]
        self.peek_Value = 0
    def isEmpty(self):
        return self.items==[]
    def peek(self):
       if self.isEmpty():
            return None  
       return self.items[-1] 
    def push(self,data):
        self.items.append(data)
    def pop(self):
        return  self.items.pop()
p=Stack()

while True:
    print("Print <Values>")
    print("push")
    print("pop")
    print("peek")
    print("quit")
    do=input("What would yoou like to do? ").split()
    operation=do[0].strip().lower()
    if operation=='push':
        p.push(int(do[1]))
    elif operation=='pop':
        if p.isEmpty():
            print("Stack is Empty")
        else:
            p.pop()
    elif operation=='peek':
        p.peek_Value=p.peek()
        if p.peek_Value is not None:
            print("Stack Peek: ",int(p.peek_Value))
    elif operation=='quit':
        print(p.items)
        break