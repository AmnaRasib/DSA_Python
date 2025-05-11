# Task 1: Define the TreeNode class
class TreeNode:
    def __init__(self, data):
        self.data = data
        self.children = []

    def add_child(self, child_node):
        self.children.append(child_node)

    def display(self, level=0):  # same as 'print_thread'
        print(" " * level * 4 + f"- {self.data}")
        for child in self.children:
            child.display(level + 1)

# Task 2 (Optional): Pre-order traversal
def traverse_preorder(node, result=None):
    if result is None:
        result = []
    result.append(node.data)
    for child in node.children:
        traverse_preorder(child, result)
    return result

# Task 3: Search for a node by content
def search_tree(node, target):
    if node.data == target:
        return node  # Return the node, not just True
    for child in node.children:
        result = search_tree(child, target)
        if result:
            return result
    return None

# Task 4: Count total nodes (used to count replies)
def count_nodes(node):
    count = 1
    for child in node.children:
        count += count_nodes(child)
    return count

# Additional: Count replies to a specific comment
def count_replies(node):
    return count_nodes(node) - 1  # exclude the comment itself

# ------------------------
# Build a sample threaded comment tree
root = TreeNode("Main Post")

comment1 = TreeNode("First comment")
comment2 = TreeNode("Second comment")
reply1 = TreeNode("Reply to first comment")
reply2 = TreeNode("Reply to reply1")
reply3 = TreeNode("Another reply to first comment")

comment1.add_child(reply1)
reply1.add_child(reply2)
comment1.add_child(reply3)

root.add_child(comment1)
root.add_child(comment2)

# ------------------------
# Display threaded comments
print("Threaded Comments:")
root.display()

# Count replies to a specific comment
target = "First comment"
node = search_tree(root, target)
if node:
    print(f"\nTotal replies to '{target}':", count_replies(node))
else:
    print(f"Comment '{target}' not found.")
