def Binary_Search(arr,patient_id):
    size=len(arr)-1
    left=0
    right=size
    while left<=right:
        mid=(left+right)//2
        if arr[mid]==patient_id:
            return mid
        elif arr[mid]<patient_id:
            left=mid+1
        elif arr[mid]>patient_id:
            right=mid-1
    return None
data=[1024, 1034, 1067, 1100, 1200, 1300, 1902, 1500, 1900]
key = 1067
print("Element found at index:", Binary_Search(data, key))
    
