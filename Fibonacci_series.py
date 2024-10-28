# Function to generate Fibonacci series up to a given limit
def fibonacci_series(limit):
    # Initialize the first two Fibonacci numbers
    a, b = 0, 1  # Start with 0 and 1

    # Loop until the current number exceeds the limit
    while a <= limit:  # Continue while a is less than or equal to the limit
        # Print the current Fibonacci number
        print(a, end=' ')  # Print the current number in the series
        # Update the Fibonacci numbers
        a, b = b, a + b  # Move to the next Fibonacci number

# Set the limit for the Fibonacci series
limit = 50  # We want the series up to 50

# Call the function to generate and print the Fibonacci series
fibonacci_series(limit)  # Generate Fibonacci numbers up to the limit
