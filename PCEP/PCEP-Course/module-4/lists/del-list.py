top_cities = ['New York City', 'Los Angeles', 'Singapore', 'Chicago', 'Houston', 'Phoenix']

# Note: del is not a function call as it doesn't take any parameters

# Deleting a single element in a list
del top_cities[2] # will delete element 2 only
print(top_cities)

# Deleting elements using slicing
del top_cities[3:] # will delete element 3 to the end of the list
print(top_cities)

del top_cities[:] # will delete all elements in the list and return an empty list
print(top_cities)

del top_cities # This will delete the list itself