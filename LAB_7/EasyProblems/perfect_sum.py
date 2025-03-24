assumed_number=6
myList=[]
sum=0

for i in range(1,assumed_number+1):
    myList.append(i)
for i in range(len(myList)):
    sum=sum+i
    if sum>=assumed_number:
        if sum==assumed_number:
            print("Perfect Sum")
            break
        else:
            print("Not a perfect Sum")
            break
        