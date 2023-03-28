# Python has over 60 exception types

# BaseException
# |
#  ````Exception````SystemExit````KeyboardInterupt````
#        |
#         ````Arthimetic Error````Lookup Error```TypeError````ValueError
#                |                      |
#                 ``ZeroDivisionError   |````IndexError
#                                        ````KeyError

# SystemExit - raised when we call a special method sys.exit() it terminates the program manually
import sys
user_name = input('What is your name? ')
if user_name == '':
    print("re, it's empty! Shutting up shop.")
    sys.exit()
print('Yiasou', user_name)


# KeyboardInterrupt - when you hit Ctrl-D for example
while True:
    print('I\'m freeeeeee!!!')
# If you mash Ctrl-C you will get a Keyboardinterrupt exception

# Exception - serve as base templates, similar to BaseException (used for internal Python exceptions)
# Exceptions can be used for your own customised exception types

# TypeError is when you try to perform an operation on the wrong data type
age = input('What is your age? ')
print(age + 10)

# ValueError is when you expect a certain data type but have another one attempting to be assigned to a different type
age = int(input('What is your age? ')) # User enters 'a' 