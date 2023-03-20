invited_guests = ['Fabio','Stavros','Aphrodite','Ariadne','Gaia']

name = input('What is your name? ')
if name in invited_guests: # can also use "not in"
    print ('Welcome!')
else:
    print("You aren't on the list")