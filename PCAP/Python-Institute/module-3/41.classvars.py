# Testing properties: class variables.
# The object inherits the property from the superclass
class Super:
    supVar = 1


class Sub(Super):
    subVar = 2


obj = Sub()

print(obj.subVar)   # 2
print(obj.supVar)   # 1




# Testing properties: instance variables.
# This is another method that can be used to assign variables using the constructor
class Super_Two:
    def __init__(self):
        self.supVar = 11


class Sub_Two(Super_Two):
    def __init__(self):
        super().__init__()      # If this line was commented out, then the object would not get the the supVar property.  
        self.subVar = 12


obj_Two = Sub_Two()

print(obj_Two.subVar)
print(obj_Two.supVar)