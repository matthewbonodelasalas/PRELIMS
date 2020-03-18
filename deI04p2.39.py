""" Matthew Bono I. De las Alas
DATALOG Lab02
Feb. 12, 2020
I have neither received nor provided any help on this (lab) activity,
nor have I concealed any violation of the Honor Code.
"""

from abc import ABCMeta, abstractmethod

class Polygon(metaclass=ABCMeta):
    def __init__(self,length_sides):
        self._length_sides = length_sides
        @abstractmethod
        def area(self):
            return area

        @abstractmethod
        def perimeter(self):
            return perimeter

class Triangle(Polygon):
    def __init__(self,length_sides):
        super()._init_(length_sides)
        self._area
        self._perimeter
    def area(self):
        triangle = 0.5 * base * height
    def perimeter(self):
        perimeter = a + b + c
        return a + b + c


class Rectangle(metaclass=ABCMeta):

    def __init__(self, lengths_of_sides):  # [side1, side2]
        super().__init__(lengths_of_sides)

    def area(self):
        area = lenght * width
        return area

    def perimeter(self):
        perimeter = 2 * (lenght + width)
        return perimeter


class Quadrilateral(metaclass=ABCMeta):
    def __init__(self,4):

    def area(self):

    def perimeter(self):



class Pentagon(metaclass=ABCMeta):
    def __init__(self,5):

    def area(self):
        area = (sqrt(5 * (5 + 2 *(sqrt(5)))) * a * a) / 4
        return area

    def perimeter(self):

class Hexagon(metaclass=ABCMeta):
    def __init__(selfself,6):

    def area(self):
        Pentagon = (5.196 / 2 )*a  # a = number of sides

    def perimeter(self):
        perimeter = 6 *


class Octagon(metaclass):
    def __init_(self,8):

    def area(self):
        Octagon = 2*(1+1.41)*(a*a)

    def perimeter(self):


