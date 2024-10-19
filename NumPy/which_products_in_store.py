''' Determine which products in a store are out of stock (quantity is 0).
    Input: inventory = np.array([10, 0, 5, 0, 20, 0]) '''

# Import the NumPy library
import numpy as np  

# Define the inventory array
inventory = np.array([10, 0, 5, 0, 20, 0])  # Input array representing quantities of products

# Identify out of stock products (where quantity is 0)
out_of_stock = inventory[inventory == 0]  # Filter the inventory to find quantities equal to 0

# Print the out of stock products
print("Out of Stock Products:", out_of_stock)  # Output the products that are out of stock
