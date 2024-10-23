# Number of rows for the pyramid
rows = 5  # Set the height of the pyramid

# Loop through each row
for i in range(rows):  # Iterate from 0 to 4 (5 rows)
    # Print spaces before the stars
    print(' ' * (rows - i - 1), end='')  # Print leading spaces for alignment
    
    # Print stars for the current row
    print('*' * (2 * i + 1))  # Print (2 * i + 1) stars for the current row
