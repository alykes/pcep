for i in range(11):
    pass # requires at least one instruction in the loop, pass is like a placeholder

for a in range(1, 6):
    for b in range (1, 6):
        print(a, 'x', b, '=', a * b)
    print('---')

# Rarely used, the else branch is always executed at least once (unless there is a break statement)
i = 5
while i < 5:
    print(i)
    i += 1
else:
    print('else', i)

# Coding exercise
guess = int(input('When was Python 1.0 released? '))
release = 1994

while guess != release:
    if guess > release:
        print('It was earlier than that!')
    elif guess < release:
        print('It was later than that!')
    guess = int(input('When was Python 1.0 released? '))
print('Correct!')

# Same functionality as above but does it differently
while True:
    answer = int(input('When was Python 1.0 released? '))
    if answer > 1994:
        print('It was earlier than that!')
    elif answer < 1994:
        print('It was later than that!')
    else:
        print('Correct!')
        break
