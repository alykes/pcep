# This example shows that the __dict__ properties for a class and for an object are different. Pay particular attention to the variable "varia"
class ExampleClass:
    varia = 1
    def __init__(self, val):
        ExampleClass.varia = val


print(ExampleClass.__dict__)        # {'__module__': '__main__', 'varia': 1, '__init__': <function ExampleClass.__init__ at 0x7fb2f01110e0>, 
                                    #  '__dict__': <attribute '__dict__' of 'ExampleClass' objects>, '__weakref__': <attribute '__weakref__' of 'ExampleClass' objects>, '__doc__': None}

example_object = ExampleClass(2)

print(ExampleClass.__dict__)        # {'__module__': '__main__', 'varia': 2, '__init__': <function ExampleClass.__init__ at 0x7fb2f01110e0>, 
                                    #  '__dict__': <attribute '__dict__' of 'ExampleClass' objects>, '__weakref__': <attribute '__weakref__' of 'ExampleClass' objects>, '__doc__': None

print(example_object.__dict__)      # {}    because varia is a CLASS variable, so there is nothing to display
