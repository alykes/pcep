lambda_func = lambda i: i * 2
initial_list = [1, 2, 3, 4, 5]

map(lambda_func, initial_list)  # This will create the iterator, which is a special kind of object and return the address in memory.

map_result = map(lambda_func, initial_list)
print(next(map_result))     # If there are no more values to return, you will get a StopIteration error.

# It is much better to use an iterator in a for loop
for element in map_result:
    print(element, end=', ')

# An other alternative is to create a list
print(list(map_result))




#Therefore the code then becomes
lambda_func = lambda i: i * 2
initial_list = [1, 2, 3, 4, 5]
map_result = map(lambda_func, initial_list)
print(list(map_result))

# The code directly above can further be simplified into the following piece of code
print(list(map(lambda i: i * 2, [1, 2, 3, 4, 5])))