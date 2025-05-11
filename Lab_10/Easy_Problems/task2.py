# Implement a function that prints a Binary Search Tree in level-order (BFS) using a queue data structure. Construct a BST from values [15, 10, 20, 8, 12, 17, 25] and display nodes level by level.
from collections import deque
# Define Node class
class Node:
    def __init__(self, data):
        self.data = data
        self.left = None
        self.right = None
# Function to insert into BST
def insert_bst(root, key):
    if root is None:
        return Node(key)
    if key < root.data:
        root.left = insert_bst(root.left, key)
    else:
        root.right = insert_bst(root.right, key)
    return root
# Function for level-order traversal (BFS)
def level_order_traversal(root):
    if root is None:
        return
    queue = deque()
    queue.append(root)
    print("Level-order (BFS) traversal:")
    while queue:
        current = queue.popleft()
        print(current.data, end=' ')
        if current.left:
            queue.append(current.left)
        if current.right:
            queue.append(current.right)
# Construct the BST
values = [15, 10, 20, 8, 12, 17, 25]
root = None
for v in values:
    root = insert_bst(root, v)
# Perform level-order traversal
level_order_traversal(root)
