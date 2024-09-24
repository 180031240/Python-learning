#Using decorators, we can add features to existing functions without touching them. You can change the behaviour of a function during the compile time itself

import Arguments

print("Name in decorators ",__name__)

def div(a,b):
    return a/b

def decorator_div(function):
    def inner(a,b):
        if(a<b):
            a, b = b, a

        return function(a,b)

    return inner

div = decorator_div(div)

print(div(2,4))


