# Write a Python program that builds a Binary Search Tree from a list of integers and then performs and prints all three types of depth-first traversals: In-order, Pre-order, and Post-order. Clearly label the output of each traversal.
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
def preorder(root):
    if root:
        print(root.data, end=' ')
        preorder(root.left)
        preorder(root.right)
def postorder(root):
    if root:
        postorder(root.left)
        postorder(root.right)
        print(root.data, end=' ')
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
        if not root.left:
            return root.right
        elif not root.right:
            return root.left
        temp = min_value_node(root.right)
        root.data = temp.data
        root.right = delete(root.right, temp.data)
    return root
values = [50, 30, 70, 20, 40, 60, 80]
root = None
for v in values:
    root = insert(root, v)
print("=== BEFORE DELETION ===")
print("In-order Traversal:")
inorder(root)
print("\nPre-order Traversal:")
preorder(root)
print("\nPost-order Traversal:")
postorder(root)

key_to_delete = 50
print(f"\n\nDeleting node with value: {key_to_delete}")
root = delete(root, key_to_delete)

print("\n=== AFTER DELETION ===")
print("In-order Traversal:")
inorder(root)
print("\nPre-order Traversal:")
preorder(root)
print("\nPost-order Traversal:")
postorder(root)
