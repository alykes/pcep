# A tuple is immutable, you can't change the elements of a tuple once it's defined

# len operations work fine on a tuple
user_data = ('Chad', 'American', 1969)
print(len(user_data)) # returns 3

# in and not in work as well
if 'American' in user_data:
    print('It\'s an American!')

# iterating through a tuple
for value in user_data:
    print(value)

# Add
user_data_2 = ('Chad', 'American', 1969) + ('male', 'Vietnam Vet')
print(user_data_2)

# Multiply
numerals = (0, 1, 2, 3) * 5
print(numerals)

# When should you use list vs tuple
# List many values of the same data type, eg, male_name, city_temps
# Tuples are used for values of different types that are somehow related, together they form a structure, eg, user_data

# tuples perform operations quicker
