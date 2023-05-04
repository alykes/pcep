# The only difference between this and the last example is that the variables are now private inside the ExampleClass
class ExampleClass:
    def __init__(self, val = 1):
        self.__first = val

    def set_second(self, val = 2):
        self.__second = val


example_object_1 = ExampleClass()
example_object_2 = ExampleClass(2)

example_object_2.set_second(3)

example_object_3 = ExampleClass(4)
example_object_3.__third = 5

# Notice that you can still make an instance variable private!
# If a private variable is inside the class code, it will be mangled.
# If you add an instance private variable outside the class code, then it doesn't get mangled.

print(example_object_1.__dict__)    # {'_ExampleClass__first': 1}
print(example_object_2.__dict__)    # {'_ExampleClass__first': 2, '_ExampleClass__second': 3}
print(example_object_3.__dict__)    # {'_ExampleClass__first': 4, '__third': 5}
