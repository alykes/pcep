import math


class Point:
    #
    def __init__(self, x=0.0, y=0.0):
        self.__x = x
        self.__y = y
    #


class Triangle:
    def __init__(self, vertice1, vertice2, vertice3):
        #
        self.vertice1 = vertice1
        self.vertice2 = vertice2
        self.vertice3 = vertice3
        #

    def perimeter(self):
        #
        return self.vertice1 + self.vertice2 + self.vertice3
        #


triangle = Triangle(Point(0, 0), Point(1, 0), Point(0, 1))
print(triangle.perimeter())
