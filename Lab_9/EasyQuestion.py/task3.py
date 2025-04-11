# 3.	Write a function to count the number of direct children of the root node
class TreeNode:
    def __init__(self,data):
        self.data=data
        self.children=[]
    def add_child(self,child_node):
        self.children.append(child_node)
    def display(self,level=0):
        print(" "*level*4+f"-{self.data}")
        for child in self.children:
            child.display(level+1)
def count_node(node):
    count=1
    for child in node.children:
        count+=count_node(child)
    return count
#Example Usage
root = TreeNode("Root")
child1 = TreeNode("Child1")
child2 = TreeNode("Child2")

root.add_child(child1)
root.add_child(child2)

child1.add_child(TreeNode("GrandChild1"))
child2.add_child(TreeNode("GrandChild2"))
root.display()
print("Total number of nodes in tree:", count_node(root))
