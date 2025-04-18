class Node:
    def __init__(self, data):
        self.data = data
        self.left = None
        self.right = None

def sorted_list_to_bst(arr):
    if not arr:
        return None
    mid = len(arr) // 2
    root = Node(arr[mid])
    root.left = sorted_list_to_bst(arr[:mid])
    root.right = sorted_list_to_bst(arr[mid+1:])
    return root

def inorder_traversal(root):
    return inorder_traversal(root.left) + [root.data] + inorder_traversal(root.right) if root else []

# Example sorted list
sorted_list = [5, 10, 15, 20, 25, 30, 35]
root = sorted_list_to_bst(sorted_list)

print("In-order Traversal of Balanced BST:")
print(inorder_traversal(root))