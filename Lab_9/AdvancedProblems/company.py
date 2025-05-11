class OrgTree:
    def __init__(self, data):
        self.data = data
        self.children = []

    def add_child(self, node):
        self.children.append(node)

    def remove_child(self, node):
        if node in self.children:
            self.children.remove(node)

    def display(self, level=0):
        print(" " * level * 4 + f"- {self.data}")
        for child in self.children:
            child.display(level + 1)

# 🔍 Helper: Search for a node and return reference
def search(node, target):
    if node.data == target:
        return node
    for child in node.children:
        result = search(child, target)
        if result:
            return result
    return None

# 🔄 Move a subtree (department) to new parent (division)
def move_subtree(root, from_name, to_name):
    # Search both nodes
    from_node = search(root, from_name)
    to_node = search(root, to_name)

    if not from_node:
        print(f"Node '{from_name}' not found.")
        return
    if not to_node:
        print(f"Node '{to_name}' not found.")
        return

    # Find and remove 'from_node' from its current parent
    def find_and_remove(node, target):
        for child in node.children:
            if child == target:
                node.remove_child(child)
                return True
            if find_and_remove(child, target):
                return True
        return False

    if find_and_remove(root, from_node):
        to_node.add_child(from_node)
        print(f"\n'{from_name}' moved under '{to_name}' successfully!")
    else:
        print(f"\nFailed to move '{from_name}'.")


root = OrgTree("Company")

hr = OrgTree("HR")
sales = OrgTree("Sales")
it = OrgTree("IT")

recruit = OrgTree("Recruitment")
training = OrgTree("Training")
software = OrgTree("Software")
hardware = OrgTree("Hardware")

hr.add_child(recruit)
hr.add_child(training)
it.add_child(software)
it.add_child(hardware)

root.add_child(hr)
root.add_child(sales)
root.add_child(it)


print("=== Organization Structure (Before Move) ===")
root.display()

# Move "Training" under "IT"
move_subtree(root, "Training", "IT")

#  Display after move
print("\n=== Organization Structure (After Move) ===")
root.display()
