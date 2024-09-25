# Getting size using getsizeof() method
# printing the same.
age=20
import sys
print(f'The max capacity of (integer) is {sys.getsizeof(age)}')

name = 'Govinda'
print(f'The capacity of text (string) is {sys.getsizeof(name)}')

height=165.5
print(f'The capacity of text (boolean) is {sys.getsizeof(height)}')
