#----------------------------------------------
# ArithmeticError
x = 1 / 0

#----------------------------------------------
# # AssertionError
from math import tan, radians
angle = int(input('Enter integral angle in degrees: '))

# We must be sure that angle != 90 + k * 180
assert angle % 180 != 90
print(tan(radians(angle)))


#----------------------------------------------
# The code shows an extravagant way
# of leaving the loop.
the_list = [1, 2, 3, 4, 5]
ix = 0
do_it = True

while do_it:
    try:
        print(the_list[ix])
        ix += 1
    except IndexError:
        do_it = False

print('Done')

#----------------------------------------------
# KeyboardInterrupt
# This code cannot be terminated
# by pressing Ctrl-C.
from time import sleep

seconds = 0

while True:
    if seconds == 15:
        break
    try:
        print(seconds)
        seconds += 1
        sleep(1)
    except KeyboardInterrupt:
        print("Don't do that!")

print("Phew, you made it out because the timer stopped!")

#----------------------------------------------
# This code causes the MemoryError exception.
# Warning: executing this code may affect your OS.
# Don't run it in production environments!
string = 'x'
try:
    while True:
        string = string + string
        print(len(string))
except MemoryError:
    print('This is not funny!')

#----------------------------------------------
# This code causes the MemoryError exception.
# WARNING: executing this code may affect your OS.
# Don't run it in production environments!

string = 'x'
try:
    while True:
        string = string + string
        print(len(string))
except MemoryError:
    print('This is not funny!')


#----------------------------------------------
# OverflowError
# The code prints subsequent
# values of exp(k), k = 1, 2, 4, 8, 16, ...
from math import exp

ex = 1

try:
    while True:
        print(exp(ex))
        ex *= 2
except OverflowError:
    print('The number is too big.')


#----------------------------------------------
# ImportError
# One of these imports will fail - which one?
try:
    import math
    import time
    import abracadabra      # This is the problem statement

except:
    print('One of your imports has failed.')

#----------------------------------------------
# KeyError
# How to abuse the dictionary
# and how to deal with it?

dictionary = { 'a': 'b', 'b': 'c', 'c': 'd' }
ch = 'a'

try:
    while True:
        ch = dictionary[ch]
        print(ch)
except KeyError:
    print('No such key:', ch)


