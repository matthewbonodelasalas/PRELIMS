""" Matthew Bono I. De las Alas
DATALOG Lab02
Feb. 19, 2020
I have neither received nor provided any help on this (lab) activity,
nor have I concealed any violation of the Honor Code.
"""
from abc import ABCMeta, abstractmethod

class Polygon(metaclass=ABCMeta): #class Polygon
    def __init__(self,length_sides): #initialization of the class
        self._length_sides = length_sides
        @abstractmethod
        def area(self): #area function
            return area #returns the area

        @abstractmethod
        def perimeter(self): #perimeter function
            return perimeter #returns the perimeter

        class Pentagon(metaclass=ABCMeta):
            def __init__(self, length_sides): #initialization of the class
                super().__init__(length_sides)
                assert 5, self.length_sides  # determines that it is a pentagon

            def area(self):  # calculates the area of pentagon
                x, y = self.length_sides[0], self.length_sides[1]  # calculates the area
                return x * y #returns the value

            def perimeter(self):  # calculates the perimeter of pentagon
                x, y = self.length_sides
                return (x + y) * 2 #returns the value

        class Hexagon(metaclass=ABCMeta):
            def __init__(self, length_sides): #initialization of the class
                super().__init__(length_sides)
                assert 6, self.length_sides  # determines that it is a hexagon

            def area(self):
                x, y = self.length_sides[0], self.length_sides[1]  # calculates the area
                return x * y #returns the value

            def perimeter(self):
                x, y = self.length_sides  # calculates the perimeter
                return (x + y) * 2 #returns the value

if __name__ == '__main__':
    Polygon(6) #Polygon 6 sides
    Polygon(5) #Polygon 5 sides











