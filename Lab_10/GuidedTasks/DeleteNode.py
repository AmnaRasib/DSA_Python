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

def min_value_node(node):
    current = node
    while current.left:
        current = current.left
    return current

def delete(root, key):
    if not root:
        return root
    if key < root.data:
        root.left = delete(root.left, key)
    elif key > root.data:
        root.right = delete(root.right, key)
    else:
        # Node with only one child or no child
        if not root.left:
            return root.right
        elif not root.right:
            return root.left
        # Node with two children
        temp = min_value_node(root.right)
        root.data = temp.data
        root.right = delete(root.right, temp.data)
    return root

values = [50, 30, 70, 20, 40, 60, 80]
root = None

# Insert nodes
for v in values:
    root = insert(root, v)

print("Inorder traversal before deletion:")
inorder(root)

# 🔥 Delete node with key
key_to_delete = 50
print(f"\n\nDeleting node with value: {key_to_delete}")
root = delete(root, key_to_delete)

print("\nInorder traversal after deletion:")
inorder(root)
