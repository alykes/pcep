# String 
favourite_band = 'Northlane'
print(favourite_band[5]) # returns l
print(favourite_band[:5])

#You can't directly replace a string character
favourite_band[0] = 'S' # This will not work

# Strings have their own methods
text = 'upper room'
text_upper = text.upper()
print(text_upper)

# isNumeric() to check if a value is a numeral
# islower()
# isupper()
# isspace()
# etc etc

user_number = input('Please enter a number: ')

if user_number.isnumeric():
    print('Thanks for entering a number!')
else:
    print('Sorry dude,', user_number, 'doesn\'t look like a number to me!')