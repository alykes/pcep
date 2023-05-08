class Vehicle:
    pass


class LandVehicle(Vehicle):
    pass


class TrackedVehicle(LandVehicle):
    pass


my_vehicle = Vehicle()
my_land_vehicle = LandVehicle()
my_tracked_vehicle = TrackedVehicle()

for obj in [my_vehicle, my_land_vehicle, my_tracked_vehicle]:
    for cls in [Vehicle, LandVehicle, TrackedVehicle]:
        print(isinstance(obj, cls), end="\t")
    print()


# Results are:
# is an instance of 	Vehicle	LandVehicle	TrackedVehicle
# my_vehicle	        True	False	    False
# my_land_vehicle	    True	True	    False
# my_tracked_vehicle	True	True	    True