def bubble_sort(arr):
    n= len(arr)
    for i in range (n):
         for j in range (i+1,n):
              if arr[i]>arr[j]:
                   arr[i],arr[j]=arr[j],arr[i]
    return arr

data = [5, 3, 8, 4, 2]
bubble_sort(data)
print("Sorted List:", data)
