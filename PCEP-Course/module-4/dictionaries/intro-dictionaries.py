# Collections used to store key value pairs, created with {}, 
# each key must be unique. 
# The latest defined value is returned if there are duplicates
# dictionaries are one way
# Keys can be any immutable data type
# Lists can't be keys!
# They are ordered collections by default

# An example of the structure below
emails = {
    'Ango': 'ango@gmail.com',
    'Mango': 'mango@gmail.com',
    'Tango': 'tango@gmail.com'
}
# This is used to retrieve the value stored in the key 'Ango'
print(emails['Ango'])


spanish_animals = {
    'dog': 'el perro',
    'cat': 'el gato',
    'horse': 'el caballo',
    'bird': 'el pajaro'
}
print(spanish_animals['dog'])

