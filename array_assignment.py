""" 1. Write a code to add 2 arrays using a for loop
    2. Write a code to find the maximum value from an array without using in-built function
    3. Write matrix multiplication
"""
from array import *
arr = array('i', [1,2,3,4,5])
arr_1 = array('i', [6,7,8,9,10])
sum = array(arr.typecode, [a for a in arr])

print(arr)
print(arr_1)
if(len(arr) != len(arr_1)):
    print("Arrays can not be added")
else:
    for i in range(len(arr)):
        sum[i] = 0
        sum[i] =  arr[i] + arr_1[i]
print('Sum of the arrays is', sum)

max = sum[0]
for i in range(1, len(sum)):
    if(max < sum[i]):
        max = sum[i]
print('Max of sum array is', max)




