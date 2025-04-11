# 1.	Create a tree with three levels and display it.
class TreeNode:
    def __init__(self,data):
        self.data=data
        self.levels=[]
    def add_level(self,level_node):
        self.levels.append(level_node)
    def display(self, level=1):
        print(" " * level * 4 + f"{level}- {self.data}")
        for level_data in self.levels:
            level_data.display(level + 1)


#Example Usage
root=TreeNode("Root")
child1=TreeNode("Child1")
child2=TreeNode("Child2")
root.add_level(child1)
root.add_level(child2)
child1.add_level(TreeNode("GrandChild1"))
child2.add_level(TreeNode("GrandChild2"))
root.display()
