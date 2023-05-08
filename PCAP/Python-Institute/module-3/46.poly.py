# This is an example of polymorphism. When ther doanything method in the One class behaves differently based on how it was called.

class One:
    def do_it(self):
        print("do_it from One")

    def doanything(self):
        self.do_it()        # This line's behaviour will change depending on how it is called, look at lines 19 and 20. 
                            # Self refers to the object and will perform differently depending on which object is currently being referenced by self.
                            # If it's one, then do_it is run in this class, that is One
                            # If it's two, then do_it is run from class Two


class Two(One):
    def do_it(self):
        print("do_it from Two")


one = One()
two = Two()

one.doanything()        # Runs the do_it method from class One
two.doanything()        # Runs the do_it method from class Two
