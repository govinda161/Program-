''' how do you find the shape of array? '''
# Import the NumPy library
import numpy as np

# Create a NumPy array (2D)
array_2d = np.array([[1, 2, 3],  # First row
                     [4, 5, 6],  # Second row
                     [7, 8, 9]]) # Third row

# Get the shape of the array
shape = array_2d.shape  # Access the 'shape' attribute to get dimensions

# Print the shape of the array
print("Shape of the Array:",shape)
