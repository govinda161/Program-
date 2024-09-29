# Q. 2. Write a python program to check whether a number is palindrome or not? 

# Function to check if a number is a palindrome
def is_palindrome(number):
    # Store the original number
    original_number = number
    reversed_number = 0
    
    # Reverse the number
    while number > 0:
        digit = number % 10
        reversed_number = reversed_number * 10 + digit
        number = number // 10
    
    # Check if the original number is equal to the reversed number
    return original_number == reversed_number

# Input from the user
num = int(input("Enter a number: "))

# Check and output the result
if is_palindrome(num):
    print("The number is a palindrome.")
else:
    print("The number is not a palindrome.")
