
def factorial(num):
    if num == 0 or num == 1:
        return 1
    else:
        f = 1
        for x in range(num, 1, -1):
            f = f * x  # Corrected to multiply by x
        return f  # Changed to return the value instead of printing

# Call the function
result = factorial(5)
print("Factorial of 5 is:", result)
  
        
        
        
    