# An example of a good contender for conversion to a lambda function.
# The print_function() takes two arguments, a list and a function.
# To convert this into a lambda function, you would need to replace the poly() function with a lambda function. 

def print_function(args, fun):
    for x in args:
        print('f(', x,')=', fun(x), sep='')


def poly(x):
    return 2 * x**2 - 4 * x + 2


print_function([x for x in range(-2, 3)], poly)

# Result
# f(-2)=18
# f(-1)=8
# f(0)=2
# f(1)=0
# f(2)=2