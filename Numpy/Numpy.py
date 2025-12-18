# listOne = [1,2,3,4,5, "al", True, ['a','b'], (1,3,4), {name:'ALi'}]
# print(listOne)

# listHere = [1,2,3,4,5]

import numpy as np

# print(type(np))

# arr = np.array([10,20,30,40, 50])

# print(arr);
# print(type(arr))

# for i in arr:
#     print(i)

# result = []

# for i in listHere:
#     result.append(i*2)

# print(result)    

# print(arr*2)     # No Loops wriiten/required. but loop happend internally in C(fast)

# print(arr.shape)
# print(arr.ndim)

# Arr2 = [
#     [1,2,3],
#     [4,5,6]]
# print(Arr2)

# matrix = np.array([
#     [1,2,3],
#     [4,5,6]
# ])

# print(matrix)

# print(matrix[1,2])

# print(len(matrix))

# for i in matrix:
#     for j in i:
#         print(j)


# print(matrix[:,1])
# print(matrix[1,:])

# print(matrix.mean())

# Question # 1:

# numArr = np.array([1,2,3,4,5,6,7,8,9,10])

# print(numArr*3);

# # Question # 2:

# twoDarray = np.array([
#     [1,2,3],
#     [4,5,6]
# ])

# print(twoDarray.shape)
# print(twoDarray.ndim)

# Question # 3:

# print(twoDarray[0,2])

# # Question # 4:

# print(numArr.sum())
# print(numArr.mean())
# print(numArr.max())

# # Question # 5:

# numList = [1,2,3,4,5]

# numPyArray = np.array(numList)
# result = numPyArray + 10;
# print(result)
# ==========================================================================


# ========== Reshape numpy array ==========

# arr = np.array([1,2,3,4,5,6,7,8,9,10,11,12])
# arr = np.arange(12)
# # print(arr)
# reshaped = arr.reshape(3,4)
# print(reshaped)


# =============== Axis ===========

# matrix = np.array([
#     [1,2,3],
#     [4,5,6]
# ])

# # print(matrix)
# print(matrix.sum(axis=0))
# print(matrix.sum(axis=1))


# ============ BroadCasting =

# arr1 = np.array([1,2,3])
# arr2 = 10;

# print(arr1 + arr2)

# arr3 = np.array([[1,2,3],[4,5,6]])
# arr4 = np.array([10,20,30])
# arr5 = [10,20,30]

# print (arr4 + arr5)


# ========== dType (Data Type)

# arr = np.array([11,12,13], dtype=np.float32)
# print(arr)
# print(arr.dtype)



# ============================= View VS Copy

# arr = np.array([1,2,3,4])
# view_arr = arr.view()
# copy_arr = arr.copy()

# copy_arr[2] = 99
# view_arr[2] = 77


# print(arr)
# print(view_arr)   #reflect changes in real
# # print(copy_arr)  # wont reflect changes in real

# Q1. Reshape a 1D array of 24 elements into 3D (2×3×4) array.

# arr = np.arange(24)

# reShaped = arr.reshape(2,3,4)
# print(reShaped)

# Q2. Create a 4×5 array and find:

# sum along rows

# sum along columns

# arr = np.array([
#     [1,2,3,4,5],
#     [6,7,8,9,10],
#     [11,12,13,14,15],
#     [16,17,18,19,20]
# ])


# print(arr.sum(axis = 0))
# print(arr.sum(axis = 1))

# Q3. Add a 1D array [1,2,3,4] to a 2×4 array using broadcasting.

# arr1 = np.array([1,2,3,4])
# arr2 = np.array([
#     [1,2,3,4],
#     [5,6,7,8]
# ])

# print(arr1+arr2)

# Q4. Create an array of floats, then change dtype to integer.

# arr = np.array([1,2,3,4], dtype=np.float32)

# print(arr, arr.dtype)
# array = arr.astype(np.int32)
# print(array, array.dtype)

# Q5. Create an array, make a view and a copy, modify both, observe changes.

# array = np.array(['a', 'b', 'c', 'd'])

# view_arr = array.view();
# copy_arr = array.copy();

# # view_arr[1] = 'l';
# copy_arr[2] = 'z';

# # print(view_arr)
# print(copy_arr)

# print(array)

