class Vehicle():
   pass
        
class Rideable():
   pass
      
class PetrolVehicle(Vehicle):
   pass
        
class Car(PetrolVehicle, Rideable):
   pass

# bases for Vehicle and Rideable
print(Vehicle.__bases__)        
print(Rideable.__bases__)
''' The output will be a tuple 
(<class 'object'>,)
(<class 'object'>,)
As no base classes are defined in the class themselves, so the inheritence is on the object itself!
'''

# bases for PetorlVehicle
print(PetrolVehicle.__bases__)  # This will return (<class '__main__.Vehicle'>,), as Vehicle is the only direct parent class for PetrolVehicle.

# bases for Car
print(Car.__bases__) 
# This will return (<class '__main__.PetrolVehicle'>, <class '__main__.Rideable'>), as Car has two direct parent classes: PetrolVehicle and Rideable. 
# We cannot see Vehicle here because Car inherits from it indirectly through PetrolVehicle