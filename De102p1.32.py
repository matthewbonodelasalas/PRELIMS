""" Matthew Bono I. De las Alas
DATALOG Lab01
Feb. 5, 2020
I have neither received nor provided any help on this (lab) activity, nor have I concealed any violation of the Honor Code.
"""

a = float(input()) #first integer
b = input()  #operator input (+,-,*,/)
c = float(input()) # second integer

if b == '+':  #addition
  x = a + c
  print("The answer is",x)
elif b == '-':  #subtraction
  x = a - c
  print("The answer is",x)
elif b == '*': #multiplication
  x = a * c
  print("The answer is",x)
elif b == '/': #division
  x = a / c
  print("The answer is",x)
else:
  print("Invalid input")