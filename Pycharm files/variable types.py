"""
 Instance variables
 There are different for different objects
 Class variable or static variables
 These are defined outside the init method and not in other methods of the class. There are defined in the class
 Namespace - The space where you create and store object/variable
        - class namespace -- where we store all class variables
        - Object/insant namespace -- where all instance variables are created.

 """

class Car:
    wheels = 4 #Class namespace, wheels is a class/static variable

    def __init__(self):
        self.company = 'TATA' #instant namespace
        self.milage = 10        #instant namespace

c1 = Car()
c2 = Car()

c1.milage = 10

print(c1.company, c1.milage, c1.wheels)

print("Changing wheels to 5")
Car.wheels = 5

print(c2.company, c2.milage, c2.wheels)