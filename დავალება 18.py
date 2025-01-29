import math


class Triangle:
    def __init__(self,a,b,c):
        self.__a = a
        self.__b = b
        self.__c = c


    def triangle_area(self):
        s = (self.__a + self.__b + self.__c) / 2
        area = math.sqrt(s * (s - self.__a) * (s - self.__b) * (s - self.__c))
        return area

    def triangle_perimeter(self):
        perimeter = self.__a + self.__b + self.__c
        return perimeter

triangle1 = Triangle(5,4,3)

print(triangle1.triangle_perimeter(),triangle1.triangle_area())


