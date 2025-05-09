def binary_search(arr,key):
    size=len(arr)-1
    left=0
    right=size
    while left <=right:
        mid=(left+right)//2
        if arr[mid]==key:
            return True
        elif arr[mid]<key:
            left=mid+1
        elif arr[mid]>key:
            right=mid-1
    return False
arr = [10,20,40,60,80]
key = 30
print("Element found at index:", binary_search(arr, key))