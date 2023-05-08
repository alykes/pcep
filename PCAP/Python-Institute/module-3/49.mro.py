class Top:
    def m_top(self):
        print("top")


class Middle(Top):
    def m_middle(self):
        print("middle")


class Bottom(Middle):
# class Bottom(Middle, Top)     # <-- This also works because it follows Python's MRO, that is Middle Precedes Top
# class Bottom(Top, Middle)     # <-- This DOES NOT work because it does not follow Python's MRO, Top is not in the line of inheritance!
                                # This line will result in a TypeError Exception!
    def m_bottom(self):         
        print("bottom")


object = Bottom()
object.m_bottom()
object.m_middle()
object.m_top()

# This works perfectly and as expected, no issues here.

