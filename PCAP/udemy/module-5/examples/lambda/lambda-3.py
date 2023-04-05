def apply_func(elements, func):
    for element in elements:
        print(func(element))

my_func = lambda x: 0       # This will always return a 0
apply_func([1, 2, 3, 4, 5], my_func)

print('----------------')

apply_func([1, 2, 3, 4, 5], lambda x: x * x)