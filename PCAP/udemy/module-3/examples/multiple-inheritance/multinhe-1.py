class Vehicle():
    pass

class Flyable():    # Could be a bird, a kite or a flying vehicle, like a plane or a helicopter.
    pass

class Airplane(Vehicle, Flyable):
    pass

my_plane = Airplane()   # inherits from both classes
