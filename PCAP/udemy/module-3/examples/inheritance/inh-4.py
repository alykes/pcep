class Vehicle:
    def __init__(self, speed):
        self.speed = speed

class LandVehicle(Vehicle): # Name of the superclass
    def __init__(self, wheel_count):
        self.wheel_count = wheel_count

class Car(LandVehicle): # Name of the superclass
    pass


my_car = Car() # Fails because one argument is expected! Will look for a constructor in all the super classes, therefore it will used in Car

my_car = Car(5) # This will now create the car object successfully! (through the Vehicle Super Class)
print(my_car.__dict__)  # {'wheel_count': 5} <= This is because Python rules state that the constructor in the immediate class is used, if there is no constructor in the immediate class, it searches through the superclasses
