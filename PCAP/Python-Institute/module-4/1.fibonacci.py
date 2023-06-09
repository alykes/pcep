# This is the "objective" version of the fibonacci number generator based on the direct iterator protocol implementation!
#
# The first two Fibonacci numbers are equal to 1;
# any other Fibonacci number is the sum of the two previous ones (e.g., Fib3 = 2, Fib4 = 3, Fib5 = 5, and so on)

class Fib:
    def __init__(self, nn):
        print("__init__")
        self.__n = nn
        self.__i = 0
        self.__p1 = self.__p2 = 1

    def __iter__(self):
        print("__iter__")
        return self

    def __next__(self):
        print("__next__")				
        self.__i += 1
        if self.__i > self.__n:
            raise StopIteration
        if self.__i in [1, 2]:
            return 1
        ret = self.__p1 + self.__p2
        self.__p1, self.__p2 = self.__p2, ret
        return ret

# fibo = Fib(10)        # This will also work
# for value in fibo:
#     print(value)

for i in Fib(10):
    print(i)

# Result
# __init__
# __iter__
# __next__
# 1
# __next__
# 1
# __next__
# 2
# __next__
# 3
# __next__
# 5
# __next__
# 8
# __next__
# 13
# __next__
# 21
# __next__
# 34
# __next__
# 55
# __next__