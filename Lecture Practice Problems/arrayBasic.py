import array as arr

arr1=arr.array('i',[1,2,3,4,5])
arr2=arr.array('f',[1.0,2.3,4.5,6.7,7.8])
# TypeCodes
print(arr1.typecode)
print(arr2.typecode)
# length
print("Length of first array: ",len(arr1))
print("Length of Second array: ",len(arr2))
# Printing the elements of the array
for i in range(0,len(arr1)):
    print(arr1[i], end=" ")
print()
for j in range(0,len(arr2)):
    print(f"{arr2[j]:.2f}", end=" ")
print()
#inserting new Elements
arr1.insert(2,4)
arr2.insert(2,4.0)
arr1.append(12)
arr2.append(12.0)
print("After inserting new elements: ")
print("Integer Array: ",arr1)
print("floating Array: ",arr2)
print("\n")
#deleting elements
arr1[2]=3
print("updating Value at index 2 in array 1: ",arr1)
arr1.pop(4)
print("After Deleting the arrays become: ")
print("Integer Array: ",arr1)
print("floating Array: ",arr2)


