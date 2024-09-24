class Computer:

    def __init__(self, cpu, ram):
        self.cpu = cpu
        self.ram = ram

    def config(self):
        print("CPU and Ram are", self.cpu, self.ram)

# <Objectname> = <Class name>(argument1, argument2, ..)


print("Com1")
com1 = Computer('i5', 16)
com1.config()

print("Com2")
com2 = Computer('i7', 24)


com2.config()


