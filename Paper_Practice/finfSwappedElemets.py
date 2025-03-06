the_list=[10,20,30,50,40]
sorted_array=sorted(the_list) #Ascending Order[10,20,30,40,50]
final_swapped=[]
for i in range(len(the_list)):
    if the_list[i] != sorted_array[i]:
        final_swapped.append(the_list[i])
print(final_swapped)
print("Sorted Array in Ascending Order ",sorted_array)
array_decend=sorted(the_list,reverse=True)
print("Sorted Array in decending Order: ",array_decend)
