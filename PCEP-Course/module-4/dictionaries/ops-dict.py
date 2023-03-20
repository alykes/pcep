# Initialising a dictionary
grades = {}

# Adding key values pairs
grades['Ango'] = 'A+'
grades['Belinda'] = 'D-'
grades['John'] = 'B+'
grades['Malaka'] = 'F'

print(grades)

# Updating a key value pair can be achieved in two ways
# Simply assign a value again to an existing key
grades['Belinda'] = 'C+'

# The alternate method is to use the update method
grades.update({'John': 'A-'})

print(grades)

# To check the length of a dictionary, use the len function
len(grades)

if 'Ango' in grades:
    print('The little rascal is there alright!')
    print('Ango has the following grade:', grades['Ango'])


# Deleting key value pairs
del grades['John']
print(grades)

# Accessing the keys and values
for element in grades:
    print(element) # this prints the key

for element in grades.keys():
    print(element) # this prints the key

for element in grades.values():
    print(element) # this prints the value

for person, grade in grades.items(): #Two control variables
    print(person, 'has the grade of:', grade)