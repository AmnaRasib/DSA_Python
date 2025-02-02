
def rotated_array(arr,steps):
   steps= steps % len(arr)
   return arr[-steps:]+arr[:-steps]

input_arr=[1,2,3,4,5]
steps=2
print("Original Array: ",input_arr)
print("rotated Array: ",rotated_array(input_arr,steps))
