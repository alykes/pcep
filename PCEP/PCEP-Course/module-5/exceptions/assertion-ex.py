# assumptions in our program that should always be true
# Used for:
# used for debugging/testing code
# documenting your code
# Not used for:
# don't use it for validating user input
# they aren't a handling error tool

def calculate_inverse(number):
    assert (number != 0), 'Got 0 as a number!'
    return 1/number

calculate_inverse(2)
calculate_inverse(0) # Generates an assertion error
# Traceback (most recent call last):
#   File "<stdin>", line 1, in <module>
#   File "<stdin>", line 2, in calculate_inverse
# AssertionError: Got 0 as a number!