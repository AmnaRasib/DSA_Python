class familyTree:
    def __init__(self,data):
        self.data=data
        self.children=[]
    def add_child(self,child_node):
        self.children.append(child_node)
    def display(self,level=0):
        print(" "*level*4 +f"- {self.data}")
        for child in self.children:
            child.display(level+1)
def search(node,target):
    if node.data==target:
        return node
    for child in node.children:
        result=search(child,target)
        if result:
            return result
    return None
def find_ancestors_path(node,target,path=None):
    if path is None:
        path=[]
    if node.data==target:
        return path
    for child in node.children:
        result=find_ancestors_path(child,target,path+[node.data])
        if result:
            return result
    return None
def count_familyMembers(node):
    count=1
    for child in node.children:
        count+=count_familyMembers(child)
    return count

root=familyTree("GrandParent")

parent1=familyTree("Parent 1")
parent2=familyTree("Parent 2")

child1=familyTree("Child 1")
child2=familyTree("Child 2")
child3=familyTree("Child 3")

parent1.add_child(child1)
parent1.add_child(child2)
parent2.add_child(child3)

root.add_child(parent1)
root.add_child(parent2)

print("Family Tree")
root.display()

target="Child 2"
search(root,target)

print("Total Family members: ",count_familyMembers(root))

target = "Child 2"
ancestors = find_ancestors_path(root, target)
if ancestors:
    print(f"Ancestors of '{target}':", " → ".join(ancestors))
else:
    print(f"No ancestors found for '{target}'")






