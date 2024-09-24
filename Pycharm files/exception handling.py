a = 5
b = 2

try:
    print(a/b)
    print("Handle opened")
    k = int(input("Please enter a number "))

except ZeroDivisionError as e:
    print("You can not divide the number by zero - ",e)

except ValueError as e:
    print("Invalid input")

except Exception as e:
    #this exception block handles all the exceptions
    print("Hey, we can not perform the calculation because of this error: ", e)

finally:

    #this can be executed though the try or except block executes
    #This block is executed irrespective of seeing the error
    print("Resource closed")
