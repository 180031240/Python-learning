#Method overloading - we are not doing it directly bcz it doesnt support in python
class Abc:
    def __init__(self,m1,m2):
        self.m1 = m1
        self.m2 = m2
    def sum(self,a=None,b=None,c=None):
        if a!=None and b!=None and c!=None:
            return a+b+c
        elif a!=None and b!=None and c==None:
            return a+b
        else:
            return a

a = Abc(21,22)
print(a.sum(1, 3))

