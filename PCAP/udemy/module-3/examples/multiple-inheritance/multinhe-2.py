class Vehicle():
    def go(self):
        print('The Vehcile is...Going!')

class Flyable():    # Could be a bird, a kite or a flying vehicle, like a plane or a helicopter.
    def fly(self):
        print('The Flyable is...Flying...!')

class Airplane(Vehicle, Flyable):
    pass

my_plane = Airplane()   # inherits from both classes
my_plane.go()           # The Vehcile is...Going!
my_plane.fly()          # The Flyable is...Flying...!
