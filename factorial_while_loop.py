# Write a python program finding the factorial of a given number using a while loop.

# Calculate factorial using a while loop
def factorial(n):
    result = 1
    while n > 0:
        result *= n
        n -= 1
    return result

# Input from the user
num = int(input("Enter a number to find its factorial: "))

# Calculate and output the factorial
print(f"The factorial of {num} is {factorial(num)}.")

