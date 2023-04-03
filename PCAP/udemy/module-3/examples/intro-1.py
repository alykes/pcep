# object approach
class Rectangle:
    def __init__(self, width, height):  # The __init__ part of the class is used to initialise the object
        self.width = width
        self.height = height

    def get_area(self):
        return self.width * self.height
    
a = int(input('What is the width? '))
b = int(input('What is the height? '))

rectangle = Rectangle(a, b)     # This creates the 'rectangle' object in memory
print('The calculated area is', rectangle.get_area())   # This calls the function on the new rectangle object