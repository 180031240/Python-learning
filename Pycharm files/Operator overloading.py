class Student:
    def __init__(self,m1,m2):
        self.m1 = m1
        self.m2 = m2
    def __add__(self,other):

        m1 = self.m1 + other.m1
        m2 = self.m2 + other.m2

        sum = Student(m1, m2)

        return sum

    def __gt__(self,other):
        s1 = self.m1 + self.m2
        s2 = other.m1 + other.m2

        if s1 > s2:
            return True
        else:
            return False

    def __str__(self):
        return '{} {}'.format(self.m1, self.m2)

s1 = Student(1,2)
s2 = Student(3,4)


if s1 > s2:
    print("s1 wins")
else:
    print("s2 wins")



#Here, we don't know if s1 + s2 are added. like when we add integers, it calls add method because they belong to int class. here, our
#student class is not having add method,, so, lets write it. It's like overloading the operator, we can change the definition of it. actually
#__add__ is a predefined method for +

sum = s1 + s2

print(sum.m2)

#We dont want to print the address of s1 but the values of s1. but print s1 gives address of object
a = 66
print(a)
print(a.__str__())
print(s1.__str__())
