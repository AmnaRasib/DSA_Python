def ordered_linear(arr,key):
    for i in range(len(arr)):
        if arr[i]==key:
            return i
        elif arr[i]>key:
            return None
    return None

arr = [10,20,40,60,80]
key = 30
print("Element found at index:", ordered_linear(arr, key))
