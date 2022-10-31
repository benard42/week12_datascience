import pandas as pd
import numpy as np
import statistics

davids_marks = np.array([
    [78, 67, 90],
    [34, 55, 23],
    [12, 89, 45]
])


mode = statistics.mode(davids_marks.flatten())

median = np.median(davids_marks)

mean = davids_marks.mean()

print(f"Mode: {mode}, median: {median}, mean: {mean}")


two_dim = np.array([1,2,3,4,5,6,7,8,9], ndmin = 2)
print(two_dim.ndim)

davids_marks = np.array([
    [78,67,90],
    [34,55,23],
    [12,89,45]
])

print(davids_marks[0][2])
print(davids_marks[2][1])

diagonal = [davids_marks[0][0],davids_marks[1][1],davids_marks[2][2]]

print(diagonal)

my_arr = np.array([[i for i in range(4)] for _ in range(4)])
print(my_arr.ndim)

#Array slicing
print(davids_marks[0,2])
print(davids_marks[2,1])
print(davids_marks[:2,:1])

print(davids_marks.dtype)

fruits = np.array(['apple','banana','cherry'])

print(fruits.dtype)

mary_marks = davids_marks.copy()

print(mary_marks)

print(mary_marks.view())

print(mary_marks.base)

print(davids_marks.shape)

arr = np.array([1,2,3,4,5])

print(arr.shape)

arr = np.array([i+1 for i range(12)])
print(arr)

arr = arr.reshape(4,3)

print(arr)

arr = arr.reshape(2,6)

print(arr)

arr = arr.reshape(2,3,2)
print(arr)

arr = np.arry([[[1],[2],[3],[4],[5],[6],[7],[8],[9],[10],[11],[12]]])
print(arr.ndim)
