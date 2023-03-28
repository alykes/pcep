# IndentationError
# ValueError

try:
    value = int(input('Enter an integer: '))
    print('The inverse of', value, 'is', 1/value)
except ValueError:
    print('You did not provide a positive integer!')
except ZeroDivisionError:
    print('You can\'t divide by zero!')
except:
    print('Something weird happened...#@?!')
finally:
    print('This finally block always runs at the end, no matter what!!')


# You can raise a SyntaxError and catch it, but you can't code Python to catch a genuine syntax error
try:
  raise SyntaxError
except:
  print('Got it!') # SyntaxError is caught here