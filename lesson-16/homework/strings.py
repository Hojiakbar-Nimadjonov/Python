#1. Convert a list to a 1D NumPy array
import numpy as np

lst = [12.23, 13.32, 100, 36.32]
arr = np.array(lst)
print("NumPy array:", arr)

#2. Create a 3x3 matrix with values from 2 to 10
matrix = np.arange(2, 11).reshape(3, 3)
print(matrix)

#3. Zero vector of size 10 and update the sixth value to 11
vec = np.zeros(10)
vec[6] = 11
print(vec)

#4. Create an array with values from 12 to 37
arr = np.arange(12, 38)
print(arr)

#5. Convert an array to float type
arr = np.array([1, 2, 3, 4], dtype=float)
print(arr)

#6. Convert Celsius to Fahrenheit
celsius = np.array([0, 12, 45.21, 34, 99.91])
fahrenheit = celsius * 9 / 5 + 32
print("Celsius:", celsius)
print("Fahrenheit:", fahrenheit)

 #7. Append values to the end of an array
arr = np.array([10, 20, 30])
new_arr = np.append(arr, [40, 50, 60, 70, 80, 90])
print("Updated array:", new_arr)

#8. Statistical functions: mean, median, standard deviation
arr = np.random.rand(10)
print("Array:", arr)
print("Mean:", np.mean(arr))
print("Median:", np.median(arr))
print("Standard Deviation:", np.std(arr))

#9. Find min and max in a 10x10 array
arr = np.random.rand(10, 10)
print("Min value:", np.min(arr))
print("Max value:", np.max(arr))

#10. Create a 3x3x3 array with random values
arr = np.random.rand(3, 3, 3)
print(arr)
