class Vehicle:
    def __init__(self, speed):
        self.speed = speed

class LandVehicle(Vehicle): # Name of the superclass
    def __init__(self, speed, wheel_count):
        Vehicle.__init__(self, speed)
        #super().__init__(speed)        # This is another way to call the constructor from the superclass. You don't have to provide self, it passed via Python automatically.
        self.wheel_count = wheel_count

class Car(LandVehicle): # Name of the superclass
    pass


my_car = Car(5, 10)     # This will now create the car object successfully! (through the Land Vehicle Super Class, which then calls the Vehcile constrcutor)
print(my_car.__dict__)  # {'speed': 5, 'wheel_count': 10} <= The Vehicle constructor is called from the LandVehicle class

print(my_car.speed)            # 5 <= this is inherited successfully from the superclass as it was inherited by the contructors.
