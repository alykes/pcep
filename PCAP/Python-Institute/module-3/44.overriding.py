# Overriding
# Both, Level1 and Level2 classes define a method named fun() and a property named var.
# Python looks from the bottom to the top, so will use the first entities that it finds. 

class Level1:
    var = 100
    def fun(self):
        return 101


class Level2(Level1):
    var = 200
    def fun(self):
        return 201


class Level3(Level2):
    pass


obj = Level3()

print(obj.var, obj.fun())
# Result 200 201