def insertion_sort(arr):
    n=len(arr)
    for i in range(1,n):
        key=arr[i] 
        j=i-1      
        while j>=0 and arr[j]>key:
          arr[j+1]=arr[j] 
          j-=1
        arr[j+1]=key
        print(f"After pass {i}: {arr}")  
    return arr
data = [5, 3, 8, 4, 2]
insertion_sort(data)
print("Sorted List:", data)
