# This code has the same functionality as the code in 11.lambda.py 
# but uses a lambda function instead of a generic function

def print_function(args, fun):
    for x in args:
        print('f(', x,')=', fun(x), sep='')

print_function([x for x in range(-2, 3)], lambda x: 2 * x**2 - 4 * x + 2)   # The section that starts with lambda is a replacement for the poly() function that was seen in 11.lambda.py

