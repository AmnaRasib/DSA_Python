class Node:
    def __init__(self, data):
        self.data = data
        self.left = None
        self.right = None
def insert_bst(root, key):
    if root is None:
        return Node(key)
    if key < root.data:
        root.left = insert_bst(root.left, key)
    else:
        root.right = insert_bst(root.right, key)
    return root
def count_nodes(root):
    if root is None:
        return 0
    return 1 + count_nodes(root.left) + count_nodes(root.right)

values = list(map(int, input("Enter values to insert into BST (space-separated): ").split()))
root = None

for val in values:
    root = insert_bst(root, val)

total = count_nodes(root)
print("Total number of nodes in BST:", total)
