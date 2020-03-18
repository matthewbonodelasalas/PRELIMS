""" Matthew Bono I. De las Alas
DATALOG Lab01
Feb. 5, 2020
I have neither received nor provided any help on this (lab) activity, nor have I concealed any violation of the Honor Code.
"""

a=int(input("Amount Charged: "))
b=int(input("Amount Given: "))
money_change=b-a
amount=money_change

bill1=amount//1000
amount%1000
bill2=amount//500
amount%500
bill3=amount//200
amount%200
bill4=amount//100
amount%100
bill5=amount//50
amount%50
bill6=amount//20
amount%20
coin7=amount//10
amount%10
coin8=amount//5
amount%5
coin9=amount//1
amount%1
cents10=amount/0.25

print("No. of Php 1000 bill/s" ,bill1)
print("No. of Php 500 bill/s" ,bill2)
print("No. of Php 200 bill/s" ,bill3)
print("No. of Php 100 bill/s" ,bill4)
print("No. of Php 50 bill/s" ,bill5)
print("No. of Php 20 bill/s" ,bill6)
print("No. of Php 10 coin/s" ,coin7)
print("No. of Php 5 coin/s" ,coin8)
print("No. of Php 1 coin/s" ,coin9)
print("No. of Php 25 cents coin/s" ,cents10)