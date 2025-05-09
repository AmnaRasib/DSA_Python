def bubble_sort(arr):
    n= len(arr)
    for i in range(n):
        swapped=False
        for j in range(0,n-i-1):
            if arr[j]>arr[j+1]:
                arr[j],arr[j+1]=arr[j+1],arr[j]
                swapped=True
        if not swapped:
            break
    return arr

data = [1,2,3,4,5,6]
bubble_sort(data)
print("Sorted List:", data)