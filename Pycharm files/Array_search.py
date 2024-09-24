from array import *

arr = array('i', [])

arr_size = int(input("Please enter the size of the array "))
for i in range(arr_size):
    arr.append( int(input("Enter the element of array ")) )

print ("The array is: ", arr)


#Searching manually

Target_num = int(input("Enter the number to be searched "))

for i in range(arr_size):
    if(arr[i] == Target_num):
        print("Number is found at ",i,"index.")
        break
else:
    print("Number not found.")

#Searching an element with a method

print (arr.index(Target_num))
