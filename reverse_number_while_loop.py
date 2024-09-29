# Q.1. Write a python program to reverse a number using a while loop.


# Reverse a number
def reverse_number(n):
    reversed_num = 0
    while n > 0:
        # Extract the last digit
        digit = n % 10
        # Build the reversed number
        reversed_num = reversed_num * 10 + digit
        # Remove the last digit from n
        n = n // 10
    return reversed_num

# Input from the user
num = int(input("Enter a number to reverse: "))

# Output the reversed number
print("Reversed number:", reverse_number(num))
