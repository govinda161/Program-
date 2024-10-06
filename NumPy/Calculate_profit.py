import numpy as np  # Import the NumPy library for numerical operations

# Revenue for each period
revenue = np.array([10000, 12000, 11000, 10500])  # Define an array for revenue

# Expenses for each period
expenses = np.array([4000, 5000, 4500, 4800])  # Define an array for expenses

# Calculate profit by subtracting expenses from revenue
profit = revenue - expenses  # Element-wise subtraction of expenses from revenue

# Print the profit for each period
print("Profit:", profit)  # Output the result
