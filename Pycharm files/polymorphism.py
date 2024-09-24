"""Polymorphism - One can take many forms
We can implement it in Duck typing
                        Operator overloading
                        Method overloading
                        Method overriding"""

"""DUCK TYPING """

class Laptop:
     def code(self,ide):
         ide.execute()
         #Here, we don't know what type of class does ide belongs to, so, we are creating our own class

class PyCharm:
    def execute(self):
        print("Inside Pycharm class and execute method")

class MyEditor:
    def execute(self):
        print("Inside MyEditor class and execute method")

#calling code now
lap1 = Laptop()
#lap1.code() #Here, we have to pass an argument for ide because in Laptop class, code method takes an argument. so, ide = Pycharm()
#It doesn't matter what type of object (Here, it is ide) you are using but important is execute method - this is duck typing
ide = MyEditor()
#ide = PyCharm()
lap1.code(ide)