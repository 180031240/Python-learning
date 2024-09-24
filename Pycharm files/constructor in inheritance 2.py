#Contructor in inheritance
class A: #Super class
    def __init__(self):
        print("In init method in class A")
    def feature1(self):
        print("Feature 1 - A is working")
    def feature2(self):
        print("Feature 2 is working")


class C:
    def __init__(self):
        print("In init method in class C")

    def feature1(self):
        print("Feature 1 - C is working")
    def feature4(self):
        print("Feature 6 is working")


class B(A,C):
    #To call init method of parent class, which one will it call? MRO comes into picture.
    """MRO - Method resolution order. It is from left to right, so we get A"""
    def __init__(self):
        super().__init__()
        print("In init method in class B")


    def feature3(self):
        print("Feature 3 is working")
    def feature4(self):
        print("Feature 4 is working")

    def festival(self):
        print("In festival method of class B")
        super().feature4()



b1 = B()

b1.feature1() # Due to MRO - Method Resolution order
b1.festival()
