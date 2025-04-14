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
def search(root,key):
    if root is None or root.data==key:
        return root
    if key<root.data:
        return search(root.left,key)
    return search(root.right,key)

#Example Usage  
values = [50, 30, 70, 20, 40, 60, 80]
root = None  

for v in values:
    root = insert(root, v)
result=search(root,40)
print("Found" if result else "Not Found")