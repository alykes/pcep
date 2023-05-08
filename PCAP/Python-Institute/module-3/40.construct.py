# This is another example of how to call the constructor of a superclass by using the super() function
# Note that you don't need to pass self to the function, just the argument.
class Super:
    def __init__(self, name):
        self.name = name

    def __str__(self):
        return "My name is " + self.name + "."


class Sub(Super):
    def __init__(self, name):
        super().__init__(name)


obj = Sub("Andy")

print(obj)
