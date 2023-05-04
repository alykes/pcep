class ExampleClass:
    def __init__(self, val):
        if val % 2 != 0:
            self.a = 1
        else:
            self.b = 1


example_object = ExampleClass(1)
print(example_object.a)

try:                            # Using a try..except block that isn't best practise
    print(example_object.b)
except AttributeError:
    pass
