# Calculate the Factorial of a Number
num= int(input("Enter a number: "))

def factorail(num):
    if num==0 and num==1:
        return 1
    else:
        f=1
        for x in range(num,1,-1):
            f=f*x
        return f
# fuction call
factorial= factorail(num)
print(f"The factorial of {num} is: {factorial}")
    
