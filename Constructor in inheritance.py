#Contructor in inheritance
class A: #Super class
    def __init__(self):
        print("In init method in class A")
    def feature1(self):
        print("Feature 1 is working")
    def feature2(self):
        print("Feature 2 is working")

class B(A):
    def __init__(self):
        print("In init method in class B")

    def feature3(self):
        print("Feature 3 is working")
    def feature4(self):
        print("Feature 4 is working")


class C(A):
    def __init__(self):
        #We are calling init method of class A
        print("In init method of class C -- > ", end="")
        super().__init__()#this init will call init of C, from it, the call jumps to init of A and again comes to init of C
        print("Printing after calling init of super class")

    def feature3(self):
        print("Feature 5 is working")
    def feature4(self):
        print("Feature 6 is working")
a1 = A()
#It calls the constructor of A if class B don't have it's own init menthod
#If class B has it's own init method, class B will use it's init method only by default
b1 = B()

#When you want to call the init method of class A from class B, we use super keyword. (Class B is child of class A)

c1 = C()
