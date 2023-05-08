# This implementation of self is used to reference a variable in the same object instance and class variable
class Classy:
    varia = 2
    def method(self):
        print(self.varia, self.var)


obj = Classy()
obj.var = 3
obj.method()

# Result:
# 2 3