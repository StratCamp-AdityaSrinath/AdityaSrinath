# Import numpy and statistics packages and name them
import numpy as np
import statistics as stat

arr = np.array([1,2,3,4,5,6,7,8,9,10]) # Create an array (a matrix)
quint = arr * 5 # Multiply all elements of the array by 5
quint_2_diff = quint - 2 # Subtract 2 from all elements of the array

print(quint_2_diff) # Print the array with all its neew values after operations above

arr2 = np.array([8,20,22,20,10,20,22,8]) # Create another array
mean_arr2 = arr2.mean() # Find the mean value within the array
median_arr2 = stat.median(arr2) # Find the element in the array with the median (50th percentile) value
mode_arr2 = stat.mode(arr2) # Find the element within the array that appears most often relative to the others

print(mean_arr2) # Print the mean
print(median_arr2) # Print the median
print(mode_arr2) # Print the mode

arr3x3 = np.array(range(1,10)).reshape((3,3)) # Create a 3 x 3 matrix using the array and reshape functions in numpy to specify the dimensions of the matrix
arr3x3_row2 = arr3x3[1] # Store the second row of the matrix in a variable for ease of use later
arr3x3_col2_horiz = [arr3x3[0][1],arr3x3[1][1],arr3x3[2][1]] # Store the second column of the matrix in a variable for ease of use later
arr3x3_col2 = np.array(arr3x3_col2_horiz).reshape((3,1)) # Reshape the elements of the second column as asking to print the variable above would result in horizontal representation

print(arr3x3_row2) # Print the second row
print(arr3x3_col2) # Print the second column