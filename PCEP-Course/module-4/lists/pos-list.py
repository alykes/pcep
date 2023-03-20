first = 10
second = 20

# To swap the values of variables, you can use the syntax below
first, second = second, first

# Swapping elements in a list
top_cities = ['New York City', 'Los Angeles', 'Chicago', 'Houston', 'Phoenix']

top_cities[0], top_cities[4] = top_cities[4], top_cities[0]
print(top_cities)

# Sorting a list of strings
# Will just print the sorted list without sorting it
print(sorted(top_cities))

top_cities.sort()
print(top_cities)

top_cities.sort(reverse=True)
print(top_cities)

# Sorting a list of numerals
random_numbers = [2, 5, 0, -3, 4]
print(top_cities)
print(sorted(top_cities))
top_cities.sort(reverse=True)