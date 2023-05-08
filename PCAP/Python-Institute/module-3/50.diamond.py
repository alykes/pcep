# The diamond problem represented as Python code.  
class A:
    pass


class B(A):
    pass


class C(A):
    pass


class D(B, C):
    pass


d = D()

# This is a second representation of the diamond code.
class Top:
    def m_top(self):
        print("top")


class Middle_Left(Top):
    def m_middle(self):             # This m_middle method has the same name as the Middle_Right method
        print("middle_left")


class Middle_Right(Top):
    def m_middle(self):             # This m_middle method has the same name as the Middle_Left method
        print("middle_right")


class Bottom(Middle_Left, Middle_Right):
    def m_bottom(self):
        print("bottom")


object = Bottom()
object.m_bottom()
object.m_middle()   # middle_left
object.m_top()

