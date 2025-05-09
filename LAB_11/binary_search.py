def binary_search(arr,key):
    size=len(arr)-1
    left_index=0
    right_index=size
    while left_index<=right_index:
        mid=(left_index + right_index) //2
        if arr[mid]==key:
            return mid
        elif arr[mid]> key:
            right_index=mid -1
        elif arr[mid] < key:
            left_index=mid+1
    return None

arr = [10,20,40,60,80]
key = 60
print("Element found at index:", binary_search(arr, key))
