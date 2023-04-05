def make_multiply_closure(x):

    def multiply(y):
        return x * y
    
    return multiply



multiply_5 = make_multiply_closure(5)       # This is supplied to the first (outer) function
multiply_12= make_multiply_closure(12)      # This is supplied to the first (outer) function


print(multiply_5(10))                       # This is supplied to the inner function
print(multiply_5(20))                       # This is supplied to the inner function


print(multiply_12(10))                      # This is supplied to the inner function
print(multiply_12(20))                      # This is supplied to the inner function