"""You can create object of inner class insidethe outer class or you can create object of inner class outside the outer class provided you use outerclass name to call it"""

class Student:

    def __init__(self, name, age):
        self.name = name
        self.age = age

    def show(self):
        print(self.name, self.age)

    class Laptop:

        def __init__(self):
            self.brand = 'HP'
            self.cpu = 'i7'
            self.ram = 16

        def show(self):
            print(self.brand, self.cpu, self.ram)


s1 = Student('Girija', 23)
s1.show()

s2 = Student.Laptop()
print("showing s2")
s2.show()