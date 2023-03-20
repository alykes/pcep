# Greater than and equals
user_age = int(input('What is your age? '))
if user_age > 30:
    print('You are over 30 years old.')
elif user_age == 30:
    print('Ding! Ding! Ding! You are exactly 30 years old!')
else:
    print('You are less than 30 years old.')

# Not equals
password = input('What is the secret password? ')
if password != '--secret':
    print('## Entry denied!')
else:
    print('## Entry granted!')

# True / False operators
if True:
    print('Condition Met')
if False:
    print('Condition never met!')
if 2 == 2.0: # Python converts the integer into a float
    print('Yep, they are equal.')