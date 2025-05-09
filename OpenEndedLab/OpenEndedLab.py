import heapq

# Vehicle Class
class Vehicle:
    def __init__(self, var_vehicle_type, var_priority, var_vehicle_id):
        self.var_vehicle_type = var_vehicle_type
        self.var_priority = var_priority
        self.var_vehicle_id = var_vehicle_id

# Slot Class
class Slot:
    def __init__(self, var_zone, var_level, var_slot_number, var_slot_type, var_distance):
        self.var_zone = var_zone
        self.var_level = var_level
        self.var_slot_number = var_slot_number
        self.var_slot_type = var_slot_type  # Bike, Car, Truck
        self.var_distance = var_distance    # Used for nearest slot
        self.var_occupied = False
        self.var_vehicle = None
        self.var_priority_reserved = False

# Parking System Class
class ParkingSystem:
    def __init__(self):
        self.var_parking_slots = {}  # HashMap: slot_id -> Slot object
        self.var_heap = []           # Min-Heap for nearest available slot
        self.var_priority_vehicles = []
        self.var_vehicle_counter = 1
        self.initialize_parking()

    def initialize_parking(self):
        # Let's initialize a simple layout: Zone A, Zone B with few slots
        var_zones = ['A', 'B']
        for var_zone in var_zones:
            for var_level in range(1, 3):  # 2 levels
                for var_slot_number in range(1, 6):  # 5 slots each level
                    var_slot_id = f"{var_zone}-L{var_level}-S{var_slot_number}"
                    if var_slot_number <= 2:
                        var_slot_type = 'Bike'
                    elif var_slot_number <= 4:
                        var_slot_type = 'Car'
                    else:
                        var_slot_type = 'Truck'
                    var_slot = Slot(var_zone, var_level, var_slot_number, var_slot_type, var_slot_number)
                    self.var_parking_slots[var_slot_id] = var_slot
                    heapq.heappush(self.var_heap, (var_slot.var_distance, var_slot_id))

    def park_vehicle(self, var_vehicle_type, var_priority):
        while self.var_heap:
            var_distance, var_slot_id = heapq.heappop(self.var_heap)
            var_slot = self.var_parking_slots[var_slot_id]
            if not var_slot.var_occupied and var_slot.var_slot_type == var_vehicle_type:
                var_vehicle = Vehicle(var_vehicle_type, var_priority, self.var_vehicle_counter)
                var_slot.var_occupied = True
                var_slot.var_vehicle = var_vehicle
                if var_priority == 'Y':
                    self.var_priority_vehicles.append(var_vehicle)
                print(f"Allocated Slot: Zone {var_slot.var_zone} - Level {var_slot.var_level} - Slot {var_slot.var_slot_number}")
                self.var_vehicle_counter += 1
                return
        print("No available slot for your vehicle type currently.")

    def remove_vehicle(self, var_slot_id):
        if var_slot_id in self.var_parking_slots:
            var_slot = self.var_parking_slots[var_slot_id]
            if var_slot.var_occupied:
                if var_slot.var_vehicle.var_priority == 'Y':
                    self.var_priority_vehicles.remove(var_slot.var_vehicle)
                var_slot.var_occupied = False
                var_slot.var_vehicle = None
                heapq.heappush(self.var_heap, (var_slot.var_distance, var_slot_id))
                print(f"Vehicle removed from {var_slot_id}")
            else:
                print("Slot already empty.")
        else:
            print("Invalid Slot ID.")

    def show_all_slots(self):
        print("\n--- Parking Slots Status ---")
        for var_slot_id, var_slot in self.var_parking_slots.items():
            var_status = "Occupied" if var_slot.var_occupied else "Available"
            print(f"{var_slot_id}: {var_slot.var_slot_type} - {var_status}")

    def show_available_evs(self):
        print("\n--- Available EV Slots ---")
        for var_slot_id, var_slot in self.var_parking_slots.items():
            if not var_slot.var_occupied and var_slot.var_slot_type == 'Car':  # Assume EVs park in Car slots
                print(f"{var_slot_id} is available for EVs")

    def show_priority_vehicles(self):
        print("\n--- Priority Vehicles Parked ---")
        if not self.var_priority_vehicles:
            print("No priority vehicles currently parked.")
        for var_vehicle in self.var_priority_vehicles:
            print(f"Vehicle ID: {var_vehicle.var_vehicle_id}, Type: {var_vehicle.var_vehicle_type}")

# Menu Driven Interface
def menu():
    var_parking_system = ParkingSystem()
    print("Open-Ended Lab-Ten\n")
    print("Welcome to Smart City Parking System")
    
    while True:
        print("\nMenu:")
        print("1. Park a Vehicle")
        print("2. Remove a Vehicle")
        print("3. Show All Parking Slots")
        print("4. Show Available Slots for EVs")
        print("5. Show Priority Vehicles")
        print("6. Exit")

        var_choice = input("Choose Option: ")

        if var_choice == '1':
            var_vehicle_type = input("Enter Vehicle Type (Bike/Car/Truck): ")
            var_priority = input("Priority (Y/N): ")
            var_parking_system.park_vehicle(var_vehicle_type, var_priority)

        elif var_choice == '2':
            var_slot_id = input("Enter Slot ID (e.g., A-L1-S2): ")
            var_parking_system.remove_vehicle(var_slot_id)

        elif var_choice == '3':
            var_parking_system.show_all_slots()

        elif var_choice == '4':
            var_parking_system.show_available_evs()

        elif var_choice == '5':
            var_parking_system.show_priority_vehicles()

        elif var_choice == '6':
            print("Good Bye 😊")
            break
        else:
            print("Invalid Choice. Try again.")

if __name__ == "__main__":
    menu()