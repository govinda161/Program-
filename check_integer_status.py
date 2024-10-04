def check_integer_status(num):
    """Determine if the input integer is positive, negative, or zero."""
    # Check if the number is greater than zero
    if num > 0:
        return "Positive"
     # Check if the number is less than zero
    elif num < 0:
        return "Negative"
    else:
        return "Zero"

# Example usage
number = int(input("Enter an integer: "))   # The user to enter an integer and convert input to an integer
status = check_integer_status(number)    # Call the function with the user's input and store the result in 'status'
print(f"The integer is: {status}")    # Print the result indicating whether the integer is positive, negative, or zero
