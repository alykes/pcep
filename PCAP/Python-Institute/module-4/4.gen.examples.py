# A basic generator
def powers_of_2(n):
    power = 1
    for i in range(n):
        yield power
        power *= 2

# The basic way to call the generator
for v in powers_of_2(8):
    print(v)

# List comprehension
t = [x for x in powers_of_2(5)]
print(t)

# The list() function can also be used to convert the subsequent generator invocations into a real list
u = list(powers_of_2(3))
print(u)

# The in operator can also be used
for i in range(20):
    if i in powers_of_2(4):
        print(i, end=" ")

