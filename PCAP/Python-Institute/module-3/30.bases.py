# An example of how to get the superclass of a class.
# Notice that we need to use the __name__ property to make it easier to read.
class SuperOne:
    pass


class SuperTwo:
    pass


class Sub(SuperOne, SuperTwo):
    pass


def printBases(cls):
    print('( ', end='')

    for x in cls.__bases__:
        print(x.__name__, end=' ')
    print(')')


printBases(SuperOne)        # object
printBases(SuperTwo)        # object
printBases(Sub)             # SuperOne SuperTwo

print(SuperOne.__bases__)   # (<class 'object'>,)
print(SuperTwo.__bases__)   # (<class 'object'>,)
print(Sub.__bases__)        # (<class '__main__.SuperOne'>, <class '__main__.SuperTwo'>)

