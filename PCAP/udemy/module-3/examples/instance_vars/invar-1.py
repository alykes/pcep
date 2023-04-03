class Dog():
    def __init__(self, name, age):
        self.name = name
        self.age = age


my_pet = Dog('Misty', 5)
my_pet.__dict__     # {'name': 'Misty', 'age': 5}

my_pet.colour = 'brown'     # Just added a random property to the object
my_pet.__dict__     # {'name': 'Misty', 'age': 5, 'colour': 'brown'}  

del my_pet.name             # Deletes the name property
my_pet.__dict__     # {'age': 5, 'colour': 'brown'}