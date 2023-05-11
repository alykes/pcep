# An example of some lambda functions.
two = lambda: 2
sqr = lambda x: x * x
pwr = lambda x, y: x ** y

for a in range(-2, 3):
    print(sqr(a), end=" ")
    print(pwr(a, two()))

# Result
# 4 4
# 1 1
# 0 0
# 1 1
# 4 4


# Let's analzye it:

# the first lambda is an anonymous parameterless function that always returns 
# 2. As we've assigned it to a variable named two, we can say that the function 
# is not anonymous anymore, and we can use the name to invoke it.

# the second one is a one-parameter anonymous function that returns the value
# of its squared argument. We've named it as such, too.

# the third lambda takes two parameters and returns the value of the first one 
# raised to the power of the second one. The name of the variable which carries 
# the lambda speaks for itself. We don't use pow to avoid confusion with the 
# built-in function of the same name and the same purpose.