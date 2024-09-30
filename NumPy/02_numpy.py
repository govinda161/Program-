import numpy as np
arr = np.array([1, 2, 3])
print(arr)
print(type(arr))

#--------------------------------
# 2D Array
arr = np.array([[1,2,3],
                [4,5,6]])
print("Array with 2 rank :",arr)
print("After using slicing :",arr[::-1])

#----------------------------------------

a = np.array([[1, 2],
              [3, 4]])
print ("Adding 1 to every element:", a + 1)

#-------------------------------------------

arr2 = np.array([4,5])
print ("\nSum of all array "
       "elements: ", arr2.sum())

#---------------------------------------
x=np.array([1,2,3,6,5,4])
print("Array before sorting",x)
sort=np.sort(x)
print("Array after sorting :",x)
#-------------------------------------
x = np.array([1,2,3,4,5,6,10])
minv=np.min(x)
maxv=np.max(x)
print("Minimum value :", minv)
print("Maxmum value :",maxv)

#--------------------------------
arr1 = np.array([1, 2, 3])
arr2 = np.array([4,5])
x = np.concatenate((arr1,arr2))
print("Array after concatenate :",x)

#--------------------------------------
arr = np.array([12,13,14,15])
arr1 = np.array([1,2,3,4])
# 1. Add
result = arr + arr1
print("After addition :",result)

# 2.Sub
sub = arr - arr1
print("After subtraction :",sub)

# 3.Multi
multi = arr * arr1
print("After multiplication :",multi)

# 4.Divide
divide = arr / arr1
print("After division :",divide)
