# Function to check if a number is an Armstrong number
def is_armstrong_number(num):
    # Convert the number to a string to work with its digits
    num_str = str(num)  # Turn the number into a string
    # Calculate the number of digits in the number
    num_digits = len(num_str)  # Count the digits

    # Calculate the sum of each digit raised to the power of the number of digits
    sum_of_powers = 0  # Initialize the sum
    for digit in num_str:  # Loop through each digit in the string
        sum_of_powers += int(digit) ** num_digits  # Add the power of the digit to the sum

    # Check if the calculated sum equals the original number
    return sum_of_powers == num  # Return True if it matches, otherwise False

# Take input from the user
input_number = int(input("Enter a number: "))  # Ask the user for a number

# Check if the input number is an Armstrong number
if is_armstrong_number(input_number):  # Call the function to check
    print(f"{input_number} is an Armstrong number.")  # Print if it is an Armstrong number
else:
    print(f"{input_number} is not an Armstrong number.")  # Print if it is not an Armstrong number
