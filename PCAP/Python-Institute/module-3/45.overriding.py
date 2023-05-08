class Left:
    var = "L"
    var_left = "LL"
    def fun(self):
        return "Left"


class Right:
    var = "R"
    var_right = "RR"
    def fun(self):
        return "Right"


class Sub(Left, Right):             # Overriding entities is done based on the order that the superclasses are defined here.  
# class Sub(Right, Left):           # This would mean that the obj.fun() would point to the fun() method in class Right! # Result --> R LL RR Right
    pass


obj = Sub()

print(obj.var, obj.var_left, obj.var_right, obj.fun())  # L LL RR Left