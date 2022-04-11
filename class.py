# import numpy library.
import numpy as np
# create array 
arr = np.array([2, 3, 4])
# console out the array
print(f"array1=\n{arr}")
# type
print (f"type:\n{type(arr)}")


# array creation with numpy.array
a = np.array(42)
b = np.array([1, 2, 3, 4, 5])
c = np.array([[1, 2, 3], [4, 5, 6]])
d = np.array([[[1, 2, 3], [4, 5, 6]], [[1, 2, 3],
[4, 5, 6]]])
e=np.array([[[[[[[6]]]]]]])
#Dimention in array.
print(a.ndim)
print(b.ndim)
print(c.ndim)
print(d.ndim)
print(e.ndim)


