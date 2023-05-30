# This implementation of self is used to reference a variable in the same object instance and class variable
class Classy:
    varia = 2
    def method(self):
        Classy.varia = 1
        self.varia = 2
        var = 4
        print(Classy.varia, self.varia, self.var, var)

obj = Classy()
obj.var = 3
obj.method()

# Result:
# 1 2 3 4

class ExampleClass:
    a = 1
    def __init__(self):
        self.b = 2


example_object = ExampleClass()
print(ExampleClass.__dict__)
print(example_object.__dict__)
print(example_object.a)

# {'__module__': '__main__', 'a': 1, '__init__': <function ExampleClass.__init__ at 0x7ffab88013b0>, '__dict__': <attribute '__dict__' of 'ExampleClass' objects>, \
# '__weakref__': <attribute '__weakref__' of 'ExampleClass' objects>, '__doc__': None}
# {'b': 2}
# 1