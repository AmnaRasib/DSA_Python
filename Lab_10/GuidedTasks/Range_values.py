class Node:
    def __init__(self, data):
        self.data = data
        self.left = None
        self.right = None

def insert(root, key):
    if root is None:
        return Node(key)
    if key < root.data:
        root.left = insert(root.left, key)
    elif key > root.data:
        root.right = insert(root.right, key)
    return root

def inorder(root):
    if root:
        inorder(root.left)
        print(root.data, end=' ')
        inorder(root.right)

def print_range(root, x, y):
    if not root:
        return
    if x < root.data:
        print_range(root.left, x, y)
    if x <= root.data <= y:
        print(root.data, end=' ')
    if y > root.data:
        print_range(root.right, x, y)
    
values = [50, 30, 70, 20, 40, 60, 80]
root = None

# Insert nodes
for v in values:
    root = insert(root, v)
print_range(root, 30, 70)  # Output: 30 40 50 60 70