def is_Prime(n):
    if n<=1:
        return False
    
    for x in range(2,int(n**0.5)+1):
        if n%x==0:
            return False
        
    return True

print("Prime Numbers from (1 to 50): ")
for num in range(1,51):
    if is_Prime(num):
        print(num, end=" ")
        