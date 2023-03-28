## Any functions that doesn't return anything will return None as default

print_return = print('Yiasas Malakes!')
print(print_return) # result None - null or no value as all, not the same as an empty string


# Testing for None
x = None
if x:
    print('None is True')
elif x is False:
    print('None is False')
else:
    print('None is not True or False. None is just None')

# Further tests
y = None
if y is None:
    print('y is None using the is operator')
if y == None:
    print('y is None using the == operator')

