class Node:
    def __init__(self,data):
        self.data=data
        self.next=None
        
        
        
def check_cycle(head):
        current=head
        while current:
            if current.next==head:
                return True
            current=current.next
        return False

node1 = Node(1)
node2 = Node(2)
node3 = Node(3)

node1.next = node2
node2.next = node3
node3.next = node1  # Intentionally creating a cycle for checking

print(check_cycle(node1))  # Output: True, as we gave the head and it returns TRUE

# BELOW IS THE CASE IF NO CYCLE EXITSS
node4 = Node(4)
node5 = Node(5)
node6 = Node(6)

node4.next = node5
node5.next = node6
node6.next = None  # Intentionally not creating a cycle for checking

print(check_cycle(node4))  # Output: False, as no nodes next pointed to head

