# 2.	Implement a method to print only the leaf nodes of a tree.
class Node:
    def __init__(self,data):
        self.data=data
        self.right=None
        self.left=None
def leaf_Node(root):
    if root is None:
      return
    if root.left is None and root.right is None:
        print(root.data,end=' ')
        return
    leaf_Node(root.left)
    leaf_Node(root.right)
root=Node(1)
root.left=Node(2)
root.right=Node(3)
root.left.left = Node(4)
root.right.left = Node(5)
root.right.right = Node(6)
root.right.right=Node(7)

print("Leaf Nodes are: ")
leaf_Node(root)
