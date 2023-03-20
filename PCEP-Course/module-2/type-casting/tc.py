# Looking at the following functions - float() int() str()

# float type-casting
height_cm = float(input('Height converter: enter your height in cm: '))
print('Your height in feet is:', height_cm / 30.48 )

height_cm = float(input('Height converter: enter your height in cm: '))
float_height_cm = float(height_cm)
print('Your height in feet is:', float_height_cm / 30.48 )

hours_worked = input('How many hours did you work last month? ')
hourly_rate = input('What is your hourly rate? ')
income = float(hours_worked) * float(hourly_rate)
print('Last month, you earned', income, 'dollars')

# int type-casting
year_born = int(input('What year were you born? '))
print('in 2100, you will be', 2100 - year_born, 'years old, provided you live this long!')

# str type-casting
temp_c = input('Enter the temperature today in Celsius degrees: ')
temp_f = float(temp_c) * 1.8 +32
temp_statement = str(temp_c) + ' degrees Celsius equals ' + str(temp_f) + ' degrees Fahrenheit.'
print(temp_statement)

