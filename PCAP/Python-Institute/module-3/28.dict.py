# This example shows __dict__ results for the method as well as the object.
# The object doesn't show the methods, only the class does
class Classy:
    varia = 1
    def __init__(self):
        self.var = 2

    def method(self):
        pass

    def __hidden(self):
        pass


obj = Classy()

print(obj.__dict__)     # {'var': 2}
print(Classy.__dict__)  # {'__module__': '__main__', 'varia': 1, '__init__': <function Classy.__init__ at 0x7ffb540e2320>, 
                        # 'method': <function Classy.method at 0x7ffb540e23b0>, '_Classy__hidden': <function Classy.__hidden at 0x7ffb540e2440>, 
                        # '__dict__': <attribute '__dict__' of 'Classy' objects>, '__weakref__': <attribute '__weakref__' of 'Classy' objects>, 
                        # '__doc__': None}
