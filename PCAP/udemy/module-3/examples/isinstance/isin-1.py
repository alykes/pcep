class Vehicle:
    def __init__(self, speed):
        self.speed = speed

class LandVehicle(Vehicle): # Name of the superclass
    def __init__(self, speed, wheel_count):
        #Vehicle.__init__(self, speed) # This is exactly the same as the line below.
        super().__init__(speed)
        self.wheel_count = wheel_count

class Car(LandVehicle): # Name of the superclass
    pass


my_vehicle = Vehicle(50)
my_land_vehicle = LandVehicle(50, 4)
my_car = Car(60, 4)

print(isinstance(my_vehicle, Vehicle))          # True
print(isinstance(my_land_vehicle, Vehicle))     # True
print(isinstance(my_car, Vehicle))              # True

print(isinstance(my_vehicle, LandVehicle))      # False
print(isinstance(my_land_vehicle, LandVehicle)) # True
print(isinstance(my_car, LandVehicle))          # True

print(isinstance(my_vehicle, Car))              # False
print(isinstance(my_land_vehicle, Car))         # False
print(isinstance(my_car, Car))                  # True

my_new_vehicle = Vehicle(60)
my_new_vehicle = my_vehicle                     # This assigns the address of the object to my_new_vehicle, therefore they are now the same object!

print(my_new_vehicle is my_new_vehicle)            # True, as they are the same object!

print(my_vehicle.__dict__, my_new_vehicle.__dict__)
my_vehicle.speed = 30
print(my_vehicle.__dict__, my_new_vehicle.__dict__)     # This references the same object
