class Node:
    def __init__(self,data):
        self.data=data
        self.right=None
        self.left=None
def find_depth(root,target,depth=0):
    if root is None:
        return -1
    if root.data==target:
        return depth
    left_depth=find_depth(root.left,target,depth+1)
    if left_depth!=-1:
        return left_depth
    right_depth=find_depth(root.right,target,depth+1)
    return right_depth
root=Node(1)
root.left=Node(2)
root.right=Node(3)
root.left.left = Node(4)
root.right.left = Node(5)
root.right.right = Node(6)
root.right.right=Node(7)
target_Node=5
depth=find_depth(root,target_Node)
print(f"Depth of {target_Node} is: {depth}")
