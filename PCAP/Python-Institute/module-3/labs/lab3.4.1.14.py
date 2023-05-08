# Works out the permiter for all three points

import math


class Point:
    #
    def __init__(self, x=0.0, y=0.0):
        self.__x = x
        self.__y = y
    #
    def getx(self):
        #
        return self.__x
        #

    def gety(self):
        #
        return self.__y
        #
    
    def distance_from_point(self, point):
        #
        x_side = self.__x - point.getx()
        y_side = self.__y - point.gety()
        
        return math.hypot(x_side, y_side)
        #


class Triangle:
    def __init__(self, vertice1, vertice2, vertice3):
        #
        self.vertice1 = vertice1
        self.vertice2 = vertice2
        self.vertice3 = vertice3
        
        self.point_list = [self.vertice1, self.vertice2, self.vertice3]
        #

    def perimeter(self):
        #
        return self.vertice1.distance_from_point(self.vertice2) + \
               self.vertice1.distance_from_point(self.vertice3) + \
               self.vertice3.distance_from_point(self.vertice2)
        #


triangle = Triangle(Point(0, 0), Point(1, 0), Point(0, 1))
print(triangle.perimeter())
