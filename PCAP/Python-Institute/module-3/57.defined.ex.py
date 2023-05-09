# An example of creating a custom exception type.
# Notice that it is derived directly from the ZeroDivisionError class and will therefore function in a similar manner
# NOTE that the branch ZeroDivisionError will be used if it is placed in front of MyZeroDivisionError as it is derived from that more general class.

class MyZeroDivisionError(ZeroDivisionError):	
    pass


def do_the_division(mine):
    if mine:
        raise MyZeroDivisionError("some worse news")
    else:		
        raise ZeroDivisionError("some bad news")


for mode in [False, True]:
    try:
        do_the_division(mode)
    except ZeroDivisionError:
        print('Division by zero')

for mode in [False, True]:
    try:
        do_the_division(mode)
    except MyZeroDivisionError:
        print('My division by zero')
    except ZeroDivisionError:
        print('Original division by zero')
