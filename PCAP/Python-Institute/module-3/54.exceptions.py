# An example of an exception as a class
try:
    i = int("Hello!")
except Exception as e:      # catches the exception object and places the value in e
    print(e)
    print(e.__str__())

# Result:
# invalid literal for int() with base 10: 'Hello!'
# invalid literal for int() with base 10: 'Hello!'

