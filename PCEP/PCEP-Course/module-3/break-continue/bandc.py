# breaks out of the whole loop
while True:
    name = input('Enter your name or type EXIT to end the program: ')
    if (name == 'EXIT'):
        break
    print('Yiasou', name, ', how are you doing?')

# continues the loop but stops processing the current loop
for i in range(1, 21):
    if i % 5 == 0:
        continue
    print('This number isn\'t divisible by 5: ', i)