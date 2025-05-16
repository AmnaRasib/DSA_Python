class DeliveryRecords:
    def __init__(self, orderID, status):
        self.orderID = orderID
        self.status = status
        self.next = None

class Queues:
    def __init__(self, order_id):
        self.order_id = order_id
        self.next = None

class City:
    def __init__(self, name):
        self.name = name
        self.sub_cities = []
        self.deliveryRecords_head = None  # Linked List Head
        self.urgent_stack = []            # Stack for urgent deliveries
        self.pending_front = None         # Queue front
        self.pending_rear = None          # Queue rear
        self.routes = {}                  # Distance info

    def add_childToRoutes(self, child, distance):
        self.sub_cities.append(child)
        self.routes[child.name] = distance

# Add city to tree
def add_city(parent, city_name, distance):
    new_city = City(city_name)
    if parent:
        parent.add_childToRoutes(new_city, distance)
    return new_city

# Add a delivery record
def add_delivery(city, order_id, status):
    new_delivery = DeliveryRecords(order_id, status)
    new_delivery.next = city.deliveryRecords_head
    city.deliveryRecords_head = new_delivery

    if status.lower() == "urgent":
        city.urgent_stack.append(order_id)
    elif status.lower() == "pending":
        new_qnode = Queues(order_id)
        if city.pending_rear is None:
            city.pending_front = city.pending_rear = new_qnode
        else:
            city.pending_rear.next = new_qnode
            city.pending_rear = new_qnode

# Show routes recursively
def show_routes(city):
    print(f"\nRoutes from {city.name}:")
    for child in city.sub_cities:
        print(f"  -> {child.name} ({city.routes[child.name]} km)")
        show_routes(child)

# Show delivery linked list
def show_deliveries(city):
    print(f"\nDelivery Records for {city.name}:")
    current = city.deliveryRecords_head
    while current:
        print(f"  Order ID: {current.orderID}, Status: {current.status}")
        current = current.next

# Show top N urgent orders
def show_UrgentOrder(city, N):
    print(f"\nLast {N} urgent deliveries for {city.name}:")
    for order in reversed(city.urgent_stack[-N:]):
        print("  Urgent Order ID:", order)

# Process first pending delivery (FIFO)
def process_pending(city):
    print(f"\nProcessing first pending delivery for {city.name}:")
    if city.pending_front:
        print("  Order ID:", city.pending_front.order_id)
        city.pending_front = city.pending_front.next
        if city.pending_front is None:
            city.pending_rear = None
    else:
        print("  No pending deliveries.")

# ----------------------
# MAIN PROGRAM
# ----------------------

# Create root city (hub)
root = add_city(None, "Headquarters", 0)

# Add connected cities
city_a = add_city(root, "Lahore", 100)
city_b = add_city(root, "Karachi", 1200)
city_c = add_city(city_a, "Multan", 300)

# Add delivery records
add_delivery(city_a, "ORD001", "Delivered")
add_delivery(city_a, "ORD002", "Urgent")
add_delivery(city_a, "ORD003", "Pending")
add_delivery(city_a, "ORD004", "Urgent")
add_delivery(city_b, "ORD005", "Pending")

# Show structure and records
show_routes(root)
show_deliveries(city_a)
show_UrgentOrder(city_a, 2)
process_pending(city_a)
process_pending(city_a)
