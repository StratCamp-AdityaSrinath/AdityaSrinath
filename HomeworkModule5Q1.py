import numpy as np
import statistics as stat

arr = np.array([1,2,3,4,5,6,7,8,9,10])
quint = arr * 5
quint_2_diff = quint - 2

print(quint_2_diff)

arr2 = np.array([8,20,22,20,10,20,22,8])
mean_arr2 = arr2.mean()
median_arr2 = stat.median(arr2)
mode_arr2 = stat.mode(arr2)

print(mean_arr2)
print(median_arr2)
print(mode_arr2)

arr3x3 = np.array(range(1,10)).reshape((3,3))
arr3x3_row2 = arr3x3[1]
arr3x3_col2_horiz = [arr3x3[0][1],arr3x3[1][1],arr3x3[2][1]]
arr3x3_col2 = np.array(arr3x3_col2_horiz).reshape((3,1))

print(arr3x3_row2)
print(arr3x3_col2)