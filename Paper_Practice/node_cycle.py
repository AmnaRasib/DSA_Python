class ListNode:
    def __init__(self, value):
        self.value = value
        self.next = None

def cycle_check(head):
    current = head
    
    while current:
        # If the next node points to the head, it will be a cycle
        if current.next == head:
            return True
        current = current.next  # Move to the next node
    
    return False  # No cycle detected is this

node1 = ListNode(1)
node2 = ListNode(2)
node3 = ListNode(3)

node1.next = node2
node2.next = node3
node3.next = node1  # Intentionally creating a cycle for checking

print(cycle_check(node1))  # Output: True, as we gave the head and it returns TRUE

# BELOW IS THE CASE IF NO CYCLE EXITSS
node4 = ListNode(4)
node5 = ListNode(5)
node6 = ListNode(6)

node4.next = node5
node5.next = node6
node6.next = None  # Intentionally not creating a cycle for checking

print(cycle_check(node4))  # Output: False, as no nodes next pointed to 
