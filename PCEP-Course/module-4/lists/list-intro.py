# Collections or container data types

# lists - multiple values of the same type
# tuples
# dictionaries

city_1 = 'New York City'
city_2 = 'Los Angeles'
city_3 = 'Chicago'
city_4 = 'Houston'
city_5 = 'Phoenix'

# better to use a list

empty_list = []

top_cities = ['New York City', 'Los Angeles', 'Chicago', 'Houston', 'Phoenix']
print(top_cities) # Prints the whole list

# Indexing
print(top_cities[0]) # returns a string of first element
print(top_cities[4])

print(top_cities[-1]) # returns a string of the last element
print(top_cities[-2]) # returns a string of the second last element
print(top_cities[-5]) # In this case will give the first element as a string

# Slicing
print(top_cities[0:2]) # returns a list of elements 0 and 1, it doesn't return element 2!

print(top_cities[2:]) # returns a list of elements starting at 2 and going to the end of the list

print(top_cities[:3]) # returns a list of elements starting at 0 and going to element 2, does not return element 3

print(top_cities[:]) # returns the entire list

print(top_cities[10:15]) # this does not return an out of range error!