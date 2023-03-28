# boolean operators
# AND
# OR
# NOT

user_age = int(input('Enter your age? '))
user_country = input('Which country are you from? ')

if user_age < 25 and user_country == 'UK':
    print('You can go straight to Laganas for a lashing!')
else:
    print('Well...ok, you can still go to Laganas.')
    print('Just watch out for malakas!')

# Python checks the condition on the left first
if user_country == 'Greece' or user_country == 'Italy':
    print('Nice one, you are from an awesome place!')
else:
    print('Oh,', user_country, 'can be a nice place')

# negates boolean value
if not user_country == 'Greece':
    print('You aren\'t from Greece malaka!')
else:
    print('Ela mesa barba!')

# Complex conditions, priority :--> NOT AND then OR 
if not user_country =='Greece' and user_age < 25 or \
    user_country == 'Greece' and user_age < 23:
    print('Bravo')
else:
    print('Pooshto re')


days = int(input('How many days ago have you purchased the item? '))
used = input('Have you used the item at all [y/n]? ')
broken = input('Has the item broken down on its own [y/n]? ')

if (not used == 'y' and days <= 10) or broken == 'y':
    print('You can get a refund.')
else:
    print('You cannot get a refund.')