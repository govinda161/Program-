import numpy as np
 
''' 1. Write a NumPy program to create an array of 10 zeros, 10 ones, and 10 fives '''
# Create array
zero = np.zeros(10)
one = np.ones(10)
five = np.full(10,5)

# Print the array
print("Array of Zeros :",zero)
print("Array of Ones :",one)
print("Array of Fives :",five)


''' 2. Write a NumPy program to create a 3x3 matrix with values ranging from 2 to 10. '''
# Create a 3x3 matrix with values ranging from 2 to 10
matrix = np.arange(2, 11).reshape(3,3)

#Print the matrix
print("3x3 matrix with values from 2 to 10 :",matrix)


''' 3. Write a NumPy program to create an array with values ranging from 12 to 38. '''
# Create an array with values from 12 to 38
array = np.arange(12, 39)

# Print the array
print("Array with values from 12 to 38 :",array)



''' 4. Write a NumPy program to convert a list and
tuple into arrays. Input: my_list = [1, 2, 3, 4, 5, 6, 7,8]
Input: my_tuple = ([8, 4, 6], [1, 2, 3])'''
my_list = [1, 2, 3, 4, 5, 6, 7, 8]
my_tuple = ([8, 4, 6], [1, 2, 3])

# Convert to array
array_from_list = np.array(my_list)
array_from_tuple = np.array(my_tuple)

# Print the array
print("Array from list :", array_from_list)
print("Array from tuple :", array_from_tuple)

