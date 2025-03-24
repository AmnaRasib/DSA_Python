class ArrayStack:
    def __init__(self,size):
        self.size=size
        self.stack=[None]*size
        self.top=-1
    def push(self,x):
        if self.top==self.size-1:
            print("Stack Overflow")
            return
        self.top+=1
        self.stack[self.top]=x
        print(f"Pushed {x} onto stack")
    def pop(self):
        if self.top==-1:
            print("Stack Underflow")
            return
        x=self.stack[self.top]
        self.top-=1
        print(f"Popped {x} from stack")

    def peek(self):
        return self.stack[self.top]
    
    def display(self):
        return self.stack[:self.top+1]
stack = ArrayStack(5)    # Create a stack of size 5
stack.push(10)      # Pushed 10
stack.push(20)      # Pushed 20
stack.push(30)      # Pushed 30
stack.display()     # Stack contents: [10, 20, 30]
print("Peek:", stack.peek())  # Peek: 30
stack.pop()         # Popped 30
stack.display() 

        

        