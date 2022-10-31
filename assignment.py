import numpy as np
import statistics
import pandas as pd 


###  Number 1 

[5 7 9]


###Number 2

array=np.zeros(10)
print("An array of 10 zeros:")
print(array)

array =  = array.reshape(2,5)

print(array)

### Number 3

data = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19, 20]

mode = statistics.mode(data.flatten())

median = np.median(data)

mean = data.mean()

StandardDeviation =statistics.stdev(data)

print(f"Mode: {mode}, median: {median}, mean: {mean}")

### number 4

arr = np.array([[11, 2, 3,3,34,55],
                     [4, 5, 16,4,5,6],
                      [7, 81, 22,5,7,8]
                      [3,4,5,6,7,8]
                      [34,5,7,85,45,7]
                      [34,5,66,75,63,34]])
 
max_element = np.max(arr)
min_element = np.min(arr)
 
print('maximum element in the array is:',
      max_element)
print('minimum element in the array is:',
      min_element)

#### Number 5


array=np.array( [
      [[ 3,  0],
      [ 7,  6]],
 
      [[ 4,  9],
      [23, 39]],
                  
      [[ 20, 33],
      [ 13, 15]]])
reshaped_array=np.reshape(array,(4,4))
print("Original array:\n", array)
print("Reshaped array:\n", reshaped_array)

###Number 6

data = [[1, 2, 3], [4, 5, 6], [7, 8, 9]]
newarr = data.reshape(1,1)

print(newarr)

