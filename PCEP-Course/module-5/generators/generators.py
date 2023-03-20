# When you want to return a large amount of values one by one
# yield

def get_number():
    for i in range(1, 4):
        yield i # You use this instead of return

generator = get_number()

print(next(generator))
print(next(generator))
print(next(generator))

# result - The generator remembers the last value that it returned
# 1
# 2
# 3
# when you reach the final number and try next again, you get an error!


## Generators should be used as below, where the function is in the for loop
for x in get_number():
    print(x)

# You can use generators to turn them into lists
numbers = list(get_number())
print(numbers)