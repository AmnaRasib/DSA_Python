def recursive_function(n):
    if n == 0:
        print("Base case reached")
        return
    print(f"Calling function with n = {n}")
    recursive_function(n - 1)
    print(f"Returning from function with n = {n}")

# Example call
recursive_function(3)
