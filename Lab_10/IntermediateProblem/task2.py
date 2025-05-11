class Node:
    def __init__(self, data):
        self.data = data
        self.left = None
        self.right = None

def is_bst(root, min_val=float('-inf'), max_val=float('inf')):
    if root is None:
        return True
    if not (min_val < root.data < max_val):
        return False
    return (is_bst(root.left, min_val, root.data) and
            is_bst(root.right, root.data, max_val))

# Valid BST
valid = Node(20)
valid.left = Node(10)
valid.right = Node(30)
valid.left.left = Node(5)
valid.left.right = Node(15)
valid.right.left = Node(25)
valid.right.right = Node(35)

# Invalid BST (25 is wrongly placed)
invalid = Node(20)
invalid.left = Node(10)
invalid.right = Node(30)
invalid.left.left = Node(5)
invalid.left.right = Node(25)  # Violates BST property

print("Valid Tree is BST:", is_bst(valid))      # True
print("Invalid Tree is BST:", is_bst(invalid))  # False
