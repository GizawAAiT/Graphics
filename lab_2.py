import numpy as np
arr = np.array([2, 3, 4])
print(arr)
print (type(arr))

a = np.array(42)
b = np.array([1, 2, 3, 4, 5])
c = np.array([[1, 2, 3], [4, 5, 6]])
d = np.array([[[1, 2, 3], [4, 5, 6]], [[1, 2, 3],
[4, 5, 6]]])
e=np.array([[[[[[[6]]]]]]])
# printing the above arrays
print(a.ndim)
print(b.ndim)
print(c.ndim)
print(d.ndim)
print(e.ndim)



# exercise 1
# Array creation types!
arrayZeros=np.zeros((2,2))
arrayOnes=np.ones((2,2))
arrayArange=np.arange(0,10,3)
arrayastype=arrayArange.astype(float)
arrayLikeZeros=np.zeros_like(arrayArange)
arrayLikeOnes=np.ones_like(arrayArange)
arrayRandom=np.random.random(6)
arrayRandint=np.random.randint(2,20, size = (5))
arrayConcatenated=np.concatenate((arrayZeros,arrayOnes),axis=None)

# displaying the above arrays
print(f"array_Zeros:=\n{arrayZeros} \n array_Ones:=\n {arrayOnes}\n array_arange:=\n {arrayArange}")
print(f"array_like_zeros:={arrayLikeZeros}\narray_like_one:={arrayLikeOnes}")
print(f"array_random:= {arrayRandom},\narray_randint:= {arrayRandint}")


# Pivoting Arrays