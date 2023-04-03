class Dog():
    counter = 0
    def __init__(self, name, age):
        self.name = name
        self.age = age
        Dog.counter += 1        # Every time the constructor is used, the variable is increased.

my_pet = Dog('Rusty', 4)

print(Dog.__name__)             # 'Dog' returns the name of the class
print(type(my_pet).__name__)    # 'Dog' returns the type of the my_pet object

print(Dog.__module__)           # Will return __main__