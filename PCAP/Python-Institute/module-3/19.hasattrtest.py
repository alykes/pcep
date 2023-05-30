# NOTE that the when running hasattr() on an object is will also pick up the class variable and consider that as an attribute!
# This is a bit of a quirk...
class ExampleClass:
    a = 1
    def __init__(self):
        self.b = 2


example_object = ExampleClass()
print(example_object.__dict__)

print(hasattr(example_object, 'b'))     # True
print(hasattr(example_object, 'a'))     # True      - I got stuck on this one for a bit...At the end of the day, all objects inherit properites from the Class.
print(hasattr(ExampleClass, 'b'))       # False     - because this only gets instantiated when an object is created.
print(hasattr(ExampleClass, 'a'))       # True

ExampleClass.a = 5      # 5
print(ExampleClass.a)

example_object.a = 8
print(example_object.a) # 8
print("------------------")

print(ExampleClass.a)   # 5

print(example_object.__dict__)

class ExampleClassTwo:
    attr = 1

print(hasattr(ExampleClassTwo, 'attr')) # True
print(hasattr(ExampleClassTwo, 'prop')) # False
