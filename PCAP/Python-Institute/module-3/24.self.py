# This example uses self to access another method within the same class.
class Classy:
    def other(self):
        print("other")

    def method(self):
        print("method")
        self.other()


obj = Classy()
obj.method()

# Result:
# method
# other

