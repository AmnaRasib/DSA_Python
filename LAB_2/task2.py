# Advanced Python Arrays
import array
numbers= array.array('i',[3,2,1,4,5])
print("Original Array: ",numbers)
numbers.reverse()
print("Reversed Array: ",numbers)
# Sort the Array
for i in range(len(numbers)):
    for j in range(i+1,len(numbers)):
        if numbers[i]>numbers[j]:
            numbers[i],numbers[j]=numbers[j],numbers[i]
print("Manually sorted Array: ",numbers)
# Find the maximum and minimum values
print("Maximum number in array: ",max(numbers))
print("Minimum number in array: ",min(numbers))
# Count occurrences of an element
numbers.append(2)
print("Occurrence of 2 in array: ",numbers.count(2))
