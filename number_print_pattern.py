def number_pattern(n):
    # Loop through numbers from 1 to n
    for i in range(1, n + 1):
        # Create a list of numbers from 1 to i and join them with spaces
        print(' '.join(str(j) for j in range(1, i + 1)))

# Example usage
number_pattern(5)
