assumed_number=6
my_list=[]
sum=0
for i in range(1,assumed_number+1):
    my_list.append(i)
for i in my_list:
    sum=sum+i
    if sum>=assumed_number:
        if sum == assumed_number:
            print("Yes! it is perfect sum")
            break
        else:
            print("NO")
            break
