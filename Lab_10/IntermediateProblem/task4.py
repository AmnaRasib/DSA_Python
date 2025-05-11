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
    else:
        root.right = insert(root.right, key)
    return root

def inorder(root):
    return inorder(root.left) + [root.data] + inorder(root.right) if root else []

def mirror_tree(root):
    if root:
        root.left, root.right = mirror_tree(root.right), mirror_tree(root.left)
    return root

# Create BST
vals = [40, 20, 10, 30, 60, 50, 70]
root = None
for val in vals:
    root = insert(root, val)

print("Original In-order:", inorder(root))
mirror_tree(root)
print("Mirrored In-order:", inorder(root))