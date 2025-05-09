def selection_sort(arr):
    n=len(arr)
    count=0
    for i in range(n):
        min_indx=i
        for j in range(i+1,n):
            if arr[j]<arr[min_indx]:
                min_indx=j
        if i!= min_indx:
          arr[i],arr[min_indx]=arr[min_indx],arr[i]  
          count=count+1 
    print("Number of counts are: ",count)
    return arr
data = [1,2,3,4,5]
selection_sort(data)
print("Sorted List:", data)