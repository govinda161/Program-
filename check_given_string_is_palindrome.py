# Function to check if a string is a palindrome
def is_palindrome(s):
    # Remove spaces and convert the string to lowercase
    s = s.replace(" ", "").lower()  # Normalize the string for comparison
    
    # Check if the string is equal to its reverse
    return s == s[::-1]  # Compare the original string with its reversed version

# Take input from the user
input_string = input("Enter a string: ")  # Prompt the user for input

# Check if the input string is a palindrome
if is_palindrome(input_string):  # Call the function and check the result
    print(f'"{input_string}" is a palindrome.')  # Output if it is a palindrome
else:
    print(f'"{input_string}" is not a palindrome.')  # Output if it is not a palindrome
