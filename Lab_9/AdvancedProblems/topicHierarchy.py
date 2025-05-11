class TopicHierarchyTree:
    def __init__(self, data):
        self.data = data
        self.children = []

    def add_child(self, child_node):
        self.children.append(child_node)

    def display(self, level=0):
        print(" " * level * 4 + f"{self.data}")
        for child in self.children:
            child.display(level + 1)

def search(topic_node, target):
    if topic_node.data == target:
        return topic_node
    for child in topic_node.children:
        result = search(child, target)
        if result:
            return result
    return None

def topic_path(topic_node, target, path=None):
    if path is None:
        path = []
    if topic_node.data == target:
        return path + [topic_node.data]
    for child in topic_node.children:
        result = topic_path(child, target, path + [topic_node.data])
        if result:
            return result
    return None

# Tree building
root = TopicHierarchyTree("Python")

oop = TopicHierarchyTree("Object Oriented Programming")
ds = TopicHierarchyTree("Data Structure")

array = TopicHierarchyTree("Arrays")
stack = TopicHierarchyTree("Stacks")
queue = TopicHierarchyTree("Queues")
tree = TopicHierarchyTree("Tree")

polymorphism = TopicHierarchyTree("Polymorphism")
encap = TopicHierarchyTree("Encapsulation")
inheritance = TopicHierarchyTree("Inheritance")
abstraction = TopicHierarchyTree("Abstraction")

# Build hierarchy
ds.add_child(array)
ds.add_child(stack)
ds.add_child(queue)
ds.add_child(tree)

oop.add_child(polymorphism)
oop.add_child(encap)
oop.add_child(inheritance)
oop.add_child(abstraction)

root.add_child(oop)
root.add_child(ds)

# Display
print("Topic Hierarchy:")
root.display()

# Search for a topic
target = "Encapsulation"
result = search(root, target)
if result:
    print(f"\n'{target}' is found successfully.")
else:
    print(f"\n'{target}' not found.")

# Show full path to a topic
target = "Tree"
path_result = topic_path(root, target)
if path_result:
    print(f"\nHierarchy of '{target}':", " → ".join(path_result))
else:
    print(f"\n'{target}' not found in hierarchy.")
