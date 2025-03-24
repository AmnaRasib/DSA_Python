class Stack:
    def __init__(self):
        self.items=[]
    def push(self,data):
        self.items.append(data)
    def pop(self):
        self.items.pop()
    def isEmpty(self):
        return self.items==[]
    def peek(self):
        if self.isEmpty():
            return None
        return self.items[-1]
p=Stack()
while True:
    print("Print <Values>")
    print("push")
    print("pop")
    print("peek")
    print("quit")
    do=input("What would you want to do?").split()
    operation=do[0].strip().lower()
    if operation=='push':
        p.push(int (do[1]))
    elif operation=='pop':
        p.pop()
    elif operation=='peek':
        p.peek()
    elif operation=='quit':
        print(p.items)
        break
    
    



