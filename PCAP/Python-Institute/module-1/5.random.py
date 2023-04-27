from random import randrange, randint

# generates 10 numbers in the range 1 to 10(inclusive)
for i in range(10):
    print(randint(1, 10), end=',')

# 2 is not inclusive
print(randrange(2), end=' ')
print(randrange(0, 2), end=' ')
print(randrange(0, 2, 1), end=' ')

# both the left and right arguments are inclusive
print(randint(0, 1))