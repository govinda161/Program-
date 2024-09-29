# Q.4. Accept numbers using input() function until the user enters 0. If user input 0 then break the while loop and display the sum of all the numbers.


# Initialize the sum variable
total_sum = 0

# Infinite loop to accept user input
while True:
    # Read input from the user
    number = int(input("Enter a number : "))
    
    # Check if the input is 0
    if number == 0:
        break
    
    # Add the number to the total sum
    total_sum += number

# Display the sum of all numbers entered
print(f"The sum of all entered numbers is: {total_sum}")
