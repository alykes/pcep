class Vehicle:
    class_message = 'This is from the Vehicle Class'
    def __init__(self, speed):
        self.speed = speed

class LandVehicle(Vehicle):             # Name of the superclass in brackets
    def __init__(self, speed, wheel_count):
        super().__init__(speed)         # This is another way to call the constructor from the superclass. You don't have to provide self, it passed via Python automatically.
        self.wheel_count = wheel_count
        print(super().class_message)    # refers to the super class variable

    def speed_up(self):
        self.speed += 5

class Car(LandVehicle):     # Name of the superclass in brackets
    def super_speed(self):
        print('NOS Activated...!')
        for press in range(3):
            super().speed_up()


my_supercar = Car(10, 4)     # This will now create the car object successfully! (through the Land Vehicle Super Class, which then calls the Vehcile constrcutor)

print(my_supercar.__dict__)  # {'speed': 10, 'wheel_count': 4}
my_supercar.super_speed()
print(my_supercar.__dict__)  # {'speed': 25, 'wheel_count': 4}
my_supercar.speed_up()
print(my_supercar.__dict__)  # {'speed': 30, 'wheel_count': 4}


