# Example of a class variable, you can see that it isn't in the constructor: __init__
# This means that the variable belongs to the actual class is stored OUTSIDE any object
class ExampleClass:
    counter = 0
    def __init__(self, val = 1):
        self.__first = val
        ExampleClass.counter += 1


example_object_1 = ExampleClass()
example_object_2 = ExampleClass(2)
example_object_3 = ExampleClass(4)

print(example_object_1.__dict__, example_object_1.counter)  # {'_ExampleClass__first': 1} 3
print(example_object_2.__dict__, example_object_2.counter)  # {'_ExampleClass__first': 2} 3
print(example_object_3.__dict__, example_object_3.counter)  # {'_ExampleClass__first': 4} 3

