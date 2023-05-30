# Summary 
class Sample:
    def __init__(self):
        self.name = Sample.__name__
    def myself(self):
        print("My name is " + self.name + " living in a " + Sample.__module__)


obj = Sample()
obj.myself()

# example of names and bases
class Snake:
    pass


class Python(Snake):
    pass


print(Python.__name__, 'is a', Snake.__name__)
print(Python.__bases__[0].__name__, 'can be a', Python.__name__)

##############################
class Galaxy:
    pass

class Star(Galaxy):
    def __init__(self, name, galaxy):
        self.name = name
        self.galaxy = galaxy
    
    # def __str__(self):
    #     return self.name + ' in ' + self.galaxy



sun = Star("Sun", "Milky Way")
print(type(sun).__name__)
print(Star.__bases__[0].__name__)
print(Galaxy.__bases__[0].__name__)
print(Galaxy.__bases__[0])
print(Galaxy)
print(Galaxy.__name__)

# Star
# Galaxy
# object
# <class 'object'>
# <class '__main__.Galaxy'>
# Galaxy

print(issubclass(Star, object))
print(issubclass(Star, Galaxy))
print(issubclass(Galaxy, object))
print()

# True
# True
# True