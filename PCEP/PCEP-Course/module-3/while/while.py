# While loops

# while condition():
#     do_something()
#     do_something2()

counter = 1
while counter < 11:
    print(counter)
    counter += 1
print('Done hombre!')


secret_number = 14
print('''
============================
=== Number Guessing Game ===
============================
''')
user_guess = int(input('Enter a number between 0 and 20: '))
while user_guess != secret_number:
    print('Wrong!')
    user_guess = int(input('Enter a number between 0 and 20: '))
print('!!Bravo!!')