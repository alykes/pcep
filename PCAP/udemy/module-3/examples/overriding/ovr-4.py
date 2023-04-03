class Animal():
    def __init__(self):
        self.species = 'general'

    def produce_sound(self):
        print('...general animal noises...')

    def present_sound(self):
        print('I can make the following sound:')
        self.produce_sound()

class Dog(Animal):
    def __init__(self):
        self.species = 'Canis Familiaris'

    def produce_sound(self):
        print('woof woof!')


my_first_pet = Animal()     # Note that we are calling the Animal constructor here!
my_second_pet = Dog()       # Note that we are calling the Dog constructor here! Changes the behaviour of the superclass and is an example of polymorphism.


my_first_pet.produce_sound()    # ...general animal noises...
print()
my_second_pet.produce_sound()   # woof woof!

## This behaviour happens because self.produce_sound() is called from the object's class, this is a little tricky! It's inherited by the dog object and uses `self` which points to the CURRENT OBJECT!
## Both present() methods behave differently because they were each created using different classes!
