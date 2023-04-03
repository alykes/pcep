class Dog():
    def __init__(self, name, age):
        self.__name = name
        self.age = age


my_pet = Dog('Misty', 5)
my_pet.__dict__     # {'_Dog__name': 'Misty', 'age': 5} Notice that the __name property is now different, this is called name 'mangling'!

my_pet.colour = 'brown'     # Just added a random property to the object
my_pet.__dict__     # {'_Dog__name': 'Misty', 'age': 5, 'colour': 'brown'}  

my_pet.__breed = 'Maltese Terrier'  # Note, this will not mangle the name because we used the __ syntax outside the class definition

my_pet.__dict__     # {'_Dog__name': 'Misty', 'age': 5, '__breed': 'Maltese Terrier', 'colour': 'brown'} Notice that the name is not mangled!