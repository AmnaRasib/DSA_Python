def linear_unordered_search(arr,key):
    for i in range(len(arr)):
        if arr[i]==key:
            return i
    return -1
arr = [40, 20, 60, 10, 80]
key = 60
print("Element found at index:", linear_unordered_search(arr, key)) 
