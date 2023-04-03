class Dog():
    counter = 0
    def __init__(self, name, age):
        self.name = name
        self.age = age
        Dog.counter += 1        # Every time the constructor is used, the variable is increased.

my_pet = Dog('Rusty', 4)


if hasattr(my_pet, 'name'):
    print('My pet\'s name is', my_pet.name)
else:
    print('This pet has no name!!')

if hasattr(Dog, 'counter'):
    print('There is a counter and its value is', Dog.counter)
else:
    print('There is no counter!!')

