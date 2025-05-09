def insertion_sort(arr):
    n=len(arr)
    for i in range(n):
        for j in range (i+1,n):
           if arr[0]>arr[j]:
             arr[0],arr[j]=arr[j],arr[0]
    return arr
data = [5, 3, 8, 4, 2]
insertion_sort(data)
print("Sorted List:", data)
