# Integers
# Will check if the values are the same
first_num = 5
second_num = 5
print(first_num is second_num)  # True

third_num = 5
fourth_num = 2
fourth_num += 3
print(third_num is fourth_num)  # True

num_1 = 2
num_2 = 50
print(num_1 is num_2)           # False

# Strings
# Python does some funny business in the backend and if two string contents contain the same contents, then they are the same object. Strings are immutable.
# If you try to change the string, Python will create a new one.
string_1 = 'Ango'
string_2 = 'Ango'
print(string_1 is string_2)     # True as they are the same string, created the same way and Python can therefore point to the same object

string_3 = 'Ango'
string_4 = 'Ang'
string_4 += 'o'

print('string_3:', string_3, 'string_4:', string_4)
print(string_3 is string_4)     # False!!!! Even though they are now the same string, they are different objects!
print(string_3 == string_4)     # True because now, we are just comparing the string contents.