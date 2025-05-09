# Binary Search Function
def binary_search(data, target):
    comparisons = 0
    low = 0
    high = len(data) - 1

    while low <= high:
        comparisons += 1
        mid = (low + high) // 2
        
        if data[mid] == target:
            return mid, comparisons
        elif data[mid] < target:
            low = mid + 1
        else:
            high = mid - 1

    return -1, comparisons

if __name__ == "__main__":
    # Dataset 10: Sorted list with 40 '1's and numbers 2-6
    dataset = sorted([1]*40 + [2, 3, 4, 5, 6])
    target = 3
    
    print("Sorted Dataset:", dataset)
    
    index, comparisons = binary_search(dataset, target)
    
    if index != -1:
        print(f"\nResult: Found at index {index}")
    else:
        print("\nResult: Not found")
    
    print(f"Comparisons Made: {comparisons}")
