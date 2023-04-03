class Vehicle():
    def go(self):
        print('The Vehcile is...Going!')

    def introduce(self):
        print('I am a Vehicle!')

class Flyable():    # Could be a bird, a kite or a flying vehicle, like a plane or a helicopter.
    def fly(self):
        print('The Flyable is...Flying...!')
    
    def introduce(self):
        print('I am a Flyable!')

class Airplane(Flyable, Vehicle):       # The order is important as it lets the class know where to look first for methods and properties, especially if they are named the same in multiple inherited classes.
    def introduce(self):
        print('I am an Airplane!')

my_plane = Airplane()   # inherits from both classes
my_plane.go()           # The Vehcile is...Going!
my_plane.fly()          # The Flyable is...Flying...!

# The methods belong to both classes above it as there are two methods with the same name!
my_plane.introduce()    # I am an Airplane!           <=== Notice the difference from the previous two examples in multinhe-3.py and multinhe-4.py
