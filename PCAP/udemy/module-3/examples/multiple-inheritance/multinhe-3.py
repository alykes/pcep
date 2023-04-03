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

class Airplane(Vehicle, Flyable):       # The order is important as it lets the class know where to look first for methods and properties, especially if they are named the same in multiple inherited classes.
    pass

my_plane = Airplane()   # inherits from both classes
my_plane.go()           # The Vehcile is...Going!
my_plane.fly()          # The Flyable is...Flying...!

# The methods belong to both classes above it as there are two methods with the same name!
my_plane.introduce()    # I am a Vehicle!           <=== Notice the difference from the next example in multinhe-4.py
