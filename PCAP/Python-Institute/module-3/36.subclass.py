# Testing the issubclass function

class Vehicle:
    pass


class LandVehicle(Vehicle):
    pass


class TrackedVehicle(LandVehicle):
    pass


for cls1 in [Vehicle, LandVehicle, TrackedVehicle]:
    for cls2 in [Vehicle, LandVehicle, TrackedVehicle]:
        print(issubclass(cls1, cls2), end="\t")
    print()

# is a subclass of →	Vehicle	LandVehicle	TrackedVehicle
# Vehicle	            True	False	    False
# LandVehicle	        True	True	    False
# TrackedVehicle	    True	True	    True


