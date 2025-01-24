# Python Arrays
import array
# an array of integers
numbers= array.array('i',[1,2,3,4,5])
print("Original Array: ",numbers)
numbers[1]=10
print("Modified Array: ",numbers)
#  Add and remove elements
numbers.append(6)
numbers.pop(0)
print("Updated Array: ",numbers)