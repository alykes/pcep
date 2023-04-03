class Vehicle:
    pass

class LandVehicle(Vehicle): # Name of the superclass
    pass

class Car(LandVehicle): # Name of the superclass
    pass


my_car = Car()
print(my_car.__dict__)  # {} the dictionary is completely empty!

