# An example of an instance variable
# Notice it exists only with the object
class ExampleClass:
    def __init__(self, val = 1):
        self.first = val

    def set_second(self, val):
        self.second = val


example_object_1 = ExampleClass()
example_object_2 = ExampleClass(2)

example_object_2.set_second(3)

example_object_3 = ExampleClass(4)
example_object_3.third = 5          # This is the instance variable!


# The __dict__ variable/property will print out the list of properties the object is currently carrying
print(example_object_1.__dict__)    # {'first': 1}
print(example_object_2.__dict__)    # {'first': 2, 'second': 3}
print(example_object_3.__dict__)    # {'first': 4, 'third': 5}

# Note here that:
# example_object_1 only has the property named first;
# example_object_2 has two properties: first and second;
# example_object_3 has been enriched with a property named third just on the fly, outside the class's code - this is possible and fully permissible.