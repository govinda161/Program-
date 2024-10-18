''' Calculate the total cost of items in a shopping cart, considering the quantity and price per item. 
    Input: quantity = np.array([2, 3, 4, 1])
    price_per_item = np.array([10.0, 5.0, 8.0, 12.0]) '''

# Import the NumPy library
import numpy as np  

# Define the quantity array
quantity = np.array([2, 3, 4, 1])  # Input array representing quantities of items

# Define the price per item array
price_per_item = np.array([10.0, 5.0, 8.0, 12.0])  # Input array representing prices of items

# Calculate the total cost for each item
total_cost = quantity * price_per_item  # Element-wise multiplication of quantity and price

# Print the total cost of items
print("Total Cost of Items:", total_cost)  # Output the total cost for each item
