"""
Create an array with 5 values and delete the values and delete the value at index number 2 without using inbuilt functions
"""

from array import *
# arr = array('i',[])
# length = int(input("Enter the length of array: "))
# for i in range(length):
#   x = int(input("Enter the next value: "))
#   arr.append(x)
# print(arr)
# val = int(input("Enter the number you want to delete:"))
# k = 0
# tempArr = array('i',[])
# for e in arr:
#   if e != val:
#       tempArr.append(e)
#   k = k+1
# arr = tempArr
# print(arr)


"""
Write a code to reverse an array without using in-built function

"""

a = array('I', [6,7,8,4,3])
print(a)

start, end, temp = 0, len(a) - 1, 0
while(start < end):
    temp = a[end]
    a[end] = a[start]
    a[start] = temp
    start+=1
    end-=1

print(a)






