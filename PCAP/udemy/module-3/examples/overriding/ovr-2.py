class Animal():
    def __init__(self):
        self.species = 'general'

    def produce_sound(self):
        print('...general animal noises...')

class Dog(Animal):
    def __init__(self):
        self.species = 'Canis Familiaris'

    def produce_sound(self):
        print('woof woof!')


my_pet = Dog()

# You can see that the method and variables are overridden even though the names are exactly the same.
# This is called method overriding.
print(my_pet.species)       # Canis Familiaris
print('Your pet opens its mouth and you hear')
my_pet.produce_sound()      # woof woof!

