class Computer:
    def __init__(self,cpu,ram):#Passing three args like object, value, ram -- com1, cpu, ram
        #Not mere passing arguments is efficient but you have to assign it to your object.
        self.cpu = cpu
        self.ram = ram


    def config(self):
        print("Inside Computer class, config method, i5, 16gb, 1TB")

com1 = Computer('i3', 14)
com2 = Computer('i2', 16)


com3 = Computer('i3', 16)

print("Comp1",com1.config())
Computer.config(com1)
com2.config()