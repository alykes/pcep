def apply_func(elements, func):
    for element in elements:
        print(func(element))

my_func = lambda x: x * x
apply_func([1, 2, 3, 4, 5], my_func)

print('------------------')

my_func2 = lambda y: 1 / y
apply_func([1, 2, 3, 4, 5], my_func2)
