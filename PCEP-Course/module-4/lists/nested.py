numbers = [1, 2, 3]
countries = ['Greece', 'Australia', 'Norway', 'England']
mixed = [1, 'Greece', 2, 'Australia', 3, 'Norway', 4, 'England'] #This is not recommended all elements should be the same type

# Nested List aka multi-dimensional list
cells = [['A1', 'A2', 'A3'], ['B1', 'B2', 'B3']]

#Accessing the list elements
cells[0] # returns the first list ['A1', 'A2', 'A3']
cells[0][0] # returns 'A1'
cells[1][2] #returns 'B3'

# To access each list as an element
for x in cells:
    print('Element:', x) # returns two lists

# To access each element within each list
for x in cells:
    for y in x:
        print('Element:', y)

# to better visualise the above
table = [['A1', 'A2', 'A3'], ['B1', 'B2', 'B3']]
for row in table:
    for cell in row:
        print('Element:', cell)

# To print it like an actual table
for row in table:
    for cell in row:
        print(cell, '', end='') # or you can use - print(cell, end=' ') 
    print()

#Nested list comprehension
# For a single element
table_comp = [i for i in range(1,6)]

table_comp = [[i for i in range(1,6)] for j in range(4)]
print(table_comp)