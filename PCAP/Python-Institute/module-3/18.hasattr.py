# NOTE that the when running hasattr() on an object is will also pick up the class variable and consider that as an attribute!
class ExampleClass:
    a = 1
    def __init__(self):
        self.b = 2


example_object = ExampleClass()

print(hasattr(example_object, 'b'))     # True
print(hasattr(example_object, 'a'))     # True      - I got stuck on this one for a bit...At the end of the day, even though inaccessible, it's still an attribute!
print(hasattr(ExampleClass, 'b'))       # False     
print(hasattr(ExampleClass, 'a'))       # True


class ExampleClassTwo:
    attr = 1

print(hasattr(ExampleClassTwo, 'attr')) # True
print(hasattr(ExampleClassTwo, 'prop')) # False
