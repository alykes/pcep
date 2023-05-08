# Inheritance example, see notes below for an explanation.
class Vehicle:
    pass


class LandVehicle(Vehicle):
    pass


class TrackedVehicle(LandVehicle):
    pass



# The Vehicle class is the superclass for both the LandVehicle and TrackedVehicle classes;
# The LandVehicle class is a subclass of Vehicle and a superclass of TrackedVehicle at the same time;
# The TrackedVehicle class is a subclass of both the Vehicle and LandVehicle classes.