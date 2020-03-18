""" Matthew Bono I. De las Alas
DATALOG Lab02
Feb. 5, 2020
I have neither received nor provided any help on this (lab) activity,
nor have I concealed any violation of the Honor Code.
"""

class Vector:
   #Vector will be shown

    def __init__(self, d):
        if isinstance(d, int):
            self._coords = [0] * d
        else:
            try:  # test if iterable
                self._coords = [val for val in d]
            except TypeError:
                raise TypeError('invalid parameter type')

    def __len__(self):
        #returns the dimension of the vector
        return len(self._coords)

    def __getitem__(self, j):
        #Return jth coordinate of vector
        return self._coords[j]

    def __setitem__(self, j, val):
        #given value will be set to the jth coordinate
        self._coords[j] = val

    def __add__(self, other):
        #Sum of two vectors will be returned
        if len(self) != len(other):  # __len__ method will be used
            raise ValueError('dimensions must agree')
        result = Vector(len(self))  # vector of zeros
        for j in range(len(self)):
            result[j] = self[j] + other[j]
        return result

    def __sub__(self, other):
        if len(self) != len(other):  #  __len__ method will be used
            raise ValueError('dimensions must agree')
        result = Vector(len(self))  # vector of zeros
        for j in range(len(self)):
            result[j] = self[j] - other[j]
        return result

    def __str__(self):
        return '<' + str(self._coords)[1:-1] + '>'#It will represent a string of vector

if __name__ == '__main__':
    # demonstrates usage of methods in class Vector:
    vector = Vector(15)
    vector[1] = 30
    vector[-1]= 55
    print(vector[4])
    a= vector + vector
    print(a)
    c= vector - a
    print(c)
    total = 0
    for entry in vector:
        total += entry