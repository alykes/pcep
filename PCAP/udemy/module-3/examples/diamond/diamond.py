class Vehicle():
    def show_power_type(self):
        print('I use any type of power!')

class ElectricVehicle(Vehicle):
    def show_power_type(self):
        print('I use Electrical power!')
        
class PetrolVehicle(Vehicle):
    def show_power_type(self):
        print('I use Petrol Power!')

class HybridCar(ElectricVehicle, PetrolVehicle):
    pass


# MRO is used - Method Resolution Order for the solution to the diamond problem
my_toyota_yaris = HybridCar()

my_toyota_yaris.show_power_type()