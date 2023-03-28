top_cities = ['New York City', 'Los Angeles', 'Chicago', 'Houston', 'Phoenix']

for city in top_cities:
    print('Current City:', city)

# To iterate through the list and also have access to the index
for city_index in range(len(top_cities)): # range generates the following list of integers 0 1 2 3 4
    print('City number', city_index, 'is :', top_cities[city_index])


# Performing operations on lists, summing numbers
spendings = [32.45, 18.65, 23.45, 78.32, 5.23]
sum = 0.0
for spending in spendings:
    sum += spending
print('Money spent:', sum)



# Coding exercise
spendings = [1346.0, 987.50, 1734.40, 2567.0, 3271.45, 2500.0, 2130.0, 2510.30, 2987.34, 3120.50, 4069.78, 1000.0]
low = 0
normal = 0
high = 0

for spending in spendings:
    if spending < 1000:
        low += 1
    elif (spending >= 1000 and spending <= 2500): # can also be replaced with "elif spending <= 2500" but isn't as clear to read
        normal += 1
    else:
        high += 1

print('Numbers of months with low spendings: ' + str(low) + ', normal spendings: ' + str(normal) + ', high spendings: ' + str(high) + '.')