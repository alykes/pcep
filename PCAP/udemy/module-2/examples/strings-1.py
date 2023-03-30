# testing the values of strings

print('lower'.islower())        # True
print('lower!!123'.islower())   # True - even though it contains other characters (including numbers)

print('UPPER'.isupper())        # True
print('UPPER!!123'.isupper())   # True - even though it contains other characters (including numbers)

print('12345'.isdigit())        # True
print('12345!!'.isdigit())      # False

print('abc'.isalpha())          # True
print('abc!!'.isalpha())        # False

print('123abc'.isalnum())       # True
print('123abc!!'.isalnum())     # False

print(''.isspace())             # False
print(' '.isspace())            # True
print('\t'.isspace())           # True
print('\n'.isspace())           # True