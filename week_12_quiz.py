import statistics
import numpy as np
import pandas as pd


#Number 1. What is the result of the following code?

a = np.array([1, 2, 3])
b = np.array([4, 5, 6])
c = a + b
print(c)

#answer = [5 7 9]

#Number 2. Create a numpy array of 10 zeros. and reshape it to (2, 5)


zero_arr = np.array([0,0,0,0,0,0,0,0,0,0])
zero_arr = zero_arr.reshape(2, 5)
print(zero_arr)

# Answer
# [[0 0 0 0 0]
#  [0 0 0 0 0]]

#Number 3. Find Mean, Mode, Median, Standard Deviation of the following data

data = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19, 20]
stats = np.array([1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19, 20])
#a) Mean 

mean = np.mean(stats)
print(mean)

#answer = 10.5

#b) Mode

mode = statistics.mode(stats.flatten())

print(stats.flatten())
print(mode)

answer = 1


#c) Median
median = np.median(stats)
print(median)

#answer = 10.5

#d) Standard Deviation
sd = np.std(stats)
print(sd)
answer = 5.766281297335398

#Number 4. create a 6x6 numpy array with random values and find the min and max values

arr = np.array([
    [3, 17, 56, 11, 5,32],
    [19,78, 77, 12, 0,21],
    [1, 69, 99, 30, 11,15],
    [102,34,178,20,70,23],
    [87, 60,33, 19, 40,209],
    [45,108, 92, 23, 2, 17]
])

print(arr.flatten())
maxi = np.max(arr)
print(maxi)
#answer = 209

mini = np.min(arr)
print(mini)
#answer = 0

#Number 5. create a 3D numpy array and reshape it to 2D

arr = np.array([1, 2, 3, 4], ndmin=3)

print(arr)
print('number of dimensions :', arr.ndim)

arr = arr.reshape(2,2)
print(arr)
print('number of dimensions :', arr.ndim)

#Answer. The 3D array = [[[1 2 3 4]]]
# number of dimensions : 3
#The 2D array will be:
# [[1 2]
#  [3 4]]
# number of dimensions : 2

#Number 6. create 1D array from this data
# data = [[1, 2, 3], [4, 5, 6], [7, 8, 9]]
array = [[1, 2, 3], [4, 5, 6], [7, 8, 9]]
array =  np.array([[1, 2, 3], [4, 5, 6], [7, 8, 9]])
array= array.reshape(9, )
print(array)
print('number of dimensions :', array.ndim)

#Answer = [1 2 3 4 5 6 7 8 9]
# number of dimensions : 1