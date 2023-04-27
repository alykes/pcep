#!/usr/bin/env python3                              # This is a shebang, shabang, hashbang, poundbang or hashpling. Tells the OS how to execute the contents of the file.
""" module.py - an example of a Python module """   # This is a doc-string, basically a multi-line comment.

__counter = 0                   # This is a "private" variable


def suml(the_list):
    global __counter
    __counter += 1

    the_sum = 0
    for element in the_list:
        the_sum += element
    return the_sum


def prodl(the_list):
    global __counter    
    __counter += 1

    prod = 1
    for element in the_list:
        prod *= element
    return prod


if __name__ == "__main__":
    print("I prefer to be a module, but I can do some tests for you.")

    my_list = [i + 1 for i in range(5)]

    print(suml(my_list) == 15)
    print(prodl(my_list) == 120)

