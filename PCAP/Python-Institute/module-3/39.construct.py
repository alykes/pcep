# An example of a subclass calling a constructor of the superclass.
class Super:
    def __init__(self, name):
        self.name = name

    def __str__(self):
        return "My name is " + self.name + "."


class Sub(Super):
    def __init__(self, name):
        Super.__init__(self, name)      # The subclass calls the constructor of the superclass on this line.

    # def __str__(self):                # This __str()__ function will override the one in super if it is uncommented.
    #     return "This is the subby: "  + self.name + "."

obj = Sub("Andy")                       # Initialise the object

print(obj)                              # The __str()__ method is also inherited from the Super Class  


