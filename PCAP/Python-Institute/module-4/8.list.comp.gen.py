# List comprehension vs generators
# This is a comparison of a tradtional list comprehension as well as one using a generator
# The only difference is that the generator is using () instead of []
the_list = [1 if x % 2 == 0 else 0 for x in range(10)]
the_generator = (1 if x % 2 == 0 else 0 for x in range(10))

for v in the_list:
    print(v, end=" ")
print()

for v in the_generator:
    print(v, end=" ")
print()
print(the_list)                 # Will print the list with all the elements
print(the_generator)            # Will print the reference to the object

# Also, you can tell which one is a generator by trying to retrieve the length of the list
print(len(the_list))
# print(len(the_generator))     # Will raise a TypeError exception "TypeError: object of type 'generator' has no len()"


# This is the standard way to do list comprehension with a conditional statement
simple_list = [1 if x % 2 == 0 else 0 for x in range(10)]

print(simple_list)              # Will print the list with all the elements

