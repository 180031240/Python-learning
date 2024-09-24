def update(x): #here, x is a formal argument
    x = 8
    print("x is ", x)
    print("id(x)", id(x))


a = 10
print("a before updating", a)
print("id(a)", id(a))
update(a) # here, a is an actual argument
print("a after update is ", a)

"""There is no call by reference or value in python instead when the address is changed inside it means that a and x are different
a -> 10
x -> 8
"""