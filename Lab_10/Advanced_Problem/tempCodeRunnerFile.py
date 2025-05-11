class PlayerNode:
    def __init__(self, name, score):
        self.name = name
        self.score = score
        self.left = None
        self.right = None

def insert_player(root, name, score):
    if root is None:
        return PlayerNode(name, score)
    if score > root.score:  # Higher scores are placed to the left
        root.left = insert_player(root.left, name, score)
    elif score < root.score:
        root.right = insert_player(root.right, name, score)
    else:  # Update score if same
        root.score = score
    return root

def inorder_traversal(root):
    if root:
        inorder_traversal(root.left)
        print(f"Player: {root.name}, Score: {root.score}")
        inorder_traversal(root.right)

def reverse_inorder_traversal(root):
    if root:
        reverse_inorder_traversal(root.right)
        print(f"Player: {root.name}, Score: {root.score}")
        reverse_inorder_traversal(root.left)

# Example Usage
root = None
root = insert_player(root, "Alice", 100)
root = insert_player(root, "Bob", 120)
root = insert_player(root, "Charlie", 90)
root = insert_player(root, "Dave", 150)

print("Leaderboard in Descending Order:")
reverse_inorder_traversal(root)

print("\nUpdating Alice's Score to 130...")
root = insert_player(root, "Alice", 130)

print("\nUpdated Leaderboard:")
reverse_inorder_traversal(root)