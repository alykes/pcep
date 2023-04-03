class Dog():
    counter = 0
    def __init__(self, name, age):
        self.__name = name
        self.age = age
        Dog.counter += 1        # Every time the constructor is used, the variable is increased.

my_pet = Dog('Ponker', 2)
adam_pet = Dog('Slapper', 4)
betty_pet = Dog('Gronk', 7)

print(my_pet.counter)       # 3 This variable is specific to the class itself
print(adam_pet.counter)     # 3
print(betty_pet.counter)    # 3

print(Dog.counter)          # 3 This is clearer to use than the above, which reference objects first