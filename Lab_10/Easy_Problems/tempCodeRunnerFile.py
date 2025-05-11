import heapq

def create_min_heap():
    print("Enter 10 integers (space-separated):")
    try:
        nums = list(map(int, input().split()))
        if len(nums) != 10:
            print("Please enter exactly 10 integers.")
            return

        # Convert list into a min-heap
        heapq.heapify(nums)

        print("Min Heap as list:", nums)

    except ValueError:
        print("Invalid input. Please enter integers only.")

# Run the function
create_min_heap()
