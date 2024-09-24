"""
Class methods, static methods, instance methods
In case of variables, class and static variables are same

"""

class Student:
    school = 'JP Morgan'

    def __init__(self,m1,m2,m3):
        self.m1 = m1
        self.m2 = m2
        self.m3 = m3

    def avg(self): #instance method
        return (self.m1+self.m2+self.m3)/3

    #if you are working with instances, we have to use self else we will use class keyword
    @classmethod #decorator
    def get_school(cls):
        return "School is " + cls.school


    @staticmethod #decorator
    def info():#It is not written to any class or any method to pass cls or self in argument part
        print("This is a student class inside a static method")


print(Student.get_school())


s1 = Student(23,24,25)
print("printing s1 and it's avg")
print(s1.m1, s1.m2, s1.m3, s1.avg())

Student.info()
"""Instance method are two types - 
   Accesor and mutator methods
   Accesor methods - When we are only fetching the values of the instance variables, we use accesor methods
   Mutator methods - To modify the values if instance variables, we use mutators
   
   def get_m1(self):
        return self.m1
   def set_m1(self,value):
        self.m1 = value
        
        
When we want a method which doesn't have anything to do with class variables, which doesn't have anything to do with instance variables, we use a static method"""
