'''Python stack can be implemented using the deque class from the collections module.
 Deque is preferred over the list in the cases where we need quicker append and pop 
 operations from both the ends of the container, as deque provides an O(1) time complexity for append and pop
 operations as compared to list which provides O(n) time complexity. '''
from collections import deque
stack=deque()

stack.append('a')
stack.append('b')
stack.append('c')

print("Initial stack")
print(stack)


print('\nElements popped from stack:')
print(stack.pop())
print(stack.pop())
print(stack.pop())

print('\nStack after elements are popped:')
print(stack)
