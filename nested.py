def mod2plus5(x1, x2, x3):

    # returns the remainder plus 5 of three values.

    def inner(x):
        # returs the remainder plus 5 of a value.
        return x % 2 + 5
    
    return (inner(x1), inner(x2), inner(x3))

print(mod2plus5(15, 15, 15))

def raise_val(n):
    # return the inner function

    def inner(x):
        # raise x to the power of n
        raised = x ** n
        return raised 
    
    return inner 

square = raise_val(2)
cube = raise_val(3)
print(square(9.23), cube(24892.3))

