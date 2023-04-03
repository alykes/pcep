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


my_first_pet = Animal()     # Note that we are calling the Animal constructor here!
my_second_pet = Dog()       # Note that we are calling the Dog constructor here! Changes the behaviour of the superclass and is an example of polymorphism.


print('Your first pet opens its mouth and you hear')
my_first_pet.produce_sound()    # ...general animal noises...
print('Well, what do you know, it\'s an animal of the type:', my_first_pet.species)
print('Your pet opens its mouth and you hear')
my_second_pet.produce_sound()   # woof woof!
print('Well, what do you know, it\'s an animal of the type:', my_second_pet.species)
