from sys import maxsize
def createStack():
    stack=[]
    return stack
def isEmpty(stack):
    return len(stack)
def push(stack,item):
    stack.append(item)
    print(item+" Pushed to stack")
def pop(stack):
    if (isEmpty(stack)):
        return str(-maxsize-1)
    return stack.pop()
def peek(stack):
    if(isEmpty(stack)):
        return str(-maxsize-1)
    return stack[len(stack)-1]

stack=createStack()
push(stack,str(12))
push(stack,str(9))
push(stack,str(8))
push(stack,str(2))
stack.pop()
print("New Stack: ",stack)






 