"""You can create object of inner class insidethe outer class or you can create object of inner class outside the outer class provided you use outerclass name to call it"""

class Student:

    def __init__(self, name, age):
        self.name = name
        self.age = age
        #creating object inside the outer class which is here student
        #The below line is important because we have created the object of inner class like initialised
        self.lap = self.Laptop()

    def show(self):
        print(self.name, self.age)
        #self.lap.show()

    class Laptop:

        def __init__(self):
            self.brand = 'HP'
            self.cpu = 'i7'
            self.ram = 16

        def show(self):
            print(self.brand, self.cpu, self.ram)


#using the laptop object which is lap outside the class
s1 = Student('Sreeya', 25)
print(s1.lap.brand)

lap1 = s1.lap
print(lap1.ram)

lap1.show()