#      Multiple inhheritance
class A: #Super class
    def feature1(self):
        print("Feature 1 is working")
    def feature2(self):
        print("Feature 2 is working")

class B():
    def feature3(self):
        print("Feature 3 is working")
    def feature4(self):
        print("Feature 4 is working")

class C(A,B): # C is inheriting from both A and B
    def feature5(self):
        print("Feature 5 is working")


a1 = A()

a1.feature1()
a1.feature2()



c1 = C()
print("Printing feature 1 in class C")
c1.feature1()
