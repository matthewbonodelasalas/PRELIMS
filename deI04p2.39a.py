""" Matthew Bono I. De las Alas
DATALOG Lab02
Feb. 17, 2020
I have neither received nor provided any help on this (lab) activity,
nor have I concealed any violation of the Honor Code.
"""

from abc import ABCMeta, abstractmethod

class Polygon(metaclass=ABCMeta): #class Polygon
    def __init__(self,length_sides): #initialization of the class
        self._length_sides = length_sides
        @abstractmethod
        def area(self):
            return area #returns the area

        @abstractmethod
        def perimeter(self):
            return perimeter #returns the perimeter

class Triangle(Polygon):
    def __init__(self,length_sides):
        super().__init__(length_sides)
        assert 3, self.length_sides # determines that it is a triangle
    def area(self):
        a, b, c = self.length_sides  #area of a triangle
        s = (a + b + c) / 2
        return (s * (s - a) * (s - b) * (s - c)) ** 0.5
    def perimeter(self):
        s = (self.length_sides[0] + self.length_sides[1] + self.length_sides[2])  #perimeter of a triangle
        return s

class IsoscelesTriangle(Triangle):

    def __init__(self, side, base):  # [side, base]
        super().__init__([side, side, base]) #triangle with only 2 sides are equal


class EquilateralTriangle(Triangle):

    def __init__(self, side):
        super().__init__([side, side, side]) #Triangle with 3 equal sides


class Rectangle(metaclass=ABCMeta):

    def __init__(self, length_sides):
        super().__init__(length_sides)
        assert 4, self.length_sides #determines that it is a rectangle

    def area(self):
        area = length * width  #calculates the area
        return area

    def perimeter(self):
        perimeter = 2 * (length + width) #calculates the perimeter
        return perimeter


class Quadrilateral(metaclass=ABCMeta):
    def __init__(self, length_sides):
        super().__init__(length_sides)
        assert 4, self.length_sides #determines that it is a quadrilateral

    def area(self):
        x, y = self.lengths_of_sides[0], self.lengths_of_sides[1] #calculates the area
        return x * y

    def perimeter(self):
        x, y = self.lengths_of_sides #calculates the perimeter
        return (x + y) * 2


class Pentagon(metaclass=ABCMeta):
    def __init__(self,length_sides):
        super().__init__(length_sides)
        assert 5, self.length_sides #determines that it is a pentagon

    def area(self): #calculates the area of pentagon
        x, y = self.length_sides[0], self.length_sides[1] #calculates the area
        return x * y

    def perimeter(self): #calculates the perimeter of pentagon
        x, y = self.length_sides
        return (x + y) * 2

class Hexagon(metaclass=ABCMeta):
    def __init__(self,length_sides):
        super().__init__(length_sides)
        assert 6, self.length_sides #determines that it is a hexagon

    def area(self):
        x, y = self.length_ides[0], self.length_sides[1] #calculates the area
        return x * y

    def perimeter(self):
        x, y = self.lengths_of_sides #calculates the perimeter
        return (x + y) * 2


class Octagon(metaclass=ABCMeta):
    def __init_(self,length_sides):
        super().__init__(length_sides)
        assert 8, self.length_sides #determines that it is an octagon

    def area(self):
        x, y = self.lengths_sides[0], self.lengths_sides[1] #calculates the area
        return x * y

    def perimeter(self):
        x, y = self.length_sides #calculates the perimeter
        return (x + y) * 2


if __name__ == '__main__':
    polygon = Polygon(3)
    a = 1
    b = 2
    c = 5
    s = (a + b + c) / 2
    print(s)