class Animal():
    def __init__(self):
        self.species = 'general'

    def produce_sound(self):
        print('...general animal noises...')

class Dog(Animal):
    pass


my_pet = Dog()

print(my_pet.species)   # general
print('Your pet opens its mouth and you hear')
my_pet.produce_sound()  # ...general animal noises...

