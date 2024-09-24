class A:
    def show(self):
        print("In class A and show method")

class B(A):
    def show(self):
        print("inside class B ")

a1 = A()
a1.show()

b1 = B()
b1.show()