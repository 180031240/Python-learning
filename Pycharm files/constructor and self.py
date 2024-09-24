"""Everytime an object is created, it is alocated to a new space
Size of object --  depends on number of variables and size of each variable
who allocates size to object - constructor
Constructors are used to initialise the objects when they are created and naming is always __init__
self is a keyword and it acts as navigator to object Comparing Objects
In java, name of constructor should be same as name of class but in python, name of constructor is __init__"""

class Person:
    def __init__(self):
        self.name = 'Girija'
        self.age = 14

    def update(self):
        self.age = 23

    def compare(self, object):
        if self.age == object.age:
            print("same")
        else:
            print("different")


person1 = Person()
print("Printing person1 --> ", person1.age, person1.name)
person1.update()
print("Printing person1 after update", person1.age, person1.name)

person2 = Person()
person2.age = 55
print("printing person 2 -->", person2.age, person2.name)

print("Comparing person1 and person2")

person1.compare(person2)

person3 = Person()
person3.age = 23

print("Ages of person1 and person 3", person1.age, person3.age)
print("Comparing between person 3 and person 1")
person3.compare(person1)
