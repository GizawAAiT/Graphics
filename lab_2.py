import numpy as np
arr = np.array([2, 3, 4])
# print(arr)
# print (type(arr))
a = np.array(42)
b = np.array([1, 2, 3, 4, 5])
c = np.array([[1, 2, 3], [4, 5, 6]])
d = np.array([[[1, 2, 3], [4, 5, 6]], [[1, 2, 3],
[4, 5, 6]]])
e=np.array([[[[[[[6]]]]]]])
# printing the above arrays
# print(a.ndim)
# print(b.ndim)
# print(c.ndim)
# print(d.ndim)
# print(e.ndim)

# exercise 1
# Array creation types!

# 1. and 2.(zeros and ones.)
arrayZeros=np.zeros((3,2,5))
arrayOnes=np.ones((2,3))
print(f"array_Zeros:=\n{arrayZeros} \n array_Ones:=\n {arrayOnes}\n array_arange:=")

# 3. and 4.(range and concat.)
arrayArange=np.arange(0,15,3)
arrayConcatenated=np.concatenate((arrayZeros,arrayOnes),axis=None)
print(f"array range: \n{arrayArange}\n array concat:\n{arrayConcatenated}")

# 5. (as type.)
arrayAstype=arrayArange.astype(float)
print(f"astype(float)\n{arrayAstype}")

# 6.(like zeros and like ones)
arrayLikeZeros=np.zeros_like(arrayArange)
arrayLikeOnes=np.ones_like(arrayArange)
print(f"like zeros\n{arrayLikeZeros}\n like ones:\n{arrayLikeOnes}")

# 7. and 8. (random)
arrayRandom=np.random.random((2,4,3))
arrayRandint=np.random.randint(20, size=(3,4,5))
print(f"random:=\n {arrayRandom},\nrandint:= \n{arrayRandint}")

# Pivoting Arrays
arr=np.array([[1, 2, 3],
              [0,8,9],
              [7,77,88]])
transposed=np.transpose(arr)
print(f"transposed=\n{transposed}")


# reshape
reshape=np.array([1,2,3,4,5,6,7,8,9,10,11,12])
reshaped=reshape.reshape(4,3)
reshaped1=reshape.reshape(2,6)
# reshaped2=reshape.reshape(4,4)
reshaped3=reshape.reshape(2,2,-1)

# flatten.
non_flat=np.array([[12,11,13],[22,23,33],[6,8,99]])
flattened_array = non_flat.flatten()
print (f"flattened:=\n{flattened_array}")

# indexing!
index_array=np.random.randint(20, size=(3,4,5))
print(index_array)
print( index_array[0][0][0])
print( index_array[1,2,3])
print( index_array[-1,-1][-1])

# Mathematical Operations of Arrays
arrat1=np.random.randint(2,6, size=(2,3,4))
arrat2=np.random.randint(2,6, size=(2,3,4))
print(f"array1=\n{arrat1}\narray2=\n{arrat2}")
print(f"sum=\n{np.add(arrat1,arrat2)}")
print(f"diff=\n{np.subtract(arrat1,arrat2)}")
print(f"prod.=\n{np.multiply(arrat1,arrat2)}")
print(f"quotient: =\n{np.divide(arrat1,arrat2)}")
print(f"power=\n{np.power(arrat1,arrat2)}")
print(f"modulo =\n{np.mod(arrat1,arrat2)}")

# matrix multiplication(dot product.)
a = np.array([[1,2,3],
              [4,5,6],
              [7,8,9]])
b = np.array([[2,3,4],
             [5,6,7],
             [8,9,10]])
o = np.matmul(a, b)
o1 = np.dot(a,b)
o2 = np.vdot(a,b)
print(f"O :\n{o} \n o1 :\n {o1} \n o2 : \n {o2}")