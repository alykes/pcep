# An example of raising an exception in your code
def bad_fun(n):
    print("Inside the function")
    raise ZeroDivisionError

try:
    bad_fun(0)
except ArithmeticError:
    print("What happened? An error?")

print("THE END.")


# The raise keyword can also be used by itself to raise a general exception
# This can ONLY be used in the except branch!
# This is also a good example of how to split the exception handling
def bad_fun_general(n):
    try:
        return n / 0
    except:
        print("I did it again!")    # This will print
        raise           # This means that you can also handle the exception outside this function, in the try..except block below!


try:
    bad_fun_general(0)
except ArithmeticError:
    print("I see!")     # This will also print

print("THE END.")       # This will rpint

