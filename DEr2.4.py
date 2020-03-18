"""Matthew Bono I. De las Alas 
   DATALOG Lab02 
   Feb.10,2020 
   I have neither recieved nor provided any help on this lab activity,nor have I concealed any violation of the Honor Code.
"""
class Flower:  #class instructor method
    def __init__(self, name, petals, price):  #initialization
        self.name = name
        self.petals = petals
        self.price = price

    def value_flower(self, name_new_value, petals_new_value, price_new_value):
        self.name = str(name_new_value) #instance variables
        self.petals = int(petals_new_value)#instance variables
        self.price = float(price_new_value)#instance variables

    def value_input(self):
        print (self.name, self.petals, self.price)


f1 = Flower ('Rose', 10,35.00) # initialization of values
f1.value_input() #get the initialized values

f1.value_flower('Yellow Bell',5,125.00) #changing of values
f1.value_input()#getting new values

f1.value_flower('Sunflower',89,300.45)#changing of values
f1.value_input()#getting new values 