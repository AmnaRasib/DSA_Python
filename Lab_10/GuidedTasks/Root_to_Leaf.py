class Node:
    def __init__(self,data):
        self.data=data
        self.left=None
        self.right=None
# function to Insert and Create
def insert(root,key):
    if root is None:
        return Node(key)
    if key < root.data:
        root.left = insert(root.left, key)
    elif key > root.data:
        root.right = insert(root.right, key)
    return root
# Inorder Traversal
def inorder(root):
    if root:
        inorder(root.left)
        print(root.data, end=' ')
        inorder(root.right)
# Search Function
def search(root,key):
    if root is None or root.data == key:
        return root
    if key<root.data:
        return search(root.left,key)
    return search(root.right,key)
# Delete a Node
def min_value(node):
    current=node
    while current.left:
        current=current.left
    return current
def delete(root,key):
    if root is None:
        return root
    if key<root.data:
        root.left=delete(root.left,key)
    elif key>root.data:
        root.right=delete(root.right,key)
    else:
        if not root.right:
            return root.left
        elif not root.left:
            return root.right
        temp=min_value(root.right)
        root.data=temp.data
        root.right=delete(root.right,temp.data)
    return root
# Values in the Range
def print_range(root,x,y):
    if not root:
        return
    if x<root.data:
        print_range(root.left,x,y)
    if x<= root.data <=y:
        print(root.data,end=' ')
    if y> root.data:
        print_range(root.right,x,y)
# Root to Leaf Paths
def root_to_leaf_paths(root,path=[]):
    if not root:
        return
    path.append(root.data)
    if not root.left and not root.right:
        print("->".join(map(str,path)))
    else:
        root_to_leaf_paths(root.left, path[:])
        root_to_leaf_paths(root.right, path[:])
# ------------------ MAIN PART ------------------

# Start with an empty tree
root = None

# Insert values into the BST
values = [50, 30, 20, 40, 70, 60, 80]
for val in values:
    root = insert(root, val)

print("\nInorder Traversal of BST:")
inorder(root)

# Search for a value
print("\n\nSearching for 60:")
found = search(root, 60)
if found:
    print("Found:", found.data)
else:
    print("Not found!")

# Delete a node
print("\nDeleting 20 (a leaf node)...")
root = delete(root, 20)
print("Inorder after deleting 20:")
inorder(root)

print("\n\nDeleting 30 (has one child)...")
root = delete(root, 30)
print("Inorder after deleting 30:")
inorder(root)

print("\n\nDeleting 50 (has two children)...")
root = delete(root, 50)
print("Inorder after deleting 50:")
inorder(root)

# Print values in a range
print("\n\nValues between 40 and 80:")
print_range(root, 40, 80)

# Show all root-to-leaf paths
print("\n\nAll Root to Leaf Paths:")
root_to_leaf_paths(root)



    

