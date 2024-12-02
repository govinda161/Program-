# Import the NumPy library
import numpy as np

# Create a NumPy array from the list
arr = np.array([20, 2, 7, 1, 34])

# Calculate the standard deviation of the array
std_dev = np.std(arr)

# Print the standard deviation
print("arr :",arr)
print("std of arr :",std_dev,'\n') 

print("More precision with float32")
print(f"std of arr: {std_dev:.6f}\n")  # Print the standard deviation with six decimal places

print("More accuracy with float64")
print(f"std of arr: {std_dev:.15f}")  # Print the standard deviation with fifteen decimal places 
