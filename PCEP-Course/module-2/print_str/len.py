len('Hello!')
#result = 6

print('Hello, World!')
print('Python Speaking!')
#result
# Hello, World!
# Python Speaking

print('Hello, World!', end='.') # end is a keyword argument and is optional, they have a default value
print('Python Speaking!')
#result
# Hello, World!.Python Speaking

first_name = 'John'
print('Your first name is', first_name, 'Welcome!', sep='-', end='=')
#result
# Your first name is-John-Welcome!=

#Note that the sep and end arguments MUST ALWAYS BE AT THE END!