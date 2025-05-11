# Node class for BST
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

# Function to calculate the height of the BST
def height_of_bst(root):
    if root is None:
        return -1  # return -1 to count edges; return 0 to count nodes
    left_height = height_of_bst(root.left)
    right_height = height_of_bst(root.right)
    return 1 + max(left_height, right_height)

# === Main Code ===
values = list(map(int, input("Enter values to insert into BST (space-separated): ").split()))
root = None

for val in values:
    root = insert_bst(root, val)

height = height_of_bst(root)
print("Height of the BST (in number of edges):", height)
