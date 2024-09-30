# 1. Convert the below list into numpy array then display the array

import numpy as np
my_list = [1, 2, 3, 4, 5]
list = np.array(my_list)
print("After convert :",list)

#2. Convert the below list into a numpy array then display the array then display the first and last index and then multiply each element by 2 and display the result.

my_list = [1,2,3,4,5]
f = np.array(my_list)
print("First element :",f[0])
s = np.array(my_list)
print("Last element :",s[-1])

#multiply
f = np.array(my_list)
print("My original array :",f)
m = f*2
print("After multiply :",m)
