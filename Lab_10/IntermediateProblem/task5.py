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

# Function to find the Lowest Common Ancestor in a BST
def find_lca(root, n1, n2):
    if root is None:
        return None

    # If both nodes are smaller than root, LCA lies in left
    if n1 < root.data and n2 < root.data:
        return find_lca(root.left, n1, n2)

    # If both nodes are greater than root, LCA lies in right
    if n1 > root.data and n2 > root.data:
        return find_lca(root.right, n1, n2)

    # If one node is on the left and the other on the right, root is LCA
    return root

# === Main Code ===
values = [20, 10, 30, 5, 15, 25, 35]
root = None
for val in values:
    root = insert_bst(root, val)

# Define two nodes to find LCA
n1 = 5
n2 = 15

lca_node = find_lca(root, n1, n2)
if lca_node:
    print(f"Lowest Common Ancestor of {n1} and {n2} is:", lca_node.data)
else:
    print("One or both nodes not found in the BST.")
